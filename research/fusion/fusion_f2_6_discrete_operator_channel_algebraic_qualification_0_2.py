"""Fusion F2.6 0.2 pre-spectral structural diagnostics.

No eigenvalue/eigenvector, propagator, Gramian, pseudospectral,
optimizer, or finite-time calculation is performed here.
"""

import json
import math
import numpy as np
from scipy.special import eval_legendre, i0e, j0, roots_laguerre, roots_hermitenorm
from numpy.polynomial.legendre import Legendre

EPS = 0.18
KY_RHOI0 = 0.3
SHAT = 0.8
MASS_RATIO = 3672.0
LEVELS = {
    "K0": dict(W=1, p=12, Nu=16, Nmu=8),
    "K1": dict(W=2, p=16, Nu=24, Nmu=12),
    "K2": dict(W=3, p=20, Nu=32, Nmu=16),
}


def lgl(p):
    P = Legendre.basis(p)
    x = np.concatenate(([-1.0], np.sort(P.deriv().roots()), [1.0]))
    w = 2.0 / (p * (p + 1) * eval_legendre(p, x) ** 2)
    return x, w


def theta_grid(W, p):
    n_elem = 2 * (2 * W + 1)
    left = -(2 * W + 1) * math.pi
    x, w = lgl(p)
    nodes, weights = [], []
    for e in range(n_elem):
        a = left + e * math.pi
        th = a + (x + 1.0) * math.pi / 2.0
        ww = w * math.pi / 2.0
        if e == 0:
            nodes.extend(th.tolist())
            weights.extend(ww.tolist())
        else:
            weights[-1] += ww[0]
            nodes.extend(th[1:].tolist())
            weights.extend(ww[1:].tolist())
    return np.asarray(nodes[1:-1]), np.asarray(weights[1:-1])


def beta(theta):
    return 1.0 / (1.0 + EPS * np.cos(theta))


def kperp_rhoi0(theta):
    return KY_RHOI0 * np.sqrt(1.0 + (SHAT * theta) ** 2)


def local_gamma_quadrature(theta, Nmu):
    be = beta(theta)
    kp = kperp_rhoi0(theta)
    z, wz = roots_laguerre(Nmu)
    b = (kp / be) ** 2
    arg = np.sqrt(2.0 * z * kp ** 2 / be)
    quad = be * np.sum(wz * np.exp(-(be - 1.0) * z) * j0(arg) ** 2)
    return b, quad, i0e(b)


def ion_moment_errors(theta, Nu, Nmu):
    u, wu = roots_hermitenorm(Nu)
    z, wz = roots_laguerre(Nmu)
    out = dict(density=0.0, energy=0.0, heat_weight=0.0)
    for be in beta(theta):
        rz = np.exp(-(be - 1.0) * z)
        su = np.sum(wu) / np.sqrt(2.0 * np.pi)
        density = be * su * np.sum(wz * rz)
        eu = np.sum(wu * u ** 2 / 2.0) / np.sqrt(2.0 * np.pi)
        ez = np.sum(wz * rz * z * be)
        energy = be * (eu * np.sum(wz * rz) + su * ez)
        heat = energy - 2.5 * density
        out["density"] = max(out["density"], abs(density - 1.0))
        out["energy"] = max(out["energy"], abs(energy - 1.5))
        out["heat_weight"] = max(out["heat_weight"], abs(heat + 1.0))
    return out


def run():
    result = {}
    rhoe_rhoi = 1.0 / math.sqrt(MASS_RATIO)
    for name, cfg in LEVELS.items():
        theta, wtheta = theta_grid(cfg["W"], cfg["p"])
        be = beta(theta)
        mV = wtheta / be ** 2
        C = 2.0 * mV
        exact, quad, bvals = [], [], []
        for th in theta:
            b, q, ex = local_gamma_quadrature(th, cfg["Nmu"])
            bvals.append(b)
            quad.append(q)
            exact.append(ex)
        exact = np.asarray(exact)
        quad = np.asarray(quad)
        bvals = np.asarray(bvals)
        diff = quad - exact
        iw = int(np.argmax(np.abs(diff)))
        result[name] = {
            "Ntheta": int(theta.size),
            "Nmu": cfg["Nmu"],
            "C_QN_cond_diag": float(C.max() / C.min()),
            "max_kperp_rhoe_nodes": float(np.max(kperp_rhoi0(theta)) * rhoe_rhoi),
            "ion_moment_max_abs_error": ion_moment_errors(theta, cfg["Nu"], cfg["Nmu"]),
            "flr_identity_full_support": {
                "max_abs_error": float(np.max(np.abs(diff))),
                "max_relative_error": float(np.max(np.abs(diff) / exact)),
                "worst_theta": float(theta[iw]),
                "worst_b_local": float(bvals[iw]),
                "worst_Gamma0_exact": float(exact[iw]),
                "worst_J0sq_quadrature": float(quad[iw]),
                "field_block_frobenius_defect_over_C": float(np.linalg.norm(mV * diff) / np.linalg.norm(C)),
                "max_local_field_block_defect_over_C": float(np.max(np.abs(mV * diff / C))),
            },
        }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run()
