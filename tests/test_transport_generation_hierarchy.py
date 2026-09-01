"""Tests for higher-order cases of the T1 transport-generation hierarchy."""

import numpy as np

from nonmodal_flux.core.gramians import whitened_accumulated_input_transport_operator
from nonmodal_flux.core.outputs import whitened_terminal_signed_output_operator
from nonmodal_flux.core.problem import TransportProblem


def _nu2_witness(kappa1: float = 1.4, kappa2: float = 0.9, rin: float = 2.2) -> TransportProblem:
    return TransportProblem(
        A=np.array(
            [
                [-1.0, 0.0, 0.0],
                [kappa1, -2.0, 0.0],
                [0.0, kappa2, -3.0],
            ]
        ),
        M=np.eye(3),
        Q=0.5
        * np.array(
            [
                [0.0, 0.0, 1.0],
                [0.0, 0.0, 0.0],
                [1.0, 0.0, 0.0],
            ]
        ),
        B=np.array([[1.0], [0.0], [0.0]]),
        Rin=np.array([[rin]]),
    )


def _scalar(operator: object) -> float:
    value = np.asarray(operator)[0, 0]
    np.testing.assert_allclose(np.imag(value), 0.0, rtol=0.0, atol=1.0e-13)
    return float(np.real(value))


def _lie_derivative(A: np.ndarray, X: np.ndarray) -> np.ndarray:
    return A.conj().T @ X + X @ A


def test_nu2_witness_has_first_nonzero_generation_at_second_lie_derivative() -> None:
    kappa1 = 1.4
    kappa2 = 0.9
    rin = 2.2
    problem = _nu2_witness(kappa1=kappa1, kappa2=kappa2, rin=rin)

    np.testing.assert_allclose(np.sort(np.linalg.eigvals(problem.A)), [-3.0, -2.0, -1.0])
    q_eigenvalues = np.linalg.eigvalsh(problem.Q)
    assert q_eigenvalues[0] < 0.0 < q_eigenvalues[-1]

    h = []
    current = problem.Q.copy()
    for _ in range(3):
        projected = problem.B.conj().T @ current @ problem.B
        h.append(float(np.real(projected[0, 0])) / rin)
        current = _lie_derivative(problem.A, current)

    np.testing.assert_allclose(h[0], 0.0, rtol=0.0, atol=1.0e-14)
    np.testing.assert_allclose(h[1], 0.0, rtol=0.0, atol=1.0e-14)
    np.testing.assert_allclose(
        h[2],
        kappa1 * kappa2 / rin,
        rtol=0.0,
        atol=2.0e-14,
    )
    assert h[2] > 0.0


def test_nu2_short_time_orders_are_quadratic_terminal_and_cubic_accumulated() -> None:
    kappa1 = 1.4
    kappa2 = 0.9
    rin = 2.2
    problem = _nu2_witness(kappa1=kappa1, kappa2=kappa2, rin=rin)
    h2 = kappa1 * kappa2 / rin

    small_horizon = 1.0e-3
    terminal_small = _scalar(
        whitened_terminal_signed_output_operator(problem, small_horizon)
    )
    accumulated_small = _scalar(
        whitened_accumulated_input_transport_operator(problem, small_horizon)
    )

    np.testing.assert_allclose(
        terminal_small / (0.5 * small_horizon**2),
        h2,
        rtol=4.0e-3,
        atol=1.0e-12,
    )
    np.testing.assert_allclose(
        accumulated_small / (small_horizon**3 / 6.0),
        h2,
        rtol=3.0e-3,
        atol=1.0e-12,
    )


def test_nu2_leading_term_residuals_have_next_expected_orders() -> None:
    kappa1 = 1.4
    kappa2 = 0.9
    rin = 2.2
    problem = _nu2_witness(kappa1=kappa1, kappa2=kappa2, rin=rin)
    h2 = kappa1 * kappa2 / rin

    horizon = 5.0e-2
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

    terminal_residual = abs(terminal - 0.5 * horizon**2 * h2)
    terminal_half_residual = abs(
        terminal_half - 0.5 * half_horizon**2 * h2
    )
    accumulated_residual = abs(accumulated - horizon**3 * h2 / 6.0)
    accumulated_half_residual = abs(
        accumulated_half - half_horizon**3 * h2 / 6.0
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
        atol=5.0e-3,
    )
