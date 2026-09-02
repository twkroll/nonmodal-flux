"""Resolution/stability qualification for the frozen D10-ZF Pilot 0.1.

This test varies only the centered Fourier-Galerkin truncation m=-K,...,K.
No transport Gramian, energy gain, optimizer, angle, or finite-horizon CORE
quantity is evaluated here.
"""

import numpy as np

from nonmodal_flux.models.hasegawa_wakatani_zonal_flow import (
    hasegawa_wakatani_zonal_flow_matrices,
)


def _generator(K: int) -> np.ndarray:
    A, _, _, _, _ = hasegawa_wakatani_zonal_flow_matrices(
        modes=tuple(range(-K, K + 1)),
        ky=1.0,
        coupling=1.0,
        kappa=1.0,
        profile_coefficients={-1: 0.5, 1: 0.5},
        fundamental_wavenumber=1.0,
    )
    return np.asarray(A)


def _alpha(K: int) -> float:
    return float(np.max(np.linalg.eigvals(_generator(K)).real))


def test_frozen_resolution_family_remains_positive_but_decays_with_K() -> None:
    # Natural centered consecutive Galerkin family fixed by D10.1.
    Ks = list(range(1, 21))
    alphas = np.array([_alpha(K) for K in Ks])

    assert np.all(alphas > 0.0)
    assert np.all(np.diff(alphas) < 0.0)

    np.testing.assert_allclose(alphas[0], 0.080363511231768, rtol=0.0, atol=2.0e-10)
    np.testing.assert_allclose(alphas[-1], 0.018565580415321, rtol=0.0, atol=3.0e-9)


def test_high_resolution_checkpoints_do_not_support_positive_limit() -> None:
    checkpoints = {32: 0.012421402071483, 48: 0.008604182289240, 64: 0.006618238979012}
    measured = {K: _alpha(K) for K in checkpoints}

    for K, expected in checkpoints.items():
        np.testing.assert_allclose(measured[K], expected, rtol=0.0, atol=8.0e-8)

    assert measured[64] < measured[48] < measured[32]
    assert measured[64] < 0.007


def test_leading_real_parts_collapse_toward_zero_across_resolution() -> None:
    # Check the first three eigenvalues after sorting by real part.  Their
    # imaginary ordering may exchange between branches; only their real-part
    # envelope is used for this numerical qualification.
    for K in (8, 16, 32, 64):
        values = np.linalg.eigvals(_generator(K))
        leading = values[np.argsort(values.real)[::-1]][:3]
        assert np.all(leading.real > 0.0)

    leading_8 = np.linalg.eigvals(_generator(8))
    leading_64 = np.linalg.eigvals(_generator(64))
    top3_8 = np.sort(leading_8.real)[-3:]
    top3_64 = np.sort(leading_64.real)[-3:]

    assert np.max(top3_64) < 0.20 * np.max(top3_8)
    assert np.max(top3_64) < 0.007
