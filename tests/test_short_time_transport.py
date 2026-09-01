"""Tests for T1 short-time transport generation from neutral inputs."""

import numpy as np

from nonmodal_flux.core.gramians import whitened_accumulated_input_transport_operator
from nonmodal_flux.core.outputs import whitened_terminal_signed_output_operator
from nonmodal_flux.core.problem import TransportProblem


def _t1_witness(kappa: float = 1.7, rin: float = 2.3) -> TransportProblem:
    return TransportProblem(
        A=np.array([[-1.0, 0.0], [kappa, -2.0]]),
        M=np.eye(2),
        Q=0.5 * np.array([[0.0, 1.0], [1.0, 0.0]]),
        B=np.array([[1.0], [0.0]]),
        Rin=np.array([[rin]]),
    )


def _psd_neutral_witness(kappa: float = 1.7, rin: float = 2.3) -> TransportProblem:
    return TransportProblem(
        A=np.array([[-1.0, 0.0], [kappa, -2.0]]),
        M=np.eye(2),
        Q=np.array([[0.0, 0.0], [0.0, 1.0]]),
        B=np.array([[1.0], [0.0]]),
        Rin=np.array([[rin]]),
    )


def _scalar(operator: object) -> float:
    value = np.asarray(operator)[0, 0]
    np.testing.assert_allclose(np.imag(value), 0.0, rtol=0.0, atol=1.0e-13)
    return float(np.real(value))


def test_indefinite_transport_neutral_witness_has_nonzero_first_generation() -> None:
    kappa = 1.7
    rin = 2.3
    problem = _t1_witness(kappa=kappa, rin=rin)

    projected_transport = problem.B.conj().T @ problem.Q @ problem.B
    np.testing.assert_allclose(projected_transport, 0.0, rtol=0.0, atol=1.0e-14)
    assert np.linalg.norm(problem.Q @ problem.B) > 0.0

    q_eigenvalues = np.linalg.eigvalsh(problem.Q)
    assert q_eigenvalues[0] < 0.0 < q_eigenvalues[-1]

    lie_derivative = problem.A.conj().T @ problem.Q + problem.Q @ problem.A
    raw_h1 = problem.B.conj().T @ lie_derivative @ problem.B
    np.testing.assert_allclose(raw_h1, np.array([[kappa]]), rtol=0.0, atol=1.0e-14)

    whitened_h1 = raw_h1[0, 0] / rin
    np.testing.assert_allclose(whitened_h1, kappa / rin, rtol=0.0, atol=1.0e-14)
    assert whitened_h1 > 0.0


def test_t1_witness_matches_exact_terminal_and_accumulated_transport() -> None:
    kappa = 1.7
    rin = 2.3
    horizon = 0.37
    problem = _t1_witness(kappa=kappa, rin=rin)

    terminal = _scalar(whitened_terminal_signed_output_operator(problem, horizon))
    accumulated = _scalar(
        whitened_accumulated_input_transport_operator(problem, horizon)
    )

    terminal_exact = (kappa / rin) * (
        np.exp(-2.0 * horizon) - np.exp(-3.0 * horizon)
    )
    accumulated_exact = (kappa / rin) * (
        (1.0 - np.exp(-2.0 * horizon)) / 2.0
        - (1.0 - np.exp(-3.0 * horizon)) / 3.0
    )

    np.testing.assert_allclose(terminal, terminal_exact, rtol=2.0e-12, atol=2.0e-13)
    np.testing.assert_allclose(accumulated, accumulated_exact, rtol=2.0e-12, atol=2.0e-13)


def test_transport_neutral_short_time_orders_are_linear_and_quadratic() -> None:
    kappa = 1.7
    rin = 2.3
    problem = _t1_witness(kappa=kappa, rin=rin)
    h1 = kappa / rin

    horizon = 2.0e-2
    half_horizon = horizon / 2.0

    terminal = _scalar(whitened_terminal_signed_output_operator(problem, horizon))
    terminal_half = _scalar(
        whitened_terminal_signed_output_operator(problem, half_horizon)
    )
    accumulated = _scalar(
        whitened_accumulated_input_transport_operator(problem, horizon)
    )
    accumulated_half = _scalar(
        whitened_accumulated_input_transport_operator(problem, half_horizon)
    )

    terminal_residual = abs(terminal - horizon * h1)
    terminal_half_residual = abs(terminal_half - half_horizon * h1)
    accumulated_residual = abs(accumulated - 0.5 * horizon**2 * h1)
    accumulated_half_residual = abs(
        accumulated_half - 0.5 * half_horizon**2 * h1
    )

    assert terminal_residual > 0.0
    assert accumulated_residual > 0.0
    np.testing.assert_allclose(
        terminal_half_residual / terminal_residual,
        0.25,
        rtol=0.0,
        atol=1.0e-2,
    )
    np.testing.assert_allclose(
        accumulated_half_residual / accumulated_residual,
        0.125,
        rtol=0.0,
        atol=5.0e-3,
    )

    small_horizon = 1.0e-3
    terminal_small = _scalar(
        whitened_terminal_signed_output_operator(problem, small_horizon)
    )
    accumulated_small = _scalar(
        whitened_accumulated_input_transport_operator(problem, small_horizon)
    )

    np.testing.assert_allclose(
        terminal_small / small_horizon,
        h1,
        rtol=3.0e-3,
        atol=1.0e-12,
    )
    np.testing.assert_allclose(
        accumulated_small / (0.5 * small_horizon**2),
        h1,
        rtol=2.0e-3,
        atol=1.0e-12,
    )


def test_psd_transport_neutrality_forces_qb_and_first_generation_to_zero() -> None:
    problem = _psd_neutral_witness()

    q_eigenvalues = np.linalg.eigvalsh(problem.Q)
    assert q_eigenvalues[0] >= 0.0

    projected_transport = problem.B.conj().T @ problem.Q @ problem.B
    np.testing.assert_allclose(projected_transport, 0.0, rtol=0.0, atol=1.0e-14)
    np.testing.assert_allclose(problem.Q @ problem.B, 0.0, rtol=0.0, atol=1.0e-14)

    lie_derivative = problem.A.conj().T @ problem.Q + problem.Q @ problem.A
    raw_h1 = problem.B.conj().T @ lie_derivative @ problem.B
    np.testing.assert_allclose(raw_h1, 0.0, rtol=0.0, atol=1.0e-14)


def test_psd_neutral_witness_matches_exact_terminal_and_accumulated_output() -> None:
    kappa = 1.7
    rin = 2.3
    horizon = 0.37
    problem = _psd_neutral_witness(kappa=kappa, rin=rin)

    terminal = _scalar(whitened_terminal_signed_output_operator(problem, horizon))
    accumulated = _scalar(
        whitened_accumulated_input_transport_operator(problem, horizon)
    )

    terminal_exact = (kappa**2 / rin) * (
        np.exp(-horizon) - np.exp(-2.0 * horizon)
    ) ** 2
    accumulated_exact = (kappa**2 / rin) * (
        (1.0 - np.exp(-2.0 * horizon)) / 2.0
        - 2.0 * (1.0 - np.exp(-3.0 * horizon)) / 3.0
        + (1.0 - np.exp(-4.0 * horizon)) / 4.0
    )

    np.testing.assert_allclose(terminal, terminal_exact, rtol=2.0e-12, atol=2.0e-13)
    np.testing.assert_allclose(accumulated, accumulated_exact, rtol=2.0e-12, atol=2.0e-13)


def test_psd_transport_neutral_short_time_orders_are_quadratic_and_cubic() -> None:
    kappa = 1.7
    rin = 2.3
    problem = _psd_neutral_witness(kappa=kappa, rin=rin)
    leading_terminal = kappa**2 / rin
    leading_accumulated = kappa**2 / (3.0 * rin)

    horizon = 2.0e-2
    half_horizon = horizon / 2.0

    terminal = _scalar(whitened_terminal_signed_output_operator(problem, horizon))
    terminal_half = _scalar(
        whitened_terminal_signed_output_operator(problem, half_horizon)
    )
    accumulated = _scalar(
        whitened_accumulated_input_transport_operator(problem, horizon)
    )
    accumulated_half = _scalar(
        whitened_accumulated_input_transport_operator(problem, half_horizon)
    )

    terminal_residual = abs(terminal - leading_terminal * horizon**2)
    terminal_half_residual = abs(
        terminal_half - leading_terminal * half_horizon**2
    )
    accumulated_residual = abs(
        accumulated - leading_accumulated * horizon**3
    )
    accumulated_half_residual = abs(
        accumulated_half - leading_accumulated * half_horizon**3
    )

    assert terminal_residual > 0.0
    assert accumulated_residual > 0.0
    np.testing.assert_allclose(
        terminal_half_residual / terminal_residual,
        0.125,
        rtol=0.0,
        atol=8.0e-3,
    )
    np.testing.assert_allclose(
        accumulated_half_residual / accumulated_residual,
        0.0625,
        rtol=0.0,
        atol=6.0e-3,
    )

    small_horizon = 1.0e-3
    terminal_small = _scalar(
        whitened_terminal_signed_output_operator(problem, small_horizon)
    )
    accumulated_small = _scalar(
        whitened_accumulated_input_transport_operator(problem, small_horizon)
    )

    np.testing.assert_allclose(
        terminal_small / small_horizon**2,
        leading_terminal,
        rtol=4.0e-3,
        atol=1.0e-12,
    )
    np.testing.assert_allclose(
        accumulated_small / small_horizon**3,
        leading_accumulated,
        rtol=4.0e-3,
        atol=1.0e-10,
    )
