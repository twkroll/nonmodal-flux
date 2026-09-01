"""Tests for signed eigenvalue asymptotics in multi-input T1 transport generation."""

import numpy as np

from nonmodal_flux.core.gramians import accumulated_signed_extrema
from nonmodal_flux.core.outputs import terminal_signed_extrema
from nonmodal_flux.core.problem import TransportProblem


def _multi_input_nu1_witness() -> TransportProblem:
    """Return a stable two-channel witness with indefinite first generation H1."""

    kappa_positive = 1.8
    kappa_negative = -1.4
    return TransportProblem(
        A=np.array(
            [
                [-1.0, 0.0, 0.0, 0.0],
                [kappa_positive, -2.0, 0.0, 0.0],
                [0.0, 0.0, -1.0, 0.0],
                [0.0, 0.0, kappa_negative, -2.0],
            ]
        ),
        M=np.eye(4),
        Q=0.5
        * np.array(
            [
                [0.0, 1.0, 0.0, 0.0],
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
                [0.0, 0.0, 1.0, 0.0],
            ]
        ),
        B=np.array(
            [
                [1.0, 0.0],
                [0.0, 0.0],
                [0.0, 1.0],
                [0.0, 0.0],
            ]
        ),
        Rin=np.diag([1.5, 2.0]),
    )


def _first_whitened_generation(problem: TransportProblem) -> np.ndarray:
    lie_derivative = problem.A.conj().T @ problem.Q + problem.Q @ problem.A
    raw = problem.B.conj().T @ lie_derivative @ problem.B
    lower = np.linalg.cholesky(problem.Rin)
    inverse_lower = np.linalg.solve(lower, np.eye(lower.shape[0]))
    return inverse_lower @ raw @ inverse_lower.conj().T


def test_multi_input_witness_has_signed_first_generation() -> None:
    problem = _multi_input_nu1_witness()

    projected = problem.B.conj().T @ problem.Q @ problem.B
    np.testing.assert_allclose(projected, 0.0, rtol=0.0, atol=1.0e-14)

    h1 = _first_whitened_generation(problem)
    expected = np.diag([-1.4 / 2.0, 1.8 / 1.5])
    np.testing.assert_allclose(
        np.sort(np.linalg.eigvalsh(h1)),
        np.sort(np.diag(expected)),
        rtol=0.0,
        atol=2.0e-14,
    )

    eigenvalues = np.linalg.eigvalsh(h1)
    assert eigenvalues[0] < 0.0 < eigenvalues[-1]


def test_signed_terminal_extrema_follow_t1_eigenvalue_asymptotics() -> None:
    problem = _multi_input_nu1_witness()
    h1_eigenvalues = np.linalg.eigvalsh(_first_whitened_generation(problem))
    horizon = 1.0e-3

    terminal_min, terminal_max = terminal_signed_extrema(problem, horizon)
    scaled = np.asarray([terminal_min, terminal_max]) / horizon

    np.testing.assert_allclose(
        scaled,
        h1_eigenvalues,
        rtol=3.0e-3,
        atol=2.0e-12,
    )


def test_signed_accumulated_extrema_follow_t1_eigenvalue_asymptotics() -> None:
    problem = _multi_input_nu1_witness()
    h1_eigenvalues = np.linalg.eigvalsh(_first_whitened_generation(problem))
    horizon = 1.0e-3

    accumulated_min, accumulated_max = accumulated_signed_extrema(problem, horizon)
    scaled = np.asarray([accumulated_min, accumulated_max]) / (0.5 * horizon**2)

    np.testing.assert_allclose(
        scaled,
        h1_eigenvalues,
        rtol=2.0e-3,
        atol=2.0e-12,
    )


def test_signed_extrema_residuals_have_next_expected_orders() -> None:
    problem = _multi_input_nu1_witness()
    h1_eigenvalues = np.linalg.eigvalsh(_first_whitened_generation(problem))
    horizon = 2.0e-2
    half_horizon = horizon / 2.0

    terminal = np.asarray(terminal_signed_extrema(problem, horizon))
    terminal_half = np.asarray(terminal_signed_extrema(problem, half_horizon))
    accumulated = np.asarray(accumulated_signed_extrema(problem, horizon))
    accumulated_half = np.asarray(accumulated_signed_extrema(problem, half_horizon))

    terminal_residual = np.abs(terminal - horizon * h1_eigenvalues)
    terminal_half_residual = np.abs(terminal_half - half_horizon * h1_eigenvalues)
    accumulated_residual = np.abs(accumulated - 0.5 * horizon**2 * h1_eigenvalues)
    accumulated_half_residual = np.abs(
        accumulated_half - 0.5 * half_horizon**2 * h1_eigenvalues
    )

    assert np.all(terminal_residual > 0.0)
    assert np.all(accumulated_residual > 0.0)
    np.testing.assert_allclose(
        terminal_half_residual / terminal_residual,
        np.full(2, 0.25),
        rtol=0.0,
        atol=1.0e-2,
    )
    np.testing.assert_allclose(
        accumulated_half_residual / accumulated_residual,
        np.full(2, 0.125),
        rtol=0.0,
        atol=5.0e-3,
    )
