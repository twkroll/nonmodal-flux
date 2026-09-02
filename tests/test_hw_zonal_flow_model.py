"""Production-model tests for the D10-ZF Fourier-Galerkin assembler."""

import numpy as np
import pytest

from nonmodal_flux.models import (
    hasegawa_wakatani_zonal_flow_matrices,
    make_hasegawa_wakatani_zonal_flow_problem,
)


def _profile() -> dict[int, complex]:
    return {1: 0.1, -1: 0.1}


def test_production_matrices_satisfy_physical_multichannel_balance() -> None:
    generator, metric, q_gamma, q_u, dissipation = (
        hasegawa_wakatani_zonal_flow_matrices(
            modes=np.arange(-3, 4),
            ky=1.0,
            coupling=1.0,
            kappa=1.0,
            profile_coefficients=_profile(),
        )
    )

    balance = generator.conj().T @ metric + metric @ generator
    expected = 2.0 * q_gamma + 2.0 * q_u - dissipation

    np.testing.assert_allclose(metric, metric.conj().T, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(q_gamma, q_gamma.conj().T, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(q_u, q_u.conj().T, rtol=0.0, atol=3.0e-16)
    assert np.linalg.eigvalsh(metric)[0] > 0.0
    assert np.linalg.eigvalsh(dissipation)[0] > -2.0e-14
    np.testing.assert_allclose(balance, expected, rtol=0.0, atol=6.0e-15)


def test_problem_constructor_targets_particle_flux_and_uses_natural_energy_input() -> None:
    modes = np.arange(-2, 3)
    problem = make_hasegawa_wakatani_zonal_flow_problem(
        modes=modes,
        ky=1.0,
        coupling=1.0,
        kappa=1.0,
        profile_coefficients=_profile(),
    )
    generator, metric, q_gamma, _, _ = hasegawa_wakatani_zonal_flow_matrices(
        modes=modes,
        ky=1.0,
        coupling=1.0,
        kappa=1.0,
        profile_coefficients=_profile(),
    )

    assert problem.state_dim == 2 * len(modes)
    assert problem.input_dim == problem.state_dim
    assert problem.uses_natural_energy_input_metric()
    np.testing.assert_allclose(problem.A, generator, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(problem.M, metric, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(problem.Q, q_gamma, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(problem.Rin, metric, rtol=0.0, atol=0.0)


def test_pure_potential_galerkin_input_space_is_multidimensional_and_transport_neutral() -> None:
    modes = np.arange(-2, 3)
    count = len(modes)
    input_map = np.vstack(
        [
            np.eye(count, dtype=np.complex128),
            np.zeros((count, count), dtype=np.complex128),
        ]
    )

    problem = make_hasegawa_wakatani_zonal_flow_problem(
        modes=modes,
        ky=1.0,
        coupling=1.0,
        kappa=1.0,
        profile_coefficients=_profile(),
        B=input_map,
    )

    assert problem.input_dim == count
    assert problem.is_transport_neutral()
    assert problem.uses_natural_energy_input_metric()
    np.testing.assert_allclose(
        problem.Rin,
        np.diag(modes.astype(float) ** 2 + 1.0),
        rtol=0.0,
        atol=0.0,
    )


def test_profile_coefficients_must_represent_a_real_zonal_velocity() -> None:
    with pytest.raises(ValueError, match="real U"):
        hasegawa_wakatani_zonal_flow_matrices(
            modes=np.arange(-2, 3),
            ky=1.0,
            coupling=1.0,
            kappa=1.0,
            profile_coefficients={1: 0.1},
        )

    with pytest.raises(ValueError, match="real U"):
        hasegawa_wakatani_zonal_flow_matrices(
            modes=np.arange(-2, 3),
            ky=1.0,
            coupling=1.0,
            kappa=1.0,
            profile_coefficients={0: 0.1j},
        )


def test_invalid_structural_parameters_are_rejected() -> None:
    base = dict(
        modes=np.arange(-2, 3),
        ky=1.0,
        coupling=1.0,
        kappa=1.0,
        profile_coefficients=_profile(),
    )

    with pytest.raises(ValueError, match="ky != 0"):
        hasegawa_wakatani_zonal_flow_matrices(**{**base, "ky": 0.0})
    with pytest.raises(ValueError, match="nonnegative"):
        hasegawa_wakatani_zonal_flow_matrices(**{**base, "coupling": -1.0})
    with pytest.raises(ValueError, match="nonnegative"):
        hasegawa_wakatani_zonal_flow_matrices(**{**base, "kappa": -1.0})
    with pytest.raises(ValueError, match="positive"):
        hasegawa_wakatani_zonal_flow_matrices(
            **{**base, "fundamental_wavenumber": 0.0}
        )
    with pytest.raises(ValueError, match="unique"):
        hasegawa_wakatani_zonal_flow_matrices(**{**base, "modes": [0, 1, 1]})
