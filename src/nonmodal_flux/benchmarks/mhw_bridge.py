from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class MHWConfig:
    """Numerical parameters for the exploratory Hasegawa-Wakatani bridge."""

    n: int = 32
    length: float = 40.0
    alpha: float = 1.0
    kappa: float = 1.0
    d_zeta: float = 2.0e-2
    d_n: float = 2.0e-2
    dt: float = 5.0e-2
    tmax: float = 320.0
    sample_every: int = 10
    seed: int = 3
    modified_coupling: bool = True


def spectral_grid(cfg: MHWConfig):
    dx = cfg.length / cfg.n
    k1 = 2.0 * np.pi * np.fft.fftfreq(cfg.n, d=dx)
    kx, ky = np.meshgrid(k1, k1, indexing="ij")
    k2 = kx**2 + ky**2
    k4 = k2**2
    invk2 = np.zeros_like(k2)
    invk2[k2 > 0] = 1.0 / k2[k2 > 0]
    modes = np.fft.fftfreq(cfg.n) * cfg.n
    mx, my = np.meshgrid(modes, modes, indexing="ij")
    dealias = (np.abs(mx) <= cfg.n / 3) & (np.abs(my) <= cfg.n / 3)
    zonal = np.isclose(ky, 0.0)
    return kx, ky, k2, k4, invk2, dealias, zonal


def potential_hat(zeta_hat: np.ndarray, invk2: np.ndarray) -> np.ndarray:
    phi_hat = -zeta_hat * invk2
    phi_hat = phi_hat.copy()
    phi_hat[0, 0] = 0.0
    return phi_hat


def mhw_rhs(
    zeta_hat: np.ndarray,
    n_hat: np.ndarray,
    cfg: MHWConfig,
    grid=None,
):
    """Return the pseudo-spectral HW/mHW right-hand side.

    With ``modified_coupling=True`` the resistive/adiabatic coupling
    alpha(phi-n) is removed for zonal ky=0 modes (Numata-style mHW).
    With ``modified_coupling=False`` the same coupling is applied to all
    non-constant modes, giving the original-HW control used in C2.
    """

    if grid is None:
        grid = spectral_grid(cfg)
    kx, ky, _k2, k4, invk2, dealias, zonal = grid
    phi_hat = potential_hat(zeta_hat, invk2)

    phi_x = np.fft.ifft2(1j * kx * phi_hat).real
    phi_y = np.fft.ifft2(1j * ky * phi_hat).real
    zeta_x = np.fft.ifft2(1j * kx * zeta_hat).real
    zeta_y = np.fft.ifft2(1j * ky * zeta_hat).real
    n_x = np.fft.ifft2(1j * kx * n_hat).real
    n_y = np.fft.ifft2(1j * ky * n_hat).real

    bracket_zeta = np.fft.fft2(phi_x * zeta_y - phi_y * zeta_x) * dealias
    bracket_n = np.fft.fft2(phi_x * n_y - phi_y * n_x) * dealias

    coupling = cfg.alpha * (phi_hat - n_hat)
    if cfg.modified_coupling:
        coupling = coupling * (~zonal)

    dzeta = (-bracket_zeta + coupling - cfg.d_zeta * k4 * zeta_hat) * dealias
    dn = (
        -bracket_n
        + coupling
        - 1j * cfg.kappa * ky * phi_hat
        - cfg.d_n * k4 * n_hat
    ) * dealias
    dzeta[0, 0] = 0.0
    dn[0, 0] = 0.0
    return dzeta, dn


def kinetic_energy_partition(zeta_hat: np.ndarray, cfg: MHWConfig, grid=None):
    """Return zonal and non-zonal ExB kinetic energies."""

    if grid is None:
        grid = spectral_grid(cfg)
    _kx, _ky, k2, _k4, invk2, _dealias, zonal = grid
    phi_hat = potential_hat(zeta_hat, invk2)
    norm = cfg.n**4
    e_zonal = 0.5 * np.sum(k2[zonal] * np.abs(phi_hat[zonal]) ** 2) / norm
    e_nonzonal = 0.5 * np.sum(k2[~zonal] * np.abs(phi_hat[~zonal]) ** 2) / norm
    return float(e_zonal), float(e_nonzonal)


def shell_kinetic_energy(
    zeta_hat: np.ndarray,
    edges: np.ndarray,
    cfg: MHWConfig,
    grid=None,
):
    """Return non-zonal kinetic energy in radial |k| shells."""

    if grid is None:
        grid = spectral_grid(cfg)
    _kx, _ky, k2, _k4, invk2, _dealias, zonal = grid
    phi_hat = potential_hat(zeta_hat, invk2)
    kmag = np.sqrt(k2)
    norm = cfg.n**4
    out = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        mask = (kmag >= lo) & (kmag < hi) & (~zonal)
        out.append(0.5 * np.sum(k2[mask] * np.abs(phi_hat[mask]) ** 2) / norm)
    return np.asarray(out, dtype=float)


def simulate(cfg: MHWConfig):
    """Integrate the exploratory HW/mHW benchmark from small random perturbations."""

    rng = np.random.default_rng(cfg.seed)
    grid = spectral_grid(cfg)
    *_, dealias, _zonal = grid
    zeta_hat = np.fft.fft2(1.0e-3 * rng.standard_normal((cfg.n, cfg.n))) * dealias
    n_hat = np.fft.fft2(1.0e-3 * rng.standard_normal((cfg.n, cfg.n))) * dealias
    zeta_hat[0, 0] = 0.0
    n_hat[0, 0] = 0.0

    samples = []
    diagnostics = []
    n_steps = int(round(cfg.tmax / cfg.dt))
    for step in range(n_steps):
        z1, n1 = mhw_rhs(zeta_hat, n_hat, cfg, grid)
        z2, n2 = mhw_rhs(
            zeta_hat + 0.5 * cfg.dt * z1,
            n_hat + 0.5 * cfg.dt * n1,
            cfg,
            grid,
        )
        z3, n3 = mhw_rhs(
            zeta_hat + 0.5 * cfg.dt * z2,
            n_hat + 0.5 * cfg.dt * n2,
            cfg,
            grid,
        )
        z4, n4 = mhw_rhs(zeta_hat + cfg.dt * z3, n_hat + cfg.dt * n3, cfg, grid)
        zeta_hat = zeta_hat + cfg.dt * (z1 + 2 * z2 + 2 * z3 + z4) / 6.0
        n_hat = n_hat + cfg.dt * (n1 + 2 * n2 + 2 * n3 + n4) / 6.0
        zeta_hat *= dealias
        n_hat *= dealias
        if step % cfg.sample_every == 0:
            ez, enz = kinetic_energy_partition(zeta_hat, cfg, grid)
            diagnostics.append((step * cfg.dt, ez, enz, ez / max(ez + enz, 1e-30)))
            samples.append((zeta_hat.copy(), n_hat.copy()))
    return np.asarray(diagnostics), samples, grid


def directional_increment_ensemble(
    zeta_hat: np.ndarray,
    shifts: tuple[int, ...],
    cfg: MHWConfig,
    grid=None,
):
    """Return x- and y-directed non-zonal potential increments separately."""

    if grid is None:
        grid = spectral_grid(cfg)
    _kx, _ky, _k2, _k4, invk2, _dealias, zonal = grid
    phi_hat = potential_hat(zeta_hat, invk2)
    phi_hat[zonal] = 0.0
    phi = np.fft.ifft2(phi_hat).real
    x_values = []
    y_values = []
    for shift in shifts:
        x_values.append((np.roll(phi, -shift, axis=0) - phi).ravel())
        y_values.append((np.roll(phi, -shift, axis=1) - phi).ravel())
    return x_values, y_values


def increment_ensemble(
    zeta_hat: np.ndarray,
    shifts: tuple[int, ...],
    cfg: MHWConfig,
    grid=None,
):
    """Return pooled x/y non-zonal potential increments (C1 compatibility helper)."""

    x_values, y_values = directional_increment_ensemble(zeta_hat, shifts, cfg, grid)
    return [np.concatenate((x, y)) for x, y in zip(x_values, y_values)]


def gaussian_markov_cmi(x_large, x_mid, x_small):
    """Gaussian CMI proxy I(X_small; X_large | X_mid), in nats."""

    corr = np.corrcoef(np.vstack((x_large, x_mid, x_small)))
    denom = np.sqrt((1.0 - corr[0, 1] ** 2) * (1.0 - corr[1, 2] ** 2))
    rho = (corr[0, 2] - corr[0, 1] * corr[1, 2]) / denom
    rho = float(np.clip(rho, -1.0 + 1e-12, 1.0 - 1e-12))
    return float(-0.5 * np.log(1.0 - rho**2))


def normalized_second_km(x_now, x_next, delta_s=np.log(2.0)):
    """Return a global normalized second conditional-moment proxy."""

    delta = x_next - x_now
    return float(np.mean(delta**2) / (2.0 * delta_s * np.mean(x_now**2)))


def pilot_summary(cfg: MHWConfig, tmin: float = 120.0, tmax: float = 310.0):
    """Run the C1 benchmark and compare low/high zonal-flow ensembles."""

    diagnostics, samples, grid = simulate(cfg)
    selected = np.flatnonzero((diagnostics[:, 0] >= tmin) & (diagnostics[:, 0] <= tmax))
    zfrac = diagnostics[selected, 3]
    z_median = float(np.median(zfrac))
    groups = {
        "low_zf": selected[zfrac <= z_median],
        "high_zf": selected[zfrac > z_median],
    }
    edges = np.asarray([0.0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.6, 3.5])
    shifts = (8, 4, 2, 1)
    summary = {"zonal_fraction_split": z_median, "groups": {}}

    for name, indices in groups.items():
        shell = []
        increment_samples = [[] for _ in shifts]
        for idx in indices:
            zeta_hat, _n_hat = samples[idx]
            shell.append(shell_kinetic_energy(zeta_hat, edges, cfg, grid))
            vals = increment_ensemble(zeta_hat, shifts, cfg, grid)
            for j, val in enumerate(vals):
                increment_samples[j].append(val)
        increments = [np.concatenate(values) for values in increment_samples]
        summary["groups"][name] = {
            "n_snapshots": int(len(indices)),
            "mean_zonal_fraction": float(np.mean(diagnostics[indices, 3])),
            "mean_shell_energy": np.mean(np.asarray(shell), axis=0).tolist(),
            "gaussian_cmi_8_4_2": gaussian_markov_cmi(
                increments[0], increments[1], increments[2]
            ),
            "gaussian_cmi_4_2_1": gaussian_markov_cmi(
                increments[1], increments[2], increments[3]
            ),
            "d2norm_8_to_4": normalized_second_km(increments[0], increments[1]),
            "d2norm_4_to_2": normalized_second_km(increments[1], increments[2]),
            "d2norm_2_to_1": normalized_second_km(increments[2], increments[3]),
        }

    summary["shell_edges"] = edges.tolist()
    return summary
