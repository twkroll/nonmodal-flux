"""Tests for finite-horizon accumulated signed-transport operators."""

import numpy as np
import scipy.integrate as sp_integrate
import scipy.linalg as sp_linalg

from nonmodal_flux.core.gramians import (
    accumulated_input_transport_operator,
    accumulated_signed_extrema,
    accumulated_transport_operator,
    whitened_accumulated_input_transport_operator,
)
from nonmodal_flux.core.problem import TransportProblem, hermiticity_error
from nonmodal_flux.core.propagators import constant_propagator


def _problem(A: np.ndarray, Q: np.ndarray) -> TransportProblem:
    n = A.shape[0]
    return TransportProblem(
        A=A,
        M=np.eye(n),
        Q=Q,
        B=np.eye(n),
        Rin=np.eye(n),
    )


def _quadrature_reference(A: np.ndarray, Q: np.ndarray, T: float) -> np.ndarray:
    def integrand(t: float) -> np.ndarray:
        phi = sp_linalg.expm(A * t)
        return phi.conj().T @ Q @ phi

    value, _ = sp_integrate.quad_vec(integrand, 0.0, T, epsabs=1.0e-12, epsrel=1.0e-12)
    return value


def test_accumulated_transport_operator_is_zero_at_zero_horizon() -> None:
    problem = _problem(
        np.array([[-1.0, 2.0], [0.0, -3.0]]),
        np.array([[0.0, 0.5], [0.5, 0.0]]),
    )

    operator = np.asarray(accumulated_transport_operator(problem, 0.0))

    np.testing.assert_allclose(operator, np.zeros((2, 2)), rtol=0.0, atol=1.0e-14)


def test_accumulated_transport_operator_matches_analytic_diagonal_case() -> None:
    rates = np.array([-0.5, -1.25])
    weights = np.array([3.0, -2.0])
    horizon = 0.4
    problem = _problem(np.diag(rates), np.diag(weights))

    operator = np.asarray(accumulated_transport_operator(problem, horizon))
    expected_diagonal = weights * (np.exp(2.0 * rates * horizon) - 1.0) / (2.0 * rates)

    np.testing.assert_allclose(
        operator,
        np.diag(expected_diagonal),
        rtol=1.0e-12,
        atol=1.0e-12,
    )


def test_accumulated_transport_operator_matches_numerical_quadrature() -> None:
    A = np.array([[-0.7, 1.4], [-0.2, -1.6]])
    Q = np.array([[0.3, 0.8], [0.8, -0.4]])
    horizon = 0.73
    problem = _problem(A, Q)

    operator = np.asarray(accumulated_transport_operator(problem, horizon))
    reference = _quadrature_reference(A, Q, horizon)

    np.testing.assert_allclose(operator, reference, rtol=1.0e-11, atol=1.0e-12)


def test_accumulated_transport_operator_supports_complex_dynamics_and_is_hermitian() -> None:
    A = np.array(
        [[-0.6 + 0.4j, 0.9 - 0.2j], [0.1j, -1.1 - 0.3j]],
        dtype=np.complex128,
    )
    Q = np.array([[0.2, 0.7j], [-0.7j, -0.3]], dtype=np.complex128)
    horizon = 0.49
    problem = _problem(A, Q)

    operator = np.asarray(accumulated_transport_operator(problem, horizon))
    reference = _quadrature_reference(A, Q, horizon)

    np.testing.assert_allclose(operator, reference, rtol=1.0e-11, atol=1.0e-12)
    assert hermiticity_error(operator) < 1.0e-12


def test_accumulated_transport_operator_satisfies_finite_horizon_lyapunov_identity() -> None:
    A = np.array([[-0.8, 1.7], [-0.3, -1.4]])
    Q = np.array([[0.1, 0.9], [0.9, -0.6]])
    horizon = 0.57
    problem = _problem(A, Q)

    operator = np.asarray(accumulated_transport_operator(problem, horizon))
    phi = np.asarray(constant_propagator(problem.A, horizon))
    lyapunov_rhs = A.conj().T @ operator + operator @ A + Q
    endpoint_integrand = phi.conj().T @ Q @ phi

    np.testing.assert_allclose(
        lyapunov_rhs,
        endpoint_integrand,
        rtol=1.0e-11,
        atol=1.0e-12,
    )


def test_accumulated_transport_operator_time_derivative_matches_lyapunov_rhs() -> None:
    A = np.array([[-0.9, 1.1], [0.2, -1.5]])
    Q = np.array([[0.4, 0.6], [0.6, -0.2]])
    horizon = 0.61
    step = 1.0e-5
    problem = _problem(A, Q)

    p_minus = np.asarray(accumulated_transport_operator(problem, horizon - step))
    p_plus = np.asarray(accumulated_transport_operator(problem, horizon + step))
    derivative = (p_plus - p_minus) / (2.0 * step)
    operator = np.asarray(accumulated_transport_operator(problem, horizon))
    lyapunov_rhs = A.conj().T @ operator + operator @ A + Q

    np.testing.assert_allclose(derivative, lyapunov_rhs, rtol=2.0e-9, atol=2.0e-10)


def test_accumulated_input_operator_matches_explicit_projection_and_is_hermitian() -> None:
    problem = TransportProblem(
        A=np.array([[-0.7, 1.4], [-0.2, -1.6]]),
        M=np.eye(2),
        Q=np.array([[0.3, 0.8], [0.8, -0.4]]),
        B=np.array([[1.0, 0.3], [-0.2, 1.0]]),
        Rin=np.eye(2),
    )
    horizon = 0.52

    p_q = np.asarray(accumulated_transport_operator(problem, horizon))
    projected = np.asarray(accumulated_input_transport_operator(problem, horizon))
    expected = problem.B.conj().T @ p_q @ problem.B

    np.testing.assert_allclose(projected, expected, rtol=1.0e-12, atol=1.0e-12)
    assert hermiticity_error(projected) < 1.0e-12


def test_accumulated_input_quadratic_form_matches_direct_time_integral() -> None:
    A = np.array(
        [[-0.6 + 0.4j, 0.9 - 0.2j], [0.1j, -1.1 - 0.3j]],
        dtype=np.complex128,
    )
    Q = np.array([[0.2, 0.7j], [-0.7j, -0.3]], dtype=np.complex128)
    B = np.array([[1.0, 0.2j], [-0.3j, 0.8]], dtype=np.complex128)
    problem = TransportProblem(A=A, M=np.eye(2), Q=Q, B=B, Rin=np.eye(2))
    horizon = 0.46
    u = np.array([0.7 - 0.2j, -1.1 + 0.4j], dtype=np.complex128)

    projected = np.asarray(accumulated_input_transport_operator(problem, horizon))
    input_space_value = np.vdot(u, projected @ u)

    def scalar_integrand(t: float) -> complex:
        x = sp_linalg.expm(A * t) @ B @ u
        return np.vdot(x, Q @ x)

    direct_value_real, _ = sp_integrate.quad(
        lambda t: float(np.real(scalar_integrand(t))),
        0.0,
        horizon,
        epsabs=1.0e-12,
        epsrel=1.0e-12,
    )
    direct_value_imag, _ = sp_integrate.quad(
        lambda t: float(np.imag(scalar_integrand(t))),
        0.0,
        horizon,
        epsabs=1.0e-12,
        epsrel=1.0e-12,
    )
    direct_value = direct_value_real + 1j * direct_value_imag

    np.testing.assert_allclose(input_space_value, direct_value, rtol=1.0e-11, atol=1.0e-12)


def test_accumulated_input_operator_respects_restricted_input_space() -> None:
    problem = TransportProblem(
        A=np.array([[-1.0, 0.0], [2.0, -2.0]]),
        M=np.eye(2),
        Q=np.array([[0.0, 0.5], [0.5, 0.0]]),
        B=np.array([[1.0], [0.0]]),
        Rin=np.array([[1.0]]),
    )
    horizon = 0.3

    projected = np.asarray(accumulated_input_transport_operator(problem, horizon))
    p_q = np.asarray(accumulated_transport_operator(problem, horizon))
    expected = problem.B.conj().T @ p_q @ problem.B

    assert projected.shape == (1, 1)
    np.testing.assert_allclose(projected, expected, rtol=1.0e-12, atol=1.0e-12)
    assert projected[0, 0] > 0.0


def test_identity_input_metric_leaves_accumulated_input_operator_unchanged() -> None:
    problem = TransportProblem(
        A=np.array([[-0.7, 1.4], [-0.2, -1.6]]),
        M=np.eye(2),
        Q=np.array([[0.3, 0.8], [0.8, -0.4]]),
        B=np.array([[1.0, 0.3], [-0.2, 1.0]]),
        Rin=np.eye(2),
    )
    horizon = 0.43

    raw = np.asarray(accumulated_input_transport_operator(problem, horizon))
    whitened = np.asarray(whitened_accumulated_input_transport_operator(problem, horizon))

    np.testing.assert_allclose(whitened, raw, rtol=1.0e-13, atol=1.0e-13)


def test_accumulated_whitening_matches_explicit_cholesky_reference() -> None:
    problem = TransportProblem(
        A=np.array([[-0.7, 1.4], [-0.2, -1.6]]),
        M=np.array([[2.0, 0.2], [0.2, 1.3]]),
        Q=np.array([[0.3, 0.8], [0.8, -0.4]]),
        B=np.array([[1.0, 0.3], [-0.2, 1.0]]),
        Rin=np.array([[2.4, 0.35], [0.35, 1.2]]),
    )
    horizon = 0.58

    raw = np.asarray(accumulated_input_transport_operator(problem, horizon))
    whitened = np.asarray(whitened_accumulated_input_transport_operator(problem, horizon))
    lower = np.linalg.cholesky(problem.Rin)
    lower_inverse = np.linalg.inv(lower)
    expected = lower_inverse @ raw @ lower_inverse.conj().T

    np.testing.assert_allclose(whitened, expected, rtol=1.0e-12, atol=1.0e-12)
    assert hermiticity_error(whitened) < 1.0e-12


def test_accumulated_whitening_preserves_generalized_rayleigh_quotient() -> None:
    problem = TransportProblem(
        A=np.array([[-0.7, 1.4], [-0.2, -1.6]]),
        M=np.array([[2.0, 0.2], [0.2, 1.3]]),
        Q=np.array([[0.3, 0.8], [0.8, -0.4]]),
        B=np.array([[1.0, 0.3], [-0.2, 1.0]]),
        Rin=np.array([[2.4, 0.35], [0.35, 1.2]]),
    )
    horizon = 0.31
    u = np.array([0.7 - 0.2j, -1.1 + 0.4j], dtype=np.complex128)

    raw = np.asarray(accumulated_input_transport_operator(problem, horizon))
    whitened = np.asarray(whitened_accumulated_input_transport_operator(problem, horizon))
    lower = np.linalg.cholesky(problem.Rin)
    v = lower.conj().T @ u

    generalized_quotient = np.vdot(u, raw @ u) / np.vdot(u, problem.Rin @ u)
    euclidean_quotient = np.vdot(v, whitened @ v) / np.vdot(v, v)

    np.testing.assert_allclose(
        euclidean_quotient,
        generalized_quotient,
        rtol=1.0e-12,
        atol=1.0e-12,
    )


def test_accumulated_whitening_supports_complex_positive_input_metric() -> None:
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

    raw = np.asarray(accumulated_input_transport_operator(problem, horizon))
    whitened = np.asarray(whitened_accumulated_input_transport_operator(problem, horizon))
    lower = np.linalg.cholesky(problem.Rin)
    lower_inverse = np.linalg.inv(lower)
    expected = lower_inverse @ raw @ lower_inverse.conj().T

    np.testing.assert_allclose(whitened, expected, rtol=1.0e-12, atol=1.0e-12)
    assert hermiticity_error(whitened) < 1.0e-12


def test_accumulated_signed_extrema_match_analytic_diagonal_case() -> None:
    rates = np.array([-0.5, -1.25])
    weights = np.array([3.0, -2.0])
    rin_diagonal = np.array([2.0, 0.5])
    horizon = 0.4
    problem = TransportProblem(
        A=np.diag(rates),
        M=np.eye(2),
        Q=np.diag(weights),
        B=np.eye(2),
        Rin=np.diag(rin_diagonal),
    )

    lambda_min, lambda_max = accumulated_signed_extrema(problem, horizon)
    accumulated_diagonal = weights * (np.exp(2.0 * rates * horizon) - 1.0) / (2.0 * rates)
    expected = accumulated_diagonal / rin_diagonal

    np.testing.assert_allclose(
        np.asarray([lambda_min, lambda_max]),
        np.asarray([expected.min(), expected.max()]),
        rtol=1.0e-12,
        atol=1.0e-12,
    )


def test_accumulated_signed_extrema_match_generalized_hermitian_eigenproblem() -> None:
    problem = TransportProblem(
        A=np.array([[-0.7, 1.4], [-0.2, -1.6]]),
        M=np.array([[2.0, 0.2], [0.2, 1.3]]),
        Q=np.array([[0.3, 0.8], [0.8, -0.4]]),
        B=np.array([[1.0, 0.3], [-0.2, 1.0]]),
        Rin=np.array([[2.4, 0.35], [0.35, 1.2]]),
    )
    horizon = 0.53

    raw = np.asarray(accumulated_input_transport_operator(problem, horizon))
    reference = sp_linalg.eigh(raw, problem.Rin, eigvals_only=True)
    lambda_min, lambda_max = accumulated_signed_extrema(problem, horizon)

    np.testing.assert_allclose(
        np.asarray([lambda_min, lambda_max]),
        np.asarray([reference[0], reference[-1]]),
        rtol=1.0e-12,
        atol=1.0e-12,
    )


def test_accumulated_signed_extrema_retain_both_transport_signs() -> None:
    problem = TransportProblem(
        A=np.zeros((2, 2), dtype=float),
        M=np.eye(2),
        Q=np.array([[0.0, 1.0], [1.0, 0.0]]),
        B=np.eye(2),
        Rin=np.eye(2),
    )
    horizon = 0.7

    lambda_min, lambda_max = accumulated_signed_extrema(problem, horizon)

    assert float(lambda_min) < 0.0 < float(lambda_max)
    np.testing.assert_allclose(
        np.asarray([lambda_min, lambda_max]),
        np.array([-horizon, horizon]),
        rtol=1.0e-13,
        atol=1.0e-13,
    )
