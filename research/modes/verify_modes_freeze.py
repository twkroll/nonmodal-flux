from __future__ import annotations

import numpy as np


def lyapunov_action(a: np.ndarray, x: np.ndarray) -> np.ndarray:
    return a.conj().T @ x + x @ a


def repeated_action(a: np.ndarray, q: np.ndarray, j: int) -> np.ndarray:
    out = q.copy()
    for _ in range(j):
        out = lyapunov_action(a, out)
    return out


def random_coordinate_covariance_check(seed: int = 7) -> dict:
    rng = np.random.default_rng(seed)
    n, m = 5, 2
    a = rng.normal(size=(n, n))
    q = rng.normal(size=(n, n))
    q = 0.5 * (q + q.T)
    b = rng.normal(size=(n, m))
    t = rng.normal(size=(n, n))
    while abs(np.linalg.det(t)) < 0.1:
        t = rng.normal(size=(n, n))

    a_y = np.linalg.solve(t, a @ t)
    b_y = np.linalg.solve(t, b)
    q_y = t.T @ q @ t

    errors = []
    for j in range(4):
        full = b.T @ repeated_action(a, q, j) @ b
        transformed = b_y.T @ repeated_action(a_y, q_y, j) @ b_y
        errors.append(float(np.linalg.norm(full - transformed)))
    return {"max_generation_matrix_error": max(errors)}


def krylov_preservation_check(seed: int = 7, order: int = 2) -> dict:
    rng = np.random.default_rng(seed)
    n, m = 6, 2
    a = rng.normal(size=(n, n))
    q = rng.normal(size=(n, n))
    q = 0.5 * (q + q.T)
    m0 = rng.normal(size=(n, n))
    metric = m0.T @ m0 + np.eye(n)
    b = rng.normal(size=(n, m))

    blocks = [b]
    current = b.copy()
    for _ in range(order):
        current = a @ current
        blocks.append(current.copy())
    jet = np.hstack(blocks)
    u, s, _ = np.linalg.svd(jet, full_matrices=False)
    rank = int(np.sum(s > 1.0e-11 * s[0]))
    v = u[:, :rank]

    g = v.T @ metric @ v
    w = metric @ v @ np.linalg.inv(g)
    a_r = w.T @ a @ v
    b_r = w.T @ b
    q_r = v.T @ q @ v

    moment_errors = []
    for j in range(order + 1):
        full = b.T @ repeated_action(a, q, j) @ b
        reduced = b_r.T @ repeated_action(a_r, q_r, j) @ b_r
        moment_errors.append(float(np.linalg.norm(full - reduced)))

    d0 = rng.normal(size=(n, n))
    d = d0.T @ d0
    q_balance = a.T @ metric + metric @ a + d
    q_balance_r = v.T @ q_balance @ v
    d_r = v.T @ d @ v
    balance_error = float(
        np.linalg.norm(a_r.T @ g + g @ a_r - (q_balance_r - d_r))
    )
    return {
        "jet_rank": rank,
        "max_generation_matrix_error": max(moment_errors),
        "projected_balance_error": balance_error,
    }


def counterexamples() -> dict:
    # Spectrally stable, nonnormal: H0=0, H1=8.
    a_non = np.array([[-1.0, 4.0], [0.0, -2.0]])
    q_non = np.array([[0.0, 1.0], [1.0, 0.0]])
    b_non = np.array([[0.0], [1.0]])

    # Normal diagonal: H0=0, H1=1. Nonnormality is not necessary.
    a_norm = np.diag([-1.0, -2.0])
    q_norm = np.diag([1.0, -1.0])
    b_norm = np.array([[1.0], [1.0]]) / np.sqrt(2.0)

    return {
        "stable_nonnormal": {
            "eigenvalues": np.linalg.eigvals(a_non).tolist(),
            "H0": float((b_non.T @ q_non @ b_non).item()),
            "H1": float((b_non.T @ lyapunov_action(a_non, q_non) @ b_non).item()),
        },
        "normal_diagonal": {
            "eigenvalues": np.linalg.eigvals(a_norm).tolist(),
            "H0": float((b_norm.T @ q_norm @ b_norm).item()),
            "H1": float((b_norm.T @ lyapunov_action(a_norm, q_norm) @ b_norm).item()),
        },
    }


def main() -> None:
    coord = random_coordinate_covariance_check()
    krylov = krylov_preservation_check()
    examples = counterexamples()

    assert coord["max_generation_matrix_error"] < 1.0e-10
    assert krylov["max_generation_matrix_error"] < 1.0e-10
    assert krylov["projected_balance_error"] < 1.0e-10
    assert abs(examples["stable_nonnormal"]["H0"]) < 1.0e-12
    assert abs(examples["stable_nonnormal"]["H1"] - 8.0) < 1.0e-12
    assert abs(examples["normal_diagonal"]["H0"]) < 1.0e-12
    assert abs(examples["normal_diagonal"]["H1"] - 1.0) < 1.0e-12

    print("coordinate covariance:", coord)
    print("Krylov / M-Galerkin preservation:", krylov)
    print("counterexamples:", examples)


if __name__ == "__main__":
    main()
