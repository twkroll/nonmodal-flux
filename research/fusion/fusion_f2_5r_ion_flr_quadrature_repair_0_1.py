"""Fusion F2.5R 0.1 ion-FLR Gauss-Laguerre repair diagnostics.

Pre-spectral / pre-effect only. This script evaluates manufactured
local-B ion-FLR identities, positive-metric field-block diagnostics,
Maxwellian moments, positive quadrature weights, and a geometry-only
between-node envelope. It does not construct or inspect A_K spectra,
propagators, Gramians, optimizers, transport effects, or GENE output.
"""

import json
import math
import numpy as np
from scipy.special import eval_legendre, i0e, j0, roots_laguerre, roots_hermitenorm
from numpy.polynomial.legendre import Legendre

EPS = 0.18
KY_RHOI0 = 0.3
SHAT = 0.8

LEVELS = {
    "K0": dict(W=1, p=12, Nu=16),
    "K1": dict(W=2, p=16, Nu=24),
    "K2": dict(W=3, p=20, Nu=32),
}

CANDIDATES = [8, 12, 16, 20, 24, 28, 32, 40, 48, 56, 64, 80, 96, 112, 128]

ABS_TOL = 1e-10
REL_TOL = 1e-8
FIELD_TOL = 1e-10
ENVELOPE_POINTS_PER_ELEMENT = 257

HISTORICAL_MOMENT_BASELINE = {
    "K0": dict(density=3.3306690738754696e-16,
               energy=3.6415315207705135e-14,
               heat_weight=3.730349362740526e-14),
    "K1": dict(density=8.881784197001252e-16,
               energy=2.6645352591003757e-15,
               heat_weight=1.9984014443252818e-15),
    "K2": dict(density=5.551115123125783e-16,
               energy=8.881784197001252e-16,
               heat_weight=1.5543122344752192e-15),
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


def envelope_grid(W):
    n_elem = 2 * (2 * W + 1)
    left = -(2 * W + 1) * math.pi
    j = np.arange(ENVELOPE_POINTS_PER_ELEMENT)
    x = np.cos(math.pi * j / (ENVELOPE_POINTS_PER_ELEMENT - 1))[::-1]
    nodes = []
    for e in range(n_elem):
        a = left + e * math.pi
        th = a + (x + 1.0) * math.pi / 2.0
        if e == 0:
            nodes.extend(th.tolist())
        else:
            nodes.extend(th[1:].tolist())
    return np.asarray(nodes[1:-1])


def beta(theta):
    return 1.0 / (1.0 + EPS * np.cos(theta))


def kperp_rhoi0(theta):
    return KY_RHOI0 * np.sqrt(1.0 + (SHAT * theta) ** 2)


def flr_identity(theta, Nmu):
    theta = np.asarray(theta)
    z, wz = roots_laguerre(Nmu)
    be = beta(theta)[:, None]
    kp = kperp_rhoi0(theta)[:, None]
    b = (kperp_rhoi0(theta) / beta(theta)) ** 2
    arg = np.sqrt(2.0 * z[None, :] * kp ** 2 / be)
    residual = np.exp(-(be - 1.0) * z[None, :])
    quad = be[:, 0] * ((residual * j0(arg) ** 2) @ wz)
    exact = i0e(b)
    diff = quad - exact
    mask = exact >= 1e-6
    rel = np.zeros_like(diff)
    rel[mask] = np.abs(diff[mask]) / exact[mask]
    return b, quad, exact, diff, rel


def active_diagnostics(theta, wtheta, Nmu):
    b, quad, exact, diff, rel = flr_identity(theta, Nmu)
    be = beta(theta)
    mV = wtheta / be ** 2
    C = 2.0 * mV
    iw = int(np.argmax(np.abs(rel)))
    return {
        "max_abs_error": float(np.max(np.abs(diff))),
        "max_relative_error": float(np.max(rel)),
        "worst_theta_relative": float(theta[iw]),
        "worst_b_local_relative": float(b[iw]),
        "field_block_frobenius_defect_over_C": float(np.linalg.norm(mV * diff) / np.linalg.norm(C)),
        "max_local_field_block_defect_over_C": float(np.max(np.abs(mV * diff / C))),
    }


def envelope_diagnostics(theta, Nmu):
    b, quad, exact, diff, rel = flr_identity(theta, Nmu)
    iw = int(np.argmax(np.abs(rel)))
    return {
        "point_count": int(theta.size),
        "max_abs_error": float(np.max(np.abs(diff))),
        "max_relative_error": float(np.max(rel)),
        "worst_theta_relative": float(theta[iw]),
        "worst_b_local_relative": float(b[iw]),
        "b_min": float(np.min(b)),
        "b_max": float(np.max(b)),
    }


def ion_moment_errors(theta, Nu, Nmu):
    u, wu = roots_hermitenorm(Nu)
    z, wz = roots_laguerre(Nmu)
    su = np.sum(wu) / np.sqrt(2.0 * np.pi)
    eu = np.sum(wu * u ** 2 / 2.0) / np.sqrt(2.0 * np.pi)
    out = dict(density=0.0, energy=0.0, heat_weight=0.0)
    for be in beta(theta):
        rz = np.exp(-(be - 1.0) * z)
        S0 = np.sum(wz * rz)
        density = be * su * S0
        ez = np.sum(wz * rz * z * be)
        energy = be * (eu * S0 + su * ez)
        heat = energy - 2.5 * density
        out["density"] = max(out["density"], abs(density - 1.0))
        out["energy"] = max(out["energy"], abs(energy - 1.5))
        out["heat_weight"] = max(out["heat_weight"], abs(heat + 1.0))
    return out


def representative_checks(Nmu):
    out = {}
    for key, th in (("theta0", 0.0), ("theta_pi", math.pi)):
        b, quad, exact, diff, rel = flr_identity(np.asarray([th]), Nmu)
        out[key] = {
            "b_local": float(b[0]),
            "Gamma0_exact": float(exact[0]),
            "J0sq_quadrature": float(quad[0]),
            "abs_error": float(abs(diff[0])),
            "relative_error": float(rel[0]),
        }
    return out


def passes(active, envelope):
    return (
        active["max_abs_error"] <= ABS_TOL
        and active["max_relative_error"] <= REL_TOL
        and active["field_block_frobenius_defect_over_C"] <= FIELD_TOL
        and active["max_local_field_block_defect_over_C"] <= FIELD_TOL
        and envelope["max_abs_error"] <= ABS_TOL
        and envelope["max_relative_error"] <= REL_TOL
    )


def run():
    result = {
        "gate": "Fusion F2.5R — Ion-FLR Magnetic-Moment Quadrature Repair / Discretization Requalification Gate 0.1",
        "candidate_sequence": CANDIDATES,
        "thresholds": {
            "max_abs_flr_identity": ABS_TOL,
            "max_relative_flr_identity_where_Gamma0_ge_1e-6": REL_TOL,
            "field_block_frobenius_over_C": FIELD_TOL,
            "field_block_max_local_over_C": FIELD_TOL,
        },
        "envelope_points_per_pi_element": ENVELOPE_POINTS_PER_ELEMENT,
        "levels": {},
        "no_spectral_work": True,
    }

    selected = []
    for name, cfg in LEVELS.items():
        theta, wtheta = theta_grid(cfg["W"], cfg["p"])
        envtheta = envelope_grid(cfg["W"])
        history = []
        chosen = None
        for Nmu in CANDIDATES:
            active = active_diagnostics(theta, wtheta, Nmu)
            envelope = envelope_diagnostics(envtheta, Nmu)
            ok = passes(active, envelope)
            history.append({"Nmu": Nmu, "active": active, "envelope": envelope, "pass": bool(ok)})
            if ok:
                chosen = Nmu
                break
        if chosen is None:
            raise RuntimeError(f"No passing N_mu found for {name}")
        if selected and chosen < selected[-1]:
            raise RuntimeError("Non-monotone repaired ladder")
        selected.append(chosen)

        z, wz = roots_laguerre(chosen)
        moments = ion_moment_errors(theta, cfg["Nu"], chosen)
        result["levels"][name] = {
            "selected_Nmu": chosen,
            "candidate_history": history,
            "ion_state_dimension": int(theta.size * cfg["Nu"] * chosen),
            "moments": moments,
            "historical_moment_baseline": HISTORICAL_MOMENT_BASELINE[name],
            "laguerre_weights": {
                "all_positive": bool(np.all(wz > 0.0)),
                "min": float(np.min(wz)),
                "max": float(np.max(wz)),
                "sum": float(np.sum(wz)),
            },
            "representative": representative_checks(chosen),
        }

    result["selected_ladder"] = dict(zip(LEVELS.keys(), selected))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    run()
