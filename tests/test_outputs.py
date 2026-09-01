"""Tests for terminal signed-output operators."""

import jax.numpy as jnp
import numpy as np

from nonmodal_flux.core.outputs import terminal_signed_output_operator
from nonmodal_flux.core.problem import TransportProblem, hermiticity_error
from nonmodal_flux.core.propagators import constant_propagator


def _real_problem() -> TransportProblem:
    return TransportProblem(
        A=np.array([[-1.0, 2.0], [0.0, -3.0]]),
        M=np.eye(2),
        Q=np.array([[0.0, 0.5], [0.5, 0.0]]),
        B=np.array([[1.0, 0.0], [0.0, 1.0]]),
        Rin=np.eye(2),
    )


def test_terminal_operator_at_zero_is_projected_initial_transport() -> None:
    problem = _real_problem()

    operator = np.asarray(terminal_signed_output_operator(problem, 0.0))
    expected = problem.B.conj().T @ problem.Q @ problem.B

    np.testing.assert_allclose(operator, expected, rtol=1.0e-13, atol=1.0e-13)


def test_terminal_operator_reproduces_direct_quadratic_output() -> None:
    problem = _real_problem()
    horizon = 0.37
    u = jnp.array([1.25 - 0.3j, -0.4 + 0.8j], dtype=jnp.complex128)

    operator = terminal_signed_output_operator(problem, horizon)
    phi = constant_propagator(problem.A, horizon)
    x_terminal = phi @ jnp.asarray(problem.B) @ u

    input_space_value = u.conj().T @ operator @ u
    state_space_value = x_terminal.conj().T @ jnp.asarray(problem.Q) @ x_terminal

    np.testing.assert_allclose(
        np.asarray(input_space_value),
        np.asarray(state_space_value),
        rtol=1.0e-12,
        atol=1.0e-12,
    )


def test_terminal_operator_is_hermitian_without_explicit_symmetrization() -> None:
    problem = _real_problem()

    operator = np.asarray(terminal_signed_output_operator(problem, 0.61))

    assert hermiticity_error(operator) < 1.0e-13


def test_terminal_operator_supports_complex_generator_and_transport_form() -> None:
    problem = TransportProblem(
        A=np.array(
            [
                [-0.5 + 0.8j, 1.2 - 0.4j],
                [0.0 + 0.0j, -1.3 - 0.2j],
            ],
            dtype=np.complex128,
        ),
        M=np.array([[2.0, 0.2j], [-0.2j, 1.0]], dtype=np.complex128),
        Q=np.array([[0.0, 0.5j], [-0.5j, 0.0]], dtype=np.complex128),
        B=np.array([[1.0], [1.0j]], dtype=np.complex128),
        Rin=np.array([[1.0]]),
    )

    operator = np.asarray(terminal_signed_output_operator(problem, 0.42))
    phi = np.asarray(constant_propagator(problem.A, 0.42))
    expected = problem.B.conj().T @ phi.conj().T @ problem.Q @ phi @ problem.B

    np.testing.assert_allclose(operator, expected, rtol=1.0e-12, atol=1.0e-12)
    assert hermiticity_error(operator) < 1.0e-13


def test_terminal_operator_respects_restricted_input_space() -> None:
    problem = TransportProblem(
        A=np.array([[-1.0, 0.0], [2.0, -2.0]]),
        M=np.eye(2),
        Q=np.array([[0.0, 0.5], [0.5, 0.0]]),
        B=np.array([[1.0], [0.0]]),
        Rin=np.array([[1.0]]),
    )

    operator = np.asarray(terminal_signed_output_operator(problem, 0.3))

    assert operator.shape == (1, 1)
    assert operator[0, 0] > 0.0
