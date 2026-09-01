from __future__ import annotations

import json

import numpy as np

from nonmodal_flux.benchmarks.mhw_bridge import (
    MHWConfig,
    directional_increment_ensemble,
    simulate,
)

SEEDS = (0, 1, 2, 3)
SHIFTS = (8, 7, 6, 5, 4, 3, 2, 1)
TMIN = 380.0
TMAX = 490.0


def transition_matrix(x: np.ndarray, y: np.ndarray, edges: np.ndarray):
    ix = np.digitize(x, edges) - 1
    iy = np.digitize(y, edges) - 1
    nb = len(edges) - 1
    valid = (ix >= 0) & (ix < nb) & (iy >= 0) & (iy < nb)
    counts = np.zeros((nb, nb), dtype=float)
    np.add.at(counts, (ix[valid], iy[valid]), 1.0)
    occupancy = counts.sum(axis=1)
    matrix = np.divide(
        counts,
        occupancy[:, None],
        out=np.zeros_like(counts),
        where=occupancy[:, None] > 0,
    )
    return matrix, occupancy


def chapman_kolmogorov_tv(x0, x1, x2, nbins: int = 21) -> float:
    values = np.concatenate((x0, x1, x2))
    limit = float(np.quantile(np.abs(values), 0.995))
    edges = np.linspace(-limit, limit, nbins + 1)
    p01, occupancy = transition_matrix(x0, x1, edges)
    p12, _ = transition_matrix(x1, x2, edges)
    p02, _ = transition_matrix(x0, x2, edges)
    predicted = p01 @ p12
    weights = occupancy / occupancy.sum()
    return float(0.5 * np.sum(weights[:, None] * np.abs(p02 - predicted)))


def local_km_polynomial_fit(
    x_now,
    x_next,
    reference_sigma,
    delta_s,
    nbins: int = 25,
    min_count: int = 200,
):
    """Finite-step D1/D2/D4 fit; not a converged Kramers-Moyal estimator."""

    u = x_now / reference_sigma
    v = x_next / reference_sigma
    du = v - u
    limit = min(3.0, float(np.quantile(np.abs(u), 0.99)))
    edges = np.linspace(-limit, limit, nbins + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    index = np.digitize(u, edges) - 1
    d1 = np.full(nbins, np.nan)
    d2 = np.full(nbins, np.nan)
    d4 = np.full(nbins, np.nan)

    for b in range(nbins):
        mask = index == b
        if mask.sum() >= min_count:
            d1[b] = np.mean(du[mask]) / delta_s
            d2[b] = np.mean(du[mask] ** 2) / (2.0 * delta_s)
            d4[b] = np.mean(du[mask] ** 4) / (24.0 * delta_s)

    valid = np.isfinite(d1) & np.isfinite(d2) & np.isfinite(d4) & (np.abs(centers) < 2.0)
    drift_basis = np.column_stack((centers[valid], centers[valid] ** 3))
    even_basis = np.column_stack((np.ones(valid.sum()), centers[valid] ** 2))
    drift = np.linalg.lstsq(drift_basis, d1[valid], rcond=None)[0]
    diffusion = np.linalg.lstsq(even_basis, d2[valid], rcond=None)[0]
    fourth = np.linalg.lstsq(even_basis, d4[valid], rcond=None)[0]
    return {
        "a1": float(drift[0]),
        "a3": float(drift[1]),
        "b0": float(diffusion[0]),
        "b2": float(diffusion[1]),
        "c0": float(fourth[0]),
        "c2": float(fourth[1]),
    }


def collect_increments(samples, indices, cfg, grid):
    x_pool = [[] for _ in SHIFTS]
    y_pool = [[] for _ in SHIFTS]
    for index in indices:
        x_values, y_values = directional_increment_ensemble(
            samples[index][0], SHIFTS, cfg, grid
        )
        for j in range(len(SHIFTS)):
            x_pool[j].append(x_values[j])
            y_pool[j].append(y_values[j])
    return [np.concatenate(v) for v in x_pool], [np.concatenate(v) for v in y_pool]


def relative_linear_change(t, values) -> float:
    slope = np.polyfit(t, values, 1)[0]
    return float(slope * (t[-1] - t[0]) / max(abs(np.mean(values)), 1.0e-30))


def analyze_seed(seed: int, modified_coupling: bool):
    cfg = MHWConfig(seed=seed, tmax=500.0, modified_coupling=modified_coupling)
    diagnostics, samples, grid = simulate(cfg)
    selected = np.flatnonzero(
        (diagnostics[:, 0] >= TMIN) & (diagnostics[:, 0] <= TMAX)
    )
    x_values, y_values = collect_increments(samples, selected, cfg, grid)
    result = {
        "seed": seed,
        "mean_zonal_fraction": float(np.mean(diagnostics[selected, 3])),
        "mean_nonzonal_energy": float(np.mean(diagnostics[selected, 2])),
        "relative_zonal_trend": relative_linear_change(
            diagnostics[selected, 0], diagnostics[selected, 3]
        ),
        "relative_nonzonal_energy_trend": relative_linear_change(
            diagnostics[selected, 0], diagnostics[selected, 2]
        ),
        "directions": {},
    }

    for name, values in (("x", x_values), ("y", y_values)):
        reference_sigma = float(np.std(values[0]))
        multistep = []
        for j, next_shift in enumerate(SHIFTS[1:5], start=1):
            delta_s = float(np.log(SHIFTS[0] / next_shift))
            fit = local_km_polynomial_fit(
                values[0], values[j], reference_sigma, delta_s
            )
            multistep.append({"next_shift": next_shift, "delta_s": delta_s, **fit})
        result["directions"][name] = {
            "sigma_r8": reference_sigma,
            "ck_tv_8_4_2": chapman_kolmogorov_tv(values[0], values[4], values[6]),
            "ck_tv_4_2_1": chapman_kolmogorov_tv(values[4], values[6], values[7]),
            "km_from_r8": multistep,
        }

    if modified_coupling:
        zfrac = diagnostics[selected, 3]
        split = float(np.median(zfrac))
        groups = {
            "low": selected[zfrac <= split],
            "high": selected[zfrac > split],
        }
        result["within_mhw_zf_split"] = {"split": split, "directions": {}}
        for direction, direction_index in (("x", 0), ("y", 1)):
            group_values = {}
            for group_name, indices in groups.items():
                incs = collect_increments(samples, indices, cfg, grid)[direction_index]
                group_values[group_name] = incs
            reference_sigma = float(np.std(group_values["low"][4]))
            low_fit = local_km_polynomial_fit(
                group_values["low"][4],
                group_values["low"][6],
                reference_sigma,
                np.log(2.0),
            )
            high_fit = local_km_polynomial_fit(
                group_values["high"][4],
                group_values["high"][6],
                reference_sigma,
                np.log(2.0),
            )
            result["within_mhw_zf_split"]["directions"][direction] = {
                "mean_zf_low": float(np.mean(diagnostics[groups["low"], 3])),
                "mean_zf_high": float(np.mean(diagnostics[groups["high"], 3])),
                "b0_low": low_fit["b0"],
                "b0_high": high_fit["b0"],
                "b0_ratio_high_low": high_fit["b0"] / low_fit["b0"],
                "a1_low": low_fit["a1"],
                "a1_high": high_fit["a1"],
                "c0_low": low_fit["c0"],
                "c0_high": high_fit["c0"],
                "ck842_low": chapman_kolmogorov_tv(
                    group_values["low"][0],
                    group_values["low"][4],
                    group_values["low"][6],
                ),
                "ck842_high": chapman_kolmogorov_tv(
                    group_values["high"][0],
                    group_values["high"][4],
                    group_values["high"][6],
                ),
                "ck421_low": chapman_kolmogorov_tv(
                    group_values["low"][4],
                    group_values["low"][6],
                    group_values["low"][7],
                ),
                "ck421_high": chapman_kolmogorov_tv(
                    group_values["high"][4],
                    group_values["high"][6],
                    group_values["high"][7],
                ),
            }
    return result


def bootstrap_mean_ci(values, seed=123, n_boot=20000):
    values = np.asarray(values, dtype=float)
    rng = np.random.default_rng(seed)
    means = values[rng.integers(0, len(values), size=(n_boot, len(values)))].mean(axis=1)
    return {
        "mean": float(values.mean()),
        "ci95": [float(v) for v in np.quantile(means, (0.025, 0.975))],
    }


def summarize(mhw, hw):
    out = {"within_mhw": {}, "mhw_vs_hw": {}, "pawula_gate": {}}
    for direction in ("x", "y"):
        within = [v["within_mhw_zf_split"]["directions"][direction] for v in mhw]
        out["within_mhw"][direction] = {
            "b0_ratio_high_low": bootstrap_mean_ci(
                [v["b0_ratio_high_low"] for v in within]
            ),
            "a1_change_high_minus_low": bootstrap_mean_ci(
                [v["a1_high"] - v["a1_low"] for v in within]
            ),
            "ck842_change_high_minus_low": bootstrap_mean_ci(
                [v["ck842_high"] - v["ck842_low"] for v in within]
            ),
            "ck421_change_high_minus_low": bootstrap_mean_ci(
                [v["ck421_high"] - v["ck421_low"] for v in within]
            ),
        }

        out["mhw_vs_hw"][direction] = {}
        for step_index in (0, 3):
            next_shift = mhw[0]["directions"][direction]["km_from_r8"][step_index][
                "next_shift"
            ]
            mhw_b0 = np.asarray(
                [
                    v["directions"][direction]["km_from_r8"][step_index]["b0"]
                    for v in mhw
                ]
            )
            hw_b0 = np.asarray(
                [
                    v["directions"][direction]["km_from_r8"][step_index]["b0"]
                    for v in hw
                ]
            )
            out["mhw_vs_hw"][direction][f"8_to_{next_shift}_b0_ratio"] = (
                bootstrap_mean_ci(mhw_b0 / hw_b0)
            )

        delta_s = np.asarray(
            [v["delta_s"] for v in mhw[0]["directions"][direction]["km_from_r8"]]
        )
        for model_name, model_values in (("mhw", mhw), ("hw", hw)):
            intercepts = []
            for value in model_values:
                c0 = np.asarray(
                    [v["c0"] for v in value["directions"][direction]["km_from_r8"]]
                )
                intercepts.append(np.polyfit(delta_s, c0, 1)[1])
            out["pawula_gate"][f"{model_name}_{direction}_d4_intercept"] = (
                bootstrap_mean_ci(intercepts)
            )
    return out


def run_c2():
    mhw = [analyze_seed(seed, True) for seed in SEEDS]
    hw = [analyze_seed(seed, False) for seed in SEEDS]
    return {
        "configuration": {
            "seeds": list(SEEDS),
            "grid": [32, 32],
            "tmax": 500.0,
            "analysis_window": [TMIN, TMAX],
            "shifts": list(SHIFTS),
        },
        "mhw": mhw,
        "hw": hw,
        "summary": summarize(mhw, hw),
    }


if __name__ == "__main__":
    print(json.dumps(run_c2(), indent=2))
