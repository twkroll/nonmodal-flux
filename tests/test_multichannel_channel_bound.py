"""Tests for the T3.2 multichannel channel-resolved finite-horizon bound."""

import numpy as np

from nonmodal_flux.core.gramians import accumulated_transport_operator
from nonmodal_flux.core.problem import TransportProblem
from nonmodal_flux.core.propagators import constant_propagator


def _channel_bound_witness() -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    float,
    float,
    float,
]:
    """Return a stable two-channel balance with a sharp global leakage constant."""

    a = np.array(
        [
            [-0.9, 0.8, 0.0],
            [-0.1, -1.4, 0.5],
            [0.0, -0.2, -1.8],
        ]
    )
    m = np.eye(3)
    dissipation = np.diag([2.2, 2.6, 3.2])
    g_target = 1.1
    g_other = 0.7

    q_other = np.array(
        [
            [-0.5, 0.3, 0.0],
            [0.3, 0.4, 0.2],
            [0.0, 0.2, 0.8],
        ]
    )
    q_target = (
        a.conj().T @ m + m @ a + dissipation - g_other * q_other
    ) / g_target

    leakage_constant = max(0.0, -float(np.linalg.eigvalsh(g_other * q_other)[0]))
    return (
        a,
        m,
        dissipation,
        q_target,
        q_other,
        g_target,
        g_other,
        leakage_constant,
    )


def _problem(a: np.ndarray, m: np.ndarray, q: np.ndarray) -> TransportProblem:
    return TransportProblem(
        A=a,
        M=m,
        Q=q,
        B=np.eye(a.shape[0]),
        Rin=np.eye(a.shape[0]),
    )


def test_witness_satisfies_balance_and_cross_channel_lower_bound() -> None:
    (
        a,
        m,
        dissipation,
        q_target,
        q_other,
        g_target,
        g_other,
        leakage_constant,
    ) = _channel_bound_witness()

    balance_left = a.conj().T @ m + m @ a
    balance_right = g_target * q_target + g_other * q_other - dissipation
    np.testing.assert_allclose(balance_left, balance_right, rtol=0.0, atol=2.0e-14)

    lower_bound_residual = g_other * q_other + leakage_constant * m
    assert np.linalg.eigvalsh(lower_bound_residual)[0] >= -2.0e-14
    assert leakage_constant > 0.0
    assert np.all(np.real(np.linalg.eigvals(a)) < 0.0)
    assert np.linalg.eigvalsh(q_target)[0] < 0.0 < np.linalg.eigvalsh(q_target)[-1]


def test_multichannel_integrated_balance_holds_at_finite_horizon() -> None:
    (
        a,
        m,
        dissipation,
        q_target,
        q_other,
        g_target,
        g_other,
        _,
    ) = _channel_bound_witness()

    target_problem = _problem(a, m, q_target)
    other_problem = _problem(a, m, q_other)
    dissipation_problem = _problem(a, m, dissipation)

    for horizon in (0.08, 0.45, 1.2):
        p_target = np.asarray(accumulated_transport_operator(target_problem, horizon))
        p_other = np.asarray(accumulated_transport_operator(other_problem, horizon))
        p_d = np.asarray(accumulated_transport_operator(dissipation_problem, horizon))
        phi = np.asarray(constant_propagator(a, horizon))
        delta_m = phi.conj().T @ m @ phi - m

        np.testing.assert_allclose(
            g_target * p_target + g_other * p_other,
            delta_m + p_d,
            rtol=2.0e-11,
            atol=4.0e-12,
        )


def test_t3_channel_resolved_operator_bound_holds() -> None:
    (
        a,
        m,
        dissipation,
        q_target,
        q_other,
        g_target,
        g_other,
        leakage_constant,
    ) = _channel_bound_witness()

    target_problem = _problem(a, m, q_target)
    other_problem = _problem(a, m, q_other)
    dissipation_problem = _problem(a, m, dissipation)
    metric_problem = _problem(a, m, m)

    for horizon in (0.05, 0.3, 0.9):
        p_target = np.asarray(accumulated_transport_operator(target_problem, horizon))
        p_other = np.asarray(accumulated_transport_operator(other_problem, horizon))
        p_d = np.asarray(accumulated_transport_operator(dissipation_problem, horizon))
        p_m = np.asarray(accumulated_transport_operator(metric_problem, horizon))
        phi = np.asarray(constant_propagator(a, horizon))
        delta_m = phi.conj().T @ m @ phi - m

        bound_residual = (
            delta_m
            + p_d
            + leakage_constant * p_m
            - g_target * p_target
        )
        expected_residual = g_other * p_other + leakage_constant * p_m
        np.testing.assert_allclose(
            bound_residual,
            expected_residual,
            rtol=2.0e-11,
            atol=4.0e-12,
        )
        assert np.linalg.eigvalsh(bound_residual)[0] >= -2.0e-11


def test_smaller_than_sharp_leakage_constant_can_break_the_bound() -> None:
    (
        a,
        m,
        dissipation,
        q_target,
        _,
        g_target,
        _,
        leakage_constant,
    ) = _channel_bound_witness()

    target_problem = _problem(a, m, q_target)
    dissipation_problem = _problem(a, m, dissipation)
    metric_problem = _problem(a, m, m)
    too_small = 0.8 * leakage_constant
    horizon = 1.0e-4

    p_target = np.asarray(accumulated_transport_operator(target_problem, horizon))
    p_d = np.asarray(accumulated_transport_operator(dissipation_problem, horizon))
    p_m = np.asarray(accumulated_transport_operator(metric_problem, horizon))
    phi = np.asarray(constant_propagator(a, horizon))
    delta_m = phi.conj().T @ m @ phi - m

    invalid_residual = delta_m + p_d + too_small * p_m - g_target * p_target
    assert np.linalg.eigvalsh(invalid_residual)[0] < -1.0e-6
