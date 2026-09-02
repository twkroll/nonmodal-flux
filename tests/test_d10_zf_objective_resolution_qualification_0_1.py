"""Resolution qualification for frozen D10-ZF Pilot 0.1 objectives.

Only the centered Galerkin truncation K is varied.  The physical point remains
U=cos(x), Lx=2*pi, ky=C=kappa=1, N=0, no additional damping, B=I and Q=Q_Gamma.
"""

from functools import lru_cache

import numpy as np
from scipy import linalg as la

from nonmodal_flux.models.hasegawa_wakatani_zonal_flow import (
    hasegawa_wakatani_zonal_flow_matrices,
)


KS = (1, 2, 4, 8, 16, 32, 64)
TS = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0)


def _phase_overlap(a: np.ndarray, b: np.ndarray) -> float:
    return float(abs(np.vdot(a, b)) / (la.norm(a) * la.norm(b)))


@lru_cache(maxsize=None)
def _basis_data(K: int):
    modes = np.arange(-K, K + 1)
    A, M, Q, _, _ = hasegawa_wakatani_zonal_flow_matrices(
        modes=modes,
        ky=1.0,
        coupling=1.0,
        kappa=1.0,
        profile_coefficients={-1: 0.5, 1: 0.5},
        fundamental_wavenumber=1.0,
    )
    mdiag = np.real(np.diag(M))
    sqrt_m = np.sqrt(mdiag)
    A_w = (sqrt_m[:, None] * A) / sqrt_m[None, :]
    Q_w = (Q / sqrt_m[:, None]) / sqrt_m[None, :]
    eigvals, V = la.eig(A_w)
    W = la.inv(V)
    Cq = V.conj().T @ Q_w @ V
    return modes, eigvals, V, W, Cq


@lru_cache(maxsize=None)
def _metrics(K: int, T: float):
    modes, eigvals, V, W, Cq = _basis_data(K)

    propagator = (V * np.exp(eigvals * T)[None, :]) @ W
    K_E = propagator.conj().T @ propagator
    K_E = 0.5 * (K_E + K_E.conj().T)
    e_values, e_vectors = la.eigh(K_E)
    v_E = e_vectors[:, -1]

    sums = eigvals.conj()[:, None] + eigvals[None, :]
    integ = np.empty_like(sums)
    mask = np.abs(sums) < 1.0e-12
    integ[mask] = T
    integ[~mask] = np.expm1(sums[~mask] * T) / sums[~mask]
    K_G = W.conj().T @ (Cq * integ) @ W
    K_G = 0.5 * (K_G + K_G.conj().T)
    q_values, q_vectors = la.eigh(K_G)
    v_G = q_vectors[:, -1]

    j_energy = float(np.real(v_E.conj().T @ K_G @ v_E))
    g_plus = float(q_values[-1])
    delta = (g_plus - j_energy) / g_plus

    n = len(modes)
    mode_weight_E = np.abs(v_E[:n]) ** 2 + np.abs(v_E[n:]) ** 2
    mode_weight_G = np.abs(v_G[:n]) ** 2 + np.abs(v_G[n:]) ** 2
    phi_fraction_E = float(np.sum(np.abs(v_E[:n]) ** 2))
    phi_fraction_G = float(np.sum(np.abs(v_G[:n]) ** 2))

    low = np.where(np.abs(modes) <= 1)[0]
    low_idx = np.concatenate([low, n + low])
    low_E = v_E[low_idx]
    low_G = v_G[low_idx]

    return {
        "GE": float(e_values[-1]),
        "qmin": float(q_values[0]),
        "qmax": g_plus,
        "delta": float(delta),
        "vE": v_E,
        "vG": v_G,
        "mode_weight_E": mode_weight_E,
        "mode_weight_G": mode_weight_G,
        "phi_fraction_E": phi_fraction_E,
        "phi_fraction_G": phi_fraction_G,
        "low_E": low_E,
        "low_G": low_G,
    }


def _embedded_mode_weights(K: int, T: float, family: str) -> np.ndarray:
    result = np.zeros(129)
    data = _metrics(K, T)
    weights = data[f"mode_weight_{family}"]
    for m, value in zip(np.arange(-K, K + 1), weights, strict=True):
        result[m + 64] = value
    return result


def test_all_preregistered_resolution_points_remain_signed_and_separated() -> None:
    for K in KS:
        for T in TS:
            data = _metrics(K, T)
            assert data["qmin"] < 0.0 < data["qmax"]
            assert data["delta"] > 0.0


def test_k1_reproduces_pilot_execution_values() -> None:
    expected_GE = [1.13254200734, 1.27891249701, 1.60677837256, 2.37187278394, 3.74361392295, 4.04698870149]
    expected_qp = [0.110876586174, 0.200464156890, 0.356794735381, 0.730104585896, 1.85813951285, 3.81089198050]
    expected_qm = [-0.087746004578, -0.127624858284, -0.147602619001, -0.135417955136, -0.110427851439, -0.079051286128]
    for T, ge, qp, qm in zip(TS, expected_GE, expected_qp, expected_qm, strict=True):
        data = _metrics(1, T)
        np.testing.assert_allclose(data["GE"], ge, rtol=0.0, atol=2.0e-9)
        np.testing.assert_allclose(data["qmax"], qp, rtol=0.0, atol=3.0e-9)
        np.testing.assert_allclose(data["qmin"], qm, rtol=0.0, atol=3.0e-9)


def test_objective_values_and_dimensionless_gap_converge_by_k16() -> None:
    for T in TS:
        k16 = _metrics(16, T)
        k64 = _metrics(64, T)
        np.testing.assert_allclose(k16["GE"], k64["GE"], rtol=1.0e-8, atol=1.0e-10)
        np.testing.assert_allclose(k16["qmax"], k64["qmax"], rtol=1.0e-9, atol=1.0e-10)
        np.testing.assert_allclose(k16["qmin"], k64["qmin"], rtol=1.0e-10, atol=1.0e-11)
        np.testing.assert_allclose(k16["delta"], k64["delta"], rtol=0.0, atol=2.0e-8)


def test_low_mode_optimizer_projections_converge_without_cross_dimension_angles() -> None:
    for T in TS:
        k8 = _metrics(8, T)
        k64 = _metrics(64, T)
        assert _phase_overlap(k8["low_E"], k64["low_E"]) > 0.99998
        assert _phase_overlap(k8["low_G"], k64["low_G"]) > 0.999999


def test_fourier_weight_distributions_and_phi_eta_structure_converge() -> None:
    for T in TS:
        k16 = _metrics(16, T)
        k64 = _metrics(64, T)
        tv_E = 0.5 * np.sum(abs(_embedded_mode_weights(16, T, "E") - _embedded_mode_weights(64, T, "E")))
        tv_G = 0.5 * np.sum(abs(_embedded_mode_weights(16, T, "G") - _embedded_mode_weights(64, T, "G")))
        assert tv_E < 1.0e-7
        assert tv_G < 1.0e-8
        np.testing.assert_allclose(k16["phi_fraction_E"], k64["phi_fraction_E"], atol=1.0e-7, rtol=0.0)
        np.testing.assert_allclose(k16["phi_fraction_G"], k64["phi_fraction_G"], atol=1.0e-8, rtol=0.0)
