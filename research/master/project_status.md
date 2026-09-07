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
- Fusion historical F2.5 discretization ladder: **FROZEN AUDIT BASELINE**.
- Fusion F2.6 `0_1`: **HOLD / HISTORICAL AUDIT RECORD**.
- Fusion local-B Ion-FLR Erratum 0.1: **STABLE**.
- Fusion F2.6 `0_2`: **FAIL / MASTER-INTEGRATED HISTORICAL DISCRETIZATION FAILURE**.
- Fusion F2.5R ion-FLR quadrature repair: **PASS / MASTER-INTEGRATED / FROZEN**.
- Fusion F2.5R Ion-FLR Quadrature Repair Integration Freeze 0.1: **STABLE — F2.6 0_3 RELEASED**.

## First-paper status

Paper 1 scientific content remains frozen. Draft 0.4 is the scientific-content baseline, not final prose. Submission preparation remains parked by user choice.

## Active post-paper program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

R1 remains the frozen structural-collapse control. The active higher-fidelity lineage remains F2-R.

## Frozen F2-R physical structure

Primary reduced candidate:

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons and reduced collisionless balance

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

The F2.3 CBC-compatible physical point remains unchanged. The continuous admissible input pair remains

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}}.
\]

The controlling local-B ion-FLR convention remains

\[
J_{0i}=J_0\!\left(k_\perp v_\perp/\Omega_i(\theta)\right),
\]

\[
\boxed{b_i(\theta)=(k_\perp\rho_{i0})^2(B_0/B(\theta))^2,\qquad \Gamma_{0i}=I_0(b_i)e^{-b_i}.}
\]

## F2.5R repaired numerical architecture

The historical F2.5 `N_mu=8/12/16` ladder remains an immutable audit baseline. The controlling repaired ion Gauss--Laguerre orders are

\[
\boxed{N_\mu=(16,24,40)\quad\text{for K0/K1/K2}.}
\]

All other F2.5 numerical objects remain unchanged. The repaired ion-state dimensions are

\[
\boxed{N_i=(18176,91584,357120).}
\]

F2.5R selected the first passing orders in the predeclared candidate sequence using only active-node and independent between-node local-B FLR manufactured identities, positive-metric field-block tolerances, positive quadrature weights and Maxwellian moment checks. The selected active-node relative FLR errors are approximately `2.32e-12 / 3.51e-11 / 5.68e-15`; independent envelope errors are approximately `3.04e-12 / 4.01e-11 / 6.44e-15`.

Branch commit `cbfd6ca9a906df7bb34bf6270a24b6c63857f545`; Python CI #405 = `SUCCESS`.

Canonical result:

`research/fusion/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`

MASTER savepoint:

`research/master/fusion_f2_5r_quadrature_repair_integration_freeze_0_1.md`

No spectrum or finite-time effect was inspected.

## Immediate next gate

Fusion F2.6 `0_3` — Discrete Generator / Helmholtz Metric / Physical Channel Reconstruction & Algebraic Balance Qualification on the repaired F2.5R ladder is the only active scientific handoff.

It must use the repaired `N_mu=16/24/40` ladder, reconstruct `A_K`, canonical positive `M_K`, `Q_Gamma,K`, `Q_qi,K`, `Q_qe,K` and quasineutrality from the frozen equations/quadratures, and qualify only structural algebra: full-support FLR identity, quasineutrality, metric positivity/Hermiticity, `B_K=I`, `R_in,K=M_K`, channel Hermiticity, ambipolarity, conservative adjoint structure and the complete F2.1 balance.

Physical channel matrices must remain independently reconstructed from radial gyrocentre flux integrals and may not be defined backwards from the balance identity.

Canonical instruction:

`research/master/prompts/fusion_f2_6_rerun_after_f2_5r_quadrature_repair_0_1.md`

## Planned dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1–F2.4 — **COMPLETE / FROZEN**;
3. historical F2.5 — **FROZEN AUDIT BASELINE**;
4. F2.6 `0_1` HOLD + local-B erratum — **COMPLETE / STABLE**;
5. F2.6 `0_2` — **FAIL / INTEGRATED HISTORICAL RECORD**;
6. F2.5R quadrature repair — **PASS / INTEGRATED / FROZEN**;
7. F2.6 `0_3` algebraic qualification — **READY**;
8. spectral qualification only after F2.6 PASS;
9. later pre-effect finite-time pilot specification/freeze;
10. one-shot finite-time execution only after all preceding gates pass.

## Other branch states

- CORE: `STABLE / PARKED`
- Fusion: `F2.6 0_3 READY`
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

No parallel science is opened. The repaired high-dimensional operator must pass algebraic qualification before any spectrum is viewed. MODES remains conditional on a concrete representation/reduction issue after such qualification; CONT remains premature without an authorized physical parameter family.

## Branch-independent / branch-dependent distinction

Branch-independent CORE methodology remains

\[
\mathfrak C=(A,M,\{Q_\alpha\},B,R_{\rm in}).
\]

Branch-dependent F2 content includes the continuous kinetic state, physical multichannel balance, toroidal geometry, physical point, full reduced input geometry, local-B ion-FLR convention and the repaired structure-preserving numerical ladder. The actually qualified discrete operators remain the F2.6 `0_3` task.

## Protected rollback chain

All first-paper savepoints remain protected. The latest post-paper savepoint is

\[
\boxed{\text{Fusion F2.5R Ion-FLR Quadrature Repair Integration Freeze 0.1}}.
\]

Historical F2.5, F2.6 `0_1`, the ion-FLR erratum, F2.6 `0_2` and the failure-integration freeze remain immutable audit points.

## Decision record

Canonical continuation now reaches **DEC-610** in `research/master/decision_branch_log_addendum_0_13.md`.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_f2_6_rerun_after_f2_5r_quadrature_repair_0_1.md`.

No spectrum, finite-time effect inspection, physical parameter scan, GENE run, F2.3/F2.4 retuning, repaired-ladder change or parallel branch work is authorized before F2.6 `0_3` returns.
