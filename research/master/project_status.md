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
- Fusion F2.6 `0_3` discrete operator/channel algebraic qualification: **PASS / INTEGRATED / HISTORICAL QUALIFIED RESULT**.
- Fusion F2.7 `0_1`: **HOLD / MASTER-INTEGRATED — SPECTRALLY INDETERMINATE**.
- Fusion F2.6A exact operator-artifact reproducibility gate: **HOLD / MASTER-INTEGRATED — EXACT HISTORICAL OPERATOR EQUIVALENCE NOT ESTABLISHED**.
- Fusion F2.6A Reproducibility HOLD Integration Freeze 0.1: **STABLE — F2.6B RELEASED**.

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

## Historical F2.6 `0_3` algebraic qualification

Canonical result:

- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_3.md`
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_3.json`

Branch commit `4db62c37d3465726be061dc7b49cbc3a81d87a55`; Python CI #412 = `SUCCESS`.

Its independently reconstructed physical channels, positive metric, conservative phase-space structure, ambipolarity and complete F2.1 discrete balance remain qualified historical results. The maximum reported complete-balance relative residuals remain approximately `1.92e-14 / 3.15e-13 / 1.61e-13`.

No F2.6 `0_3` conclusion is revoked by later reproducibility work.

## F2.7 / F2.6A provenance blocker

F2.7 `0_1` ran no eigensolver and remains spectrally indeterminate because the historical qualified operator is not available as a uniquely identified executable/serialized artifact.

F2.6A then audited the canonical repository and CI provenance. Canonical result:

- `research/fusion/fusion_f2_6a_canonical_operator_artifact_reproducibility_gate_0_1.md`
- `research/fusion/fusion_f2_6a_canonical_operator_artifact_reproducibility_manifest_0_1.json`

Branch commit `1ac71cd2ad0d5e9c7388c5b21229629484323aa2`; Python CI #426 = `SUCCESS`.

F2.6A confirms that the report/diagnostics do not uniquely identify the exact coefficient-level maps `E_K`, `F_K`, `E_K^{-1}`. The F2.6 `0_3` CI run published no artifacts, and no original source builder or exact factor archive is canonically recoverable. Therefore F2.6A correctly refused to create a substitute implementation and returned HOLD.

MASTER savepoint:

`research/master/fusion_f2_6a_reproducibility_hold_integration_freeze_0_1.md`

## Immediate next gate

The only active scientific handoff is

\[
\boxed{\text{F2.6B — Source-Level Matrix-Free Operator Implementation Freeze / Algebraic Requalification Gate 0.1}.}
\]

F2.6B must create a **new versioned** source-level implementation of the already-frozen F2-R numerical model, explicitly freeze all coefficient-level choices previously left implicit, expose deterministic `apply_E/apply_F/solve_E` interfaces, and rerun the complete F2.6 pre-spectral algebraic qualification on K0/K1/K2.

It may not claim exact historical source identity with F2.6 `0_3`. It must preserve F2.1–F2.5R, including the repaired `N_mu=16/24/40` ladder, physical channel definitions, geometry, input pair and representation family.

Canonical instruction:

`research/master/prompts/fusion_f2_6b_source_level_operator_implementation_requalification_gate_0_1.md`

## Planned dependency chain

1. F2.1–F2.4 — **COMPLETE / FROZEN**;
2. historical F2.5/F2.6 failure lineage — **PRESERVED AUDIT RECORDS**;
3. F2.5R quadrature repair — **PASS / FROZEN**;
4. F2.6 `0_3` algebraic qualification — **PASS / HISTORICAL QUALIFIED RESULT**;
5. F2.7 `0_1` spectral qualification — **HOLD / INTEGRATED**;
6. F2.6A exact-artifact reproducibility — **HOLD / INTEGRATED**;
7. F2.6B source-level implementation freeze + algebraic requalification — **READY**;
8. new versioned F2.7 rerun only after F2.6B PASS + MASTER integration;
9. explicit MASTER spectral-regime acceptance after a qualified F2.7 result;
10. targeted Fusion literature positioning and pre-effect finite-time pilot specification only after regime acceptance;
11. one-shot finite-time execution only after a subsequent pilot freeze.

## Other branch states

- CORE: `STABLE / PARKED`
- Fusion: `F2.6B READY`
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

No parallel science is opened. The present blocker is source-level numerical provenance/reproducibility. It does not justify MODES, CONT or Literature. Fusion remains the sole active branch.

## Branch-independent / branch-dependent distinction

Branch-independent CORE methodology remains

\[
\mathfrak C=(A,M,\{Q_\alpha\},B,R_{\rm in}).
\]

Branch-dependent F2 content includes the continuous kinetic state, multichannel balance, toroidal geometry, physical point, input geometry, local-B ion-FLR convention, repaired numerical ladder and historically qualified algebraic structure. The active missing object is a canonical **new versioned source-level executable implementation** of that frozen numerical model, followed by algebraic requalification.

## Protected rollback chain

All first-paper savepoints remain protected. The latest post-paper savepoint is

\[
\boxed{\text{Fusion F2.6A Reproducibility HOLD Integration Freeze 0.1}}.
\]

F2.7 HOLD, F2.6 `0_3`, F2.5R and all prior F2.5/F2.6 records remain immutable audit points.

## Decision record

Canonical continuation now reaches **DEC-640** in `research/master/decision_branch_log_addendum_0_16.md`.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_f2_6b_source_level_operator_implementation_requalification_gate_0_1.md`.

No spectrum, finite-time effect inspection, physical parameter scan, GENE run, damping/collision addition, retuning or parallel branch work is authorized before F2.6B returns.
