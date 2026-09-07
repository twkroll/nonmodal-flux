# MASTER Project Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Global scientific savepoints

- CORE Mathematical / Integration / Interpretation freezes: **STABLE**.
- Plasma/D10-ZF Pilot 0.2: **P2-A**, frozen.
- Neuro/CMC Pilot 0.1: **NEURO-STRONG**, frozen.
- Climate-A/Phillips-QG Pilot 0.1: **CLIM-WEAK**, frozen.
- Climate-B/Bickley-jet Pilot 0.1: **CLIM-B-FAIL**, frozen.
- Manuscript Revision 0.4: **COMPLETE — PASS**.
- First Paper Scientific Content Freeze 0.1: **STABLE — SCIENTIFIC CONTENT BASELINE FROZEN / SUBMISSION TRACK PARKED**.
- Fusion R1 structural no-go / literature positioning: **FROZEN / PILOT BLOCKED**.
- Fusion F2.1–F2.4: **PASS / INTEGRATED / FROZEN**.
- Historical F2.5/F2.6 `0_1`/`0_2`: **IMMUTABLE AUDIT RECORDS**.
- Fusion local-B Ion-FLR Erratum 0.1: **STABLE**.
- Fusion F2.5R ion-FLR quadrature repair: **PASS / INTEGRATED / FROZEN**.
- Historical Fusion F2.6 `0_3`: **PASS / INTEGRATED / QUALIFIED AUDIT RESULT**.
- Historical Fusion F2.7 `0_1`: **HOLD / INTEGRATED — SPECTRALLY INDETERMINATE FROM MISSING EXECUTABLE PROVENANCE**.
- Fusion F2.6A provenance recovery: **HOLD / INTEGRATED**.
- Fusion F2.6B source-level operator implementation / algebraic requalification: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.6B Source-Level Operator PASS Integration Freeze 0.1: **STABLE — F2.7 `0_2` RELEASED**.

## First-paper status

Paper 1 scientific content remains frozen. Draft 0.4 is the scientific-content baseline, not final prose. Submission preparation remains parked by user choice.

## Active post-paper program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

The active higher-fidelity lineage remains F2-R.

## Frozen F2-R structure

The primary reduced candidate remains finite-ion-FLR electrostatic local-GK ions plus collisionless bounce-averaged trapped electrons with leading adiabatic passing electrons and

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

The F2.3 physical point, F2.4 input pair, local-B ion-FLR convention and repaired magnetic-moment ladder remain frozen:

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}},
\]

\[
\boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.}
\]

All other F2.5/F2.5R objects remain frozen.

## Canonical executable F2.6B realization

F2.6B provides the new provenance-clean source-level realization for all downstream numerical work.

Canonical files:

- `research/fusion/fusion_f2_6b_source_level_operator_implementation_requalification_gate_0_1.md`;
- `research/fusion/fusion_f2_6b_operator_0_1.py`;
- `research/fusion/fusion_f2_6b_requalification_0_1.py`;
- `research/fusion/fusion_f2_6b_requalification_diagnostics_0_1.json`;
- `tests/test_fusion_f2_6b_operator_0_1.py`.

Branch commit `83f004412183d43a1653d3a3a2f9ad104482de7d`; Python CI #433 = `SUCCESS`.

The committed public interfaces are `build_operator(level)`, `apply_E(op,x)`, `apply_F(op,x)`, `solve_E(op,x)`. The frozen NumPy C-order state is ion `h_i[theta,u,zeta]` followed by trapped-electron `h_e[well,energy,lambda]` with

\[
\boxed{N_{\rm total}(K0,K1,K2)=(18608,\ 93204,\ 361152).}
\]

The complete pre-spectral algebraic requalification passes on K0/K1/K2, including full-support FLR, quasineutrality, positive canonical metric, conservative adjoint/skew structure, independently constructed physical-channel Hermiticity, ambipolarity and complete F2.1 balance. Maximum complete-balance relative residuals are approximately

\[
\boxed{1.29\times10^{-13},\qquad5.64\times10^{-13},\qquad5.87\times10^{-13}.}
\]

No spectrum or finite-time quantity was inspected.

MASTER savepoint:

`research/master/fusion_f2_6b_source_level_operator_pass_integration_freeze_0_1.md`

Historical F2.6 `0_3`, F2.6A and F2.7 `0_1` remain preserved audit records. Downstream work must use F2.6B and may not claim source identity with historical F2.6 `0_3`.

## Immediate next gate

The only active scientific handoff is

\[
\boxed{\text{F2.7 `0_2` — Numerical / Spectral Qualification on the F2.6B Source-Level Operator}.}
\]

It must use the committed F2.6B operator directly and determine the rightmost spectral edge / spectral abscissa on K0/K1/K2 with residual certification, independent numerical repetition and refinement robustness.

A robustly unstable result must be reported without damping or retuning. A marginal or unresolved edge returns HOLD. No finite-time propagator or objective calculation is authorized in F2.7 `0_2`.

Canonical instruction:

`research/master/prompts/fusion_f2_7_rerun_on_f2_6b_source_operator_0_1.md`

## Planned dependency chain

1. F2.1–F2.4 — **COMPLETE / FROZEN**;
2. historical F2.5/F2.6 failure lineage — **PRESERVED AUDIT RECORDS**;
3. F2.5R quadrature repair — **PASS / FROZEN**;
4. historical F2.6 `0_3` algebraic qualification — **PASS / QUALIFIED AUDIT RESULT**;
5. historical F2.7 `0_1` spectral qualification — **HOLD / INTEGRATED**;
6. F2.6A provenance recovery — **HOLD / INTEGRATED**;
7. F2.6B source-level implementation + algebraic requalification — **PASS / INTEGRATED / FROZEN**;
8. F2.7 `0_2` numerical/spectral qualification on F2.6B — **READY**;
9. explicit MASTER spectral-regime acceptance after F2.7 `0_2`;
10. targeted Fusion literature positioning and pre-effect finite-time pilot specification only after regime acceptance;
11. one-shot finite-time execution only after a subsequent pilot freeze.

## Other branch states

- CORE: `STABLE / PARKED`
- Fusion: `F2.7 0_2 READY`
- Literature: `WAIT`
- MODES: `PARKED / conditional companion`
- CONT: `PARKED`
- CASCADE: `PARKED`
- Neuro extensions: parked
- Climate extensions: parked
- Manuscript/submission: parked
- Power Grids: `PROTECTED`
- Photonics/Waves: `PROTECTED`

## Parallelism decision

No parallel science is opened. Fusion remains the sole active branch. MODES remains conditional on a concrete representation/reduction issue; CONT remains premature without an authorized physical parameter family.

## Branch-independent / branch-dependent distinction

Branch-independent CORE methodology remains

\[
\mathfrak C=(A,M,\{Q_\alpha\},B,R_{\rm in}).
\]

Branch-dependent F2 content now includes the continuous kinetic state, multichannel balance, toroidal geometry, physical point, full reduced input geometry, local-B ion-FLR convention, repaired numerical ladder and a provenance-clean algebraically qualified source-level discrete operator implementation. The modal regime itself remains the F2.7 `0_2` task.

## Protected rollback chain

All first-paper savepoints remain protected. The latest post-paper savepoint is

\[
\boxed{\text{Fusion F2.6B Source-Level Operator PASS Integration Freeze 0.1}}.
\]

F2.6A HOLD, F2.7 `0_1` HOLD, historical F2.6 `0_3`, F2.5R and all prior F2.5/F2.6 records remain immutable audit points.

## Decision record

Canonical continuation now reaches **DEC-650** in `research/master/decision_branch_log_addendum_0_17.md`.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_f2_7_rerun_on_f2_6b_source_operator_0_1.md`.

No finite-time effect inspection, physical parameter scan, GENE run, damping/collision addition, upstream retuning or parallel branch work is authorized before F2.7 `0_2` returns.
