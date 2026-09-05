"""Single-point Fusion F1.4 numerical/spectral qualification.

Governance guardrails:
- exactly one F1.3-frozen parameter point;
- no parameter or wavenumber scan;
- no time horizon;
- no propagator, Gramian, finite-time objective, optimizer or transient-growth calculation;
- no damping or spectral rescue.
"""

from __future__ import annotations

import numpy as np


STRUCT_TOL = 1.0e-12


def frozen_matrices():
    # F1.3-frozen single point only.
    tau_i = 1.0
    R_over_Ln = 2.2
    R_over_LT = 6.9
    safety_q = 1.4
    kx_rhoi = 0.0
    ky_rhoi = 0.3

    b_p = kx_rhoi**2 + ky_rhoi**2
    C = 1.0 / (tau_i + b_p)
    omega_tilde = ky_rhoi
    kappa_tilde = 1.0 / safety_q
    Gn_tilde = -1j * ky_rhoi * R_over_Ln
    Gp_tilde = -1j * ky_rhoi * (R_over_Ln + R_over_LT)

    A = np.array(
        [
            [C * Gn_tilde - 2j * omega_tilde * C,
             -1j * kappa_tilde,
             -1j * omega_tilde,
             -1j * omega_tilde],
            [-1j * kappa_tilde * C,
             -2j * omega_tilde,
             -1j * kappa_tilde,
             0.0],
            [C * Gp_tilde + 4j * omega_tilde * (1.0 - C),
             -3j * kappa_tilde,
             -7j * omega_tilde,
             -1j * omega_tilde],
            [C * Gp_tilde + 3j * omega_tilde * (1.0 - C),
             -1j * kappa_tilde,
             -1j * omega_tilde,
             -5j * omega_tilde],
        ],
        dtype=complex,
    )

    M = np.array(
        [
            [2.5 + C, 0.0, -0.5, -1.0],
            [0.0, 1.0, 0.0, 0.0],
            [-0.5, 0.0, 0.5, 0.0],
            [-1.0, 0.0, 0.0, 1.0],
        ],
        dtype=complex,
    )

    Q0 = np.array(
        [
            [0.0, 0.0, 1j / 4.0, 1j / 2.0],
            [0.0, 0.0, 0.0, 0.0],
            [-1j / 4.0, 0.0, 0.0, 0.0],
            [-1j / 2.0, 0.0, 0.0, 0.0],
        ],
        dtype=complex,
    )
    Qhat = ky_rhoi * C * Q0

    A0 = A.copy()
    A0[0, 0] -= C * Gn_tilde
    A0[2, 0] -= C * Gp_tilde
    A0[3, 0] -= C * Gp_tilde

    B = np.eye(4, dtype=complex)
    Rin = M.copy()

    coeffs = {
        "tau_i": tau_i,
        "R_over_Ln": R_over_Ln,
        "R_over_LT": R_over_LT,
        "q": safety_q,
        "kx_rhoi": kx_rhoi,
        "ky_rhoi": ky_rhoi,
        "b_p": b_p,
        "C": C,
        "omega_tilde": omega_tilde,
        "kappa_tilde": kappa_tilde,
        "Gn_tilde": Gn_tilde,
        "Gp_tilde": Gp_tilde,
    }
    return A, A0, M, Qhat, B, Rin, coeffs


def cross_phase(z: np.ndarray, C: float, ky_rhoi: float) -> float:
    return float(
        -ky_rhoi
        * C
        * np.imag(np.conj(z[0]) * (0.5 * z[2] + z[3]))
    )


def qualify():
    A, A0, M, Qhat, B, Rin, c = frozen_matrices()

    # Structural checks only.
    assert np.max(np.abs(M - M.conj().T)) < STRUCT_TOL
    assert np.min(np.linalg.eigvalsh(M)) > 0.0
    assert np.max(np.abs(Qhat - Qhat.conj().T)) < STRUCT_TOL
    assert np.linalg.matrix_rank(Qhat, tol=STRUCT_TOL) == 2
    assert np.linalg.matrix_rank(B, tol=STRUCT_TOL) == 4
    assert np.max(np.abs(Rin - M)) == 0.0

    balance = A.conj().T @ M + M @ A
    balance_rhs = 2.0 * c["R_over_LT"] * Qhat
    balance_residual = np.max(np.abs(balance - balance_rhs))
    assert balance_residual < STRUCT_TOL

    conservative_residual = np.max(np.abs(A0.conj().T @ M + M @ A0))
    assert conservative_residual < STRUCT_TOL

    # Fixed deterministic physical-channel tests: no optimization/search.
    states = (
        np.array([1.0, 0.0, 1j, 0.0], dtype=complex),
        np.array([1 + 1j, 0.2, 0.3 - 0.4j, -0.2 + 0.7j], dtype=complex),
        np.array([0.2 - 0.5j, -0.1j, 1.2 + 0.3j, -0.4 - 0.2j], dtype=complex),
        np.array([0.0, 1 + 2j, 0.3 + 0.1j, -0.7 + 0.4j], dtype=complex),
    )
    for z in states:
        matrix_value = float(np.real(np.vdot(z, Qhat @ z)))
        direct_value = cross_phase(z, c["C"], c["ky_rhoi"])
        assert abs(matrix_value - direct_value) < STRUCT_TOL

    # Coordinate congruence to temperature variables.
    T = np.array(
        [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [1, 0, 1, 0],
         [1, 0, 0, 1]],
        dtype=complex,
    )
    My = T.conj().T @ M @ T
    Qy = T.conj().T @ Qhat @ T
    assert np.min(np.linalg.eigvalsh(My)) > 0.0
    assert np.linalg.matrix_rank(Qy, tol=STRUCT_TOL) == 2

    # Complete single-point spectrum.
    eigvals, eigvecs = np.linalg.eig(A)
    A_norm = np.linalg.norm(A, 2)
    spec_tol = 100.0 * np.finfo(float).eps * max(1.0, A_norm)
    alpha = float(np.max(eigvals.real))
    assert abs(alpha) < spec_tol  # F1.4 marginal classification.

    L = np.linalg.cholesky(M)
    W = L.conj().T

    return {
        "A": A,
        "M": M,
        "Qhat": Qhat,
        "eigvals": eigvals,
        "alpha": alpha,
        "spec_tol": spec_tol,
        "balance_residual": balance_residual,
        "conservative_residual": conservative_residual,
        "cond_M": np.linalg.cond(M, 2),
        "cond_W": np.linalg.cond(W, 2),
        "cond_eigvecs": np.linalg.cond(eigvecs, 2),
        "coeffs": c,
    }


if __name__ == "__main__":
    out = qualify()
    np.set_printoptions(precision=12, suppress=True)
    print("A_tilde=\n", out["A"])
    print("M=\n", out["M"])
    print("Qhat=\n", out["Qhat"])
    print("eigenvalues=", out["eigvals"])
    print("alpha=", out["alpha"])
    print("spectral tolerance=", out["spec_tol"])
    print("balance residual=", out["balance_residual"])
    print("source-free residual=", out["conservative_residual"])
    print("cond2(M)=", out["cond_M"])
    print("cond2(whitening)=", out["cond_W"])
    print("cond2(eigenvectors)=", out["cond_eigvecs"])
