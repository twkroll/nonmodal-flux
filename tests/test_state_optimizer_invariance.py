"""Tests for extremal-input invariance under state-coordinate changes."""

import numpy as np

from nonmodal_flux.core.gramians import accumulated_signed_extremal_inputs
from nonmodal_flux.core.outputs import terminal_signed_extremal_inputs
from nonmodal_flux.core.problem import TransportProblem


def _transform_state_coordinates(problem: TransportProblem, transform: np.ndarray) -> TransportProblem:
    inverse = np.linalg.inv(transform)
    inverse_adjoint = inverse.conj().T
    return TransportProblem(
        A=transform @ problem.A @ inverse,
        M=inverse_adjoint @ problem.M @ inverse,
        Q=inverse_adjoint @ problem.Q @ inverse,
        B=transform @ problem.B,
        Rin=problem.Rin,
    )


def _assert_equal_up_to_phase(actual: np.ndarray, expected: np.ndarray) -> None:
    actual = np.asarray(actual)
    expected = np.asarray(expected)
    overlap = np.vdot(expected, actual)
    assert abs(overlap) > 1.0e-12
    phase = overlap / abs(overlap)
    np.testing.assert_allclose(actual / phase, expected, rtol=4.0e-11, atol=4.0e-12)


def _assert_state_coordinate_optimizer_invariance(
    problem: TransportProblem,
    transform: np.ndarray,
    horizon: float,
) -> None:
    transformed = _transform_state_coordinates(problem, transform)

    terminal_reference = terminal_signed_extremal_inputs(problem, horizon)
    terminal_transformed = terminal_signed_extremal_inputs(transformed, horizon)
    accumulated_reference = accumulated_signed_extremal_inputs(problem, horizon)
    accumulated_transformed = accumulated_signed_extremal_inputs(transformed, horizon)

    terminal_min_ref, terminal_u_min_ref, terminal_max_ref, terminal_u_max_ref = terminal_reference
    terminal_min_new, terminal_u_min_new, terminal_max_new, terminal_u_max_new = terminal_transformed
    accumulated_min_ref, accumulated_u_min_ref, accumulated_max_ref, accumulated_u_max_ref = (
        accumulated_reference
    )
    accumulated_min_new, accumulated_u_min_new, accumulated_max_new, accumulated_u_max_new = (
        accumulated_transformed
    )

    assert float(terminal_min_ref) < float(terminal_max_ref)
    assert float(accumulated_min_ref) < float(accumulated_max_ref)

    np.testing.assert_allclose(
        np.asarray([terminal_min_new, terminal_max_new]),
        np.asarray([terminal_min_ref, terminal_max_ref]),
        rtol=3.0e-11,
        atol=3.0e-12,
    )
    np.testing.assert_allclose(
        np.asarray([accumulated_min_new, accumulated_max_new]),
        np.asarray([accumulated_min_ref, accumulated_max_ref]),
        rtol=3.0e-11,
        atol=3.0e-12,
    )

    # A state-coordinate change does not reparameterize the admissible input u.
    _assert_equal_up_to_phase(np.asarray(terminal_u_min_new), np.asarray(terminal_u_min_ref))
    _assert_equal_up_to_phase(np.asarray(terminal_u_max_new), np.asarray(terminal_u_max_ref))
    _assert_equal_up_to_phase(
        np.asarray(accumulated_u_min_new), np.asarray(accumulated_u_min_ref)
    )
    _assert_equal_up_to_phase(
        np.asarray(accumulated_u_max_new), np.asarray(accumulated_u_max_ref)
    )


def test_extremal_inputs_are_invariant_under_real_state_coordinate_change() -> None:
    problem = TransportProblem(
        A=np.array([[-0.7, 1.4], [-0.2, -1.6]]),
        M=np.array([[2.0, 0.2], [0.2, 1.3]]),
        Q=np.array([[0.3, 0.8], [0.8, -0.4]]),
        B=np.array([[1.0, 0.3], [-0.2, 1.0]]),
        Rin=np.array([[2.4, 0.35], [0.35, 1.2]]),
    )
    transform = np.array([[1.7, -0.4], [0.6, 0.9]])

    _assert_state_coordinate_optimizer_invariance(problem, transform, horizon=0.49)


def test_extremal_inputs_are_invariant_under_complex_state_coordinate_change() -> None:
    problem = TransportProblem(
        A=np.array(
            [[-0.6 + 0.4j, 0.9 - 0.2j], [0.1j, -1.1 - 0.3j]],
            dtype=np.complex128,
        ),
        M=np.array([[2.0, 0.15j], [-0.15j, 1.4]], dtype=np.complex128),
        Q=np.array([[0.2, 0.7j], [-0.7j, -0.3]], dtype=np.complex128),
        B=np.array([[1.0, 0.2j], [-0.3j, 0.8]], dtype=np.complex128),
        Rin=np.array(
            [[2.0, 0.3 + 0.2j], [0.3 - 0.2j, 1.5]],
            dtype=np.complex128,
        ),
    )
    transform = np.array(
        [[1.3 + 0.2j, -0.4 + 0.1j], [0.5 - 0.3j, 0.8 + 0.4j]],
        dtype=np.complex128,
    )

    _assert_state_coordinate_optimizer_invariance(problem, transform, horizon=0.38)
