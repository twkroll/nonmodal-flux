"""Cross-check terminal and accumulated signed-transport APIs."""

import numpy as np

from nonmodal_flux.core.gramians import (
    accumulated_input_transport_operator,
    accumulated_signed_extrema,
    accumulated_signed_extremal_inputs,
    whitened_accumulated_input_transport_operator,
)
from nonmodal_flux.core.outputs import (
    terminal_signed_extrema,
    terminal_signed_extremal_inputs,
    terminal_signed_output_operator,
    whitened_terminal_signed_output_operator,
)
from nonmodal_flux.core.problem import TransportProblem


def _complex_problem() -> TransportProblem:
    return TransportProblem(
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


def test_derivative_of_accumulated_input_operator_matches_terminal_operator() -> None:
    problem = _complex_problem()
    horizon = 0.41
    step = 1.0e-5

    accumulated_minus = np.asarray(
        accumulated_input_transport_operator(problem, horizon - step)
    )
    accumulated_plus = np.asarray(
        accumulated_input_transport_operator(problem, horizon + step)
    )
    derivative = (accumulated_plus - accumulated_minus) / (2.0 * step)
    terminal = np.asarray(terminal_signed_output_operator(problem, horizon))

    np.testing.assert_allclose(derivative, terminal, rtol=3.0e-9, atol=3.0e-10)


def test_derivative_of_whitened_accumulated_operator_matches_whitened_terminal_operator() -> None:
    problem = _complex_problem()
    horizon = 0.37
    step = 1.0e-5

    accumulated_minus = np.asarray(
        whitened_accumulated_input_transport_operator(problem, horizon - step)
    )
    accumulated_plus = np.asarray(
        whitened_accumulated_input_transport_operator(problem, horizon + step)
    )
    derivative = (accumulated_plus - accumulated_minus) / (2.0 * step)
    terminal = np.asarray(whitened_terminal_signed_output_operator(problem, horizon))

    np.testing.assert_allclose(derivative, terminal, rtol=3.0e-9, atol=3.0e-10)


def test_static_dynamics_give_exact_terminal_accumulated_scaling_and_same_optimizers() -> None:
    problem = TransportProblem(
        A=np.zeros((2, 2), dtype=float),
        M=np.eye(2),
        Q=np.diag([-1.0, 2.0]),
        B=np.eye(2),
        Rin=np.array([[2.0, 0.2], [0.2, 1.0]]),
    )
    horizon = 0.63

    terminal_raw = np.asarray(terminal_signed_output_operator(problem, horizon))
    accumulated_raw = np.asarray(accumulated_input_transport_operator(problem, horizon))
    terminal_whitened = np.asarray(
        whitened_terminal_signed_output_operator(problem, horizon)
    )
    accumulated_whitened = np.asarray(
        whitened_accumulated_input_transport_operator(problem, horizon)
    )

    np.testing.assert_allclose(
        accumulated_raw,
        horizon * terminal_raw,
        rtol=1.0e-13,
        atol=1.0e-13,
    )
    np.testing.assert_allclose(
        accumulated_whitened,
        horizon * terminal_whitened,
        rtol=1.0e-13,
        atol=1.0e-13,
    )

    terminal_min, terminal_max = terminal_signed_extrema(problem, horizon)
    accumulated_min, accumulated_max = accumulated_signed_extrema(problem, horizon)
    np.testing.assert_allclose(
        np.asarray([accumulated_min, accumulated_max]),
        horizon * np.asarray([terminal_min, terminal_max]),
        rtol=1.0e-13,
        atol=1.0e-13,
    )

    _, terminal_u_min, _, terminal_u_max = terminal_signed_extremal_inputs(
        problem, horizon
    )
    _, accumulated_u_min, _, accumulated_u_max = accumulated_signed_extremal_inputs(
        problem, horizon
    )
    rin = problem.Rin

    min_overlap = abs(
        np.vdot(np.asarray(terminal_u_min), rin @ np.asarray(accumulated_u_min))
    )
    max_overlap = abs(
        np.vdot(np.asarray(terminal_u_max), rin @ np.asarray(accumulated_u_max))
    )

    np.testing.assert_allclose(min_overlap, 1.0, rtol=1.0e-12, atol=1.0e-12)
    np.testing.assert_allclose(max_overlap, 1.0, rtol=1.0e-12, atol=1.0e-12)
