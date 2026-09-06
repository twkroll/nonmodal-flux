# MASTER Project Status

**Last updated:** 2026-09-06  
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
- Fusion F2.6 `0_1`: **HOLD / MASTER-INTEGRATED AS DIAGNOSTIC RECORD**.
- Fusion F2.6 Ion-FLR Convention Clarification / Erratum 0.1: **STABLE — F2.6 RESUMPTION RELEASED**.

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

The numerical representation remains frozen as

\[
\boxed{
\text{compact-support ballooning Galerkin/SBP spectral elements}
\times\text{ Hermite--Laguerre ion velocity representation}
+\text{ regularized trapped-electron orbit quadrature}
}
\]

with the unchanged predeclared K0/K1/K2 ladder and no artificial damping/filtering. No F2.5 basis, cutoff, quadrature or resolution was changed after F2.6 returned HOLD.

## F2.6 HOLD and ion-FLR erratum

F2.6 `0_1` stopped before any spectrum because the manufactured ion-FLR check exposed an inconsistent pair of conventions: local `J0i` used `Omega_i(theta)`, while the polarization argument had been implemented with the reference `rho_i0=vTi/Omega_i(B0)` without the local field factor.

Historical HOLD record:

- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_1.md`
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_1.json`

F2.6 HOLD commit `ef5a20e728a5a6ca0dfb1cd2cd012f4003a4c0f1`; Python CI #385 = `SUCCESS`.

MASTER resolved the blocker in

`research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`.

The reference benchmark normalization remains

\[
\rho_{i0}=v_{Ti}/\Omega_i(B_0),
\qquad
k_y\rho_{i0}=0.3,
\]

and the local gyroaverage remains

\[
J_{0i}=J_0\!\left(k_\perp v_\perp/\Omega_i(\theta)\right).
\]

The controlling local ion-FLR polarization argument is now

\[
\boxed{
 b_i(\theta)
 =(k_\perp(\theta)\rho_{i0})^2\left(\frac{B_0}{B(\theta)}\right)^2,
\qquad
\Gamma_{0i}=I_0(b_i)e^{-b_i}.
}
\]

This restores the intended Maxwellian relation `Gamma0i=<J0i^2>` while leaving the physical benchmark point and numerical architecture unchanged. The alternative of replacing the local gyroaverage by a reference-`B0` gyroaverage is rejected.

## Immediate next gate

Fusion F2.6 resumes only through

`research/master/prompts/fusion_f2_6_resume_after_ion_flr_erratum_0_1.md`.

The resumed gate must rebuild all affected FLR-dependent discrete objects on the unchanged K0/K1/K2 ladder, create versioned `0_2` result/diagnostic files, and complete the pre-spectral algebraic qualification: quasineutrality, positive Helmholtz metric, input-cost inheritance, physical-channel Hermiticity, ambipolarity, conservative phase-space adjoint structure and the complete F2.1 balance.

No eigenvalue, growth-rate, pseudospectral, propagator, Gramian, optimizer or finite-time quantity is authorized.

## Planned dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1 candidate/balance — **COMPLETE / FROZEN**;
3. F2.2 geometry/conventions — **COMPLETE / FROZEN**;
4. F2.3 physical point — **COMPLETE / FROZEN**;
5. F2.4 kinetic input geometry / input cost — **COMPLETE / FROZEN**;
6. F2.5 discretization / quadrature specification — **COMPLETE / FROZEN**;
7. F2.6 `0_1` algebraic qualification — **HOLD / INTEGRATED**;
8. ion-FLR convention erratum — **COMPLETE / STABLE**;
9. F2.6 corrected `0_2` algebraic qualification — **READY**;
10. numerical/free-energy/spectral qualification only after F2.6 PASS;
11. later pre-effect finite-time pilot specification/freeze;
12. one-shot finite-time execution only after all preceding gates pass;
13. fully kinetic/GENE-compatible reference validation through separately released gates.

## Other branch states

- CORE: `STABLE / PARKED`
- Fusion: `F2.6 RESUMPTION READY`
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

No parallel science is opened. The corrected F2.6 algebraic gate must pass before any spectrum is viewed. MODES remains conditional on a concrete representation/reduction issue after a qualified high-dimensional operator exists; CONT remains premature without an authorized parameter family.

## Branch-independent / branch-dependent distinction

Branch-independent CORE methodology remains

\[
\mathfrak C=(A,M,\{Q_\alpha\},B,R_{\rm in}).
\]

Branch-dependent F2 content includes the continuous kinetic state, Helmholtz metric, physical multichannel balance, toroidal geometry, one physical point, full reduced input geometry, fixed structure-preserving numerical representation and now an explicit local-B ion-FLR convention. Actual qualified discrete operators remain the F2.6 task.

## Protected rollback chain

All first-paper savepoints remain protected. The latest post-paper savepoint is

\[
\boxed{\text{Fusion F2.6 Ion-FLR Convention Clarification / Erratum 0.1}}.
\]

The historical F2.6 HOLD and the F2.5 discretization integration freeze remain preserved audit/rollback points.

## Decision record

Canonical continuation now reaches **DEC-590** in `research/master/decision_branch_log_addendum_0_11.md`.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_f2_6_resume_after_ion_flr_erratum_0_1.md`.

No spectrum, finite-time effect inspection, parameter scan, GENE run, F2.3/F2.4/F2.5 retuning or parallel branch work is authorized before F2.6 returns again.
