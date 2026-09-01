"""Tests for reachable-subspace sharpening of the T3 leakage constant."""

import numpy as np

from nonmodal_flux.core.gramians import (
    accumulated_signed_extrema,
    accumulated_transport_operator,
)
from nonmodal_flux.core.problem import TransportProblem
from nonmodal_flux.core.propagators import constant_propagator


def _reachable_witness() -> tuple[
    TransportProblem,
    np.ndarray,
    np.ndarray,
    float,
    float,
]:
    """Return a contractive three-state witness with a proper reachable subspace."""

    a = np.array(
        [
            [-1.0, 0.0, 0.0],
            [0.8, -1.4, 0.0],
            [0.0, 0.0, -2.0],
        ]
    )
    m = np.eye(3)
    b = np.array([[1.0], [0.0], [0.0]])
    g_target = 1.1
    g_competing = 1.0
    q_competing = np.diag([-0.2, 0.1, -3.0])
    dissipation = np.diag([3.0, 3.2, 4.5])

    q_target = (
        a.conj().T @ m
        + m @ a
        + dissipation
        - g_competing * q_competing
    ) / g_target

    problem = TransportProblem(
        A=a,
        M=m,
        Q=q_target,
        B=b,
        Rin=b.conj().T @ m @ b,
    )
    return problem, q_competing, dissipation, g_target, g_competing


def _with_observable(problem: TransportProblem, observable: np.ndarray) -> TransportProblem:
    return TransportProblem(
        A=problem.A,
        M=problem.M,
        Q=observable,
        B=problem.B,
        Rin=problem.Rin,
    )


def _reachable_basis(problem: TransportProblem) -> np.ndarray:
    """Return an orthonormal basis for span{B, AB, ..., A^(n-1)B}."""

    blocks = [problem.B]
    current = problem.B
    for _ in range(1, problem.state_dim):
        current = problem.A @ current
        blocks.append(current)
    controllability = np.hstack(blocks)
    basis, singular_values, _ = np.linalg.svd(controllability, full_matrices=False)
    rank = int(np.sum(singular_values > 1.0e-12))
    return basis[:, :rank]


def _leakage_constant(
    metric: np.ndarray,
    weighted_observable: np.ndarray,
    basis: np.ndarray,
) -> float:
    """Return max(0, -lambda_min) on a subspace for the metric Rayleigh quotient."""

    restricted_q = basis.conj().T @ weighted_observable @ basis
    restricted_m = basis.conj().T @ metric @ basis
    lower = np.linalg.cholesky(restricted_m)
    inverse_lower = np.linalg.solve(lower, np.eye(lower.shape[0]))
    whitened = inverse_lower @ restricted_q @ inverse_lower.conj().T
    return max(0.0, -float(np.min(np.linalg.eigvalsh(whitened))))


def test_reachable_subspace_excludes_the_globally_worst_leakage_direction() -> None:
    problem, q_competing, _, _, g_competing = _reachable_witness()
    reachable = _reachable_basis(problem)

    assert reachable.shape == (3, 2)
    np.testing.assert_allclose(reachable[2, :], 0.0, rtol=0.0, atol=2.0e-14)

    global_basis = np.eye(problem.state_dim)
    global_leakage = _leakage_constant(
        problem.M,
        g_competing * q_competing,
        global_basis,
    )
    reachable_leakage = _leakage_constant(
        problem.M,
        g_competing * q_competing,
        reachable,
    )

    np.testing.assert_allclose(global_leakage, 3.0, rtol=0.0, atol=2.0e-14)
    np.testing.assert_allclose(reachable_leakage, 0.2, rtol=0.0, atol=2.0e-14)
    assert reachable_leakage < 0.1 * global_leakage


def test_reachable_leakage_lower_bound_holds_along_admissible_dynamics() -> None:
    problem, q_competing, _, _, g_competing = _reachable_witness()
    reachable = _reachable_basis(problem)
    leakage = _leakage_constant(problem.M, g_competing * q_competing, reachable)

    for horizon in (0.0, 0.35, 1.0):
        phi = np.asarray(constant_propagator(problem.A, horizon))
        state = phi @ problem.B
        residual = float(
            np.real(
                (state.conj().T @ (g_competing * q_competing + leakage * problem.M) @ state)[
                    0, 0
                ]
            )
        )
        assert residual >= -2.0e-13


def test_reachable_leakage_gives_valid_and_strictly_tighter_projected_t3_bound() -> None:
    problem, q_competing, dissipation, g_target, g_competing = _reachable_witness()
    reachable = _reachable_basis(problem)
    reachable_leakage = _leakage_constant(
        problem.M,
        g_competing * q_competing,
        reachable,
    )
    global_leakage = _leakage_constant(
        problem.M,
        g_competing * q_competing,
        np.eye(problem.state_dim),
    )

    competing_problem = _with_observable(problem, q_competing)
    dissipation_problem = _with_observable(problem, dissipation)
    metric_problem = _with_observable(problem, problem.M)

    for horizon in (0.1, 0.5, 1.2):
        p_target = np.asarray(accumulated_transport_operator(problem, horizon))
        p_competing = np.asarray(
            accumulated_transport_operator(competing_problem, horizon)
        )
        p_d = np.asarray(accumulated_transport_operator(dissipation_problem, horizon))
        p_m = np.asarray(accumulated_transport_operator(metric_problem, horizon))
        phi = np.asarray(constant_propagator(problem.A, horizon))
        delta_m = phi.conj().T @ problem.M @ phi - problem.M

        np.testing.assert_allclose(
            g_target * p_target + g_competing * p_competing,
            delta_m + p_d,
            rtol=2.0e-11,
            atol=3.0e-12,
        )

        projected_reachable_residual = problem.B.conj().T @ (
            delta_m + p_d + reachable_leakage * p_m - g_target * p_target
        ) @ problem.B
        assert float(np.real(projected_reachable_residual[0, 0])) >= -4.0e-12

        reachable_upper = float(
            np.real(
                (problem.B.conj().T @ (delta_m + p_d + reachable_leakage * p_m) @ problem.B)[
                    0, 0
                ]
            )
        )
        global_upper = float(
            np.real(
                (problem.B.conj().T @ (delta_m + p_d + global_leakage * p_m) @ problem.B)[
                    0, 0
                ]
            )
        )
        assert reachable_upper < global_upper


def test_reachable_leakage_sharpens_the_contractive_gain_bound() -> None:
    problem, q_competing, dissipation, g_target, g_competing = _reachable_witness()
    reachable = _reachable_basis(problem)
    reachable_leakage = _leakage_constant(
        problem.M,
        g_competing * q_competing,
        reachable,
    )
    global_leakage = _leakage_constant(
        problem.M,
        g_competing * q_competing,
        np.eye(problem.state_dim),
    )
    dissipation_problem = _with_observable(problem, dissipation)

    assert np.max(np.linalg.eigvalsh(problem.A.conj().T @ problem.M + problem.M @ problem.A)) < 0.0
    assert problem.uses_natural_energy_input_metric()

    for horizon in (0.1, 0.5, 1.2):
        _, target_max = accumulated_signed_extrema(problem, horizon)
        _, dissipation_max = accumulated_signed_extrema(dissipation_problem, horizon)

        reachable_bound = (
            float(dissipation_max) + reachable_leakage * horizon
        ) / g_target
        global_bound = (float(dissipation_max) + global_leakage * horizon) / g_target

        assert float(target_max) <= reachable_bound + 4.0e-12
        assert reachable_bound < global_bound
