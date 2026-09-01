"""Single-mode D2-A pilot branch: transport generation and full-state separation.

The transport-neutral subspace for one complex two-field HW mode is necessarily
one-dimensional.  This file therefore tests two complementary facts:

1. the neutral pure-potential input dynamically generates outward particle
   transport even though physical energy decreases monotonically; and
2. on the full two-dimensional state space, energy-optimal and accumulated-
   transport-optimal initial conditions are distinct at finite horizon.

The second statement is deliberately *not* claimed inside the one-dimensional
transport-neutral subspace.
"""

import numpy as np

from nonmodal_flux.core.gramians import (
    accumulated_signed_extrema,
    accumulated_signed_extremal_modes,
)
from nonmodal_flux.core.propagators import constant_propagator
from nonmodal_flux.models.hasegawa_wakatani import make_hasegawa_wakatani_problem


PARAMETERS = dict(kx=0.5, ky=1.0, coupling=1.0, kappa=1.0, damping=0.15)


def _angle(v: np.ndarray, w: np.ndarray) -> float:
    v = np.asarray(v)
    w = np.asarray(w)
    cosine = abs(np.vdot(v, w)) / (np.linalg.norm(v) * np.linalg.norm(w))
    return float(np.arccos(np.clip(cosine, 0.0, 1.0)))


def _whitened_terminal_energy_operator(problem, horizon: float) -> np.ndarray:
    phi = np.asarray(constant_propagator(problem.A, horizon))
    propagated = phi @ problem.B
    raw = propagated.conj().T @ problem.M @ propagated

    lower = np.linalg.cholesky(problem.Rin)
    inverse_lower = np.linalg.solve(lower, np.eye(problem.input_dim))
    return inverse_lower @ raw @ inverse_lower.conj().T


def _whitened_terminal_flux_operator(problem, horizon: float) -> np.ndarray:
    phi = np.asarray(constant_propagator(problem.A, horizon))
    propagated = phi @ problem.B
    raw = propagated.conj().T @ problem.Q @ propagated

    lower = np.linalg.cholesky(problem.Rin)
    inverse_lower = np.linalg.solve(lower, np.eye(problem.input_dim))
    return inverse_lower @ raw @ inverse_lower.conj().T


def test_neutral_potential_input_generates_transport_during_monotone_energy_decay() -> None:
    potential_input = np.array([[1.0], [0.0]], dtype=np.complex128)
    problem = make_hasegawa_wakatani_problem(**PARAMETERS, B=potential_input)

    assert problem.is_transport_neutral()
    assert problem.uses_natural_energy_input_metric()

    energy_rate = problem.A.conj().T @ problem.M + problem.M @ problem.A
    assert np.linalg.eigvalsh(energy_rate)[-1] < 0.0

    first_transport_derivative = (
        problem.B.conj().T
        @ (problem.A.conj().T @ problem.Q + problem.Q @ problem.A)
        @ problem.B
    )
    normalized_h1 = np.real(first_transport_derivative[0, 0] / problem.Rin[0, 0])
    np.testing.assert_allclose(normalized_h1, 0.8, rtol=0.0, atol=3.0e-14)

    horizon = 1.0
    q_min, q_max = accumulated_signed_extrema(problem, horizon)
    np.testing.assert_allclose(float(q_min), 0.1319394768570538, rtol=0.0, atol=4.0e-12)
    np.testing.assert_allclose(float(q_max), 0.1319394768570538, rtol=0.0, atol=4.0e-12)
    assert float(q_max) > 0.0

    terminal_flux = _whitened_terminal_flux_operator(problem, horizon)[0, 0].real
    np.testing.assert_allclose(terminal_flux, 0.1446027265939886, rtol=0.0, atol=4.0e-12)
    assert terminal_flux > 0.0

    energy_ratio = _whitened_terminal_energy_operator(problem, horizon)[0, 0].real
    np.testing.assert_allclose(energy_ratio, 0.5655597832955765, rtol=0.0, atol=4.0e-12)
    assert energy_ratio < 1.0


def test_full_single_mode_energy_and_transport_optima_are_distinct_at_finite_horizon() -> None:
    problem = make_hasegawa_wakatani_problem(**PARAMETERS)
    horizon = 1.0

    energy_operator = _whitened_terminal_energy_operator(problem, horizon)
    energy_values, energy_vectors = np.linalg.eigh(energy_operator)

    q_min, q_mode_min, q_max, q_mode_max = accumulated_signed_extremal_modes(
        problem, horizon
    )
    q_mode_max = np.asarray(q_mode_max)

    np.testing.assert_allclose(
        energy_values,
        np.array([0.01656892, 0.90504223]),
        rtol=0.0,
        atol=8.0e-9,
    )
    np.testing.assert_allclose(float(q_min), -0.12889160, rtol=0.0, atol=8.0e-9)
    np.testing.assert_allclose(float(q_max), 0.27250824, rtol=0.0, atol=8.0e-9)

    separation_angle = _angle(energy_vectors[:, -1], q_mode_max)
    np.testing.assert_allclose(
        separation_angle,
        0.4828203778149154,
        rtol=0.0,
        atol=8.0e-9,
    )
    assert separation_angle > np.deg2rad(25.0)

    # The negative branch is also physically present in the unrestricted state space.
    assert float(q_min) < 0.0 < float(q_max)
    assert np.isclose(np.linalg.norm(np.asarray(q_mode_min)), 1.0, atol=2.0e-12)
