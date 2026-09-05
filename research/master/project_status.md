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
- Fusion R1 structural no-go and literature positioning: **FROZEN / PILOT BLOCKED**.
- Fusion F2.1 two-species local-GK balance: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.2 local magnetic-geometry / kinetic conventions: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.3 physical geometry/gradient/wavenumber point: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.3 Physical-Parameter Integration Freeze 0.1: **STABLE — F2.4 RELEASED**.

## First-paper status

Paper 1 scientific content remains frozen. Draft 0.4 is the scientific-content baseline, not final prose. Submission preparation remains parked by user choice.

## Active post-paper program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

R1 remains the frozen structural-collapse control. The active higher-fidelity lineage is F2-R.

## Frozen F2-R model

Primary reduced candidate:

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons.

The positive Helmholtz free energy defines the continuous metric `M_F2`, and the reduced balance is

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

The R1 affine redundancy is not structurally forced in F2-R, but no finite-time objective separation has been inspected.

## Frozen F2.2 geometry

Primary family:

\[
\boxed{\text{large-aspect-ratio circular local tokamak}+\hat s\text{-}\alpha_{\rm MHD}\text{ ballooning-space flux tube}}
\]

with the source-consistent Clebsch/Fourier, shear/twist, magnetic-drift, trapped/passing, bounce-average, finite-ion-FLR, reduced-electron and no-parity conventions frozen.

## Frozen F2.3 single physical point

\[
\boxed{
\begin{gathered}
R_0/a=2.77778,
\quad r_0/a=0.5,
\quad \epsilon=0.18,
\quad q=1.4,
\quad \hat s=0.8,
\quad \alpha_{\rm MHD}=0,\\
Z_i=+1,
\quad Z_e=-1,
\quad m_i/m_e=3672,
\quad T_i/T_e=1,
\quad n_i=n_e,\\
a/L_n=0.8,
\quad a/L_{T_i}=a/L_{T_e}=2.49,\\
k_y\rho_i=+0.3,
\quad \theta_0=0,
\quad k_{x0}=0.
\end{gathered}
}
\]

Normalization: `vTi=sqrt(Ti/mi)`, `rho_i=vTi/Omega_i`, `tau_ref=R0/vTi`. The single point was frozen without parameter scans or spectral/finite-time inspection.

F2.3 branch commit `fcd012219427ce0243151d2cfb7796236778d966`; Python CI #362 = `SUCCESS`.

Canonical MASTER savepoint:

`research/master/fusion_f2_3_physical_parameter_integration_freeze_0_1.md`

## Immediate next gate

Fusion F2.4 — Kinetic Admissible Input Geometry / Input-Cost Freeze 0.1 is the only active scientific handoff.

It must derive the continuous initial-condition pair `(B,R_in)` from physical local-GK admissibility and preparation-cost semantics before any numerical basis is chosen. The candidate `B=I`, `R_in=M_F2` must be evaluated rather than assumed. Any restriction must come from exact physical constraints, not from expected optimizer separation.

Canonical instruction:

`research/master/prompts/fusion_f2_4_kinetic_input_geometry_input_cost_freeze_0_1.md`

## Planned dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1 candidate/balance — **COMPLETE / FROZEN**;
3. F2.2 geometry/conventions — **COMPLETE / FROZEN**;
4. F2.3 physical point — **COMPLETE / FROZEN**;
5. F2.4 kinetic input geometry / input cost — **READY**;
6. structure-preserving phase-space discretization and physical discrete-channel reconstruction;
7. numerical/free-energy/spectral qualification;
8. later pre-effect finite-time pilot specification/freeze;
9. one-shot finite-time execution only after all preceding gates pass;
10. fully kinetic/GENE-compatible reference validation through separately released gates.

## Other branch states

- CORE: `STABLE / PARKED`
- Fusion: `F2.4 READY`
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

No parallel science is opened. The continuous kinetic input geometry must be fixed before discretization so that numerical basis choices cannot silently define physical admissibility. MODES remains conditional on a later concrete high-dimensional representation issue; CONT remains premature before an authorized parameter family exists.

## Branch-independent / branch-dependent distinction

Branch-independent CORE methodology remains

\[
\mathfrak C=(A,M,\{Q_\alpha\},B,R_{\rm in}).
\]

Branch-dependent F2 content now includes the continuous kinetic state, positive Helmholtz metric, physical particle/heat channels, exact multi-channel balance, source-consistent toroidal geometry family and one frozen physical benchmark point. The input geometry and all discrete representations remain unfrozen.

## Protected rollback chain

All first-paper savepoints remain protected. The latest post-paper rollback point is:

\[
\boxed{\text{Fusion F2.3 Physical-Parameter Integration Freeze 0.1}}.
\]

## Decision record

- base through DEC-443;
- Addendum 0.1 through DEC-486;
- Addendum 0.2 through DEC-502;
- Addendum 0.3 through DEC-510;
- Addendum 0.4 through DEC-520;
- Addendum 0.5 through DEC-529;
- Addendum 0.6 through DEC-540;
- Addendum 0.7 through DEC-550;
- Addendum 0.8 through DEC-560.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_f2_4_kinetic_input_geometry_input_cost_freeze_0_1.md`.

No phase-space discretization, spectrum, GENE run, finite-time effect inspection, input-subspace scan, R1/F2.3 retuning or parallel branch work is authorized before F2.4 returns.
