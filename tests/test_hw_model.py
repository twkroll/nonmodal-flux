"""Tests for the minimal D2-A Hasegawa-Wakatani model constructor."""

import numpy as np
import pytest

from nonmodal_flux.models.hasegawa_wakatani import (
    hasegawa_wakatani_matrices,
    make_hasegawa_wakatani_problem,
)


def test_hw_matrices_reproduce_frozen_d2a_formulas() -> None:
    kx = 0.6
    ky = -0.9
    coupling = 1.7
    kappa = 0.8
    damping = 0.13
    k2 = kx**2 + ky**2

    generator, metric, particle_flux, sink = hasegawa_wakatani_matrices(
        kx=kx,
        ky=ky,
        coupling=coupling,
        kappa=kappa,
        damping=damping,
    )

    expected_generator = np.array(
        [
            [-coupling / k2 - damping, coupling / k2],
            [coupling - 1j * kappa * ky, -coupling - damping],
        ],
        dtype=np.complex128,
    )
    expected_metric = np.diag([k2, 1.0]).astype(np.complex128)
    expected_flux = 0.5 * ky * np.array(
        [[0.0, 1j], [-1j, 0.0]], dtype=np.complex128
    )
    expected_sink = (
        2.0
        * coupling
        * np.array([[1.0, -1.0], [-1.0, 1.0]], dtype=np.complex128)
        + 2.0 * damping * expected_metric
    )

    np.testing.assert_allclose(generator, expected_generator, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(metric, expected_metric, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(particle_flux, expected_flux, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(sink, expected_sink, rtol=0.0, atol=0.0)


def test_hw_matrices_satisfy_exact_energy_particle_flux_balance() -> None:
    generator, metric, particle_flux, sink = hasegawa_wakatani_matrices(
        kx=0.45,
        ky=1.05,
        coupling=1.25,
        kappa=0.72,
        damping=0.19,
    )

    left = generator.conj().T @ metric + metric @ generator
    right = 2.0 * 0.72 * particle_flux - sink

    np.testing.assert_allclose(left, right, rtol=0.0, atol=3.0e-14)
    np.testing.assert_allclose(metric, metric.conj().T, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(particle_flux, particle_flux.conj().T, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(sink, sink.conj().T, rtol=0.0, atol=0.0)
    assert np.min(np.linalg.eigvalsh(metric)) > 0.0
    assert np.min(np.linalg.eigvalsh(sink)) >= -2.0e-14
    flux_eigenvalues = np.linalg.eigvalsh(particle_flux)
    assert flux_eigenvalues[0] < 0.0 < flux_eigenvalues[-1]


def test_hw_problem_defaults_to_full_state_and_natural_energy_input_metric() -> None:
    problem = make_hasegawa_wakatani_problem(
        kx=0.5,
        ky=0.8,
        coupling=1.4,
        kappa=0.6,
    )
    generator, metric, particle_flux, _ = hasegawa_wakatani_matrices(
        kx=0.5,
        ky=0.8,
        coupling=1.4,
        kappa=0.6,
    )

    np.testing.assert_allclose(problem.A, generator, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(problem.M, metric, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(problem.Q, particle_flux, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(problem.B, np.eye(2), rtol=0.0, atol=0.0)
    np.testing.assert_allclose(problem.Rin, metric, rtol=0.0, atol=0.0)
    assert problem.uses_natural_energy_input_metric()
    assert not problem.is_transport_neutral()


def test_hw_problem_accepts_transport_neutral_restricted_input() -> None:
    input_map = np.array([[1.0], [0.0]], dtype=np.complex128)
    problem = make_hasegawa_wakatani_problem(
        kx=0.7,
        ky=1.1,
        coupling=1.3,
        kappa=0.9,
        B=input_map,
    )

    expected_rin = input_map.conj().T @ problem.M @ input_map
    np.testing.assert_allclose(problem.Rin, expected_rin, rtol=0.0, atol=0.0)
    assert problem.input_dim == 1
    assert problem.uses_natural_energy_input_metric()
    assert problem.is_transport_neutral()


def test_hw_problem_preserves_explicit_input_metric() -> None:
    input_map = np.array([[1.0], [0.4j]], dtype=np.complex128)
    input_metric = np.array([[2.5]], dtype=np.complex128)
    problem = make_hasegawa_wakatani_problem(
        kx=0.9,
        ky=0.6,
        coupling=0.8,
        kappa=1.0,
        damping=0.05,
        B=input_map,
        Rin=input_metric,
    )

    np.testing.assert_allclose(problem.B, input_map, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(problem.Rin, input_metric, rtol=0.0, atol=0.0)
    assert not problem.uses_natural_energy_input_metric()


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"kx": 0.5, "ky": 0.0, "coupling": 1.0, "kappa": 1.0}, "non-zonal"),
        ({"kx": 0.5, "ky": 0.8, "coupling": -0.1, "kappa": 1.0}, "coupling"),
        ({"kx": 0.5, "ky": 0.8, "coupling": 1.0, "kappa": -0.1}, "kappa"),
        (
            {"kx": 0.5, "ky": 0.8, "coupling": 1.0, "kappa": 1.0, "damping": -0.1},
            "damping",
        ),
        ({"kx": np.nan, "ky": 0.8, "coupling": 1.0, "kappa": 1.0}, "finite"),
    ],
)
def test_hw_matrices_reject_parameters_outside_frozen_pilot_domain(
    kwargs: dict[str, float], message: str
) -> None:
    with pytest.raises(ValueError, match=message):
        hasegawa_wakatani_matrices(**kwargs)
