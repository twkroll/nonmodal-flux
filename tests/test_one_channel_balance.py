"""Tests for the T2 one-channel balance and its short-time T4 interpretation."""

import numpy as np

from nonmodal_flux.core.gramians import (
    accumulated_signed_extremal_modes,
    accumulated_transport_operator,
)
from nonmodal_flux.core.problem import TransportProblem
from nonmodal_flux.core.propagators import constant_propagator


def _balance_witness() -> tuple[TransportProblem, np.ndarray, float]:
    """Return a stable transport-neutral witness satisfying A^H M + M A = g Q - D."""

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


def _angle(v: np.ndarray, w: np.ndarray) -> float:
    cosine = abs(np.vdot(v, w)) / (np.linalg.norm(v) * np.linalg.norm(w))
    return float(np.arccos(np.clip(cosine, 0.0, 1.0)))


def _terminal_energy_top_mode(problem: TransportProblem, horizon: float) -> np.ndarray:
    phi = np.asarray(constant_propagator(problem.A, horizon))
    propagated = phi @ problem.B
    raw = propagated.conj().T @ problem.M @ propagated

    lower = np.linalg.cholesky(problem.Rin)
    inverse_lower = np.linalg.solve(lower, np.eye(problem.input_dim))
    whitened = inverse_lower @ raw @ inverse_lower.conj().T
    _, eigenvectors = np.linalg.eigh(whitened)
    return eigenvectors[:, -1]


def test_witness_satisfies_one_channel_balance_and_transport_neutrality() -> None:
    problem, d, g = _balance_witness()

    balance_left = problem.A.conj().T @ problem.M + problem.M @ problem.A
    balance_right = g * problem.Q - d
    np.testing.assert_allclose(balance_left, balance_right, rtol=0.0, atol=2.0e-14)

    assert np.all(np.linalg.eigvalsh(d) > 0.0)
    assert np.all(np.real(np.linalg.eigvals(problem.A)) < 0.0)
    assert problem.uses_natural_energy_input_metric()
    assert problem.is_transport_neutral()


def test_t2_integrated_balance_identity_holds_at_finite_horizon() -> None:
    problem, d, g = _balance_witness()
    dissipation_problem = _dissipation_problem(problem, d)

    for horizon in (0.07, 0.4, 1.1):
        p_q = np.asarray(accumulated_transport_operator(problem, horizon))
        p_d = np.asarray(accumulated_transport_operator(dissipation_problem, horizon))
        phi = np.asarray(constant_propagator(problem.A, horizon))
        delta_m = phi.conj().T @ problem.M @ phi - problem.M

        np.testing.assert_allclose(
            g * p_q,
            delta_m + p_d,
            rtol=2.0e-11,
            atol=3.0e-12,
        )


def test_transport_neutral_balance_makes_energy_direction_least_dissipative() -> None:
    problem, d, _ = _balance_witness()

    e1 = problem.B.conj().T @ (
        problem.A.conj().T @ problem.M + problem.M @ problem.A
    ) @ problem.B
    projected_d = problem.B.conj().T @ d @ problem.B

    np.testing.assert_allclose(e1, -projected_d, rtol=0.0, atol=2.0e-14)

    dissipation_values, dissipation_vectors = np.linalg.eigh(projected_d)
    energy_values, energy_vectors = np.linalg.eigh(e1)
    assert dissipation_values[0] < dissipation_values[-1]
    assert energy_values[-1] > energy_values[0]
    assert _angle(energy_vectors[:, -1], dissipation_vectors[:, 0]) < 1.0e-12


def test_short_time_energy_and_transport_optima_select_different_physical_mechanisms() -> None:
    problem, _, _ = _balance_witness()

    e1 = problem.B.conj().T @ (
        problem.A.conj().T @ problem.M + problem.M @ problem.A
    ) @ problem.B
    h1 = problem.B.conj().T @ (
        problem.A.conj().T @ problem.Q + problem.Q @ problem.A
    ) @ problem.B

    e_values, e_vectors = np.linalg.eigh(e1)
    h_values, h_vectors = np.linalg.eigh(h1)
    energy_limit = e_vectors[:, -1]
    transport_limit = h_vectors[:, -1]

    assert e_values[-1] > e_values[-2]
    assert h_values[-1] > h_values[-2]
    assert h_values[-1] > 0.0
    limiting_angle = _angle(energy_limit, transport_limit)
    assert limiting_angle > 1.2

    horizon = 1.0e-3
    energy_mode = _terminal_energy_top_mode(problem, horizon)
    _, _, _, transport_mode = accumulated_signed_extremal_modes(problem, horizon)
    transport_mode = np.asarray(transport_mode)

    assert _angle(energy_mode, energy_limit) < 2.0e-4
    assert _angle(transport_mode, transport_limit) < 2.0e-4
    np.testing.assert_allclose(
        _angle(energy_mode, transport_mode),
        limiting_angle,
        rtol=0.0,
        atol=4.0e-4,
    )
