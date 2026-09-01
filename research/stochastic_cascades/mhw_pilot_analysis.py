from __future__ import annotations

import json

import numpy as np

from nonmodal_flux.benchmarks.mhw_bridge import MHWConfig, increment_ensemble, simulate


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
    """Weighted total-variation error of P(2|0) versus P(2|1)P(1|0)."""

    vals = np.concatenate((x0, x1, x2))
    limit = float(np.quantile(np.abs(vals), 0.995))
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
    nbins: int = 25,
    delta_s=np.log(2.0),
):
    """Fit D1=a1*u+a3*u^3 and D2=b0+b2*u^2 for one scale step.

    u is normalized by a fixed reference sigma so that low/high-ZF coefficients
    remain directly comparable.  This is still a finite-step pilot estimator,
    not a delta-s -> 0 extrapolation.
    """

    u = x_now / reference_sigma
    v = x_next / reference_sigma
    du = v - u
    limit = min(3.0, float(np.quantile(np.abs(u), 0.99)))
    edges = np.linspace(-limit, limit, nbins + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    index = np.digitize(u, edges) - 1
    d1 = np.full(nbins, np.nan)
    d2 = np.full(nbins, np.nan)
    for b in range(nbins):
        mask = index == b
        if mask.sum() >= 300:
            d1[b] = np.mean(du[mask]) / delta_s
            d2[b] = np.mean(du[mask] ** 2) / (2.0 * delta_s)
    valid = np.isfinite(d1) & np.isfinite(d2) & (np.abs(centers) < 2.0)
    drift_basis = np.column_stack((centers[valid], centers[valid] ** 3))
    diffusion_basis = np.column_stack((np.ones(valid.sum()), centers[valid] ** 2))
    drift = np.linalg.lstsq(drift_basis, d1[valid], rcond=None)[0]
    diffusion = np.linalg.lstsq(diffusion_basis, d2[valid], rcond=None)[0]
    return drift, diffusion


def extended_summary(cfg=MHWConfig(), tmin=120.0, tmax=310.0):
    diagnostics, samples, grid = simulate(cfg)
    selected = np.flatnonzero((diagnostics[:, 0] >= tmin) & (diagnostics[:, 0] <= tmax))
    zfrac = diagnostics[selected, 3]
    split = float(np.median(zfrac))
    groups = {
        "low_zf": selected[zfrac <= split],
        "high_zf": selected[zfrac > split],
    }
    shifts = (8, 4, 2, 1)
    increments = {}
    for name, indices in groups.items():
        pooled = [[] for _ in shifts]
        for idx in indices:
            values = increment_ensemble(samples[idx][0], shifts, cfg, grid)
            for j, value in enumerate(values):
                pooled[j].append(value)
        increments[name] = [np.concatenate(v) for v in pooled]

    reference_sigma = float(np.std(increments["low_zf"][1]))
    out = {"zonal_fraction_split": split, "reference_sigma_r4": reference_sigma, "groups": {}}
    for name, values in increments.items():
        drift, diffusion = local_km_polynomial_fit(values[1], values[2], reference_sigma)
        out["groups"][name] = {
            "mean_zonal_fraction": float(np.mean(diagnostics[groups[name], 3])),
            "ck_tv_8_4_2": chapman_kolmogorov_tv(values[0], values[1], values[2]),
            "ck_tv_4_2_1": chapman_kolmogorov_tv(values[1], values[2], values[3]),
            "drift_fit_r4_to_r2": drift.tolist(),
            "diffusion_fit_r4_to_r2": diffusion.tolist(),
        }
    return out


if __name__ == "__main__":
    print(json.dumps(extended_summary(), indent=2))
