import numpy as np

from nonmodal_flux.benchmarks.mhw_bridge import (
    MHWConfig,
    directional_increment_ensemble,
    kinetic_energy_partition,
    mhw_rhs,
    shell_kinetic_energy,
    spectral_grid,
)


def _pure_zonal_state(cfg):
    zeta_hat = np.zeros((cfg.n, cfg.n), dtype=complex)
    n_hat = np.zeros_like(zeta_hat)
    zeta_hat[2, 0] = 1.0 + 0.2j
    n_hat[2, 0] = -0.4 + 0.1j
    return zeta_hat, n_hat


def test_modified_coupling_vanishes_for_zonal_modes():
    cfg = MHWConfig(
        n=16,
        length=20.0,
        d_zeta=0.0,
        d_n=0.0,
        kappa=0.0,
        modified_coupling=True,
    )
    grid = spectral_grid(cfg)
    *_, zonal = grid
    zeta_hat, n_hat = _pure_zonal_state(cfg)
    dzeta, dn = mhw_rhs(zeta_hat, n_hat, cfg, grid)

    assert np.allclose(dzeta[zonal], 0.0)
    assert np.allclose(dn[zonal], 0.0)


def test_original_hw_control_retains_zonal_coupling():
    cfg = MHWConfig(
        n=16,
        length=20.0,
        d_zeta=0.0,
        d_n=0.0,
        kappa=0.0,
        modified_coupling=False,
    )
    grid = spectral_grid(cfg)
    zeta_hat, n_hat = _pure_zonal_state(cfg)
    dzeta, dn = mhw_rhs(zeta_hat, n_hat, cfg, grid)

    assert not np.allclose(dzeta[2, 0], 0.0)
    assert not np.allclose(dn[2, 0], 0.0)
    assert np.allclose(dzeta[2, 0], dn[2, 0])


def test_shells_partition_nonzonal_kinetic_energy():
    cfg = MHWConfig(n=16, length=20.0)
    grid = spectral_grid(cfg)
    *_, dealias, _zonal = grid
    rng = np.random.default_rng(1)
    zeta_hat = np.fft.fft2(rng.standard_normal((cfg.n, cfg.n))) * dealias

    e_zonal, e_nonzonal = kinetic_energy_partition(zeta_hat, cfg, grid)
    edges = np.linspace(0.0, 10.0, 101)
    shell_energy = shell_kinetic_energy(zeta_hat, edges, cfg, grid)

    assert e_zonal >= 0.0
    assert np.isclose(shell_energy.sum(), e_nonzonal, rtol=1e-12, atol=1e-12)


def test_directional_increments_are_kept_separate():
    cfg = MHWConfig(n=16, length=20.0)
    grid = spectral_grid(cfg)
    *_, dealias, _zonal = grid
    rng = np.random.default_rng(2)
    zeta_hat = np.fft.fft2(rng.standard_normal((cfg.n, cfg.n))) * dealias

    shifts = (4, 2, 1)
    x_values, y_values = directional_increment_ensemble(zeta_hat, shifts, cfg, grid)

    assert len(x_values) == len(shifts)
    assert len(y_values) == len(shifts)
    assert all(v.shape == (cfg.n * cfg.n,) for v in x_values + y_values)
    assert not np.allclose(x_values[0], y_values[0])
