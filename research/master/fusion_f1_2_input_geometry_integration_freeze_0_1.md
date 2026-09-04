# Fusion F1.2 Input Geometry / Input-Cost Integration Freeze 0.1

**Date:** 2026-09-04  
**Authority:** MASTER  
**Status:** `STABLE — F1.2 INPUT GEOMETRY FROZEN / CANDIDATE-CONVENTION FREEZE RELEASED`

## Scope

This MASTER freeze integrates only the completed Fusion F1.2 admissible-input geometry / input-cost gate. It performs no finite-time optimization, no parameter or horizon scan, no FLR/GK extension, no new literature search, and no modification of the frozen first-paper content.

## Integrated F1.2 result

Canonical branch result:

`research/fusion/fusion_admissible_input_geometry_input_cost_gate_0_1.md`

Branch verdict:

\[
\boxed{\text{F1.2 PASS — RETURN TO MASTER FOR FUSION CANDIDATE/CONVENTION FREEZE}}
\]

For the already-closed anisotropic-ZLR four-moment R1 tangent state

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad \Phi=\mathcal C_k N,
\]

the physically admissible initial-condition ensemble is the full retained tangent state. The electrostatic relation reconstructs \(\Phi\) from \(N\) and imposes no further linear relation among the four retained state coordinates.

The frozen input geometry and cost are

\[
\boxed{B=I_4,\qquad R_{\rm in}=M_k,\qquad \operatorname{rank}(B)=4.}
\]

Here `B=I_4` means full state-space initial-condition admissibility for the closed tangent model; it is **not** a claim that four independent laboratory actuators exist.

The input cost is the already-frozen positive perturbation free energy,

\[
R_{\rm in}=M_k=M_k^\dagger\succ0.
\]

The instantaneous restricted heat channel is not transport neutral:

\[
B^\dagger Q_{q_i,k}B=Q_{q_i,k},
\]

which for \(k_y\neq0\) remains rank 2 and indefinite with signature `(1,1,2)`. Transport neutrality was not imposed and is not part of the F1.2 physical admissibility decision.

The same `B,R_in` interpretation applies to both the slab and minimal-curvature R1 generators because they share the same closed state coordinates, electrostatic closure, free-energy metric and physical heat-flux channel.

## Freeze classification

The following are now `STABLE` for the R1 pre-effect lineage:

- full four-dimensional closed tangent-state initial-condition admissibility;
- `B=I_4` in the frozen state ordering;
- `R_in=M_k` as the fixed-free-energy input cost;
- `rank(B)=4`;
- the distinction between state-space admissibility and experimental actuator realizability;
- non-neutral, rank-2 indefinite instantaneous restricted heat-channel geometry;
- basis covariance under invertible reparametrization of the same admissible state space;
- common applicability to slab and minimal-curvature R1.

No finite-time heat/energy optimum, optimizer angle, performance gap, horizon dependence, parameter dependence or effect magnitude is frozen or authorized by this file.

## Reproducibility

F1.2 branch commit:

`8d555475577e77e93f9646df60343a34f0503525`

Python CI #316 = `SUCCESS`.

## Next gate released

The next authorized scientific task is **Fusion F1.3 — Candidate / Convention Freeze 0.1**.

Its purpose is to freeze one reduced Fusion candidate using only physical and structural criteria before any finite-time objective-separation inspection. The minimal-curvature anisotropic-ZLR R1 branch is the intended primary candidate if the frozen derivation chain remains internally consistent; the slab branch is an analytic/limiting control and must not be promoted or demoted based on a later effect.

The gate must freeze, at minimum, the exact state ordering and normalization, electrostatic closure, generator convention, free-energy metric, heat-flux operator, input geometry/cost, equilibrium-gradient and curvature conventions, dissipation/closure choice, time normalization, and one physical parameter point chosen without effect inspection.

Canonical handoff:

`research/master/prompts/fusion_candidate_convention_freeze_0_1.md`

## Rollback and STOP

This file is a new post-paper rollback point after the B5.5 Integration Freeze and F1.2 branch result. It does not modify any first-paper savepoint.

If F1.3 cannot freeze a unique physically defensible candidate/convention without effect-oriented choices, return to MASTER with `HOLD` or `FAIL`; do not open numerical qualification or finite-time optimization.

**STOP — F1.2 INTEGRATED; F1.3 MAY PROCEED ONLY VIA THE COMMITTED HANDOFF.**