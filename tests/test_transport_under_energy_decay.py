"""Tests for positive signed transport despite monotone physical-energy decay."""

import numpy as np

from nonmodal_flux.core.gramians import accumulated_signed_extrema
from nonmodal_flux.core.outputs import terminal_signed_extrema
from nonmodal_flux.core.problem import TransportProblem
from nonmodal_flux.core.propagators import constant_propagator


def _contractive_transport_witness(kappa: float = 1.5) -> TransportProblem:
    """Return a stable transport-neutral witness with globally contractive energy."""

    return TransportProblem(
        A=np.array([[-1.0, 0.0], [kappa, -2.0]]),
        M=np.eye(2),
        Q=0.5 * np.array([[0.0, 1.0], [1.0, 0.0]]),
        B=np.array([[1.0], [0.0]]),
        Rin=np.array([[1.0]]),
    )


def test_witness_is_energy_contractive_transport_neutral_and_generates_positive_flux() -> None:
    kappa = 1.5
    problem = _contractive_transport_witness(kappa=kappa)

    assert problem.uses_natural_energy_input_metric()
    assert problem.is_transport_neutral()

    energy_generator = problem.A.conj().T @ problem.M + problem.M @ problem.A
    energy_rates = np.linalg.eigvalsh(energy_generator)
    assert energy_rates[-1] < 0.0

    first_transport_generation = problem.B.conj().T @ (
        problem.A.conj().T @ problem.Q + problem.Q @ problem.A
    ) @ problem.B
    np.testing.assert_allclose(
        first_transport_generation,
        np.array([[kappa]]),
        rtol=0.0,
        atol=1.0e-14,
    )
    assert first_transport_generation[0, 0] > 0.0


def test_terminal_energy_operator_is_contractive_at_finite_horizons() -> None:
    problem = _contractive_transport_witness()

    for horizon in (0.05, 0.4, 1.2):
        phi = np.asarray(constant_propagator(problem.A, horizon))
        energy_change = phi.conj().T @ problem.M @ phi - problem.M
        assert np.linalg.eigvalsh(energy_change)[-1] < 1.0e-12


def test_same_admissible_disturbance_loses_energy_but_produces_positive_transport() -> None:
    problem = _contractive_transport_witness()
    horizon = 0.2

    initial_state = problem.B[:, 0]
    initial_energy = float(np.real(initial_state.conj().T @ problem.M @ initial_state))

    phi = np.asarray(constant_propagator(problem.A, horizon))
    terminal_state = phi @ initial_state
    terminal_energy = float(np.real(terminal_state.conj().T @ problem.M @ terminal_state))

    terminal_min, terminal_max = terminal_signed_extrema(problem, horizon)
    accumulated_min, accumulated_max = accumulated_signed_extrema(problem, horizon)

    assert terminal_energy < initial_energy
    assert float(terminal_max) > 0.0
    assert float(accumulated_max) > 0.0
    np.testing.assert_allclose(terminal_min, terminal_max, rtol=0.0, atol=1.0e-14)
    np.testing.assert_allclose(accumulated_min, accumulated_max, rtol=0.0, atol=1.0e-14)


def test_positive_transport_has_t1_short_time_onset_under_energy_decay() -> None:
    kappa = 1.5
    problem = _contractive_transport_witness(kappa=kappa)
    horizon = 1.0e-3

    _, terminal_max = terminal_signed_extrema(problem, horizon)
    _, accumulated_max = accumulated_signed_extrema(problem, horizon)

    np.testing.assert_allclose(
        float(terminal_max) / horizon,
        kappa,
        rtol=3.0e-3,
        atol=1.0e-12,
    )
    np.testing.assert_allclose(
        float(accumulated_max) / (0.5 * horizon**2),
        kappa,
        rtol=2.0e-3,
        atol=1.0e-12,
    )
