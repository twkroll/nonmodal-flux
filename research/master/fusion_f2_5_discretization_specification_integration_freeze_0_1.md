# Fusion F2.5 Discretization-Specification Integration Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER  
**Status:** `STABLE — F2.5 DISCRETIZATION / QUADRATURE SPECIFICATION FROZEN / F2.6 DISCRETE OPERATOR-CHANNEL ALGEBRA GATE RELEASED`

## Scope

This MASTER freeze integrates only the completed `Fusion F2.5 — Structure-Preserving Phase-Space Discretization / Quadrature Specification Freeze 0.1`. It performs no discrete generator or transport-channel construction, no spectrum or growth-rate calculation, no propagator/Gramian construction, no optimizer calculation, no GENE execution and no finite-time objective inspection.

Canonical branch result:

`research/fusion/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`

Branch verdict:

\[
\boxed{\text{F2.5 PASS — STRUCTURE-PRESERVING DISCRETIZATION / QUADRATURE SPECIFICATION FROZEN — RETURN TO MASTER}}
\]

Branch commit:

`43de899b547b2ccc1d0c11ecb6788dfce6cb6b47`

Python CI #378 = `SUCCESS`.

## Frozen numerical architecture

The F2-R numerical state-space package is frozen as

\[
\boxed{
\text{compact-support ballooning Galerkin/SBP spectral elements}
\times\text{ Hermite--Laguerre ion velocity representation}
+\text{ regularized trapped-electron orbit quadrature}
}
\]

with continuous time left unfrozen.

Frozen structural rules include:

- ballooning windows ending at magnetic maxima with compact-support LGL spectral elements;
- weak/SBP assembly of the collisionless ion parallel/mirror phase-space flow, with no boundary damping, filtering, hyperdiffusion or hypercollision;
- symmetric Gauss--Hermite ion `v_parallel` representation and Gauss--Laguerre magnetic-moment representation, retaining both velocity signs and no parity reduction;
- trapped-electron generalized Laguerre energy, interior Legendre pitch quadrature, explicit well labels and analytic regularization of bounce singularities;
- no state degree of freedom on trapped/passing separatrices or the ion turning set;
- exact finite-ion `J0i` and `Gamma0i` evaluation with no small-argument expansion;
- algebraic quasineutrality reconstruction/elimination of `phi_K`, never an extra physical input coordinate;
- later `M_K` derived directly from the positive Helmholtz functional and required to satisfy `M_K=M_K^dagger>0` without shifts or clipping;
- conforming inheritance `B_K=I`, `R_in,K=M_K`;
- later particle, ion-heat and trapped-electron-heat channels reconstructed on the same state space and same physical quadratures.

## Frozen three-level refinement ladder

| quantity | K0 primary | K1 | K2 |
|---|---:|---:|---:|
| `Theta_max` | `3 pi` | `5 pi` | `7 pi` |
| complete electron wells | 3 | 5 | 7 |
| `theta` elements | 6 | 10 | 14 |
| LGL degree `p_theta` | 12 | 16 | 20 |
| interior `theta` DOF | 71 | 159 | 279 |
| ion Hermite order | 16 | 24 | 32 |
| ion Laguerre order | 8 | 12 | 16 |
| trapped-e energy order | 12 | 18 | 24 |
| trapped-e pitch order | 12 | 18 | 24 |
| bounce quadrature order | 24 | 36 | 48 |

Approximate kinetic-state sizes are `N_i/N_e = 9088/432`, `45792/1620`, `142848/4032` for K0/K1/K2 before implementation-specific sparse elimination.

At the frozen F2.3 point, the maximum retained-support reduced-electron ordering parameters are approximately

\[
\max(k_\perp\rho_e)\approx0.03765,\ 0.06241,\ 0.08724
\]

on K0/K1/K2 respectively. These are ordering checks only, not convergence or effect claims.

## Frozen anti-bias boundary

No cutoff, quadrature order, basis order or domain size was selected from any F2-R eigenvalue, stability result, transport magnitude, nonnormality, transient growth or optimizer-separation effect. No hidden intermediate resolution may replace the frozen ladder after physical results are inspected. If the ladder is computationally infeasible or structurally fails, the branch must return to MASTER rather than silently modify it.

## Next gate released

The next authorized task is

**Fusion F2.6 — Discrete Generator / Helmholtz Metric / Physical Channel Reconstruction & Algebraic Balance Qualification Gate 0.1**.

Its purpose is to instantiate the frozen K0/K1/K2 representation and construct, from the already-frozen physical equations and quadratures,

\[
A_K,\qquad M_K,\qquad Q_{\Gamma,K},\qquad Q_{q_i,K},\qquad Q_{q_e,K},
\]

plus the algebraic quasineutrality reconstruction, and then test only structural/algebraic qualification before any spectrum is inspected.

The gate must verify, at minimum:

1. quasineutrality reconstruction residuals;
2. `M_K=M_K^dagger>0` with no loading/clipping;
3. `B_K=I`, `R_in,K=M_K` in the conforming representation;
4. Hermiticity of all three physical channel forms;
5. particle-channel ambipolarity on the frozen hydrogenic state;
6. source-free collisionless skew/adjoint structure of the conservative phase-space advection;
7. the complete F2.1 discrete free-energy balance using the independently reconstructed physical channels;
8. predeclared manufactured/quadrature consistency and K0/K1/K2 structural convergence diagnostics.

No eigenvalues, growth rates, pseudospectra, propagators, Gramians, cumulative channel operators, optimizer directions, angles, performance gaps, parameter scans, GENE runs or finite-time objectives are authorized in F2.6.

Canonical handoff:

`research/master/prompts/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_1.md`

## Rollback / STOP

This file is a new protected post-paper rollback point after the F2.4 input-geometry freeze. F2.3 physical parameters, F2.4 input geometry and F2.5 numerical architecture may not be retuned in response to later operator or spectral behavior.

**STOP — F2.5 INTEGRATED; F2.6 MAY PROCEED ONLY VIA THE COMMITTED HANDOFF.**
