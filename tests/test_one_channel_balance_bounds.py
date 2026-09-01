"""Tests for the finite-horizon T2 bounds in the contractive one-channel case."""

import numpy as np

from nonmodal_flux.core.gramians import (
    accumulated_signed_extrema,
    whitened_accumulated_input_transport_operator,
)
from nonmodal_flux.core.problem import TransportProblem
from nonmodal_flux.core.propagators import constant_propagator


def _contractive_balance_witness() -> tuple[TransportProblem, np.ndarray, float]:
    """Return a natural-metric witness with A^H M + M A = g Q - D <= 0."""

    g = 1.2
    q = np.block(
        [
            [np.zeros((2, 2)), np.eye(2)],
            [np.eye(2), np.zeros((2, 2))],
        ]
    )
    d = np.diag([1.5, 2.5, 3.0, 3.5])
    cross_skew = np.array([[0.4, 0.3], [-0.1, -0.2]])
    skew = np.block(
        [
            [np.zeros((2, 2)), cross_skew],
            [-cross_skew.T, np.zeros((2, 2))],
        ]
    )
    a = 0.5 * (g * q - d) + skew
    b = np.vstack([np.eye(2), np.zeros((2, 2))])

    problem = TransportProblem(
        A=a,
        M=np.eye(4),
        Q=q,
        B=b,
        Rin=np.eye(2),
    )
    return problem, d, g


def _dissipation_problem(problem: TransportProblem, d: np.ndarray) -> TransportProblem:
    return TransportProblem(
        A=problem.A,
        M=problem.M,
        Q=d,
        B=problem.B,
        Rin=problem.Rin,
    )


def _whitened_terminal_energy_operator(problem: TransportProblem, horizon: float) -> np.ndarray:
    phi = np.asarray(constant_propagator(problem.A, horizon))
    propagated = phi @ problem.B
    raw = propagated.conj().T @ problem.M @ propagated

    lower = np.linalg.cholesky(problem.Rin)
    inverse_lower = np.linalg.solve(lower, np.eye(problem.input_dim))
    return inverse_lower @ raw @ inverse_lower.conj().T


def test_balance_witness_is_energy_contractive() -> None:
    problem, d, g = _contractive_balance_witness()

    rate = problem.A.conj().T @ problem.M + problem.M @ problem.A
    np.testing.assert_allclose(rate, g * problem.Q - d, rtol=0.0, atol=2.0e-14)
    assert np.linalg.eigvalsh(rate)[-1] < 0.0
    assert problem.uses_natural_energy_input_metric()

    for horizon in (0.05, 0.3, 1.0):
        h_e = _whitened_terminal_energy_operator(problem, horizon)
        assert np.linalg.eigvalsh(np.eye(problem.input_dim) - h_e)[0] >= -2.0e-12


def test_t2_matrix_bounds_hold_for_contracting_one_channel_balance() -> None:
    problem, d, g = _contractive_balance_witness()
    dissipation_problem = _dissipation_problem(problem, d)
    identity = np.eye(problem.input_dim)

    for horizon in (0.03, 0.2, 0.8, 1.5):
        h_q = np.asarray(whitened_accumulated_input_transport_operator(problem, horizon))
        h_d = np.asarray(
            whitened_accumulated_input_transport_operator(dissipation_problem, horizon)
        )

        upper_slack = h_d / g - h_q
        lower_slack = h_q + identity / g

        assert np.linalg.eigvalsh(upper_slack)[0] >= -4.0e-11
        assert np.linalg.eigvalsh(lower_slack)[0] >= -4.0e-11


def test_t2_signed_extrema_obey_scalar_bounds() -> None:
    problem, d, g = _contractive_balance_witness()
    dissipation_problem = _dissipation_problem(problem, d)

    for horizon in (0.03, 0.2, 0.8, 1.5):
        q_min, q_max = accumulated_signed_extrema(problem, horizon)
        h_d = np.asarray(
            whitened_accumulated_input_transport_operator(dissipation_problem, horizon)
        )
        d_max = np.linalg.eigvalsh(h_d)[-1]

        assert float(q_max) <= d_max / g + 5.0e-11
        assert float(q_min) >= -1.0 / g - 5.0e-11


def test_whitened_t2_identity_explains_both_bounds() -> None:
    problem, d, g = _contractive_balance_witness()
    dissipation_problem = _dissipation_problem(problem, d)
    identity = np.eye(problem.input_dim)

    for horizon in (0.1, 0.6, 1.2):
        h_q = np.asarray(whitened_accumulated_input_transport_operator(problem, horizon))
        h_d = np.asarray(
            whitened_accumulated_input_transport_operator(dissipation_problem, horizon)
        )
        h_e = _whitened_terminal_energy_operator(problem, horizon)

        np.testing.assert_allclose(
            g * h_q,
            h_e - identity + h_d,
            rtol=2.0e-11,
            atol=4.0e-12,
        )
        assert np.linalg.eigvalsh(identity - h_e)[0] >= -3.0e-12
        assert np.linalg.eigvalsh(h_e)[0] >= -3.0e-12
        assert np.linalg.eigvalsh(h_d)[0] >= -3.0e-12
