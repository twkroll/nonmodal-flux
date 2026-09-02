import numpy as np
import scipy.integrate as integrate
import scipy.linalg as la


HORIZONS = np.array([0.007, 0.014, 0.028, 0.056, 0.112, 0.224])


def frozen_objects():
    A = np.zeros((16, 16), dtype=float)
    triplets = [
        (1, 2, 1.0),
        (2, 1, -316666.666667), (2, 2, -1000.0),
        (2, 3, -66666.6666667), (2, 5, -133333.333333),
        (3, 4, 1.0),
        (4, 1, 66666.6666667), (4, 3, -316666.666667),
        (4, 4, -1000.0), (4, 15, -16666.6666667),
        (5, 6, 1.0),
        (6, 1, 8333.33333333), (6, 5, -12239.5833333),
        (6, 6, -125.0), (6, 7, 4166.66666667), (6, 15, -1041.66666667),
        (7, 8, 1.0),
        (8, 5, -2380.95238095), (8, 7, -2465.98639456),
        (8, 8, -71.4285714286),
        (9, 10, 1.0),
        (10, 3, 16666.6666667), (10, 9, -316666.666667),
        (10, 10, -1000.0), (10, 11, -66666.6666667),
        (10, 13, -133333.333333),
        (11, 12, 1.0),
        (12, 9, 66666.6666667), (12, 11, -316666.666667),
        (12, 12, -1000.0),
        (13, 14, 1.0),
        (14, 9, 8333.33333333), (14, 13, -12239.5833333),
        (14, 14, -125.0), (14, 15, 4166.66666667),
        (15, 16, 1.0),
        (16, 3, 595.238095238), (16, 13, -2380.95238095),
        (16, 15, -2465.98639456), (16, 16, -71.4285714286),
    ]
    for row, col, value in triplets:
        A[row - 1, col - 1] = value

    M = np.diag(
        [
            250000.0, 1.0, 250000.0, 1.0, 3906.25, 1.0,
            1275.51020408163, 1.0,
            250000.0, 1.0, 250000.0, 1.0, 3906.25, 1.0,
            1275.51020408163, 1.0,
        ]
    )

    A_path = np.zeros_like(A)
    A_path[9, 2] = 16666.6666666667
    Q = 0.5 * (A_path.T @ M + M @ A_path)

    b_aff = np.zeros(16)
    b_aff[1] = 16000.0
    delta = 0.001
    columns = []
    for tau in (0.002, 0.016):
        rhs = (la.expm(A * (tau + delta)) - la.expm(A * tau)) @ b_aff
        columns.append(la.solve(A, rhs))
    B = np.column_stack(columns)

    return A, M, Q, B


def finite_channel_primary(A, Q, T):
    # Stable finite-horizon identity for stable A:
    # A.T P_inf + P_inf A = -Q,
    # P_Q(T) = P_inf - exp(A.T T) P_inf exp(A T).
    P_inf = la.solve_continuous_lyapunov(A.T, -Q)
    E = la.expm(A * T)
    return P_inf - E.T @ P_inf @ E


def finite_channel_quad(A, Q, T):
    def integrand(t):
        E = la.expm(A * t)
        return (E.T @ Q @ E).ravel()

    value, _ = integrate.quad_vec(
        integrand, 0.0, T, epsabs=1e-12, epsrel=1e-12, norm="2"
    )
    return value.reshape(A.shape)


def test_frozen_structural_gates():
    A, M, Q, B = frozen_objects()
    alpha = np.max(la.eigvals(A).real)
    assert np.isclose(alpha, -33.0964092356, rtol=0.0, atol=5e-10)
    assert alpha < 0.0

    assert np.linalg.norm(M - M.T, ord="fro") == 0.0
    assert np.linalg.eigvalsh(M).min() > 0.0

    assert np.linalg.norm(Q - Q.T, ord="fro") == 0.0

    R_in = np.eye(2)
    assert np.linalg.eigvalsh(R_in).min() > 0.0

    assert np.linalg.matrix_rank(B) == 2
    sqrt_M = np.diag(np.sqrt(np.diag(M)))
    assert np.linalg.cond(sqrt_M @ B) <= 100.0
    assert np.isclose(np.linalg.cond(sqrt_M @ B), 34.2939603, rtol=2e-8)


def test_frozen_semigroup_gate():
    A, _, _, _ = frozen_objects()
    for T in HORIZONS:
        left = la.expm(A * T)
        right = la.expm(A * (2.0 * T / 3.0)) @ la.expm(A * (T / 3.0))
        rel = np.linalg.norm(left - right, ord="fro") / np.linalg.norm(left, ord="fro")
        assert rel < 1e-10


def test_cumulative_channel_against_adaptive_quadrature():
    A, _, Q, _ = frozen_objects()
    for T in HORIZONS:
        primary = finite_channel_primary(A, Q, T)
        independent = finite_channel_quad(A, Q, T)
        rel = (
            np.linalg.norm(primary - independent, ord="fro")
            / np.linalg.norm(independent, ord="fro")
        )
        assert rel < 1e-8


def test_finite_time_operator_gates():
    A, M, Q, B = frozen_objects()

    for T in HORIZONS:
        E = la.expm(A * T)
        K_M = B.T @ E.T @ M @ E @ B
        P_Q = finite_channel_primary(A, Q, T)
        K_Q = B.T @ P_Q @ B

        rel_h_m = np.linalg.norm(K_M - K_M.T, ord="fro") / np.linalg.norm(
            K_M, ord="fro"
        )
        rel_h_q = np.linalg.norm(K_Q - K_Q.T, ord="fro") / np.linalg.norm(
            K_Q, ord="fro"
        )
        assert rel_h_m <= 1e-10
        assert rel_h_q <= 1e-10

        K_M_h = 0.5 * (K_M + K_M.T)
        assert np.linalg.eigvalsh(K_M_h).min() >= -1e-10 * np.linalg.norm(
            K_M_h, ord=2
        )
