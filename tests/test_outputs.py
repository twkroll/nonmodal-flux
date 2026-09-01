"""Tests for terminal signed-output operators."""

import jax.numpy as jnp
import numpy as np
import scipy.linalg as sp_linalg

from nonmodal_flux.core.outputs import (
    terminal_signed_extrema,
    terminal_signed_extremal_inputs,
    terminal_signed_extremal_modes,
    terminal_signed_output_operator,
    whitened_terminal_signed_output_operator,
)
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


def _nontrivial_metric_problem() -> TransportProblem:
    return TransportProblem(
        A=np.array([[-0.7, 1.4], [-0.2, -1.6]]),
        M=np.array([[2.0, 0.2], [0.2, 1.3]]),
        Q=np.array([[0.3, 0.8], [0.8, -0.4]]),
        B=np.array([[1.0, 0.3], [-0.2, 1.0]]),
        Rin=np.array([[2.4, 0.35], [0.35, 1.2]]),
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


def test_identity_input_metric_leaves_terminal_operator_unchanged() -> None:
    problem = _real_problem()
    horizon = 0.43

    raw = np.asarray(terminal_signed_output_operator(problem, horizon))
    whitened = np.asarray(whitened_terminal_signed_output_operator(problem, horizon))

    np.testing.assert_allclose(whitened, raw, rtol=1.0e-13, atol=1.0e-13)


def test_whitening_matches_explicit_cholesky_reference_for_nonidentity_metric() -> None:
    problem = _nontrivial_metric_problem()
    horizon = 0.58

    raw = np.asarray(terminal_signed_output_operator(problem, horizon))
    whitened = np.asarray(whitened_terminal_signed_output_operator(problem, horizon))
    lower = np.linalg.cholesky(problem.Rin)
    lower_inverse = np.linalg.inv(lower)
    expected = lower_inverse @ raw @ lower_inverse.conj().T

    np.testing.assert_allclose(whitened, expected, rtol=1.0e-12, atol=1.0e-12)
    assert not np.allclose(whitened, raw)


def test_whitening_preserves_generalized_rayleigh_quotient() -> None:
    problem = _nontrivial_metric_problem()
    horizon = 0.31
    u = np.array([0.7 - 0.2j, -1.1 + 0.4j], dtype=np.complex128)

    raw = np.asarray(terminal_signed_output_operator(problem, horizon))
    whitened = np.asarray(whitened_terminal_signed_output_operator(problem, horizon))
    lower = np.linalg.cholesky(problem.Rin)
    v = lower.conj().T @ u

    generalized_quotient = (u.conj().T @ raw @ u) / (u.conj().T @ problem.Rin @ u)
    euclidean_quotient = (v.conj().T @ whitened @ v) / (v.conj().T @ v)

    np.testing.assert_allclose(
        euclidean_quotient,
        generalized_quotient,
        rtol=1.0e-12,
        atol=1.0e-12,
    )


def test_whitened_terminal_operator_is_hermitian_without_symmetrization() -> None:
    problem = _nontrivial_metric_problem()

    whitened = np.asarray(whitened_terminal_signed_output_operator(problem, 0.77))

    assert hermiticity_error(whitened) < 1.0e-12


def test_whitening_supports_complex_positive_input_metric() -> None:
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
    horizon = 0.49

    raw = np.asarray(terminal_signed_output_operator(problem, horizon))
    whitened = np.asarray(whitened_terminal_signed_output_operator(problem, horizon))
    lower = np.linalg.cholesky(problem.Rin)
    lower_inverse = np.linalg.inv(lower)
    expected = lower_inverse @ raw @ lower_inverse.conj().T

    np.testing.assert_allclose(whitened, expected, rtol=1.0e-12, atol=1.0e-12)
    assert hermiticity_error(whitened) < 1.0e-12


def test_terminal_signed_extrema_match_analytic_diagonal_case() -> None:
    problem = TransportProblem(
        A=np.diag([-0.5, -1.25]),
        M=np.eye(2),
        Q=np.diag([3.0, -2.0]),
        B=np.eye(2),
        Rin=np.diag([2.0, 0.5]),
    )
    horizon = 0.4

    lambda_min, lambda_max = terminal_signed_extrema(problem, horizon)
    expected_values = np.array(
        [
            3.0 * np.exp(-2.0 * 0.5 * horizon) / 2.0,
            -2.0 * np.exp(-2.0 * 1.25 * horizon) / 0.5,
        ]
    )

    np.testing.assert_allclose(
        np.asarray([lambda_min, lambda_max]),
        np.asarray([expected_values.min(), expected_values.max()]),
        rtol=1.0e-12,
        atol=1.0e-12,
    )


def test_terminal_signed_extrema_match_generalized_hermitian_eigenproblem() -> None:
    problem = _nontrivial_metric_problem()
    horizon = 0.53

    raw = np.asarray(terminal_signed_output_operator(problem, horizon))
    reference = sp_linalg.eigh(raw, problem.Rin, eigvals_only=True)
    lambda_min, lambda_max = terminal_signed_extrema(problem, horizon)

    np.testing.assert_allclose(
        np.asarray([lambda_min, lambda_max]),
        np.asarray([reference[0], reference[-1]]),
        rtol=1.0e-12,
        atol=1.0e-12,
    )


def test_terminal_signed_extrema_retain_both_transport_signs() -> None:
    problem = TransportProblem(
        A=np.zeros((2, 2), dtype=float),
        M=np.eye(2),
        Q=np.array([[0.0, 1.0], [1.0, 0.0]]),
        B=np.eye(2),
        Rin=np.eye(2),
    )

    lambda_min, lambda_max = terminal_signed_extrema(problem, 0.7)

    assert float(lambda_min) < 0.0 < float(lambda_max)
    np.testing.assert_allclose(
        np.asarray([lambda_min, lambda_max]),
        np.array([-1.0, 1.0]),
        rtol=1.0e-13,
        atol=1.0e-13,
    )


def test_terminal_extremal_modes_are_unit_norm_and_satisfy_eigenproblem() -> None:
    problem = _nontrivial_metric_problem()
    horizon = 0.47

    lambda_min, v_min, lambda_max, v_max = terminal_signed_extremal_modes(problem, horizon)
    operator = np.asarray(whitened_terminal_signed_output_operator(problem, horizon))
    v_min_np = np.asarray(v_min)
    v_max_np = np.asarray(v_max)

    np.testing.assert_allclose(np.vdot(v_min_np, v_min_np), 1.0, rtol=1.0e-12, atol=1.0e-12)
    np.testing.assert_allclose(np.vdot(v_max_np, v_max_np), 1.0, rtol=1.0e-12, atol=1.0e-12)
    np.testing.assert_allclose(
        operator @ v_min_np,
        float(lambda_min) * v_min_np,
        rtol=1.0e-12,
        atol=1.0e-12,
    )
    np.testing.assert_allclose(
        operator @ v_max_np,
        float(lambda_max) * v_max_np,
        rtol=1.0e-12,
        atol=1.0e-12,
    )


def test_terminal_extremal_mode_rayleigh_quotients_equal_extrema() -> None:
    problem = _nontrivial_metric_problem()
    horizon = 0.39

    lambda_min, v_min, lambda_max, v_max = terminal_signed_extremal_modes(problem, horizon)
    operator = np.asarray(whitened_terminal_signed_output_operator(problem, horizon))
    v_min_np = np.asarray(v_min)
    v_max_np = np.asarray(v_max)
    rq_min = np.vdot(v_min_np, operator @ v_min_np) / np.vdot(v_min_np, v_min_np)
    rq_max = np.vdot(v_max_np, operator @ v_max_np) / np.vdot(v_max_np, v_max_np)

    np.testing.assert_allclose(rq_min, np.asarray(lambda_min), rtol=1.0e-12, atol=1.0e-12)
    np.testing.assert_allclose(rq_max, np.asarray(lambda_max), rtol=1.0e-12, atol=1.0e-12)


def test_terminal_extremal_modes_are_orthogonal_in_nondegenerate_case() -> None:
    problem = TransportProblem(
        A=np.diag([-0.2, -0.9]),
        M=np.eye(2),
        Q=np.diag([-1.0, 2.0]),
        B=np.eye(2),
        Rin=np.diag([1.5, 0.7]),
    )

    lambda_min, v_min, lambda_max, v_max = terminal_signed_extremal_modes(problem, 0.6)

    assert float(lambda_min) < float(lambda_max)
    np.testing.assert_allclose(
        np.vdot(np.asarray(v_min), np.asarray(v_max)),
        0.0,
        rtol=0.0,
        atol=1.0e-13,
    )


def test_reconstructed_extremal_inputs_have_unit_input_cost() -> None:
    problem = _nontrivial_metric_problem()
    horizon = 0.44

    _, u_min, _, u_max = terminal_signed_extremal_inputs(problem, horizon)
    u_min_np = np.asarray(u_min)
    u_max_np = np.asarray(u_max)

    cost_min = np.vdot(u_min_np, problem.Rin @ u_min_np)
    cost_max = np.vdot(u_max_np, problem.Rin @ u_max_np)

    np.testing.assert_allclose(cost_min, 1.0, rtol=1.0e-12, atol=1.0e-12)
    np.testing.assert_allclose(cost_max, 1.0, rtol=1.0e-12, atol=1.0e-12)


def test_reconstructed_extremal_inputs_satisfy_generalized_eigenproblem() -> None:
    problem = _nontrivial_metric_problem()
    horizon = 0.52

    lambda_min, u_min, lambda_max, u_max = terminal_signed_extremal_inputs(problem, horizon)
    raw = np.asarray(terminal_signed_output_operator(problem, horizon))
    u_min_np = np.asarray(u_min)
    u_max_np = np.asarray(u_max)

    np.testing.assert_allclose(
        raw @ u_min_np,
        np.asarray(lambda_min) * (problem.Rin @ u_min_np),
        rtol=1.0e-12,
        atol=1.0e-12,
    )
    np.testing.assert_allclose(
        raw @ u_max_np,
        np.asarray(lambda_max) * (problem.Rin @ u_max_np),
        rtol=1.0e-12,
        atol=1.0e-12,
    )


def test_reconstructed_extremal_inputs_reproduce_direct_terminal_outputs() -> None:
    problem = _nontrivial_metric_problem()
    horizon = 0.36

    lambda_min, u_min, lambda_max, u_max = terminal_signed_extremal_inputs(problem, horizon)
    phi = np.asarray(constant_propagator(problem.A, horizon))

    for eigenvalue, optimizer in ((lambda_min, u_min), (lambda_max, u_max)):
        u = np.asarray(optimizer)
        x_terminal = phi @ problem.B @ u
        direct_output = np.vdot(x_terminal, problem.Q @ x_terminal)
        input_cost = np.vdot(u, problem.Rin @ u)

        np.testing.assert_allclose(input_cost, 1.0, rtol=1.0e-12, atol=1.0e-12)
        np.testing.assert_allclose(
            direct_output,
            np.asarray(eigenvalue),
            rtol=1.0e-12,
            atol=1.0e-12,
        )
