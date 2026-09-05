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
- Fusion F2.4 Kinetic Input-Geometry / Input-Cost Integration Freeze 0.1: **STABLE — F2.5 RELEASED**.

## First-paper status

Paper 1 scientific content remains frozen. Draft 0.4 is the scientific-content baseline, not final prose. Submission preparation remains parked by user choice.

## Active post-paper program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

R1 remains the frozen structural-collapse control. The active higher-fidelity lineage is F2-R.

## Frozen F2-R model and point

Primary reduced candidate:

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons.

The reduced free-energy balance is

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

Primary geometry family:

\[
\boxed{\text{large-aspect-ratio circular local tokamak}+\hat s\text{-}\alpha_{\rm MHD}\text{ ballooning-space flux tube}}
\]

Frozen physical point:

\[
\boxed{
\begin{gathered}
R_0/a=2.77778,\ r_0/a=0.5,\ \epsilon=0.18,\ q=1.4,\ \hat s=0.8,\ \alpha_{\rm MHD}=0,\\
Z_i=+1,\ Z_e=-1,\ m_i/m_e=3672,\ T_i/T_e=1,\ n_i=n_e,\\
a/L_n=0.8,\ a/L_{T_i}=a/L_{T_e}=2.49,\\
k_y\rho_i=+0.3,\ \theta_0=0,\ k_{x0}=0.
\end{gathered}}
\]

Normalization: `vTi=sqrt(Ti/mi)`, `rho_i=vTi/Omega_i`, `tau_ref=R0/vTi`. No retuning is allowed.

## Frozen F2.4 input geometry

The physically admissible input space is the full finite-Helmholtz-free-energy tangent space of the already reduced F2-R model,

\[
\mathcal H_{F2}=\overline{\mathcal D_0}^{\|\cdot\|_{F2}},
\qquad
\|x\|_{F2}^2=\langle x,\mathcal M_{F2}x\rangle=2W[x].
\]

Quasineutrality reconstructs the electrostatic field and does not impose an extra kinetic-state null constraint. The continuous input pair is frozen as

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}}.
\]

The fixed budget is initial Helmholtz free energy, not laboratory actuator energy. No parity, transport-neutral or effect-motivated input restriction is authorized.

F2.4 branch commit `eabc44856458c7450946050c8ab04362904ef9ac`; Python CI #371 = `SUCCESS`.

Canonical MASTER savepoint:

`research/master/fusion_f2_4_input_geometry_integration_freeze_0_1.md`

## Immediate next gate

Fusion F2.5 — Structure-Preserving Phase-Space Discretization / Quadrature Specification Freeze 0.1 is the only active scientific handoff.

It must freeze the numerical state-space architecture, ballooning/velocity-space representation, separatrix/turning-point and bounce quadrature treatment, quasineutrality handling, free-energy construction targets and a predeclared refinement ladder. It may not inspect spectra, transient growth or finite-time objective separation.

Canonical instruction:

`research/master/prompts/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`

## Planned dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1 candidate/balance — **COMPLETE / FROZEN**;
3. F2.2 geometry/conventions — **COMPLETE / FROZEN**;
4. F2.3 physical point — **COMPLETE / FROZEN**;
5. F2.4 kinetic input geometry / input cost — **COMPLETE / FROZEN**;
6. F2.5 structure-preserving discretization / quadrature specification — **READY**;
7. discrete generator/metric/particle/heat-channel reconstruction and algebraic balance qualification;
8. numerical/free-energy/spectral qualification;
9. later pre-effect finite-time pilot specification/freeze;
10. one-shot finite-time execution only after all preceding gates pass;
11. fully kinetic/GENE-compatible reference validation through separately released gates.

## Other branch states

- CORE: `STABLE / PARKED`
- Fusion: `F2.5 READY`
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

No parallel science is opened. The discretization must be frozen before discrete operator algebra or spectral qualification so later numerical behavior cannot influence basis/cutoff choices. MODES remains conditional on a concrete reduction/representation issue; CONT remains premature without an authorized parameter family.

## Branch-independent / branch-dependent distinction

Branch-independent CORE methodology remains

\[
\mathfrak C=(A,M,\{Q_\alpha\},B,R_{\rm in}).
\]

Branch-dependent F2 content now includes the continuous kinetic state, positive Helmholtz metric, physical transport channels and balance, toroidal geometry, one physical point, and the full reduced initial-condition geometry. The numerical discretization and discrete operators remain unfrozen.

## Protected rollback chain

All first-paper savepoints remain protected. The latest post-paper rollback point is

\[
\boxed{\text{Fusion F2.4 Kinetic Input-Geometry / Input-Cost Integration Freeze 0.1}}.
\]

## Decision record

Canonical continuation now reaches **DEC-570** in `decision_branch_log_addendum_0_9.md`.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`.

No spectrum, phase-space effect scan, GENE run, finite-time objective inspection, R1/F2.3 retuning, F2.4 input-space change or parallel branch work is authorized before F2.5 returns.
