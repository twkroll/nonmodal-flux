"""Blind stability-only screen for D10-ZF Pilot 0.2.

The preregistration is research/d10_zf_pilot_0_2_blind_stability_preregistration.md.
Only spectra and spectral abscissae are evaluated.  No CORE, transport, energy,
or optimizer quantities are formed here.
"""

import numpy as np

from nonmodal_flux.models.hasegawa_wakatani_zonal_flow import (
    hasegawa_wakatani_zonal_flow_matrices,
)


KS = (32, 64, 96, 128)
NUS = (0.0, 0.005, 0.010, 0.015, 0.020, 0.030, 0.050)
SAFETY_MARGIN = 5.0e-3
EXPECTED_ALPHA0 = {
    32: 0.012421402071483274,
    64: 0.006618238979011768,
    96: 0.004507562028930615,
    128: 0.0034218752347878367,
}
EXPECTED_SELECTED_NU = 0.020


def _undamped_generator(K: int) -> np.ndarray:
    A, _, _, _, _ = hasegawa_wakatani_zonal_flow_matrices(
        modes=tuple(range(-K, K + 1)),
        ky=1.0,
        coupling=1.0,
        kappa=1.0,
        profile_coefficients={-1: 0.5, 1: 0.5},
        fundamental_wavenumber=1.0,
    )
    return A


def _spectral_abscissa(A: np.ndarray) -> float:
    return float(np.max(np.linalg.eigvals(A).real))


def test_preregistered_undamped_high_resolution_abscissae() -> None:
    for K in KS:
        alpha = _spectral_abscissa(_undamped_generator(K))
        np.testing.assert_allclose(alpha, EXPECTED_ALPHA0[K], rtol=0.0, atol=3.0e-10)


def test_uniform_damping_shifts_the_spectrum_and_selects_smallest_qualified_value() -> None:
    # A_nu = A_0 - nu I, so the entire spectrum shifts rigidly by -nu.
    alpha0 = {K: _spectral_abscissa(_undamped_generator(K)) for K in KS}

    qualifies = []
    for nu in NUS:
        worst_alpha = max(alpha0[K] - nu for K in KS)
        qualifies.append(worst_alpha <= -SAFETY_MARGIN)

    assert qualifies == [False, False, False, False, True, True, True]
    selected = next(nu for nu, ok in zip(NUS, qualifies, strict=True) if ok)
    assert selected == EXPECTED_SELECTED_NU

    expected_selected = {
        32: -0.0075785979285167265,
        64: -0.013381761020988233,
        96: -0.015492437971069386,
        128: -0.016578124765212164,
    }
    for K in KS:
        A0 = _undamped_generator(K)
        Anu = A0 - selected * np.eye(A0.shape[0], dtype=np.complex128)
        alpha = _spectral_abscissa(Anu)
        np.testing.assert_allclose(alpha, expected_selected[K], rtol=0.0, atol=3.0e-10)
        assert alpha <= -SAFETY_MARGIN
