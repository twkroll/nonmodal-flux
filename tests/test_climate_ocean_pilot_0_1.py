import numpy as np
from scipy import integrate, linalg

S = 150.0
U = 0.5
R = 0.072337962962963
HORIZONS = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0)
RESOLUTIONS = ((4, 4), (8, 8), (12, 12), (16, 16), (24, 24))


def matrices(m: int, n: int):
    k = 2.0 * np.pi * m / 30.0
    ell = np.pi * n / 10.0
    a = k * k + ell * ell
    b = a + 1.0
    A = np.array(
        [
            [-R + 1j * k / a, -1j * k * U],
            [1j * k * U * (1.0 - a) / b, -R + 1j * k / b],
        ],
        dtype=complex,
    )
    M = S * np.diag([a, b]).astype(complex)
    Q = (S / 2.0) * np.array([[0.0, -1j * k], [1j * k, 0.0]], dtype=complex)
    Minvhalf = (1.0 / np.sqrt(S)) * np.diag([a**-0.5, b**-0.5]).astype(complex)
    return A, M, Q, Minvhalf


def heat_integral_augmented(A, Q, T):
    L = np.kron(np.eye(2), A.conj().T) + np.kron(A.T, np.eye(2))
    q = Q.reshape(-1, order="F")
    C = np.zeros((5, 5), dtype=complex)
    C[:4, :4] = L
    C[:4, 4] = q
    return linalg.expm(C * T)[:4, 4].reshape((2, 2), order="F")


def heat_integral_lyapunov(A, Q, T):
    E = linalg.expm(A * T)
    X = linalg.solve_sylvester(A.conj().T, A, -Q)
    return X - E.conj().T @ X @ E


def operators(m, n, T):
    A, M, Q, Minvhalf = matrices(m, n)
    E = linalg.expm(A * T)
    KE = Minvhalf @ E.conj().T @ M @ E @ Minvhalf
    H = heat_integral_augmented(A, Q, T)
    KH = Minvhalf @ H @ Minvhalf
    return KE, KH, E, H, A, M, Q, Minvhalf


def scan(Mx, Ny, T):
    best_E = None
    best_H = None
    min_H = None
    for m in range(1, Mx + 1):
        for n in range(1, Ny + 1):
            KE, KH, *_ = operators(m, n, T)
            evE, vecE = linalg.eigh((KE + KE.conj().T) / 2.0)
            evH, vecH = linalg.eigh((KH + KH.conj().T) / 2.0)
            cand_E = (float(evE[-1]), m, n, vecE[:, -1])
            cand_H = (float(evH[-1]), m, n, vecH[:, -1])
            cand_min = (float(evH[0]), m, n, vecH[:, 0])
            if best_E is None or cand_E[0] > best_E[0]:
                best_E = cand_E
            if best_H is None or cand_H[0] > best_H[0]:
                best_H = cand_H
            if min_H is None or cand_min[0] < min_H[0]:
                min_H = cand_min
    return best_E, best_H, min_H


def test_frozen_structure_and_stability():
    for Mx, Ny in RESOLUTIONS:
        for m in range(1, Mx + 1):
            for n in range(1, Ny + 1):
                A, M, Q, _ = matrices(m, n)
                Am, Mm, Qm, _ = matrices(-m, n)
                assert np.linalg.norm(M - M.conj().T) == 0.0
                assert np.min(np.linalg.eigvalsh(M)) > 0.0
                qev = np.linalg.eigvalsh(Q)
                assert qev[0] < 0.0 < qev[-1]
                assert np.linalg.norm(Q - Q.conj().T) == 0.0
                assert np.max(np.real(np.linalg.eigvals(A))) < 0.0
                assert abs(np.max(np.real(np.linalg.eigvals(A))) + R) < 2e-15
                assert np.linalg.norm(Am - A.conj()) < 1e-14
                assert np.linalg.norm(Qm - Q.conj()) < 1e-14
                assert np.linalg.norm(Mm - M) == 0.0


def test_augmented_integral_matches_lyapunov_tail():
    worst = 0.0
    for T in HORIZONS:
        for m in range(1, 25):
            for n in range(1, 25):
                A, _, Q, _ = matrices(m, n)
                H1 = heat_integral_augmented(A, Q, T)
                H2 = heat_integral_lyapunov(A, Q, T)
                rel = np.linalg.norm(H1 - H2) / max(
                    1.0, np.linalg.norm(H1), np.linalg.norm(H2)
                )
                worst = max(worst, rel)
    assert worst < 1e-11


def test_resolution_robust_objectives_and_optimizer_support():
    expected_E = ((3, 1), (3, 1), (3, 1), (4, 1), (4, 1), (3, 2))
    expected_H = ((3, 1), (3, 1), (3, 1), (4, 1), (4, 1), (4, 2))
    for j, T in enumerate(HORIZONS):
        results = [scan(Mx, Ny, T) for Mx, Ny in RESOLUTIONS]
        reference = results[2]
        for result in results[3:]:
            for idx in range(3):
                assert abs(result[idx][0] - reference[idx][0]) < 1e-13
        assert reference[0][1:3] == expected_E[j]
        assert reference[1][1:3] == expected_H[j]
        for result in results[2:]:
            assert result[0][1:3] == expected_E[j]
            assert result[1][1:3] == expected_H[j]


def test_long_horizon_weak_verdict_and_direct_checks():
    T = 8.0
    energy, heat, _ = scan(12, 12, T)
    assert energy[1:3] == (3, 2)
    assert heat[1:3] == (4, 2)
    angle_deg = 90.0
    KEe, KHe, _, _, Ae, Me, Qe, Mihe = operators(energy[1], energy[2], T)
    _, KHh, _, _, Ah, Mh, Qh, Mihh = operators(heat[1], heat[2], T)
    vE = energy[3]
    vH = heat[3]
    Jplus = heat[0]
    J_at_E = float(np.real(np.vdot(vE, KHe @ vE)))
    gap = (Jplus - J_at_E) / Jplus
    assert abs(gap - 0.04118455337553623) < 1e-12
    assert angle_deg >= 5.0
    assert gap < 0.05
    assert not (angle_deg >= 20.0 and gap >= 0.25)
    for A, M, Q, Mih, v, KE, KH in (
        (Ae, Me, Qe, Mihe, vE, KEe, KHe),
        (Ah, Mh, Qh, Mihh, vH, operators(heat[1], heat[2], T)[0], KHh),
    ):
        x0 = Mih @ v
        xT = linalg.expm(A * T) @ x0
        direct_E = float(np.real(np.vdot(xT, M @ xT)))
        op_E = float(np.real(np.vdot(v, KE @ v)))
        assert abs(direct_E - op_E) / max(1e-12, abs(direct_E), abs(op_E)) < 1e-8

        def flux(t):
            xt = linalg.expm(A * t) @ x0
            return float(np.real(np.vdot(xt, Q @ xt)))

        direct_H = integrate.quad(
            flux, 0.0, T, epsrel=1e-10, epsabs=1e-12, limit=100
        )[0]
        op_H = float(np.real(np.vdot(v, KH @ v)))
        assert abs(direct_H - op_H) / max(1e-12, abs(direct_H), abs(op_H)) < 1e-8
