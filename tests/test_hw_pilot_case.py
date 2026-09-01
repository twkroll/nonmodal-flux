"""Diagnostics for the single spectrally stable D2-A Hasegawa-Wakatani pilot."""

import numpy as np
import scipy.linalg

from nonmodal_flux.core.gramians import accumulated_input_transport_operator
from nonmodal_flux.models.hasegawa_wakatani import (
    hasegawa_wakatani_matrices,
    make_hasegawa_wakatani_problem,
)


PILOT = dict(
    kx=0.5,
    ky=1.0,
    coupling=1.0,
    kappa=1.0,
    damping=0.15,
)


def test_selected_pilot_is_spectrally_stable_and_metric_nonnormal() -> None:
    generator, metric, _, _ = hasegawa_wakatani_matrices(**PILOT)

    eigenvalues = np.linalg.eigvals(generator)
    assert np.max(np.real(eigenvalues)) < -0.06

    metric_sqrt = scipy.linalg.sqrtm(metric)
    inverse_metric_sqrt = scipy.linalg.solve(metric_sqrt, np.eye(2))
    energy_coordinate_generator = metric_sqrt @ generator @ inverse_metric_sqrt
    normality_commutator = (
        energy_coordinate_generator.conj().T @ energy_coordinate_generator
        - energy_coordinate_generator @ energy_coordinate_generator.conj().T
    )
    assert np.linalg.norm(normality_commutator, ord="fro") > 1.0


def test_selected_pilot_has_exact_balance_and_strict_energy_contraction() -> None:
    generator, metric, particle_flux, sink = hasegawa_wakatani_matrices(**PILOT)

    balance = generator.conj().T @ metric + metric @ generator
    expected = 2.0 * PILOT["kappa"] * particle_flux - sink
    np.testing.assert_allclose(balance, expected, rtol=0.0, atol=3.0e-14)

    balance_eigenvalues = np.linalg.eigvalsh(balance)
    assert balance_eigenvalues[-1] < -0.10
    assert np.linalg.eigvalsh(sink)[0] > 0.0

    lower = np.linalg.cholesky(metric)
    inverse_lower = np.linalg.solve(lower, np.eye(2))
    whitened_balance = inverse_lower @ balance @ inverse_lower.conj().T
    generalized_rates = np.linalg.eigvalsh(whitened_balance)
    assert generalized_rates[-1] < -0.09


def test_pure_potential_input_is_transport_neutral_but_generates_positive_flux() -> None:
    input_map = np.array([[1.0], [0.0]], dtype=np.complex128)
    problem = make_hasegawa_wakatani_problem(**PILOT, B=input_map)

    assert problem.is_transport_neutral()
    assert problem.uses_natural_energy_input_metric()
    np.testing.assert_allclose(problem.Rin, np.array([[1.25]]), rtol=0.0, atol=0.0)

    first_transport_derivative = (
        problem.A.conj().T @ problem.Q + problem.Q @ problem.A
    )
    normalized_h1 = (
        input_map.conj().T @ first_transport_derivative @ input_map / problem.Rin
    )
    np.testing.assert_allclose(normalized_h1, np.array([[0.8]]), rtol=0.0, atol=3.0e-14)

    horizon = 1.0
    accumulated = np.asarray(accumulated_input_transport_operator(problem, horizon))
    normalized_transport = float(np.real(accumulated[0, 0] / problem.Rin[0, 0]))
    assert normalized_transport > 0.13

    propagator = scipy.linalg.expm(problem.A * horizon)
    final_state = propagator @ input_map
    initial_energy = float(np.real(input_map.conj().T @ problem.M @ input_map)[0, 0])
    final_energy = float(np.real(final_state.conj().T @ problem.M @ final_state)[0, 0])
    assert final_energy / initial_energy < 0.57


def test_single_mode_flux_form_has_only_one_positive_and_one_negative_direction() -> None:
    _, _, particle_flux, _ = hasegawa_wakatani_matrices(**PILOT)

    eigenvalues = np.linalg.eigvalsh(particle_flux)
    assert eigenvalues[0] < 0.0 < eigenvalues[1]
    assert np.linalg.det(particle_flux) < 0.0
