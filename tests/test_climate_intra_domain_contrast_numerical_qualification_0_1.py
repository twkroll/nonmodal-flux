import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy import linalg as la

BETA = 0.8
R = 0.05787037037037
LX = 20.0
LY = 10.0
GG = 8.0 * (np.tanh(5.0) ** 3 / 3.0 - np.tanh(5.0) ** 5 / 5.0)
RUNGS = [(8, 16), (12, 24), (16, 32), (20, 40), (24, 48)]


def coefficient_matrices(ny, nq):
    z, w = leggauss(nq)
    y = 5.0 * z
    w = 5.0 * w
    n = np.arange(1, ny + 1)
    phi = np.sqrt(2.0 / LY) * np.sin(np.outer(y + 5.0, n * np.pi / LY))
    dphi = (
        np.sqrt(2.0 / LY)
        * np.cos(np.outer(y + 5.0, n * np.pi / LY))
        * (n * np.pi / LY)
    )
    s = 1.0 / np.cosh(y) ** 2
    u = s
    upp = 4.0 * s - 6.0 * s**2
    c = BETA - upp
    gp = 6.0 * s**2 - 4.0 * s
    un = phi.T @ (w[:, None] * (u[:, None] * phi))
    cn = phi.T @ (w[:, None] * (c[:, None] * phi))
    rn = phi.T @ (w[:, None] * (gp[:, None] * dphi))
    return un, cn, rn


def modal_objects(m, ny, un, cn, rn):
    k = 2.0 * np.pi * m / LX
    ell = np.arange(1, ny + 1) * np.pi / LY
    kappa2 = k * k + ell * ell
    d_inv = np.diag(-1.0 / kappa2)
    d = -np.diag(kappa2)
    a = -R * np.eye(ny) - 1j * k * d_inv @ (un @ d + cn)
    mmat = 2.0 * LX * np.diag(kappa2)
    q = 1j * k / GG * (rn - rn.T)
    return a, mmat, q


def test_quadrature_parity_and_channel_structure():
    for _, ny in RUNGS:
        x512 = coefficient_matrices(ny, 512)
        x1024 = coefficient_matrices(ny, 1024)
        for a, b in zip(x512, x1024):
            rel = la.norm(b - a, "fro") / max(1.0, la.norm(b, "fro"))
            assert rel <= 1e-12

        un, cn, rn = x512
        n = np.arange(1, ny + 1)
        opposite = (n[:, None] % 2) != (n[None, :] % 2)
        same = ~opposite
        assert np.max(np.abs(un[opposite])) < 1e-12
        assert np.max(np.abs(cn[opposite])) < 1e-12

        _, mmat, q = modal_objects(1, ny, un, cn, rn)
        assert np.allclose(mmat, mmat.conj().T, atol=1e-13, rtol=0)
        assert np.min(np.diag(mmat)) > 0
        assert la.norm(q - q.conj().T, "fro") <= 1e-12
        assert np.max(np.abs(q[same])) < 1e-12
        evq = la.eigvalsh(q)
        assert evq[0] < 0 < evq[-1]


def test_predeclared_sign_witness():
    ny = 16
    un, cn, rn = coefficient_matrices(ny, 512)
    _, mmat, q = modal_objects(1, ny, un, cn, rn)
    cp = np.zeros(ny, dtype=complex)
    cm = np.zeros(ny, dtype=complex)
    cp[0], cp[1] = 1.0, 1j
    cm[0], cm[1] = 1.0, -1j

    qp = np.vdot(cp, q @ cp).real
    qm = np.vdot(cm, q @ cm).real
    ep = 0.5 * np.vdot(cp, mmat @ cp).real
    em = 0.5 * np.vdot(cm, mmat @ cm).real
    assert np.isclose(qp, -qm, rtol=1e-13, atol=1e-14)
    assert np.isclose(ep, em, rtol=1e-14, atol=1e-14)

    z, w = leggauss(1024)
    y = 5.0 * z
    w = 5.0 * w
    n = np.arange(1, ny + 1)
    phi = np.sqrt(2.0 / LY) * np.sin(np.outer(y + 5.0, n * np.pi / LY))
    dphi = (
        np.sqrt(2.0 / LY)
        * np.cos(np.outer(y + 5.0, n * np.pi / LY))
        * (n * np.pi / LY)
    )
    s = 1.0 / np.cosh(y) ** 2
    gp = 6.0 * s**2 - 4.0 * s
    k = 2.0 * np.pi / LX

    def direct(c):
        f = phi @ c
        fp = dphi @ c
        reynolds = -2.0 * k * np.imag(fp * np.conj(f))
        return np.sum(w * gp * reynolds) / GG

    assert np.isclose(qp, direct(cp), rtol=2e-13, atol=1e-14)
    assert np.isclose(qm, direct(cm), rtol=2e-13, atol=1e-14)


def test_spectral_stability_and_eigen_residuals_all_frozen_rungs():
    for mx, ny in RUNGS:
        un, cn, rn = coefficient_matrices(ny, 512)
        alpha = -np.inf
        worst_resid = 0.0
        n = np.arange(1, ny + 1)
        opposite = (n[:, None] % 2) != (n[None, :] % 2)
        for m in range(1, mx + 1):
            a, _, _ = modal_objects(m, ny, un, cn, rn)
            assert np.max(np.abs(a[opposite])) < 1e-10
            vals, vecs = la.eig(a)
            alpha = max(alpha, np.max(vals.real))
            anorm = la.norm(a, 2)
            for j, lam in enumerate(vals):
                v = vecs[:, j]
                resid = la.norm(a @ v - lam * v) / max(1.0, anorm, abs(lam))
                worst_resid = max(worst_resid, resid)
        assert alpha < 0.0
        assert abs(alpha + R) < 1e-10
        assert worst_resid < 1e-10
