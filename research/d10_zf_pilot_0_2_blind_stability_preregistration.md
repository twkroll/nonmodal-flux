# D10-ZF Pilot 0.2 — Blind Stability Preregistration

**Date:** 2026-09-02  
**Status:** PREREGISTERED BEFORE SPECTRAL EVALUATION

## Scope lock

The physical D10-ZF point is fixed to

```math
U(x)=\cos x,\qquad L_x=2\pi,\qquad k_y=1,
```

```math
C=\kappa=1,\qquad N=0,
```

with the existing physical definitions of `M`, `Q_Gamma`, and full-state admissibility `B=I` unchanged.

No `K_Gamma`, `K_E`, `theta`, `Delta_Gamma`, energy optimizer, or transport optimizer may be computed or inspected during this qualification.

## Only varied axis

Use only the already existing uniform perpendicular damping axis

```math
\nu_\perp\ge0,
\qquad
A_{K,\nu}=A_{K,0}-\nu_\perp I.
```

This is the same physical damping form already used in the frozen HW branch; it leaves `M` and `Q_Gamma` unchanged and adds the physical metric sink `2 nu_perp M` to the energy balance. No other model parameter is changed.

## Preregistered discrete damping values

Evaluate exactly

```text
nu_perp in {0, 0.005, 0.010, 0.015, 0.020, 0.030, 0.050}.
```

The search set must not be expanded after results are seen.

## Preregistered high-resolution set

Evaluate exactly the centered Fourier-Galerkin truncations

```text
K in {32, 64, 96, 128},
```

with modes `m=-K,...,K` and state dimension `4K+2`.

## Stability criterion and safety margin

For each pair define

```math
\alpha_K(\nu_\perp)=\max_{\lambda\in\sigma(A_{K,\nu})}\operatorname{Re}\lambda.
```

A candidate damping value qualifies as **resolution-robustly stable with numerical safety margin** iff

```math
\max_{K\in\{32,64,96,128\}}\alpha_K(\nu_\perp)\le -5\times10^{-3}.
```

The Pilot-0.2 damping choice is the **smallest preregistered** `nu_perp` satisfying that criterion on all four resolutions.

If no preregistered value qualifies, STOP without enlarging the damping set.

## Prohibited during qualification

Do not compute or inspect

```math
K_\Gamma,\quad K_E,\quad \vartheta,\quad \Delta_\Gamma,
\quad u_E^\star,\quad u_\Gamma^\star.
```

Do not vary `U`, `C`, `kappa`, `k_y`, `B`, `Q_Gamma`, the domain, or the zonal-flow profile.

This file is intentionally committed before spectral evaluation so the selection remains blind with respect to CORE/transport objectives.
