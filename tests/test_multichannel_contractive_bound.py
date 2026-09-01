"""Tests for the T3.3 contractive-energy multichannel transport bound."""

import numpy as np

from nonmodal_flux.core.gramians import (
    accumulated_signed_extrema,
    accumulated_transport_operator,
)
from nonmodal_flux.core.problem import TransportProblem
from nonmodal_flux.core.propagators import constant_propagator


def _contractive_multichannel_witness() -> tuple[
    TransportProblem,
    np.ndarray,
    np.ndarray,
    float,
    float,
    float,
]:
    """Return a stable two-channel witness with a sharp global leakage constant."""

    a = np.diag([-1.0, -1.5])
    m = np.eye(2)
    g_target = 1.2
    g_competing = 0.7
    q_target = np.diag([0.6, -0.3])
    q_competing = np.diag([-0.4, 0.2])
    dissipation = (
        g_target * q_target
        + g_competing * q_competing
        - (a.conj().T @ m + m @ a)
    )
    b = np.array([[1.0, 0.3], [0.2, 1.0]])
    rin = b.conj().T @ m @ b

    leakage = -float(np.min(np.linalg.eigvalsh(g_competing * q_competing)))
    problem = TransportProblem(
        A=a,
        M=m,
        Q=q_target,
        B=b,
        Rin=rin,
    )
    return problem, q_competing, dissipation, g_target, g_competing, leakage


def _with_observable(problem: TransportProblem, observable: np.ndarray) -> TransportProblem:
    return TransportProblem(
        A=problem.A,
        M=problem.M,
        Q=observable,
        B=problem.B,
        Rin=problem.Rin,
    )


def test_witness_satisfies_balance_contraction_and_competing_channel_lower_bound() -> None:
    problem, q_competing, dissipation, g_target, g_competing, leakage = (
        _contractive_multichannel_witness()
    )

    balance_left = problem.A.conj().T @ problem.M + problem.M @ problem.A
    balance_right = g_target * problem.Q + g_competing * q_competing - dissipation
    np.testing.assert_allclose(balance_left, balance_right, rtol=0.0, atol=2.0e-14)

    assert np.all(np.linalg.eigvalsh(dissipation) > 0.0)
    assert np.all(np.linalg.eigvalsh(balance_left) < 0.0)
    assert problem.uses_natural_energy_input_metric()

    leakage_residual = g_competing * q_competing + leakage * problem.M
    assert np.min(np.linalg.eigvalsh(leakage_residual)) >= -2.0e-14
    np.testing.assert_allclose(leakage, 0.28, rtol=0.0, atol=2.0e-14)


def test_contractive_energy_implies_delta_m_nonpositive_and_p_m_below_t_m() -> None:
    problem, _, _, _, _, _ = _contractive_multichannel_witness()
    metric_problem = _with_observable(problem, problem.M)

    for horizon in (0.08, 0.45, 1.2):
        phi = np.asarray(constant_propagator(problem.A, horizon))
        delta_m = phi.conj().T @ problem.M @ phi - problem.M
        p_m = np.asarray(accumulated_transport_operator(metric_problem, horizon))

        assert np.max(np.linalg.eigvalsh(delta_m)) <= 2.0e-13
        assert np.min(np.linalg.eigvalsh(horizon * problem.M - p_m)) >= -2.0e-13


def test_t3_3_channel_resolved_operator_bound_holds() -> None:
    problem, _, dissipation, g_target, _, leakage = _contractive_multichannel_witness()
    dissipation_problem = _with_observable(problem, dissipation)

    for horizon in (0.08, 0.45, 1.2):
        p_target = np.asarray(accumulated_transport_operator(problem, horizon))
        p_d = np.asarray(accumulated_transport_operator(dissipation_problem, horizon))
        residual = p_d + leakage * horizon * problem.M - g_target * p_target

        assert np.min(np.linalg.eigvalsh(residual)) >= -4.0e-12


def test_t3_3_positive_gain_bound_holds_with_natural_input_metric() -> None:
    problem, _, dissipation, g_target, _, leakage = _contractive_multichannel_witness()
    dissipation_problem = _with_observable(problem, dissipation)

    for horizon in (0.08, 0.45, 1.2):
        _, target_max = accumulated_signed_extrema(problem, horizon)
        _, dissipation_max = accumulated_signed_extrema(dissipation_problem, horizon)
        upper_bound = (float(dissipation_max) + leakage * horizon) / g_target

        assert float(target_max) > 0.0
        assert float(target_max) <= upper_bound + 4.0e-12
