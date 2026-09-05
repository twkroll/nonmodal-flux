# Fusion F2.3 Physical-Parameter Integration Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER  
**Status:** `STABLE — F2.3 PHYSICAL POINT FROZEN / F2.4 KINETIC INPUT-GEOMETRY GATE RELEASED`

## Scope

This MASTER freeze integrates only the completed `Fusion F2.3 — Physical Geometry / Gradient / Wavenumber Parameter Freeze 0.1`. It performs no phase-space discretization, no kinetic input optimization, no spectrum calculation, no GENE execution, no finite-time propagator/Gramian construction and no objective-separation inspection.

Canonical branch result:

`research/fusion/fusion_f2_3_physical_parameter_freeze_0_1.md`

Branch verdict:

\[
\boxed{\text{F2.3 PASS — PHYSICAL GEOMETRY/GRADIENT/WAVENUMBER POINT FROZEN — RETURN TO MASTER}}
\]

Branch commit:

`fcd012219427ce0243151d2cfb7796236778d966`

Python CI #362 = `SUCCESS`.

## Frozen single physical point

The primary F2-R candidate remains

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

in the already-frozen large-aspect-ratio circular `s-alpha` ballooning-space geometry.

The single pre-effect CBC-compatible point is frozen as

\[
\boxed{
\begin{gathered}
R_0/a=2.77778,
\quad r_0/a=0.5,
\quad \epsilon=0.18,
\quad q=1.4,
\quad \hat s=0.8,
\quad \alpha_{\rm MHD}=0,\\
Z_i=+1,
\quad Z_e=-1,
\quad m_i/m_e=3672,
\quad T_i/T_e=1,
\quad n_i=n_e,\\
a/L_n=0.8,
\quad a/L_{T_i}=a/L_{T_e}=2.49,\\
k_y\rho_i=+0.3,
\quad \theta_0=0,
\quad k_{x0}=0.
\end{gathered}
}
\]

Equivalent major-radius gradients are

\[
R_0/L_n=2.222224,
\qquad
R_0/L_{T_i}=R_0/L_{T_e}=6.9166722.
\]

The normalization is frozen as

\[
v_{Ti}=\sqrt{T_i/m_i},
\qquad
\rho_i=v_{Ti}/\Omega_i,
\qquad
\tau_{\rm ref}=R_0/v_{Ti}.
\]

No alternate parameter point was inspected for stability, nonnormality, transport magnitude or objective separation.

## Physical ordering consequences retained

At the frozen point all three F2.1 source coefficients are nonzero:

\[
G_\Gamma\neq0,
\qquad
G_{T,i}\neq0,
\qquad
G_{T,e}\neq0.
\]

This preserves the multi-channel balance possibility established in F2.1, but it does not prove linear independence of any later discrete channel matrices and does not imply optimizer separation.

The trapped region is determined by the frozen geometry rather than tuned independently. With `epsilon=0.18` and `lambda_hat=lambda B0`,

\[
0.82<\widehat\lambda<1.18,
\]

and the local outboard-midplane trapped pitch fraction is approximately `0.5523`.

With `m_i/m_e=3672` and `T_i=T_e`,

\[
\rho_e/\rho_i\approx0.01650,
\qquad
k_\perp(0)\rho_e\approx0.00495,
\]

so the reduced-electron `k_perp rho_e << 1` ordering is plausible at the ballooning centre. The later discretization/qualification stage must still verify that ordering on the retained ballooning support.

## Freeze boundaries

F2.3 freezes only the physical point and normalization. The following remain unresolved and block numerical execution:

1. kinetic admissible initial-condition map `B`;
2. physical input-cost metric `R_in`;
3. ballooning-line and velocity-space discretization, quadrature and separatrix treatment;
4. discrete quasineutrality reconstruction;
5. discrete physical particle/ion-heat/electron-heat channel operators;
6. structure-preserving free-energy/balance qualification and complete spectrum;
7. later finite-time pilot specification/freeze;
8. fully kinetic collisional reference and GENE-compatible mapping details.

No spectrum, growth rate, propagator, cumulative objective, optimizer, angle or performance gap has yet been inspected for F2-R.

## MASTER gate-order decision

The next gate must be the kinetic admissible-input geometry / input-cost freeze before phase-space discretization.

Reason: the continuous state space and positive Helmholtz metric are already frozen, while a structure-preserving discretization must know which physical perturbation subspace is admissible and what quantity defines the fixed initial budget. Freezing discretization first could silently bake numerical basis restrictions into `B` or `R_in`.

The next gate may decide whether the full finite-free-energy kinetic tangent space is admissible or whether physical constraints require a proper subspace. It must derive any restriction from the already-frozen gyrokinetic state/quasineutrality structure, not from expected finite-time effect size. It must also decide whether `R_in` is the Helmholtz free-energy metric restricted to the admissible input space or another independently justified physical preparation cost.

## Next task released

**Fusion F2.4 — Kinetic Admissible Input Geometry / Input-Cost Freeze 0.1**

Canonical handoff:

`research/master/prompts/fusion_f2_4_kinetic_input_geometry_input_cost_freeze_0_1.md`

Execute only in `60 – FUSION – Gyrofluid/Gyrokinetic Transport` via bare `GO` under the shared Prompt Handoff Protocol.

## Rollback / STOP

This file is a new protected post-paper rollback point after the F2.2 geometry/convention freeze.

R1 remains a frozen structural no-go control. F2.3 may not be retuned after any later spectral or finite-time inspection.

**STOP — F2.3 INTEGRATED; F2.4 MAY PROCEED ONLY VIA THE COMMITTED HANDOFF.**
