"""Execution checks for frozen D10-ZF Pilot 0.2.

The physical point and the blind-selected uniform damping are fixed:
U=cos(x), Lx=2*pi, ky=C=kappa=1, N=0, nu_perp=0.020,
B=I and the physical M,Q_Gamma inherited from D10-ZF.

Only the preregistered K=(32,64,96) and T=(0.25,0.5,1,2,4,8) are used.
"""

from functools import lru_cache

import numpy as np
from scipy import linalg as la
from scipy.integrate import cumulative_trapezoid
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import expm_multiply

from nonmodal_flux.models.hasegawa_wakatani_zonal_flow import (
    hasegawa_wakatani_zonal_flow_matrices,
)


KS = (32, 64, 96)
TS = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0)
NU = 0.020

EXPECTED_ALPHA = {
    32: -0.0075785979285167265,
    64: -0.013381761020988233,
    96: -0.015492437971069386,
}
EXPECTED_GE = np.array([
    1.17474002048919,
    1.37760790779905,
    1.87827579465046,
    3.37165924771795,
    9.41174568112634,
    39.7632346459493,
])
EXPECTED_QPLUS = np.array([
    0.110347370245754,
    0.198692327664067,
    0.353516930280735,
    0.769879426840236,
    2.76273797475996,
    16.0639684298744,
])
EXPECTED_QMINUS = np.array([
    -0.0873636748022255,
    -0.126689993119504,
    -0.146221619690173,
    -0.133649662544427,
    -0.119061194326872,
    -0.115154144295559,
])
EXPECTED_DELTA = np.array([
    0.708518585895642,
    0.643691588934530,
    0.504337166853530,
    0.292030299625714,
    0.149468002218145,
    0.143128492131179,
])
EXPECTED_THETA_DEG = np.array([
    65.5296460893304,
    61.6673410699927,
    53.3959703433885,
    40.9757522046032,
    28.6897452413558,
    28.0301792476517,
])
EXPECTED_PHI_E = np.array([
    0.794525160493176,
    0.807309896478239,
    0.827660249608673,
    0.859830331744411,
    0.913537702985467,
    0.969082455996279,
])
EXPECTED_PHI_G = np.array([
    0.556997776309287,
    0.603068656475160,
    0.669590480536890,
    0.754212432724962,
    0.853136127763974,
    0.947422937505700,
])
EXPECTED_PHASE_E = np.array([
    0.422376366508462,
    0.379600546239079,
    0.305804642354412,
    0.220593649460306,
    0.136614730697460,
    0.0541860976158421,
])
EXPECTED_PHASE_G = np.array([
    1.55052563354987,
    1.49122692461888,
    1.27933228560907,
    0.809557937230313,
    0.325110602646094,
    0.0925993449977082,
])


@lru_cache(maxsize=None)
def _basis_data(K: int):
    modes = np.arange(-K, K + 1)
    A0, M, Q, _, _ = hasegawa_wakatani_zonal_flow_matrices(
        modes=modes,
        ky=1.0,
        coupling=1.0,
        kappa=1.0,
        profile_coefficients={-1: 0.5, 1: 0.5},
        fundamental_wavenumber=1.0,
    )
    A = A0 - NU * np.eye(A0.shape[0], dtype=np.complex128)
    mdiag = np.real(np.diag(M))
    sqrt_m = np.sqrt(mdiag)
    A_w = (sqrt_m[:, None] * A) / sqrt_m[None, :]
    Q_w = (Q / sqrt_m[:, None]) / sqrt_m[None, :]
    eigvals, V = la.eig(A_w)
    W = la.inv(V)
    Cq = V.conj().T @ Q_w @ V
    return modes, A, sqrt_m, A_w, Q_w, eigvals, V, W, Cq


@lru_cache(maxsize=None)
def _metrics(K: int, T: float):
    modes, _, sqrt_m, _, _, eigvals, V, W, Cq = _basis_data(K)
    propagator = (V * np.exp(eigvals * T)[None, :]) @ W

    K_E_raw = propagator.conj().T @ propagator
    herm_E = la.norm(K_E_raw - K_E_raw.conj().T, ord="fro") / la.norm(K_E_raw, ord="fro")
    K_E = 0.5 * (K_E_raw + K_E_raw.conj().T)
    e_values, e_vectors = la.eigh(K_E)
    w_E = e_vectors[:, -1]

    sums = eigvals.conj()[:, None] + eigvals[None, :]
    integ = np.empty_like(sums)
    mask = np.abs(sums) < 1.0e-12
    integ[mask] = T
    integ[~mask] = np.expm1(sums[~mask] * T) / sums[~mask]
    K_G_raw = W.conj().T @ (Cq * integ) @ W
    herm_G = la.norm(K_G_raw - K_G_raw.conj().T, ord="fro") / la.norm(K_G_raw, ord="fro")
    K_G = 0.5 * (K_G_raw + K_G_raw.conj().T)
    q_values, q_vectors = la.eigh(K_G)
    w_G = q_vectors[:, -1]
    w_minus = q_vectors[:, 0]

    g_plus = float(q_values[-1])
    g_minus = float(q_values[0])
    j_energy = float(np.real(w_E.conj().T @ K_G @ w_E))
    delta = float((g_plus - j_energy) / g_plus)
    theta = float(np.degrees(np.arccos(np.clip(abs(np.vdot(w_E, w_G)), 0.0, 1.0))))

    n = len(modes)
    mode_weight_E = np.abs(w_E[:n]) ** 2 + np.abs(w_E[n:]) ** 2
    mode_weight_G = np.abs(w_G[:n]) ** 2 + np.abs(w_G[n:]) ** 2
    phi_E = float(np.sum(np.abs(w_E[:n]) ** 2))
    phi_G = float(np.sum(np.abs(w_G[:n]) ** 2))

    u_E = w_E / sqrt_m
    u_G = w_G / sqrt_m
    def coherence_phase(u):
        phi = u[:n]
        eta = u[n:]
        c = np.vdot(eta, phi) / (la.norm(eta) * la.norm(phi))
        return float(abs(c)), float(np.angle(c))

    coh_E, phase_E = coherence_phase(u_E)
    coh_G, phase_G = coherence_phase(u_G)

    return {
        "GE": float(e_values[-1]),
        "qplus": g_plus,
        "qminus": g_minus,
        "jE": j_energy,
        "delta": delta,
        "theta": theta,
        "wE": w_E,
        "wG": w_G,
        "wminus": w_minus,
        "mode_weight_E": mode_weight_E,
        "mode_weight_G": mode_weight_G,
        "phiE": phi_E,
        "phiG": phi_G,
        "cohE": coh_E,
        "cohG": coh_G,
        "phaseE": phase_E,
        "phaseG": phase_G,
        "hermE": float(herm_E),
        "hermG": float(herm_G),
        "K_G": K_G,
    }


def _common_projection_overlap(K_small: int, K_big: int, T: float, family: str):
    small = _metrics(K_small, T)[family]
    big = _metrics(K_big, T)[family]
    modes_big = np.arange(-K_big, K_big + 1)
    n_big = len(modes_big)
    idx = np.where(np.abs(modes_big) <= K_small)[0]
    projected = np.concatenate([big[idx], big[n_big + idx]])
    overlap = abs(np.vdot(small, projected)) / (la.norm(small) * la.norm(projected))
    tail = 1.0 - la.norm(projected) ** 2
    return float(overlap), float(tail)


def test_s0_resolution_robust_spectral_stability() -> None:
    for K in KS:
        _, A, *_ = _basis_data(K)
        alpha = float(np.max(la.eigvals(A).real))
        np.testing.assert_allclose(alpha, EXPECTED_ALPHA[K], rtol=0.0, atol=3.0e-10)
        assert alpha < -5.0e-3


def test_preregistered_scalar_objectives_and_separation() -> None:
    for K in KS:
        got_GE = []
        got_qp = []
        got_qm = []
        got_delta = []
        got_theta = []
        for T in TS:
            data = _metrics(K, T)
            got_GE.append(data["GE"])
            got_qp.append(data["qplus"])
            got_qm.append(data["qminus"])
            got_delta.append(data["delta"])
            got_theta.append(data["theta"])
            assert data["GE"] > 1.0
            assert data["qminus"] < 0.0 < data["qplus"]
            assert data["delta"] > 0.0
            assert data["theta"] > 0.0
        np.testing.assert_allclose(got_GE, EXPECTED_GE, rtol=0.0, atol=2.0e-9)
        np.testing.assert_allclose(got_qp, EXPECTED_QPLUS, rtol=0.0, atol=3.0e-9)
        np.testing.assert_allclose(got_qm, EXPECTED_QMINUS, rtol=0.0, atol=3.0e-9)
        np.testing.assert_allclose(got_delta, EXPECTED_DELTA, rtol=0.0, atol=3.0e-9)
        np.testing.assert_allclose(got_theta, EXPECTED_THETA_DEG, rtol=0.0, atol=3.0e-7)


def test_preregistered_phi_eta_and_phase_structure() -> None:
    for K in KS:
        np.testing.assert_allclose([_metrics(K, T)["phiE"] for T in TS], EXPECTED_PHI_E, atol=2.0e-9, rtol=0.0)
        np.testing.assert_allclose([_metrics(K, T)["phiG"] for T in TS], EXPECTED_PHI_G, atol=2.0e-9, rtol=0.0)
        np.testing.assert_allclose([_metrics(K, T)["phaseE"] for T in TS], EXPECTED_PHASE_E, atol=2.0e-9, rtol=0.0)
        np.testing.assert_allclose([_metrics(K, T)["phaseG"] for T in TS], EXPECTED_PHASE_G, atol=2.0e-9, rtol=0.0)
        assert all(_metrics(K, T)["cohE"] > 0.97 for T in TS)
        assert all(_metrics(K, T)["cohG"] > 0.96 for T in TS)


def test_resolution_comparison_uses_common_fourier_subspaces() -> None:
    for T in TS:
        for family in ("wE", "wG"):
            overlap, tail = _common_projection_overlap(32, 96, T, family)
            assert overlap > 1.0 - 2.0e-12
            assert abs(tail) < 2.0e-12
        for key in ("GE", "qplus", "qminus", "delta", "theta", "phiE", "phiG", "phaseE", "phaseG"):
            values = np.array([_metrics(K, T)[key] for K in KS])
            assert np.max(values) - np.min(values) < 5.0e-10


def test_numerical_hermiticity_normalization_and_rayleigh_checks() -> None:
    for K in KS:
        for T in TS:
            data = _metrics(K, T)
            assert data["hermE"] < 2.0e-12
            assert data["hermG"] < 2.0e-9
            np.testing.assert_allclose(np.vdot(data["wE"], data["wE"]).real, 1.0, atol=3.0e-12, rtol=0.0)
            np.testing.assert_allclose(np.vdot(data["wG"], data["wG"]).real, 1.0, atol=3.0e-12, rtol=0.0)
            rayleigh = float(np.real(data["wG"].conj().T @ data["K_G"] @ data["wG"]))
            np.testing.assert_allclose(rayleigh, data["qplus"], atol=4.0e-9, rtol=0.0)
            residual = la.norm(data["K_G"] @ data["wG"] - data["qplus"] * data["wG"])
            assert residual < 2.0e-9


def test_direct_k64_modal_energy_and_transport_trajectories() -> None:
    K = 64
    modes, _, _, A_w, Q_w, eigvals, V, _, _ = _basis_data(K)
    leading = int(np.argmax(eigvals.real))
    w_modal = V[:, leading] / la.norm(V[:, leading])

    for T in TS:
        data = _metrics(K, T)
        times = np.linspace(0.0, T, 2001)
        for family, w0 in (("modal", w_modal), ("energy", data["wE"]), ("transport", data["wG"])):
            states = expm_multiply(csr_matrix(A_w), w0, start=0.0, stop=T, num=len(times), endpoint=True)
            energy = np.real(np.einsum("bi,bi->b", states.conj(), states))
            gamma = np.real(np.einsum("bi,ij,bj->b", states.conj(), Q_w, states))
            cumulative = cumulative_trapezoid(gamma, times, initial=0.0)
            np.testing.assert_allclose(energy[0], 1.0, atol=4.0e-12, rtol=0.0)
            if family == "energy":
                np.testing.assert_allclose(energy[-1], data["GE"], atol=3.0e-9, rtol=0.0)
            if family == "transport":
                np.testing.assert_allclose(cumulative[-1], data["qplus"], atol=8.0e-8, rtol=0.0)
        # The least-damped modal trajectory must decay at the stable pilot point.
        modal_states = expm_multiply(csr_matrix(A_w), w_modal, start=0.0, stop=T, num=2, endpoint=True)
        modal_energy = np.real(np.einsum("bi,bi->b", modal_states.conj(), modal_states))
        assert modal_energy[-1] < modal_energy[0]
