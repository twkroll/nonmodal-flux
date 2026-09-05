# MASTER Project Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Global scientific savepoints

- CORE Mathematical / Integration / Interpretation freezes: **STABLE**.
- Plasma/D10-ZF Pilot 0.2: **P2-A**, frozen.
- Neuro/CMC Pilot 0.1: **NEURO-STRONG**, frozen.
- Climate-A/Phillips-QG Pilot 0.1: **CLIM-WEAK**, frozen.
- Climate-B/Bickley-jet Pilot 0.1: **CLIM-B-FAIL — resolution robustness failure**, frozen.
- Manuscript Revision 0.4: **COMPLETE — PASS**.
- First Paper Scientific Content Freeze 0.1: **STABLE — SCIENTIFIC CONTENT BASELINE FROZEN / SUBMISSION TRACK PARKED**.
- Fusion R1 structural no-go / literature positioning: **FROZEN / PILOT BLOCKED**.
- Fusion F2.1 two-species local-GK balance: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.2 local magnetic geometry / kinetic conventions: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.3 physical geometry/gradient/wavenumber point: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.4 kinetic input geometry / input cost: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.5 structure-preserving discretization / quadrature specification: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.5 Discretization-Specification Integration Freeze 0.1: **STABLE — F2.6 RELEASED**.

## First-paper status

Paper 1 scientific content remains frozen. Draft 0.4 is the scientific-content baseline, not final prose. Submission preparation remains parked by user choice.

## Active post-paper program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

R1 remains the frozen structural-collapse control. The active higher-fidelity lineage is F2-R.

## Frozen F2-R physical structure

Primary reduced candidate:

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons. Its reduced collisionless balance is

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

Primary geometry is the frozen large-aspect-ratio circular `s-alpha` ballooning-space flux tube. The F2.3 CBC-compatible physical point remains unchanged and may not be retuned.

The continuous admissible input geometry remains

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}}.
\]

## Frozen F2.5 numerical architecture

The numerical representation is frozen as

\[
\boxed{
\text{compact-support ballooning Galerkin/SBP spectral elements}
\times\text{ Hermite--Laguerre ion velocity representation}
+\text{ regularized trapped-electron orbit quadrature}
}
\]

with no artificial damping/filtering, exact finite-ion FLR, algebraic quasineutrality elimination, both ion velocity signs retained and no parity/transport-neutral pruning.

The K0/K1/K2 refinement ladder is fixed before any F2-R spectral or finite-time inspection. The later metric must come directly from the positive Helmholtz functional and satisfy `M_K=M_K^dagger>0` without shifts or clipping. The later physical particle/ion-heat/electron-heat channels must be reconstructed from the frozen radial gyrocentre flux integrals using the same state space and quadratures.

F2.5 branch commit `43de899b547b2ccc1d0c11ecb6788dfce6cb6b47`; Python CI #378 = `SUCCESS`.

Canonical MASTER savepoint:

`research/master/fusion_f2_5_discretization_specification_integration_freeze_0_1.md`

## Immediate next gate

Fusion F2.6 — Discrete Generator / Helmholtz Metric / Physical Channel Reconstruction & Algebraic Balance Qualification Gate 0.1 is the only active scientific handoff.

F2.6 must instantiate exactly K0/K1/K2, construct `A_K`, `M_K`, `Q_Gamma,K`, `Q_qi,K`, `Q_qe,K` and discrete quasineutrality from the already-frozen physical equations/quadratures, and test only structural algebra: quasineutrality, positivity, Hermiticity, input-cost inheritance, ambipolarity, conservative phase-space adjoint structure and the complete F2.1 balance. It may not inspect the spectrum or any finite-time objective.

Canonical instruction:

`research/master/prompts/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_1.md`

## Planned dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1 candidate/balance — **COMPLETE / FROZEN**;
3. F2.2 geometry/conventions — **COMPLETE / FROZEN**;
4. F2.3 physical point — **COMPLETE / FROZEN**;
5. F2.4 kinetic input geometry / input cost — **COMPLETE / FROZEN**;
6. F2.5 discretization / quadrature specification — **COMPLETE / FROZEN**;
7. F2.6 discrete operator/channel algebraic qualification — **READY**;
8. later numerical/free-energy/spectral qualification;
9. later pre-effect finite-time pilot specification/freeze;
10. one-shot finite-time execution only after all preceding gates pass;
11. fully kinetic/GENE-compatible reference validation through separately released gates.

## Other branch states

- CORE: `STABLE / PARKED`
- Fusion: `F2.6 READY`
- Literature: `WAIT`
- MODES: `PARKED / conditional companion`
- CONT: `PARKED`
- CASCADE: `PARKED`
- Neuro: frozen first result; extensions parked
- Climate: A/B frozen; no B repair or third-candidate rescue lineage
- Manuscript/submission: parked
- Power Grids: `PROTECTED`
- Photonics/Waves: `PROTECTED`

## Parallelism decision

No parallel science is opened. F2.6 must establish a physically valid discrete operator/channel algebra before any spectrum is viewed. MODES remains conditional on a concrete representation/reduction issue after the high-dimensional operator is qualified; CONT remains premature without an authorized parameter family.

## Branch-independent / branch-dependent distinction

Branch-independent CORE methodology remains

\[
\mathfrak C=(A,M,\{Q_\alpha\},B,R_{\rm in}).
\]

Branch-dependent F2 content now includes the continuous kinetic state, Helmholtz metric, physical multichannel balance, toroidal geometry, one physical point, full reduced input geometry and a fixed structure-preserving numerical representation/refinement ladder. Actual discrete operators and their algebraic qualification remain the F2.6 task.

## Protected rollback chain

All first-paper savepoints remain protected. The latest post-paper rollback point is

\[
\boxed{\text{Fusion F2.5 Discretization-Specification Integration Freeze 0.1}}.
\]

## Decision record

Canonical continuation now reaches **DEC-580** in `research/master/decision_branch_log_addendum_0_10.md`.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_1.md`.

No spectrum, finite-time effect inspection, parameter scan, GENE run, F2.3/F2.4/F2.5 change or parallel branch work is authorized before F2.6 returns.
