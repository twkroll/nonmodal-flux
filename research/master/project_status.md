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
- Fusion F2.6 `0_3` discrete operator/channel algebraic qualification: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.7 `0_1`: **HOLD / MASTER-INTEGRATED — SPECTRALLY INDETERMINATE BECAUSE CANONICAL EXECUTABLE OPERATOR ARTIFACT IS MISSING**.
- Fusion F2.7 HOLD / Canonical Operator-Artifact Integration Freeze 0.1: **STABLE — F2.6A RELEASED**.

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

F2.6 `0_3` remains the canonical pre-spectral algebraic qualification. Its independently reconstructed physical channels, positive metric, conservative phase-space structure, ambipolarity and complete F2.1 discrete balance remain frozen as PASS.

## F2.7 HOLD

Canonical result:

- `research/fusion/fusion_f2_7_numerical_spectral_qualification_gate_0_1.md`
- `research/fusion/fusion_f2_7_numerical_spectral_qualification_diagnostics_0_1.json`

Branch commit `e4453080cae805a4e50d019975f6722130e88903`; Python CI #419 = `SUCCESS`.

No eigensolver was run. F2.7 reports no Ritz pairs, eigenvalues or spectral abscissa. The repository lacks a versioned executable/serialized artifact sufficient to instantiate the exact already-qualified F2.6 `0_3` maps

\[
E_Kx,\qquad F_Kx,\qquad E_K^{-1}x
\]

on K0/K1/K2 without making new implementation choices. Therefore the spectral regime is currently **indeterminate**, not established stable, unstable or marginal.

MASTER savepoint:

`research/master/fusion_f2_7_hold_operator_artifact_integration_freeze_0_1.md`

## Immediate next gate

The only active scientific handoff is

\[
\boxed{\text{F2.6A — Canonical Matrix-Free Operator Artifact / Reproducibility Freeze 0.1}.}
\]

Its task is only to publish/freeze a versioned executable matrix-free implementation or equivalent serialized factor set for the exact F2.6 `0_3` operator and reproduce the already-frozen structural diagnostics. It may not change F2.1–F2.5R.

If exact equivalence cannot be demonstrated from canonical information, F2.6A must return HOLD rather than introduce a substitute implementation.

Canonical instruction:

`research/master/prompts/fusion_f2_6a_canonical_operator_artifact_reproducibility_gate_0_1.md`

## Planned dependency chain

1. F2.1–F2.4 — **COMPLETE / FROZEN**;
2. historical F2.5/F2.6 failure lineage — **PRESERVED AUDIT RECORDS**;
3. F2.5R quadrature repair — **PASS / FROZEN**;
4. F2.6 `0_3` algebraic qualification — **PASS / FROZEN**;
5. F2.7 `0_1` spectral qualification — **HOLD / INTEGRATED**;
6. F2.6A canonical operator-artifact reproducibility gate — **READY**;
7. F2.7 rerun only after F2.6A PASS + MASTER integration;
8. explicit MASTER spectral-regime acceptance after a qualified F2.7 result;
9. targeted Fusion literature positioning and pre-effect finite-time pilot specification only after regime acceptance;
10. one-shot finite-time execution only after a subsequent pilot freeze.

## Other branch states

- CORE: `STABLE / PARKED`
- Fusion: `F2.6A READY`
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

No parallel science is opened. The missing canonical operator artifact is a localized reproducibility blocker, not a reason to open MODES, CONT or Literature. Fusion remains the only active branch.

## Branch-independent / branch-dependent distinction

Branch-independent CORE methodology remains

\[
\mathfrak C=(A,M,\{Q_\alpha\},B,R_{\rm in}).
\]

Branch-dependent F2 content includes the continuous kinetic state, multichannel balance, toroidal geometry, physical point, full reduced input geometry, local-B ion-FLR convention, repaired numerical ladder and algebraically qualified discrete operator/channel structure. The missing object is the canonical executable realization of that already-qualified discrete operator.

## Protected rollback chain

All first-paper savepoints remain protected. The latest post-paper savepoint is

\[
\boxed{\text{Fusion F2.7 HOLD / Canonical Operator-Artifact Integration Freeze 0.1}}.
\]

All prior F2.5/F2.6/F2.5R savepoints remain immutable audit points.

## Decision record

Canonical continuation now reaches **DEC-630** in `research/master/decision_branch_log_addendum_0_15.md`.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_f2_6a_canonical_operator_artifact_reproducibility_gate_0_1.md`.

No spectrum, finite-time effect inspection, physical parameter scan, GENE run, damping/collision addition, retuning or parallel branch work is authorized before F2.6A returns.
