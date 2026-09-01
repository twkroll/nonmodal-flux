from __future__ import annotations

import json

import numpy as np

from nonmodal_flux.benchmarks.mhw_bridge import MHWConfig, potential_hat, simulate
from research.stochastic_cascades.C2_falsification import (
    chapman_kolmogorov_tv,
    local_km_polynomial_fit,
    relative_linear_change,
)

SEEDS = (0, 1, 2, 3)
PLATEAU_SEEDS = (0, 2, 3)
TMIN = 380.0
TMAX = 490.0
PHYSICAL_INCREMENT_SHIFTS_64 = (16, 14, 12, 10, 8)
GAUSSIAN_LENGTHS = (10.0, 8.75, 7.5, 6.25, 5.0)
SHARP_KCUTS = (0.6, 0.7, 0.8, 0.9, 1.0)


def selected_indices(diagnostics, tmin=TMIN, tmax=TMAX):
    return np.flatnonzero((diagnostics[:, 0] >= tmin) & (diagnostics[:, 0] <= tmax))


def nonzonal_potential_hat(zeta_hat, cfg, grid):
    *_prefix, invk2, _dealias, zonal = grid
    phi_hat = potential_hat(zeta_hat, invk2)
    phi_hat = phi_hat.copy()
    phi_hat[zonal] = 0.0
    return phi_hat


def directional_increments(zeta_hat, shifts, cfg, grid):
    phi = np.fft.ifft2(nonzonal_potential_hat(zeta_hat, cfg, grid)).real
    x = [(np.roll(phi, -shift, axis=0) - phi).ravel() for shift in shifts]
    y = [(np.roll(phi, -shift, axis=1) - phi).ravel() for shift in shifts]
    return x, y


def gaussian_coarse_fields(zeta_hat, lengths, cfg, grid):
    _kx, _ky, k2, *_ = grid
    kmag = np.sqrt(k2)
    phi_hat = nonzonal_potential_hat(zeta_hat, cfg, grid)
    out = []
    for ell in lengths:
        # Smooth low-pass with nominal cutoff kc=2*pi/ell.
        multiplier = np.exp(-0.5 * (kmag * ell / (2.0 * np.pi)) ** 2)
        out.append(np.fft.ifft2(phi_hat * multiplier).real.ravel())
    return out


def sharp_lowpass_fields(zeta_hat, kcuts, cfg, grid):
    _kx, _ky, k2, *_ = grid
    kmag = np.sqrt(k2)
    phi_hat = nonzonal_potential_hat(zeta_hat, cfg, grid)
    return [np.fft.ifft2(phi_hat * (kmag <= kc)).real.ravel() for kc in kcuts]


def pool_observable(samples, indices, builder, scales, cfg, grid):
    pools = [[] for _ in scales]
    for idx in indices:
        values = builder(samples[idx][0], scales, cfg, grid)
        for j, value in enumerate(values):
            pools[j].append(value)
    return [np.concatenate(v) for v in pools]


def pool_directional_increments(samples, indices, shifts, cfg, grid):
    xp = [[] for _ in shifts]
    yp = [[] for _ in shifts]
    for idx in indices:
        xv, yv = directional_increments(samples[idx][0], shifts, cfg, grid)
        for j in range(len(shifts)):
            xp[j].append(xv[j])
            yp[j].append(yv[j])
    return [np.concatenate(v) for v in xp], [np.concatenate(v) for v in yp]


def central_km(x_now, x_next, sigma, delta_s, half_width=0.25):
    u = x_now / sigma
    du = x_next / sigma - u
    mask = np.abs(u) < half_width
    return {
        "d2_center": float(np.mean(du[mask] ** 2) / (2.0 * delta_s)),
        "d4_center": float(np.mean(du[mask] ** 4) / (24.0 * delta_s)),
        "n_center": int(mask.sum()),
    }


def analyze_increment_coordinate(samples, diagnostics, cfg, grid):
    indices = selected_indices(diagnostics)
    x, y = pool_directional_increments(
        samples, indices, PHYSICAL_INCREMENT_SHIFTS_64, cfg, grid
    )
    result = {}
    for direction, values in (("x", x), ("y", y)):
        sigma = float(np.std(values[0]))
        rows = []
        for j, next_shift in enumerate(PHYSICAL_INCREMENT_SHIFTS_64[1:], start=1):
            delta_s = float(np.log(PHYSICAL_INCREMENT_SHIFTS_64[0] / next_shift))
            fit = local_km_polynomial_fit(values[0], values[j], sigma, delta_s)
            rows.append(
                {
                    "next_shift": next_shift,
                    "delta_s": delta_s,
                    **fit,
                    **central_km(values[0], values[j], sigma, delta_s),
                }
            )
        b0 = np.asarray([row["b0"] for row in rows])
        c0 = np.asarray([row["c0"] for row in rows])
        delta_s = np.asarray([row["delta_s"] for row in rows])
        result[direction] = {
            "rows": rows,
            "b0_cv": float(np.std(b0) / abs(np.mean(b0))),
            "d4_fit_intercept": float(np.polyfit(delta_s, c0, 1)[1]),
            "ck_16_12_8": chapman_kolmogorov_tv(values[0], values[2], values[4]),
        }
    return result


def analyze_gaussian_coordinate(samples, diagnostics, cfg, grid):
    indices = selected_indices(diagnostics)
    values = pool_observable(
        samples, indices, gaussian_coarse_fields, GAUSSIAN_LENGTHS, cfg, grid
    )
    sigma = float(np.std(values[0]))
    rows = []
    for j, ell in enumerate(GAUSSIAN_LENGTHS[1:], start=1):
        delta_s = float(np.log(GAUSSIAN_LENGTHS[0] / ell))
        rows.append(
            {
                "ell": ell,
                "delta_s": delta_s,
                **central_km(values[0], values[j], sigma, delta_s),
            }
        )
    delta_s = np.asarray([row["delta_s"] for row in rows])
    d2 = np.asarray([row["d2_center"] for row in rows])
    d4 = np.asarray([row["d4_center"] for row in rows])
    return {
        "rows": rows,
        "d2_power": float(np.polyfit(np.log(delta_s), np.log(d2), 1)[0]),
        "d4_power": float(np.polyfit(np.log(delta_s), np.log(d4), 1)[0]),
        "ck_10_7p5_5": chapman_kolmogorov_tv(values[0], values[2], values[4]),
    }


def analyze_sharp_coordinate(samples, diagnostics, cfg, grid):
    indices = selected_indices(diagnostics)
    values = pool_observable(samples, indices, sharp_lowpass_fields, SHARP_KCUTS, cfg, grid)
    sigma = float(np.std(values[0]))
    rows = []
    for j, kc in enumerate(SHARP_KCUTS[1:], start=1):
        delta_s = float(np.log(kc / SHARP_KCUTS[0]))
        rows.append(
            {
                "kc": kc,
                "delta_s": delta_s,
                **central_km(values[0], values[j], sigma, delta_s),
            }
        )
    delta_s = np.asarray([row["delta_s"] for row in rows])
    d2 = np.asarray([row["d2_center"] for row in rows])
    d4 = np.asarray([row["d4_center"] for row in rows])
    return {
        "rows": rows,
        "d2_power": float(np.polyfit(np.log(delta_s), np.log(d2), 1)[0]),
        "d4_power": float(np.polyfit(np.log(delta_s), np.log(d4), 1)[0]),
        "ck_0p6_0p8_1p0": chapman_kolmogorov_tv(values[0], values[2], values[4]),
    }


def analyze_seed(seed):
    cfg = MHWConfig(n=64, seed=seed, tmax=500.0, modified_coupling=True)
    diagnostics, samples, grid = simulate(cfg)
    indices = selected_indices(diagnostics)
    t = diagnostics[indices, 0]
    zf = diagnostics[indices, 3]
    enz = diagnostics[indices, 2]
    out = {
        "seed": seed,
        "mean_zonal_fraction": float(np.mean(zf)),
        "relative_zonal_trend": relative_linear_change(t, zf),
        "mean_nonzonal_energy": float(np.mean(enz)),
        "relative_nonzonal_energy_trend": relative_linear_change(t, enz),
    }
    if seed in PLATEAU_SEEDS:
        out["increments"] = analyze_increment_coordinate(samples, diagnostics, cfg, grid)
        out["gaussian"] = analyze_gaussian_coordinate(samples, diagnostics, cfg, grid)
        out["sharp"] = analyze_sharp_coordinate(samples, diagnostics, cfg, grid)
    return out


def run_c3():
    seeds = [analyze_seed(seed) for seed in SEEDS]
    accepted = [value for value in seeds if value["seed"] in PLATEAU_SEEDS]
    return {
        "configuration": {
            "grid": [64, 64],
            "tmax": 500.0,
            "analysis_window": [TMIN, TMAX],
            "all_seeds": list(SEEDS),
            "plateau_seeds": list(PLATEAU_SEEDS),
            "physical_increment_shifts": list(PHYSICAL_INCREMENT_SHIFTS_64),
            "gaussian_lengths": list(GAUSSIAN_LENGTHS),
            "sharp_kcuts": list(SHARP_KCUTS),
        },
        "seeds": seeds,
        "summary": {
            "mean_increment_ck_x": float(
                np.mean([v["increments"]["x"]["ck_16_12_8"] for v in accepted])
            ),
            "mean_increment_ck_y": float(
                np.mean([v["increments"]["y"]["ck_16_12_8"] for v in accepted])
            ),
            "mean_gaussian_ck": float(
                np.mean([v["gaussian"]["ck_10_7p5_5"] for v in accepted])
            ),
            "mean_sharp_ck": float(
                np.mean([v["sharp"]["ck_0p6_0p8_1p0"] for v in accepted])
            ),
            "gaussian_d2_powers": [v["gaussian"]["d2_power"] for v in accepted],
            "gaussian_d4_powers": [v["gaussian"]["d4_power"] for v in accepted],
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_c3(), indent=2))
