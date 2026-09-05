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
- Fusion F2.1 two-species local-GK candidate/balance specification: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.1 Two-Species GK Balance Integration Freeze 0.1: **STABLE — F2.2 RELEASED**.

## First-paper status

Paper 1 scientific content remains frozen. Draft 0.4 is a scientific-content baseline, not final prose. Submission preparation remains parked by user choice.

## Active post-paper program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

R1 remains the frozen one-channel structural-collapse control. The active higher-fidelity lineage now begins with F2-R.

## Frozen F2-R architecture

Primary reduced candidate:

\[
\boxed{
\text{finite-ion-FLR electrostatic local-GK ions}
+\text{collisionless bounce-averaged trapped electrons}
}
\]

with passing electrons adiabatic at leading order in the slow-electron-transit ordering.

Higher-fidelity reference:

\[
\boxed{
\text{fully kinetic two-species electrostatic local GK}
+\text{H-theorem-compatible physical collisions}
}
\]

The reduced state is continuous in kinetic phase space,

\[
x=(g_i(l,E_i,\mu_i,\sigma),\,g_e^{\rm tr}(E_e,\lambda,w)),
\]

and the potential is reconstructed from quasineutrality. The positive Helmholtz free energy defines a continuous positive metric `M_F2`.

Physical particle and heat channels are defined independently from radial gyrocentre flux integrals. Electrostatic quasineutrality imposes charge-flux ambipolarity; for hydrogen this reduces ion/electron particle fluxes to one particle channel while leaving ion and trapped-electron heat fluxes distinct.

The reduced collisionless balance is

\[
\boxed{
\frac{dW}{dt}
=G_\Gamma\Gamma
+G_{T,i}q_i
+G_{T,e}q_e^{\rm tr}.
}
\]

Hence the exact R1 two-operator affine redundancy is no longer structurally forced in F2-R. This does not establish any finite-time optimizer separation or effect magnitude.

F2.1 branch commit `93e855b1618a92a6a20724a09549897112b23b7d`; Python CI #347 = `SUCCESS`.

Canonical MASTER savepoint:

`research/master/fusion_f2_1_two_species_gk_balance_integration_freeze_0_1.md`

## Immediate next gate

Fusion F2.2 — Local Magnetic-Geometry Family / Kinetic Convention Freeze 0.1 is the only active scientific handoff.

F2.2 must select and freeze one source-faithful local toroidal geometry family and continuous coordinate/Fourier/ballooning/magnetic-drift/trapped-particle/bounce-average conventions. It must explicitly separate the geometry family from numerical geometry parameters that remain for a later physical-parameter freeze.

Canonical instruction:

`research/master/prompts/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`

## Planned dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1 two-species local-GK candidate/balance specification — **COMPLETE / FROZEN**;
3. F2.2 local magnetic-geometry family / kinetic conventions — **READY**;
4. physical geometry/gradient/wavenumber parameter freeze;
5. kinetic admissible input geometry / input-cost freeze;
6. structure-preserving phase-space discretization and physical discrete-channel reconstruction;
7. numerical/spectral qualification;
8. later pre-effect pilot specification/freeze before any finite-time objective execution;
9. fully kinetic/GENE-compatible reference validation only through separately released gates.

## Other branch states

- CORE: `STABLE / PARKED`
- Fusion: `F2.2 READY`
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

No parallel science is opened. Geometry must be fixed before parameter selection, kinetic input geometry, discretization or numerical qualification. MODES remains conditional on a later concrete high-dimensional representation issue; CONT remains premature before a physical parameter family is defined.

## Branch-independent / branch-dependent distinction

Branch-independent CORE methodology remains

\[
\mathfrak C=(A,M,\{Q_\alpha\},B,R_{\rm in}).
\]

Branch-dependent F2 content now includes the continuous kinetic state, positive Helmholtz metric, physical ambipolar particle channel, distinct ion/electron heat channels and the exact source balance. The geometry family, numerical parameter point, kinetic input geometry and discrete representation remain unfrozen.

## Protected rollback chain

All first-paper savepoints remain protected. Post-paper savepoints now include:

1. Post-Paper Scientific Roadmap Gate 0.1;
2. Fusion B5.5 Integration Freeze 0.1;
3. Fusion F1.2 Input Geometry / Input-Cost Integration Freeze 0.1;
4. Fusion F1.3 Candidate / Convention Integration Freeze 0.1;
5. Fusion F1.4 Marginal / Structural Integration Freeze 0.1;
6. Fusion R1 Structural-Redundancy Literature Integration Freeze 0.1;
7. Fusion F2.1 Two-Species GK Balance Integration Freeze 0.1.

## Decision record

- base through DEC-443;
- Addendum 0.1 through DEC-486;
- Addendum 0.2 through DEC-502;
- Addendum 0.3 through DEC-510;
- Addendum 0.4 through DEC-520;
- Addendum 0.5 through DEC-529;
- Addendum 0.6 through DEC-540.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`.

No geometry/parameter scans, phase-space discretization, GENE run, kinetic input optimization, spectral/transient calculation or finite-time effect inspection is authorized before F2.2 returns.
