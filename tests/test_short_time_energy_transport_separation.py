"""Tests for T4 short-time separation of energy- and transport-optimal inputs."""

import numpy as np

from nonmodal_flux.core.gramians import accumulated_signed_extremal_modes
from nonmodal_flux.core.problem import TransportProblem
from nonmodal_flux.core.propagators import constant_propagator


def _separation_witness() -> TransportProblem:
    """Return a stable transport-neutral witness with distinct E1 and H1 optima."""

    energy_block = np.array([[-1.0, 0.4], [0.4, -1.4]])
    transport_generation = np.diag([1.8, -1.0])
    latent_block = np.array([[-2.0, 0.2], [0.0, -2.5]])
    coupling = 0.5 * transport_generation

    A = np.block(
        [
            [energy_block, np.zeros((2, 2))],
            [coupling, latent_block],
        ]
    )
    Q = np.block(
        [
            [np.zeros((2, 2)), np.eye(2)],
            [np.eye(2), np.zeros((2, 2))],
        ]
    )
    B = np.vstack([np.eye(2), np.zeros((2, 2))])

    return TransportProblem(
        A=A,
        M=np.eye(4),
        Q=Q,
        B=B,
        Rin=np.eye(2),
    )


def _angle(v: np.ndarray, w: np.ndarray) -> float:
    v = np.asarray(v)
    w = np.asarray(w)
    cosine = abs(np.vdot(v, w)) / (np.linalg.norm(v) * np.linalg.norm(w))
    return float(np.arccos(np.clip(cosine, 0.0, 1.0)))


def _leading_operators(problem: TransportProblem) -> tuple[np.ndarray, np.ndarray]:
    e1_raw = problem.B.conj().T @ (
        problem.A.conj().T @ problem.M + problem.M @ problem.A
    ) @ problem.B
    h1_raw = problem.B.conj().T @ (
        problem.A.conj().T @ problem.Q + problem.Q @ problem.A
    ) @ problem.B

    lower = np.linalg.cholesky(problem.Rin)
    inverse_lower = np.linalg.solve(lower, np.eye(problem.input_dim))
    e1 = inverse_lower @ e1_raw @ inverse_lower.conj().T
    h1 = inverse_lower @ h1_raw @ inverse_lower.conj().T
    return e1, h1


def _terminal_energy_top_mode(problem: TransportProblem, horizon: float) -> np.ndarray:
    phi = np.asarray(constant_propagator(problem.A, horizon))
    propagated_inputs = phi @ problem.B
    raw = propagated_inputs.conj().T @ problem.M @ propagated_inputs

    lower = np.linalg.cholesky(problem.Rin)
    inverse_lower = np.linalg.solve(lower, np.eye(problem.input_dim))
    whitened = inverse_lower @ raw @ inverse_lower.conj().T
    _, eigenvectors = np.linalg.eigh(whitened)
    return eigenvectors[:, -1]


def test_witness_has_natural_metric_transport_neutrality_and_distinct_leading_optima() -> None:
    problem = _separation_witness()

    assert problem.uses_natural_energy_input_metric()
    assert problem.is_transport_neutral()
    np.testing.assert_allclose(
        np.sort(np.real(np.linalg.eigvals(problem.A))),
        np.array([-2.5, -2.0, -1.647213595499958, -0.752786404500042]),
        rtol=0.0,
        atol=2.0e-13,
    )

    e1, h1 = _leading_operators(problem)
    e_values, e_vectors = np.linalg.eigh(e1)
    h_values, h_vectors = np.linalg.eigh(h1)

    assert e_values[-1] > e_values[-2]
    assert h_values[-1] > h_values[-2]
    assert h_values[0] < 0.0 < h_values[-1]

    limiting_angle = _angle(e_vectors[:, -1], h_vectors[:, -1])
    assert 0.4 < limiting_angle < 0.7


def test_short_time_energy_and_accumulated_transport_modes_converge_to_distinct_limits() -> None:
    problem = _separation_witness()
    e1, h1 = _leading_operators(problem)
    _, e_vectors = np.linalg.eigh(e1)
    _, h_vectors = np.linalg.eigh(h1)
    e_limit = e_vectors[:, -1]
    q_limit = h_vectors[:, -1]
    limiting_angle = _angle(e_limit, q_limit)

    horizon = 1.0e-3
    energy_mode = _terminal_energy_top_mode(problem, horizon)
    _, _, _, transport_mode = accumulated_signed_extremal_modes(problem, horizon)
    transport_mode = np.asarray(transport_mode)

    assert _angle(energy_mode, e_limit) < 2.0e-4
    assert _angle(transport_mode, q_limit) < 7.0e-5

    finite_angle = _angle(energy_mode, transport_mode)
    np.testing.assert_allclose(
        finite_angle,
        limiting_angle,
        rtol=0.0,
        atol=3.0e-4,
    )
    assert finite_angle > 0.5


def test_energy_transport_separation_angle_has_linear_short_time_correction() -> None:
    problem = _separation_witness()
    e1, h1 = _leading_operators(problem)
    _, e_vectors = np.linalg.eigh(e1)
    _, h_vectors = np.linalg.eigh(h1)
    limiting_angle = _angle(e_vectors[:, -1], h_vectors[:, -1])

    horizon = 2.0e-2
    half_horizon = horizon / 2.0

    energy_mode = _terminal_energy_top_mode(problem, horizon)
    _, _, _, transport_mode = accumulated_signed_extremal_modes(problem, horizon)
    angle = _angle(energy_mode, np.asarray(transport_mode))

    energy_mode_half = _terminal_energy_top_mode(problem, half_horizon)
    _, _, _, transport_mode_half = accumulated_signed_extremal_modes(
        problem,
        half_horizon,
    )
    angle_half = _angle(energy_mode_half, np.asarray(transport_mode_half))

    error = abs(angle - limiting_angle)
    half_error = abs(angle_half - limiting_angle)
    assert error > 0.0
    np.testing.assert_allclose(
        half_error / error,
        0.5,
        rtol=0.0,
        atol=2.0e-2,
    )
