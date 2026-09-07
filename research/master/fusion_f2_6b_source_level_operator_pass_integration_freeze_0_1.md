# Fusion F2.6B Source-Level Operator PASS Integration Freeze 0.1

**Date:** 2026-09-07  
**Authority:** MASTER  
**Status:** `STABLE — F2.6B PASS INTEGRATED / SOURCE-LEVEL OPERATOR FROZEN / F2.7 0_2 RELEASED`

## Scope

This freeze integrates only the completed

`Fusion F2.6B — Source-Level Matrix-Free Operator Implementation Freeze / Algebraic Requalification Gate 0.1`.

Canonical branch result:

`research/fusion/fusion_f2_6b_source_level_operator_implementation_requalification_gate_0_1.md`

Canonical executable operator:

`research/fusion/fusion_f2_6b_operator_0_1.py`

Canonical requalification driver:

`research/fusion/fusion_f2_6b_requalification_0_1.py`

Machine-readable diagnostics:

`research/fusion/fusion_f2_6b_requalification_diagnostics_0_1.json`

Focused regression test:

`tests/test_fusion_f2_6b_operator_0_1.py`

Branch verdict:

\[
\boxed{\text{F2.6B PASS — SOURCE-LEVEL MATRIX-FREE OPERATOR IMPLEMENTATION FROZEN / ALGEBRA REQUALIFIED — RETURN TO MASTER}.}
\]

Branch commit:

`83f004412183d43a1653d3a3a2f9ad104482de7d`

Python CI #433 = `SUCCESS`.

## Provenance-clean implementation freeze

F2.6B is a **new versioned executable realization** of the already-frozen F2-R model and numerical architecture. It does not claim source identity with the historical F2.6 `0_3` realization whose exact source provenance could not be recovered.

The public generalized-operator interface is frozen as

- `build_operator(level)`;
- `apply_E(op,x)`;
- `apply_F(op,x)`;
- `solve_E(op,x)`.

The state layout is frozen in NumPy C-order as ion `h_i[theta,u,zeta]` followed by trapped-electron `h_e[well,energy,lambda]`.

The total state dimensions are

\[
\boxed{N_{\rm total}(K0,K1,K2)=(18608,\ 93204,\ 361152).}
\]

The repaired magnetic-moment ladder remains unchanged:

\[
\boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.}
\]

All F2.1–F2.5R physical and numerical objects remain frozen.

## Algebraic requalification integrated

The source-level implementation passes the complete pre-spectral F2.6 qualification on K0/K1/K2:

- full-support local-`B` ion-FLR identity;
- positive phase-space weights and Maxwellian/orbit checks;
- quasineutrality and exact Woodbury/Schur `solve_E` consistency;
- canonical Hermitian positive Helmholtz metric;
- `B_K=I`, `R_in,K=M_K`;
- ion streaming/mirror and complete conservative phase-space skew/adjoint structure;
- independently constructed Hermitian particle/ion-heat/trapped-electron-heat channels;
- hydrogenic particle ambipolarity;
- complete F2.1 discrete free-energy balance.

The complete-balance maximum relative residuals are

\[
\boxed{1.29\times10^{-13},\qquad5.64\times10^{-13},\qquad5.87\times10^{-13}}
\]

for K0/K1/K2.

A fixed manufactured state gives

\[
2W_K=8.5835647932,\quad8.5972174967,\quad8.6039815033,
\]

with decreasing successive relative changes.

The diagnostics include deterministic seeds, tolerances, level metadata and SHA-256 regression hashes for level-defining numerical arrays. No spectrum or finite-time quantity entered the implementation or requalification.

## Historical lineage boundary

Historical F2.6 `0_3` remains a qualified algebraic audit result. F2.6A remains the factual HOLD establishing that exact source identity with that historical realization cannot be proven. F2.7 `0_1` remains the historical spectral HOLD caused by that provenance gap.

F2.6B supersedes neither the historical scientific record nor its audit meaning; it provides the **new canonical executable realization for all downstream numerical work**.

No downstream calculation may claim to use the unrecoverable historical F2.6 `0_3` source realization. Future spectral and finite-time work must use the F2.6B source-level implementation unless MASTER explicitly opens a new version.

## MASTER consequence: F2.7 0_2 released

MASTER now releases a new versioned spectral qualification:

\[
\boxed{\text{F2.7 `0_2` — Numerical / Spectral Qualification on the F2.6B Source-Level Operator}.}
\]

F2.7 `0_2` must import/use the committed F2.6B operator directly and determine the rightmost modal spectral edge on K0/K1/K2 with residual certification, independent eigensolver repetition and refinement robustness.

A robustly unstable frozen point must be reported factually and may not be rescued by damping, collisions or parameter retuning. A marginal or numerically unresolved spectral edge returns HOLD. MASTER must explicitly accept the resulting spectral regime before any finite-time pilot specification.

F2.7 `0_2` remains strictly modal/spectral. It may not construct propagators, Gramians, cumulative objectives, transport optimizers, principal angles, performance gaps or horizon curves.

Canonical handoff:

`research/master/prompts/fusion_f2_7_rerun_on_f2_6b_source_operator_0_1.md`

## Parallelism / rollback / STOP

This integration freeze is a new protected post-paper rollback point. F2.6A HOLD, F2.7 `0_1` HOLD, historical F2.6 `0_3`, F2.5R and the earlier F2.5/F2.6 audit lineage remain preserved.

Fusion remains the only active scientific branch. Literature, MODES, CONT, CASCADE and CORE 0.2 remain parked; Power Grid and Photonics/Waves remain protected; Paper-1 submission remains parked.

**STOP — F2.6B SOURCE-LEVEL OPERATOR FROZEN / F2.7 `0_2` MAY PROCEED ONLY THROUGH THE COMMITTED HANDOFF.**
