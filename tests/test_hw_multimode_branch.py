"""Two-mode D2-A branch with a genuinely multidimensional neutral input space.

The modes are uncoupled copies of the already frozen D2-A physics.  The purpose
of this diagnostic is not to add new plasma physics, but to remove the
one-dimensional neutral-subspace obstruction of a single complex two-field
mode.  Each admissible input is initially pure potential in one Fourier mode,
so the whole two-dimensional input space satisfies B^H Q B = 0 exactly.
"""

import numpy as np

from nonmodal_flux.core.gramians import (
    accumulated_signed_extremal_modes,
    whitened_accumulated_input_transport_operator,
)
from nonmodal_flux.core.problem import TransportProblem
from nonmodal_flux.core.propagators import constant_propagator
from nonmodal_flux.models.hasegawa_wakatani import hasegawa_wakatani_matrices


COMMON = dict(ky=1.0, coupling=1.0, kappa=1.0, damping=0.15)
MODE_1 = dict(kx=0.5, **COMMON)
MODE_2 = dict(kx=1.5, **COMMON)


def _block_diag(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.block(
        [
            [a, np.zeros((a.shape[0], b.shape[1]), dtype=np.complex128)],
            [np.zeros((b.shape[0], a.shape[1]), dtype=np.complex128), b],
        ]
    )


def _two_mode_problem() -> TransportProblem:
    a1, m1, q1, _ = hasegawa_wakatani_matrices(**MODE_1)
    a2, m2, q2, _ = hasegawa_wakatani_matrices(**MODE_2)

    a = _block_diag(a1, a2)
    m = _block_diag(m1, m2)
    q = _block_diag(q1, q2)

    # Column 1: pure potential in mode 1; column 2: pure potential in mode 2.
    b = np.array(
        [
            [1.0, 0.0],
            [0.0, 0.0],
            [0.0, 1.0],
            [0.0, 0.0],
        ],
        dtype=np.complex128,
    )
    rin = b.conj().T @ m @ b
    return TransportProblem(A=a, M=m, Q=q, B=b, Rin=rin)


def _angle(v: np.ndarray, w: np.ndarray) -> float:
    v = np.asarray(v)
    w = np.asarray(w)
    cosine = abs(np.vdot(v, w)) / (np.linalg.norm(v) * np.linalg.norm(w))
    return float(np.arccos(np.clip(cosine, 0.0, 1.0)))


def _whitened_terminal_energy_operator(problem: TransportProblem, horizon: float) -> np.ndarray:
    phi = np.asarray(constant_propagator(problem.A, horizon))
    propagated = phi @ problem.B
    raw = propagated.conj().T @ problem.M @ propagated

    lower = np.linalg.cholesky(problem.Rin)
    inverse_lower = np.linalg.solve(lower, np.eye(problem.input_dim))
    return inverse_lower @ raw @ inverse_lower.conj().T


def _leading_short_time_operators(problem: TransportProblem) -> tuple[np.ndarray, np.ndarray]:
    energy_raw = problem.B.conj().T @ (
        problem.A.conj().T @ problem.M + problem.M @ problem.A
    ) @ problem.B
    transport_raw = problem.B.conj().T @ (
        problem.A.conj().T @ problem.Q + problem.Q @ problem.A
    ) @ problem.B

    lower = np.linalg.cholesky(problem.Rin)
    inverse_lower = np.linalg.solve(lower, np.eye(problem.input_dim))
    return (
        inverse_lower @ energy_raw @ inverse_lower.conj().T,
        inverse_lower @ transport_raw @ inverse_lower.conj().T,
    )


def test_two_mode_input_space_is_two_dimensional_natural_and_transport_neutral() -> None:
    problem = _two_mode_problem()

    assert problem.state_dim == 4
    assert problem.input_dim == 2
    assert problem.is_transport_neutral()
    assert problem.uses_natural_energy_input_metric()

    np.testing.assert_allclose(
        problem.Rin,
        np.diag([1.25, 3.25]),
        rtol=0.0,
        atol=2.0e-14,
    )

    eigenvalues = np.linalg.eigvals(problem.A)
    assert np.max(np.real(eigenvalues)) < 0.0

    energy_rate = problem.A.conj().T @ problem.M + problem.M @ problem.A
    assert np.linalg.eigvalsh(energy_rate)[-1] < 0.0


def test_short_time_energy_and_transport_generators_select_different_neutral_modes() -> None:
    problem = _two_mode_problem()
    e1, h1 = _leading_short_time_operators(problem)

    np.testing.assert_allclose(
        e1,
        np.diag([-1.9, -0.9153846153846155]),
        rtol=0.0,
        atol=4.0e-14,
    )
    np.testing.assert_allclose(
        h1,
        np.diag([0.8, 0.3076923076923077]),
        rtol=0.0,
        atol=4.0e-14,
    )

    _, energy_vectors = np.linalg.eigh(e1)
    _, transport_vectors = np.linalg.eigh(h1)
    angle = _angle(energy_vectors[:, -1], transport_vectors[:, -1])

    # Least initial energy decay is mode 2, strongest flux generation is mode 1.
    np.testing.assert_allclose(angle, np.pi / 2.0, rtol=0.0, atol=2.0e-14)


def test_finite_horizon_neutral_energy_and_transport_optima_remain_distinct() -> None:
    problem = _two_mode_problem()
    horizon = 1.0

    energy_operator = _whitened_terminal_energy_operator(problem, horizon)
    transport_operator = np.asarray(
        whitened_accumulated_input_transport_operator(problem, horizon)
    )

    np.testing.assert_allclose(
        energy_operator,
        np.diag([0.5655597832955765, 0.6542872829481534]),
        rtol=0.0,
        atol=8.0e-9,
    )
    np.testing.assert_allclose(
        transport_operator,
        np.diag([0.1319394768570538, 0.07319416570918078]),
        rtol=0.0,
        atol=8.0e-9,
    )

    energy_values, energy_vectors = np.linalg.eigh(energy_operator)
    q_min, _, q_max, q_mode_max = accumulated_signed_extremal_modes(problem, horizon)
    q_mode_max = np.asarray(q_mode_max)

    np.testing.assert_allclose(
        energy_values[-1],
        np.real(energy_operator[1, 1]),
        rtol=0.0,
        atol=2.0e-14,
    )
    np.testing.assert_allclose(float(q_min), 0.07319416570918078, rtol=0.0, atol=8.0e-9)
    np.testing.assert_allclose(float(q_max), 0.1319394768570538, rtol=0.0, atol=8.0e-9)

    separation_angle = _angle(energy_vectors[:, -1], q_mode_max)
    np.testing.assert_allclose(
        separation_angle,
        np.pi / 2.0,
        rtol=0.0,
        atol=2.0e-7,
    )

    # Both admissible directions lose energy, but they rank oppositely for the two objectives.
    assert np.real(energy_operator[1, 1]) > np.real(energy_operator[0, 0])
    assert np.real(transport_operator[0, 0]) > np.real(transport_operator[1, 1]) > 0.0
