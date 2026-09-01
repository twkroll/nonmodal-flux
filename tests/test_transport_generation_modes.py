"""Tests for T1 short-time convergence of signed extremal modes."""

import numpy as np

from nonmodal_flux.core.gramians import accumulated_signed_extremal_modes
from nonmodal_flux.core.outputs import terminal_signed_extremal_modes
from nonmodal_flux.core.problem import TransportProblem


def _mixed_multi_input_witness() -> TransportProblem:
    """Return a stable neutral-input witness whose finite-time modes rotate."""

    kappa_positive = 2.0
    kappa_negative = -1.5
    source_mixing = np.array(
        [[1.0, 0.7 + 0.3j], [0.5 - 0.2j, 1.0]],
        dtype=np.complex128,
    )
    return TransportProblem(
        A=np.array(
            [
                [-0.4 + 0.3j, 0.0, 0.0, 0.0],
                [kappa_positive, -2.4 - 0.2j, 0.0, 0.0],
                [0.0, 0.0, -1.4 + 0.1j, 0.0],
                [0.0, 0.0, kappa_negative, -3.7 + 0.7j],
            ],
            dtype=np.complex128,
        ),
        M=np.eye(4, dtype=np.complex128),
        Q=0.5
        * np.array(
            [
                [0.0, 1.0, 0.0, 0.0],
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
                [0.0, 0.0, 1.0, 0.0],
            ],
            dtype=np.complex128,
        ),
        B=np.array(
            [
                source_mixing[0],
                [0.0, 0.0],
                source_mixing[1],
                [0.0, 0.0],
            ],
            dtype=np.complex128,
        ),
        Rin=np.array(
            [[1.4, 0.25 + 0.15j], [0.25 - 0.15j, 1.2]],
            dtype=np.complex128,
        ),
    )


def _first_whitened_generation(problem: TransportProblem) -> np.ndarray:
    lie_derivative = problem.A.conj().T @ problem.Q + problem.Q @ problem.A
    raw = problem.B.conj().T @ lie_derivative @ problem.B
    lower = np.linalg.cholesky(problem.Rin)
    left = np.linalg.solve(lower, raw)
    return np.linalg.solve(lower, left.conj().T).conj().T


def _phase_invariant_sine(actual: np.ndarray, expected: np.ndarray) -> float:
    actual = np.asarray(actual)
    expected = np.asarray(expected)
    actual = actual / np.linalg.norm(actual)
    expected = expected / np.linalg.norm(expected)
    overlap = min(1.0, float(abs(np.vdot(expected, actual))))
    return float(np.sqrt(max(0.0, 1.0 - overlap**2)))


def _mode_errors(problem: TransportProblem, horizon: float) -> tuple[np.ndarray, np.ndarray]:
    h1_eigenvalues, h1_modes = np.linalg.eigh(_first_whitened_generation(problem))
    assert h1_eigenvalues[0] < 0.0 < h1_eigenvalues[-1]
    assert h1_eigenvalues[-1] - h1_eigenvalues[0] > 1.0

    _, terminal_min, _, terminal_max = terminal_signed_extremal_modes(problem, horizon)
    _, accumulated_min, _, accumulated_max = accumulated_signed_extremal_modes(problem, horizon)

    terminal_errors = np.array(
        [
            _phase_invariant_sine(terminal_min, h1_modes[:, 0]),
            _phase_invariant_sine(terminal_max, h1_modes[:, -1]),
        ]
    )
    accumulated_errors = np.array(
        [
            _phase_invariant_sine(accumulated_min, h1_modes[:, 0]),
            _phase_invariant_sine(accumulated_max, h1_modes[:, -1]),
        ]
    )
    return terminal_errors, accumulated_errors


def test_mixed_witness_is_transport_neutral_with_simple_signed_h1() -> None:
    problem = _mixed_multi_input_witness()

    projected = problem.B.conj().T @ problem.Q @ problem.B
    np.testing.assert_allclose(projected, 0.0, rtol=0.0, atol=1.0e-14)

    h1 = _first_whitened_generation(problem)
    np.testing.assert_allclose(h1, h1.conj().T, rtol=0.0, atol=2.0e-14)
    eigenvalues = np.linalg.eigvalsh(h1)
    assert eigenvalues[0] < 0.0 < eigenvalues[-1]
    assert eigenvalues[-1] - eigenvalues[0] > 1.0


def test_terminal_extremal_modes_converge_to_h1_eigenvectors() -> None:
    problem = _mixed_multi_input_witness()

    errors = []
    for horizon in (0.1, 0.05, 0.025):
        terminal_errors, _ = _mode_errors(problem, horizon)
        errors.append(terminal_errors)

    errors = np.asarray(errors)
    assert np.all(errors[1:] < errors[:-1])
    np.testing.assert_allclose(
        errors[2] / errors[1],
        np.full(2, 0.5),
        rtol=0.0,
        atol=4.0e-2,
    )

    terminal_small, _ = _mode_errors(problem, 0.01)
    assert np.all(terminal_small < 1.0e-2)


def test_accumulated_extremal_modes_converge_to_h1_eigenvectors() -> None:
    problem = _mixed_multi_input_witness()

    errors = []
    for horizon in (0.1, 0.05, 0.025):
        _, accumulated_errors = _mode_errors(problem, horizon)
        errors.append(accumulated_errors)

    errors = np.asarray(errors)
    assert np.all(errors[1:] < errors[:-1])
    np.testing.assert_allclose(
        errors[2] / errors[1],
        np.full(2, 0.5),
        rtol=0.0,
        atol=4.0e-2,
    )

    _, accumulated_small = _mode_errors(problem, 0.01)
    assert np.all(accumulated_small < 6.0e-3)
