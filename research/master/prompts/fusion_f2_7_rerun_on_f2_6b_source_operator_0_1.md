# Fusion F2.7 `0_2` — Numerical / Spectral Qualification on F2.6B Source-Level Operator

**Date:** 2026-09-07  
**Authority:** MASTER  
**Execution branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

## Objective

Determine and qualify the rightmost modal spectral regime of the **new canonical F2.6B source-level operator implementation** before any finite-time propagator or transport-objective calculation is permitted.

This is a modal/spectral gate only.

## Mandatory controlling inputs

Read and preserve:

- `research/master/fusion_f2_6b_source_level_operator_pass_integration_freeze_0_1.md`;
- `research/fusion/fusion_f2_6b_source_level_operator_implementation_requalification_gate_0_1.md`;
- `research/fusion/fusion_f2_6b_operator_0_1.py`;
- `research/fusion/fusion_f2_6b_requalification_0_1.py`;
- `research/fusion/fusion_f2_6b_requalification_diagnostics_0_1.json`;
- `tests/test_fusion_f2_6b_operator_0_1.py`;
- `research/master/fusion_f2_5r_quadrature_repair_integration_freeze_0_1.md`;
- the frozen F2.1–F2.4 integration lineage and local-B ion-FLR erratum;
- the shared MASTER Prompt Handoff Protocol.

Use exactly the committed F2.6B implementation and frozen K0/K1/K2 ladder. Do not reconstruct, modify or replace the operator source for spectral convenience.

## Frozen generalized operator

For each level use the committed public interfaces

- `build_operator(level)`;
- `apply_E(op,x)`;
- `apply_F(op,x)`;
- `solve_E(op,x)`.

The spectral generator is

\[
A_K=E_K^{-1}F_K,
\]

implemented matrix-free by applying `apply_F` followed by `solve_E`.

The total dimensions are

\[
N_{\rm total}(K0,K1,K2)=(18608,\ 93204,\ 361152).
\]

The repaired ion magnetic-moment orders remain

\[
N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.
\]

## Required spectral qualification

For K0/K1/K2:

1. determine the rightmost modal spectrum sufficiently to classify
   \[
   \alpha_K=\max\operatorname{Re}\sigma(A_K),
   \]
   with matrix-free sparse/generalized eigensolver methods appropriate to the committed dimensions;
2. report every retained rightmost Ritz/eigenvalue used for classification, its residual norm, solver tolerance, requested/converged Ritz count and convergence information;
3. repeat the rightmost calculation with at least one independent numerical configuration (for example different Krylov dimension, shift/target strategy or deterministic start vector) and demonstrate that the identified edge is not a single-run artifact;
4. compare the rightmost spectral edge across K0/K1/K2 and state whether the sign classification is robust under the frozen refinement ladder;
5. report conditioning/solve diagnostics relevant to the actual matrix-free generalized problem, including the committed `E_K`/Schur solve and any shift-invert linear systems actually introduced by the eigensolver;
6. if left/right eigenvectors are available without changing the gate scope, report a standard eigenvalue sensitivity/conditioning indicator, but do not reinterpret it as a transport optimizer or nonmodal result;
7. classify exactly one regime:
   - `spectrally stable`: robustly `alpha_K<0` beyond numerical uncertainty;
   - `spectrally unstable`: robustly `alpha_K>0` beyond numerical uncertainty;
   - `marginal/indeterminate`: sign is numerically consistent with zero, solver convergence is insufficient, or refinement does not support a robust classification.

A full dense spectrum is not required and should not be attempted at K1/K2 merely for completeness. The goal is a defensible rightmost-edge classification with residual certification and refinement robustness.

## Historical provenance rule

This F2.7 rerun is **not** a continuation on the unrecoverable historical F2.6 `0_3` source realization. It must state explicitly that all reported spectral quantities belong to the F2.6B source-level implementation frozen in `research/fusion/fusion_f2_6b_operator_0_1.py`.

Historical F2.7 `0_1` remains an immutable HOLD audit record and must not be overwritten.

## No-rescue / no-retuning rule

If the frozen F2.6B point is robustly unstable, report that fact. Do not add damping, collisions, filtering or change the physical point, wavenumber, input geometry or resolution ladder to obtain stability.

If the spectral edge is marginal or not robustly resolved, return HOLD with the exact unresolved numerical object. If a new inconsistency invalidates the already requalified F2.6B operator itself, return FAIL rather than silently modifying it.

## Explicitly forbidden work

Do **not**:

- modify `research/fusion/fusion_f2_6b_operator_0_1.py` to improve spectral behavior;
- construct `exp(A_K t)` or any time propagator;
- construct Gramians, cumulative channel operators or finite-time energy operators;
- compute energy-, particle- or heat-optimal initial conditions;
- compute principal angles, performance gaps, transient amplification curves or horizon dependence;
- scan physical parameters, gradients, wavenumbers, ballooning angles, input subspaces or resolutions outside K0/K1/K2;
- alter F2.1–F2.5R, the local-B FLR convention, physical channels, input geometry or repaired ladder;
- add collisions, damping, hypercollision, diffusion, filters, absorbing layers or metric regularization;
- run GENE or another external GK solver;
- reopen R1, MODES, CONT, CASCADE, Power Grid, Photonics or Paper-1 work.

A local pseudospectral diagnostic may be used only if a specific eigenvalue-convergence ambiguity requires it; if used, keep it narrow and do not turn F2.7 into a nonmodal analysis.

## Required output

Create new versioned outputs; do not overwrite F2.7 `0_1`:

- `research/fusion/fusion_f2_7_numerical_spectral_qualification_gate_0_2.md`;
- machine-readable spectral diagnostics under `research/fusion/` with an F2.7 `0_2` filename;
- any reproducible spectral driver/source required for the calculation, versioned as F2.7 `0_2` and importing the frozen F2.6B operator;
- update `research/fusion/STATUS.md` in the same work package.

Return exactly one of:

- `F2.7 PASS — SPECTRALLY STABLE / NUMERICALLY QUALIFIED — RETURN TO MASTER`;
- `F2.7 PASS — SPECTRALLY UNSTABLE / NUMERICALLY QUALIFIED — RETURN TO MASTER`;
- `F2.7 HOLD — MARGINAL OR SPECTRALLY INDETERMINATE — RETURN TO MASTER`;
- `F2.7 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Expected MASTER decision after return

MASTER must explicitly accept or reject the qualified spectral regime before any finite-time pilot specification. Only after that decision may targeted Fusion literature positioning and/or a pre-effect finite-time pilot freeze be considered.

**STOP / RETURN TO MASTER AFTER F2.7 `0_2`.**
