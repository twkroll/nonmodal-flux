"""Tests for T2 single-channel balance identities, bounds, and T4 short-time interpretation."""

import numpy as np

from nonmodal_flux.core.gramians import (
    accumulated_signed_extremal_modes,
    accumulated_signed_extrema,
    accumulated_transport_operator,
    whitened_accumulated_input_transport_operator,
)
from nonmodal_flux.core.problem import TransportProblem
from nonmodal_flux.core.propagators import constant_propagator


def _single_channel_witness() -> tuple[TransportProblem, TransportProblem, float, np.ndarray]:
    """Return a contractive balance witness and a matching dissipation-output problem."""

    g = 1.3
    d_input = np.diag([1.6, 2.4])
    d_latent = np.diag([3.0, 3.4])
    dissipation = np.block(
        [
            [d_input, np.zeros((2, 2))],
            [np.zeros((2, 2)), d_latent],
        ]
    )

    q = np.block(
        [
            [np.zeros((2, 2)), np.eye(2)],
            [np.eye(2), np.zeros((2, 2))],
        ]
    )
    coupling = np.array([[0.15, 0.55], [0.55, 0.90]])
    a = np.block(
        [
            [-0.5 * d_input, g * np.eye(2) - coupling.T],
            [coupling, -0.5 * d_latent],
        ]
    )
    b = np.vstack([np.eye(2), np.zeros((2, 2))])
    m = np.eye(4)
    rin = b.T @ m @ b

    transport_problem = TransportProblem(A=a, M=m, Q=q, B=b, Rin=rin)
    dissipation_problem = TransportProblem(A=a, M=m, Q=dissipation, B=b, Rin=rin)
    return transport_problem, dissipation_problem, g, dissipation


def _angle(v: np.ndarray, w: np.ndarray) -> float:
    v = np.asarray(v)
    w = np.asarray(w)
    cosine = abs(np.vdot(v, w)) / (np.linalg.norm(v) * np.linalg.norm(w))
    return float(np.arccos(np.clip(cosine, 0.0, 1.0)))


def _terminal_energy_operator(problem: TransportProblem, horizon: float) -> np.ndarray:
    phi = np.asarray(constant_propagator(problem.A, horizon))
    propagated = phi @ problem.B
    return propagated.conj().T @ problem.M @ propagated


def test_single_channel_witness_satisfies_balance_and_contractivity() -> None:
    problem, _, g, dissipation = _single_channel_witness()

    balance_left = problem.A.conj().T @ problem.M + problem.M @ problem.A
    balance_right = g * problem.Q - dissipation
    np.testing.assert_allclose(balance_left, balance_right, rtol=0.0, atol=2.0e-14)

    assert np.linalg.eigvalsh(dissipation)[0] > 0.0
    assert np.linalg.eigvalsh(balance_left)[-1] < 0.0
    assert np.max(np.real(np.linalg.eigvals(problem.A))) < 0.0
    assert problem.uses_natural_energy_input_metric()
    assert problem.is_transport_neutral()


def test_t2_exact_state_and_whitened_balance_identities() -> None:
    problem, dissipation_problem, g, _ = _single_channel_witness()
    horizon = 0.37

    p_q = np.asarray(accumulated_transport_operator(problem, horizon))
    p_d = np.asarray(accumulated_transport_operator(dissipation_problem, horizon))
    phi = np.asarray(constant_propagator(problem.A, horizon))
    energy_change = phi.conj().T @ problem.M @ phi - problem.M

    np.testing.assert_allclose(
        g * p_q,
        energy_change + p_d,
        rtol=3.0e-11,
        atol=3.0e-12,
    )

    h_q = np.asarray(whitened_accumulated_input_transport_operator(problem, horizon))
    h_d = np.asarray(
        whitened_accumulated_input_transport_operator(dissipation_problem, horizon)
    )
    h_e = _terminal_energy_operator(problem, horizon)

    np.testing.assert_allclose(
        g * h_q,
        h_e - np.eye(problem.input_dim) + h_d,
        rtol=3.0e-11,
        atol=3.0e-12,
    )


def test_t2_contractive_signed_bounds_hold() -> None:
    problem, dissipation_problem, g, _ = _single_channel_witness()
    horizon = 0.53

    h_q = np.asarray(whitened_accumulated_input_transport_operator(problem, horizon))
    h_d = np.asarray(
        whitened_accumulated_input_transport_operator(dissipation_problem, horizon)
    )
    difference = h_d / g - h_q
    assert np.linalg.eigvalsh(difference)[0] > -2.0e-11

    lambda_min, lambda_max = accumulated_signed_extrema(problem, horizon)
    lambda_min = float(np.asarray(lambda_min))
    lambda_max = float(np.asarray(lambda_max))
    upper_bound = np.linalg.eigvalsh(h_d)[-1] / g

    assert lambda_max <= upper_bound + 2.0e-11
    assert lambda_min >= -1.0 / g - 2.0e-11


def test_short_time_energy_optimum_is_least_dissipative_direction() -> None:
    problem, _, g, dissipation = _single_channel_witness()

    projected_q = problem.B.conj().T @ problem.Q @ problem.B
    projected_d = problem.B.conj().T @ dissipation @ problem.B
    e1 = problem.B.conj().T @ (
        problem.A.conj().T @ problem.M + problem.M @ problem.A
    ) @ problem.B
    np.testing.assert_allclose(projected_q, 0.0, rtol=0.0, atol=1.0e-14)
    np.testing.assert_allclose(e1, -projected_d, rtol=0.0, atol=2.0e-14)

    d_values, d_vectors = np.linalg.eigh(projected_d)
    e_values, e_vectors = np.linalg.eigh(e1)
    assert d_values[0] < d_values[-1]
    assert e_values[-1] > e_values[0]
    assert _angle(d_vectors[:, 0], e_vectors[:, -1]) < 1.0e-12

    h1 = problem.B.conj().T @ (
        problem.A.conj().T @ problem.Q + problem.Q @ problem.A
    ) @ problem.B
    h_values, h_vectors = np.linalg.eigh(h1)
    assert h_values[-1] > 0.0
    assert _angle(e_vectors[:, -1], h_vectors[:, -1]) > 0.9

    horizon = 1.0e-3
    energy_operator = _terminal_energy_operator(problem, horizon)
    _, finite_energy_vectors = np.linalg.eigh(energy_operator)
    _, _, _, finite_transport_mode = accumulated_signed_extremal_modes(problem, horizon)

    assert _angle(finite_energy_vectors[:, -1], e_vectors[:, -1]) < 5.0e-4
    assert _angle(np.asarray(finite_transport_mode), h_vectors[:, -1]) < 5.0e-4

    # The one-channel balance fixes the energy derivative on the neutral input
    # subspace through dissipation, but it does not force the flux-generation
    # direction to coincide with the least-dissipative direction.
    assert g > 0.0
