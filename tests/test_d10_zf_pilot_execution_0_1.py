"""Preregistered execution checks for the frozen D10-ZF Pilot 0.1.

This file does not tune or alter the pilot.  It evaluates exactly the frozen
parameter point U(x)=cos(x), Lx=2*pi, ky=C=kappa=1, modes=(-1,0,1), no
additional damping, B=I_6 and Rin=M at the preregistered horizons.
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid

from nonmodal_flux.core.gramians import (
    accumulated_signed_extremal_inputs,
    whitened_accumulated_input_transport_operator,
)
from nonmodal_flux.core.propagators import constant_propagator
from nonmodal_flux.models.hasegawa_wakatani_zonal_flow import (
    make_hasegawa_wakatani_zonal_flow_problem,
)


HORIZONS = np.array([0.25, 0.5, 1.0, 2.0, 4.0, 8.0])
EXPECTED_SPECTRUM = np.array(
    [
        0.08036351123176821 + 0.029519858630783394j,
        0.06089446327260969 - 0.3083015254264103j,
        0.03899252593783323 - 0.8187469847342025j,
        -1.5608944632726097 + 0.3083015254264102j,
        -1.7577783738398133 - 0.01194340945163995j,
        -1.8615776633291782 + 0.8011705355553988j,
    ]
)
EXPECTED_ENERGY_GAIN = np.array(
    [1.1325420073438985, 1.2789124970124384, 1.6067783725603826,
     2.3718727839414980, 3.7436139229532497, 4.0469887014928885]
)
EXPECTED_QMIN = np.array(
    [-0.08774600457764799, -0.12762485828431774, -0.14760261900142663,
     -0.13541795513576788, -0.11042785143879685, -0.07905128613483861]
)
EXPECTED_QMAX = np.array(
    [0.11087658617399050, 0.20046415688950114, 0.35679473538072390,
     0.7301045858959734, 1.8581395128453324, 3.8108919805591626]
)
EXPECTED_THETA_DEG = np.array(
    [46.223981130946086, 41.547300160717576, 33.83287337911526,
     26.052466854806166, 23.119706360223983, 58.48321641408995]
)
EXPECTED_J_ENERGY = np.array(
    [0.049932149911247406, 0.10646726324869665, 0.24218953124296894,
     0.6142514830549245, 1.6487397590985378, 2.3699284128693545]
)
EXPECTED_DELTA_GAMMA = EXPECTED_QMAX - EXPECTED_J_ENERGY


def _problem():
    return make_hasegawa_wakatani_zonal_flow_problem(
        modes=(-1, 0, 1),
        ky=1.0,
        coupling=1.0,
        kappa=1.0,
        profile_coefficients={-1: 0.5, 1: 0.5},
        fundamental_wavenumber=1.0,
    )


def _whitened_terminal_energy(problem, horizon: float) -> np.ndarray:
    phi = np.asarray(constant_propagator(problem.A, horizon))
    raw = phi.conj().T @ problem.M @ phi
    lower = np.linalg.cholesky(problem.Rin)
    left = np.linalg.solve(lower, raw)
    return np.linalg.solve(lower, left.conj().T).conj().T


def _physical_input(problem, whitened_mode: np.ndarray) -> np.ndarray:
    lower = np.linalg.cholesky(problem.Rin)
    u = np.linalg.solve(lower.conj().T, whitened_mode)
    cost = np.real(u.conj().T @ problem.Rin @ u)
    return u / np.sqrt(cost)


def _angle_deg(v: np.ndarray, w: np.ndarray) -> float:
    cosine = abs(np.vdot(v, w)) / (np.linalg.norm(v) * np.linalg.norm(w))
    return float(np.rad2deg(np.arccos(np.clip(cosine, 0.0, 1.0))))


def test_frozen_pilot_spectrum_is_unstable_without_retuning() -> None:
    problem = _problem()
    eigenvalues = np.linalg.eigvals(problem.A)
    eigenvalues = eigenvalues[np.argsort(eigenvalues.real)[::-1]]

    np.testing.assert_allclose(eigenvalues, EXPECTED_SPECTRUM, rtol=0.0, atol=2.0e-12)
    np.testing.assert_allclose(eigenvalues[0].real, 0.08036351123176821, rtol=0.0, atol=2e-12)
    assert eigenvalues[0].real > 0.0


def test_preregistered_horizon_metrics_and_optimizer_separation() -> None:
    problem = _problem()

    energy_gains = []
    qmins = []
    qmaxs = []
    angles = []
    j_energy = []
    deltas = []

    for horizon in HORIZONS:
        energy_operator = _whitened_terminal_energy(problem, float(horizon))
        energy_values, energy_vectors = np.linalg.eigh(energy_operator)
        v_energy = energy_vectors[:, -1]
        u_energy = _physical_input(problem, v_energy)

        k_gamma = np.asarray(
            whitened_accumulated_input_transport_operator(problem, float(horizon))
        )
        q_values, q_vectors = np.linalg.eigh(k_gamma)
        v_gamma = q_vectors[:, -1]

        p_gamma_raw = np.linalg.cholesky(problem.Rin) @ k_gamma @ np.linalg.cholesky(problem.Rin).conj().T
        j_e = float(np.real(u_energy.conj().T @ p_gamma_raw @ u_energy))

        energy_gains.append(float(energy_values[-1]))
        qmins.append(float(q_values[0]))
        qmaxs.append(float(q_values[-1]))
        angles.append(_angle_deg(v_energy, v_gamma))
        j_energy.append(j_e)
        deltas.append(float(q_values[-1] - j_e))

    np.testing.assert_allclose(energy_gains, EXPECTED_ENERGY_GAIN, rtol=0.0, atol=2.0e-9)
    np.testing.assert_allclose(qmins, EXPECTED_QMIN, rtol=0.0, atol=3.0e-9)
    np.testing.assert_allclose(qmaxs, EXPECTED_QMAX, rtol=0.0, atol=3.0e-9)
    np.testing.assert_allclose(angles, EXPECTED_THETA_DEG, rtol=0.0, atol=2.0e-7)
    np.testing.assert_allclose(j_energy, EXPECTED_J_ENERGY, rtol=0.0, atol=4.0e-9)
    np.testing.assert_allclose(deltas, EXPECTED_DELTA_GAMMA, rtol=0.0, atol=4.0e-9)

    assert np.all(np.asarray(deltas) > 0.0)
    assert np.all(np.asarray(angles) > 20.0)
    assert np.all(np.asarray(qmins) < 0.0)
    assert np.all(np.asarray(qmaxs) > 0.0)


def test_optimizer_normalization_rayleigh_and_direct_trajectory_integral_checks() -> None:
    problem = _problem()

    for horizon, expected_qmax in zip(HORIZONS, EXPECTED_QMAX, strict=True):
        energy_operator = _whitened_terminal_energy(problem, float(horizon))
        energy_values, energy_vectors = np.linalg.eigh(energy_operator)
        v_energy = energy_vectors[:, -1]
        u_energy = _physical_input(problem, v_energy)

        qmin, u_min, qmax, u_gamma = accumulated_signed_extremal_inputs(
            problem, float(horizon)
        )
        u_min = np.asarray(u_min)
        u_gamma = np.asarray(u_gamma)

        np.testing.assert_allclose(
            np.real(u_energy.conj().T @ problem.Rin @ u_energy),
            1.0,
            rtol=0.0,
            atol=3.0e-12,
        )
        np.testing.assert_allclose(
            np.real(u_gamma.conj().T @ problem.Rin @ u_gamma),
            1.0,
            rtol=0.0,
            atol=3.0e-12,
        )
        np.testing.assert_allclose(
            np.real(u_min.conj().T @ problem.Rin @ u_min),
            1.0,
            rtol=0.0,
            atol=3.0e-12,
        )

        phi = np.asarray(constant_propagator(problem.A, float(horizon)))
        direct_energy = float(np.real((phi @ u_energy).conj().T @ problem.M @ (phi @ u_energy)))
        np.testing.assert_allclose(direct_energy, energy_values[-1], rtol=0.0, atol=2.0e-9)

        # Direct trajectory integration of Gamma(t) must reproduce the cumulative optimum.
        times = np.linspace(0.0, float(horizon), 4001)
        states = np.array(
            [np.asarray(constant_propagator(problem.A, float(t))) @ u_gamma for t in times]
        )
        gamma = np.real(np.einsum("bi,ij,bj->b", states.conj(), problem.Q, states))
        j_direct = cumulative_trapezoid(gamma, times, initial=0.0)[-1]
        np.testing.assert_allclose(j_direct, expected_qmax, rtol=0.0, atol=8.0e-8)
        np.testing.assert_allclose(float(qmax), expected_qmax, rtol=0.0, atol=4.0e-9)
        assert float(qmin) < 0.0 < float(qmax)

        k_gamma = np.asarray(
            whitened_accumulated_input_transport_operator(problem, float(horizon))
        )
        hermiticity_defect = np.linalg.norm(k_gamma - k_gamma.conj().T, ord="fro")
        relative_defect = hermiticity_defect / np.linalg.norm(k_gamma, ord="fro")
        assert relative_defect < 2.0e-9
