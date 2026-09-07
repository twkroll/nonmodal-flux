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
- Fusion historical F2.5 and F2.6 `0_1`/`0_2`: **IMMUTABLE AUDIT BASELINE**.
- Fusion local-B Ion-FLR Erratum 0.1: **STABLE**.
- Fusion F2.5R ion-FLR quadrature repair: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.6 `0_3` discrete operator/channel algebraic qualification: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.6 Discrete-Algebra PASS Integration Freeze 0.1: **STABLE — F2.7 RELEASED**.

## First-paper status

Paper 1 scientific content remains frozen. Draft 0.4 is the scientific-content baseline, not final prose. Submission preparation remains parked by user choice.

## Active post-paper program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

R1 remains the frozen structural-collapse control. The active higher-fidelity lineage remains F2-R.

## Frozen F2-R structure

Primary reduced candidate:

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons and reduced collisionless balance

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

The F2.3 CBC-compatible physical point and F2.4 input pair remain frozen:

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}}.
\]

The controlling local-B ion-FLR convention remains

\[
J_{0i}=J_0\!\left(k_\perp v_\perp/\Omega_i(\theta)\right),
\qquad
\boxed{b_i(\theta)=(k_\perp\rho_{i0})^2(B_0/B(\theta))^2,\quad \Gamma_{0i}=I_0(b_i)e^{-b_i}.}
\]

The controlling repaired magnetic-moment orders are

\[
\boxed{N_\mu=(16,24,40)\quad\text{for K0/K1/K2}.}
\]

All other F2.5 numerical objects remain unchanged.

## F2.6 0_3 qualified discrete algebra

Canonical result:

- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_3.md`
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_3.json`

Branch commit `4db62c37d3465726be061dc7b49cbc3a81d87a55`; Python CI #412 = `SUCCESS`.

The repaired full-support FLR identity, quasineutrality, canonical positive Helmholtz metric, conservative weak/SBP phase-space structure, independently reconstructed particle/ion-heat/trapped-electron-heat channels, ambipolarity and the complete F2.1 discrete free-energy balance all qualify on K0/K1/K2. The maximum reported complete-balance relative residuals are approximately `1.92e-14 / 3.15e-13 / 1.61e-13`.

No spectrum or finite-time quantity was inspected in F2.6 `0_3`.

MASTER savepoint:

`research/master/fusion_f2_6_discrete_algebra_pass_integration_freeze_0_1.md`

## Immediate next gate

Fusion F2.7 — Numerical / Spectral Qualification Gate 0.1 is the only active scientific handoff.

It may determine the rightmost spectral edge and spectral abscissa of the frozen repaired K0/K1/K2 operators, with residual certification, independent eigensolver repetition and refinement-robustness diagnostics. It must classify the frozen point as spectrally stable, unstable or marginal/indeterminate without changing the point or adding damping.

A full dense spectrum at K1/K2 is not required. A robust rightmost-spectrum classification is required.

F2.7 may not construct propagators, Gramians, cumulative objectives, transport optimizers, principal angles, performance gaps or horizon scans.

Canonical instruction:

`research/master/prompts/fusion_f2_7_numerical_spectral_qualification_gate_0_1.md`

## Planned dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1–F2.4 — **COMPLETE / FROZEN**;
3. historical F2.5/F2.6 failure lineage — **PRESERVED AUDIT RECORDS**;
4. F2.5R quadrature repair — **PASS / FROZEN**;
5. F2.6 `0_3` algebraic qualification — **PASS / FROZEN**;
6. F2.7 numerical/spectral qualification — **READY**;
7. explicit MASTER spectral-regime acceptance after F2.7;
8. targeted Fusion literature/positioning audit and pre-effect finite-time pilot specification only after regime acceptance;
9. one-shot finite-time execution only after a subsequent pilot freeze.

## Other branch states

- CORE: `STABLE / PARKED`
- Fusion: `F2.7 READY`
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

No parallel science is opened. F2.7 is the sole active dependency. MODES remains conditional on a concrete representation/reduction issue; CONT remains premature without an authorized physical parameter family.

## Branch-independent / branch-dependent distinction

Branch-independent CORE methodology remains

\[
\mathfrak C=(A,M,\{Q_\alpha\},B,R_{\rm in}).
\]

Branch-dependent F2 content now includes the continuous kinetic state, multichannel balance, toroidal geometry, physical point, full reduced input geometry, local-B ion-FLR convention, repaired numerical ladder and an algebraically qualified discrete operator/channel representation. The modal regime itself remains the F2.7 task.

## Protected rollback chain

All first-paper savepoints remain protected. The latest post-paper savepoint is

\[
\boxed{\text{Fusion F2.6 Discrete-Algebra PASS Integration Freeze 0.1}}.
\]

Historical F2.5/F2.6 and F2.5R records remain immutable audit points.

## Decision record

Canonical continuation now reaches **DEC-620** in `research/master/decision_branch_log_addendum_0_14.md`.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_f2_7_numerical_spectral_qualification_gate_0_1.md`.

No finite-time effect inspection, physical parameter scan, GENE run, damping/collision addition, F2.3/F2.4/F2.5R retuning or parallel branch work is authorized before F2.7 returns.
