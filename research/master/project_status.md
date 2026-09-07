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
- Fusion historical F2.5 discretization ladder: **PASS / FROZEN AUDIT BASELINE**.
- Fusion F2.6 `0_1`: **HOLD / HISTORICAL AUDIT RECORD**.
- Fusion F2.6 Ion-FLR Convention Clarification / Erratum 0.1: **STABLE**.
- Fusion resumed F2.6 `0_2`: **FAIL / MASTER-INTEGRATED — FROZEN DISCRETIZATION/FLR-RESOLUTION FAILURE**.
- Fusion F2.6 Discrete-Algebra Failure Integration Freeze 0.1: **STABLE — F2.5R RELEASED**.

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

The controlling local-B ion-FLR convention is

\[
J_{0i}=J_0\!\left(k_\perp v_\perp/\Omega_i(\theta)\right),
\]

\[
\boxed{b_i(\theta)=(k_\perp\rho_{i0})^2(B_0/B(\theta))^2,\qquad \Gamma_{0i}=I_0(b_i)e^{-b_i}.}
\]

## F2.6 `0_2` failure

Canonical result:

- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_2.md`
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_2.json`
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_0_2.py`

Branch commit `78db3e41c2cce29d505f13401f6f0878cb40f854`; Python CI #398 = `SUCCESS`.

The local-B erratum fixes the earlier convention conflict, but the historical F2.5 ion magnetic-moment quadrature orders `N_mu=8/12/16` do not resolve the source-consistent FLR identity uniformly over the expanding K0/K1/K2 ballooning support. Maximum relative errors are approximately `3.70e-4 / 1.30e-2 / 3.05e-1`. The positive-Helmholtz versus `g`-form field-block defect also worsens, so the complete F2.1 discrete balance cannot be certified on all historical levels.

This is a **numerical discretization failure**, not evidence against the continuous F2-R model, F2.3 physical point, F2.4 input geometry or local-B FLR convention. No spectrum or finite-time effect was inspected.

MASTER savepoint:

`research/master/fusion_f2_6_discrete_algebra_failure_integration_freeze_0_1.md`

## Immediate next gate

Fusion F2.5R — Ion-FLR Magnetic-Moment Quadrature Repair / Discretization Requalification Gate 0.1 is the only active scientific handoff.

Only the ion Gauss--Laguerre magnetic-moment order `N_mu` is reopened. The representation family itself remains Gauss--Laguerre; all physical parameters, input geometry, ballooning windows/basis, ion Hermite representation, trapped-electron representation, bounce quadrature, quasineutrality treatment and physical channels remain frozen.

F2.5R must select a new monotone K0/K1/K2 `N_mu` ladder from predeclared manufactured local-B FLR and positive-metric structural tolerances only. It may perform a quadrature-order search, but no spectrum/effect calculation. If Gauss--Laguerre is not computationally or structurally defensible, it must return `HOLD` rather than change representation family silently.

Canonical instruction:

`research/master/prompts/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`

## Planned dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1–F2.4 — **COMPLETE / FROZEN**;
3. historical F2.5 — **FROZEN AUDIT BASELINE**;
4. F2.6 `0_1` HOLD + local-B erratum — **COMPLETE / STABLE**;
5. resumed F2.6 `0_2` — **FAIL / INTEGRATED**;
6. F2.5R quadrature repair — **READY**;
7. later F2.6 rerun only after F2.5R PASS and MASTER integration;
8. spectral qualification only after F2.6 PASS;
9. later pre-effect finite-time pilot specification/freeze;
10. one-shot finite-time execution only after all preceding gates pass.

## Other branch states

- CORE: `STABLE / PARKED`
- Fusion: `F2.5R READY`
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

No parallel science is opened. The present failure is a localized numerical quadrature-resolution defect and does not justify MODES or CONT. F2.5R must be frozen before any new discrete algebra or spectrum is viewed.

## Branch-independent / branch-dependent distinction

Branch-independent CORE methodology remains

\[
\mathfrak C=(A,M,\{Q_\alpha\},B,R_{\rm in}).
\]

Branch-dependent F2 content includes the continuous kinetic state, physical multichannel balance, toroidal geometry, physical point, full reduced input geometry, local-B ion-FLR convention and the historical numerical architecture. Only the ion magnetic-moment resolution is currently reopened under F2.5R.

## Protected rollback chain

All first-paper savepoints remain protected. The latest post-paper savepoint is

\[
\boxed{\text{Fusion F2.6 Discrete-Algebra Failure Integration Freeze 0.1}}.
\]

Historical F2.5, F2.6 `0_1`, the ion-FLR erratum and F2.6 `0_2` remain immutable audit points.

## Decision record

Canonical continuation now reaches **DEC-600** in `research/master/decision_branch_log_addendum_0_12.md`.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`.

No spectrum, finite-time effect inspection, physical parameter scan, GENE run, F2.3/F2.4 retuning or parallel branch work is authorized before F2.5R returns.
