"""Tests for whitened extremal modes of accumulated signed transport."""

import numpy as np

from nonmodal_flux.core.gramians import (
    accumulated_signed_extremal_modes,
    whitened_accumulated_input_transport_operator,
)
from nonmodal_flux.core.problem import TransportProblem


def _nontrivial_metric_problem() -> TransportProblem:
    return TransportProblem(
        A=np.array([[-0.7, 1.4], [-0.2, -1.6]]),
        M=np.array([[2.0, 0.2], [0.2, 1.3]]),
        Q=np.array([[0.3, 0.8], [0.8, -0.4]]),
        B=np.array([[1.0, 0.3], [-0.2, 1.0]]),
        Rin=np.array([[2.4, 0.35], [0.35, 1.2]]),
    )


def test_accumulated_extremal_modes_are_unit_norm_and_satisfy_eigenproblem() -> None:
    problem = _nontrivial_metric_problem()
    horizon = 0.47

    lambda_min, v_min, lambda_max, v_max = accumulated_signed_extremal_modes(
        problem, horizon
    )
    operator = np.asarray(whitened_accumulated_input_transport_operator(problem, horizon))
    v_min = np.asarray(v_min)
    v_max = np.asarray(v_max)

    np.testing.assert_allclose(np.vdot(v_min, v_min), 1.0, rtol=1.0e-12, atol=1.0e-12)
    np.testing.assert_allclose(np.vdot(v_max, v_max), 1.0, rtol=1.0e-12, atol=1.0e-12)
    np.testing.assert_allclose(operator @ v_min, lambda_min * v_min, rtol=1.0e-11, atol=1.0e-12)
    np.testing.assert_allclose(operator @ v_max, lambda_max * v_max, rtol=1.0e-11, atol=1.0e-12)


def test_accumulated_extremal_mode_rayleigh_quotients_equal_extrema() -> None:
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
    horizon = 0.39

    lambda_min, v_min, lambda_max, v_max = accumulated_signed_extremal_modes(
        problem, horizon
    )
    operator = np.asarray(whitened_accumulated_input_transport_operator(problem, horizon))
    v_min = np.asarray(v_min)
    v_max = np.asarray(v_max)

    rq_min = np.vdot(v_min, operator @ v_min) / np.vdot(v_min, v_min)
    rq_max = np.vdot(v_max, operator @ v_max) / np.vdot(v_max, v_max)

    np.testing.assert_allclose(rq_min, lambda_min, rtol=1.0e-11, atol=1.0e-12)
    np.testing.assert_allclose(rq_max, lambda_max, rtol=1.0e-11, atol=1.0e-12)


def test_accumulated_extremal_modes_are_orthogonal_when_extrema_are_nondegenerate() -> None:
    problem = TransportProblem(
        A=np.diag([-0.2, -0.9]),
        M=np.eye(2),
        Q=np.diag([-1.0, 2.0]),
        B=np.eye(2),
        Rin=np.diag([1.5, 0.7]),
    )
    horizon = 0.6

    lambda_min, v_min, lambda_max, v_max = accumulated_signed_extremal_modes(
        problem, horizon
    )
    v_min = np.asarray(v_min)
    v_max = np.asarray(v_max)

    assert float(lambda_min) < float(lambda_max)
    np.testing.assert_allclose(np.vdot(v_min, v_max), 0.0, rtol=0.0, atol=1.0e-12)
