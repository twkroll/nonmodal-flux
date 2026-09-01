"""Tests for invariance under invertible state and input coordinate changes."""

import numpy as np

from nonmodal_flux.core.gramians import (
    accumulated_input_transport_operator,
    accumulated_signed_extrema,
    accumulated_signed_extremal_inputs,
)
from nonmodal_flux.core.outputs import (
    terminal_signed_extrema,
    terminal_signed_extremal_inputs,
    terminal_signed_output_operator,
)
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


def _transform_input_coordinates(problem: TransportProblem, transform: np.ndarray) -> TransportProblem:
    inverse = np.linalg.inv(transform)
    inverse_adjoint = inverse.conj().T
    return TransportProblem(
        A=problem.A,
        M=problem.M,
        Q=problem.Q,
        B=problem.B @ inverse,
        Rin=inverse_adjoint @ problem.Rin @ inverse,
    )


def _assert_terminal_and_accumulated_extrema_invariant(
    problem: TransportProblem,
    transform: np.ndarray,
    horizon: float,
) -> None:
    transformed = _transform_state_coordinates(problem, transform)

    terminal_reference = np.asarray(terminal_signed_extrema(problem, horizon))
    terminal_transformed = np.asarray(terminal_signed_extrema(transformed, horizon))
    accumulated_reference = np.asarray(accumulated_signed_extrema(problem, horizon))
    accumulated_transformed = np.asarray(accumulated_signed_extrema(transformed, horizon))

    np.testing.assert_allclose(
        terminal_transformed,
        terminal_reference,
        rtol=2.0e-11,
        atol=2.0e-12,
    )
    np.testing.assert_allclose(
        accumulated_transformed,
        accumulated_reference,
        rtol=2.0e-11,
        atol=2.0e-12,
    )


def _assert_input_operators_invariant(
    problem: TransportProblem,
    transform: np.ndarray,
    horizon: float,
) -> None:
    transformed = _transform_state_coordinates(problem, transform)

    terminal_reference = np.asarray(terminal_signed_output_operator(problem, horizon))
    terminal_transformed = np.asarray(terminal_signed_output_operator(transformed, horizon))
    accumulated_reference = np.asarray(accumulated_input_transport_operator(problem, horizon))
    accumulated_transformed = np.asarray(
        accumulated_input_transport_operator(transformed, horizon)
    )

    np.testing.assert_allclose(
        terminal_transformed,
        terminal_reference,
        rtol=2.0e-11,
        atol=2.0e-12,
    )
    np.testing.assert_allclose(
        accumulated_transformed,
        accumulated_reference,
        rtol=2.0e-11,
        atol=2.0e-12,
    )


def _assert_input_coordinate_extrema_invariant(
    problem: TransportProblem,
    transform: np.ndarray,
    horizon: float,
) -> None:
    transformed = _transform_input_coordinates(problem, transform)

    terminal_reference = np.asarray(terminal_signed_extrema(problem, horizon))
    terminal_transformed = np.asarray(terminal_signed_extrema(transformed, horizon))
    accumulated_reference = np.asarray(accumulated_signed_extrema(problem, horizon))
    accumulated_transformed = np.asarray(accumulated_signed_extrema(transformed, horizon))

    np.testing.assert_allclose(
        terminal_transformed,
        terminal_reference,
        rtol=2.0e-11,
        atol=2.0e-12,
    )
    np.testing.assert_allclose(
        accumulated_transformed,
        accumulated_reference,
        rtol=2.0e-11,
        atol=2.0e-12,
    )


def _assert_input_coordinate_operator_covariance(
    problem: TransportProblem,
    transform: np.ndarray,
    horizon: float,
) -> None:
    transformed = _transform_input_coordinates(problem, transform)
    inverse = np.linalg.inv(transform)
    inverse_adjoint = inverse.conj().T

    terminal_reference = np.asarray(terminal_signed_output_operator(problem, horizon))
    terminal_transformed = np.asarray(terminal_signed_output_operator(transformed, horizon))
    terminal_expected = inverse_adjoint @ terminal_reference @ inverse

    accumulated_reference = np.asarray(accumulated_input_transport_operator(problem, horizon))
    accumulated_transformed = np.asarray(
        accumulated_input_transport_operator(transformed, horizon)
    )
    accumulated_expected = inverse_adjoint @ accumulated_reference @ inverse

    np.testing.assert_allclose(
        terminal_transformed,
        terminal_expected,
        rtol=2.0e-11,
        atol=2.0e-12,
    )
    np.testing.assert_allclose(
        accumulated_transformed,
        accumulated_expected,
        rtol=2.0e-11,
        atol=2.0e-12,
    )


def _assert_equal_up_to_phase(actual: np.ndarray, expected: np.ndarray) -> None:
    actual = np.asarray(actual)
    expected = np.asarray(expected)
    overlap = np.vdot(expected, actual)
    assert abs(overlap) > 1.0e-12
    phase = overlap / abs(overlap)
    np.testing.assert_allclose(actual / phase, expected, rtol=3.0e-11, atol=3.0e-12)


def _assert_extremal_inputs_transform_covariantly(
    problem: TransportProblem,
    transform: np.ndarray,
    horizon: float,
) -> None:
    transformed = _transform_input_coordinates(problem, transform)

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
        rtol=2.0e-11,
        atol=2.0e-12,
    )
    np.testing.assert_allclose(
        np.asarray([accumulated_min_new, accumulated_max_new]),
        np.asarray([accumulated_min_ref, accumulated_max_ref]),
        rtol=2.0e-11,
        atol=2.0e-12,
    )

    _assert_equal_up_to_phase(np.asarray(terminal_u_min_new), transform @ terminal_u_min_ref)
    _assert_equal_up_to_phase(np.asarray(terminal_u_max_new), transform @ terminal_u_max_ref)
    _assert_equal_up_to_phase(
        np.asarray(accumulated_u_min_new), transform @ accumulated_u_min_ref
    )
    _assert_equal_up_to_phase(
        np.asarray(accumulated_u_max_new), transform @ accumulated_u_max_ref
    )


def test_signed_extrema_are_invariant_under_real_state_coordinate_change() -> None:
    problem = TransportProblem(
        A=np.array([[-0.7, 1.4], [-0.2, -1.6]]),
        M=np.array([[2.0, 0.2], [0.2, 1.3]]),
        Q=np.array([[0.3, 0.8], [0.8, -0.4]]),
        B=np.array([[1.0, 0.3], [-0.2, 1.0]]),
        Rin=np.array([[2.4, 0.35], [0.35, 1.2]]),
    )
    transform = np.array([[1.7, -0.4], [0.6, 0.9]])

    _assert_terminal_and_accumulated_extrema_invariant(problem, transform, horizon=0.53)


def test_signed_extrema_are_invariant_under_complex_state_coordinate_change() -> None:
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

    _assert_terminal_and_accumulated_extrema_invariant(problem, transform, horizon=0.41)


def test_input_operators_are_invariant_under_real_state_coordinate_change() -> None:
    problem = TransportProblem(
        A=np.array([[-0.7, 1.4], [-0.2, -1.6]]),
        M=np.array([[2.0, 0.2], [0.2, 1.3]]),
        Q=np.array([[0.3, 0.8], [0.8, -0.4]]),
        B=np.array([[1.0, 0.3], [-0.2, 1.0]]),
        Rin=np.array([[2.4, 0.35], [0.35, 1.2]]),
    )
    transform = np.array([[1.7, -0.4], [0.6, 0.9]])

    _assert_input_operators_invariant(problem, transform, horizon=0.37)


def test_input_operators_are_invariant_under_complex_state_coordinate_change() -> None:
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

    _assert_input_operators_invariant(problem, transform, horizon=0.29)


def test_signed_extrema_are_invariant_under_real_input_coordinate_change() -> None:
    problem = TransportProblem(
        A=np.array([[-0.7, 1.4], [-0.2, -1.6]]),
        M=np.array([[2.0, 0.2], [0.2, 1.3]]),
        Q=np.array([[0.3, 0.8], [0.8, -0.4]]),
        B=np.array([[1.0, 0.3], [-0.2, 1.0]]),
        Rin=np.array([[2.4, 0.35], [0.35, 1.2]]),
    )
    transform = np.array([[1.5, -0.6], [0.4, 1.1]])

    _assert_input_coordinate_extrema_invariant(problem, transform, horizon=0.47)


def test_signed_extrema_are_invariant_under_complex_input_coordinate_change() -> None:
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
        [[1.2 + 0.1j, -0.3 + 0.4j], [0.5 - 0.2j, 0.9 + 0.3j]],
        dtype=np.complex128,
    )

    _assert_input_coordinate_extrema_invariant(problem, transform, horizon=0.35)


def test_input_operators_transform_covariantly_under_real_input_coordinate_change() -> None:
    problem = TransportProblem(
        A=np.array([[-0.7, 1.4], [-0.2, -1.6]]),
        M=np.array([[2.0, 0.2], [0.2, 1.3]]),
        Q=np.array([[0.3, 0.8], [0.8, -0.4]]),
        B=np.array([[1.0, 0.3], [-0.2, 1.0]]),
        Rin=np.array([[2.4, 0.35], [0.35, 1.2]]),
    )
    transform = np.array([[1.5, -0.6], [0.4, 1.1]])

    _assert_input_coordinate_operator_covariance(problem, transform, horizon=0.43)


def test_input_operators_transform_covariantly_under_complex_input_coordinate_change() -> None:
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
        [[1.2 + 0.1j, -0.3 + 0.4j], [0.5 - 0.2j, 0.9 + 0.3j]],
        dtype=np.complex128,
    )

    _assert_input_coordinate_operator_covariance(problem, transform, horizon=0.33)


def test_extremal_inputs_transform_covariantly_under_real_input_coordinate_change() -> None:
    problem = TransportProblem(
        A=np.array([[-0.7, 1.4], [-0.2, -1.6]]),
        M=np.array([[2.0, 0.2], [0.2, 1.3]]),
        Q=np.array([[0.3, 0.8], [0.8, -0.4]]),
        B=np.array([[1.0, 0.3], [-0.2, 1.0]]),
        Rin=np.array([[2.4, 0.35], [0.35, 1.2]]),
    )
    transform = np.array([[1.5, -0.6], [0.4, 1.1]])

    _assert_extremal_inputs_transform_covariantly(problem, transform, horizon=0.39)


def test_extremal_inputs_transform_covariantly_under_complex_input_coordinate_change() -> None:
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
        [[1.2 + 0.1j, -0.3 + 0.4j], [0.5 - 0.2j, 0.9 + 0.3j]],
        dtype=np.complex128,
    )

    _assert_extremal_inputs_transform_covariantly(problem, transform, horizon=0.31)
