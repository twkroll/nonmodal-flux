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
- Fusion F2.2 local magnetic-geometry family / kinetic conventions: **PASS / INTEGRATED / FROZEN**.
- Fusion F2.2 Geometry / Kinetic-Convention Integration Freeze 0.1: **STABLE — F2.3 RELEASED**.

## First-paper status

Paper 1 scientific content remains frozen. Draft 0.4 is a scientific-content baseline, not final prose. Submission preparation remains parked by user choice.

## Active post-paper program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

R1 remains the frozen one-channel structural-collapse control. The active higher-fidelity lineage is F2-R.

## Frozen F2-R architecture and balance

Primary reduced candidate:

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with passing electrons adiabatic at leading order. Higher-fidelity reference: fully kinetic two-species electrostatic local GK with H-theorem-compatible physical collisions.

The reduced continuous balance is

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

Electrostatic ambipolarity reduces the two species particle fluxes to one particle channel for hydrogen, while ion and trapped-electron heat fluxes remain distinct. Thus the R1 affine redundancy is not structurally forced, but no finite-time optimizer separation has been inspected.

## Frozen F2.2 geometry family and conventions

Primary geometry family:

\[
\boxed{\text{large-aspect-ratio circular local tokamak}+\hat s\text{-}\alpha_{\rm MHD}\text{ flux-tube geometry in ballooning space}}
\]

Frozen conventions include:

- Clebsch orientation and outward radial sign;
- infinite ballooning coordinate with outboard midplane at `theta=0`;
- `exp[i(k_psi psi+k_alpha alpha)]`, `k_alpha != 0`;
- circular `B(theta)=B0/[1+epsilon cos(theta)]` and line metric;
- `s-alpha` `k_perp(theta)` and twist-and-shift sign;
- signed curvature/grad-B drift convention;
- trapped/passing pitch classification, bounce points and exact orbit-time bounce averaging;
- finite ion FLR, leading adiabatic passing electrons and `k_perp rho_e << 1` reduced-electron ordering;
- no parity reduction.

No numerical geometry values, gradients, temperature ratio, wavenumbers, input geometry or discretization were frozen in F2.2.

F2.2 branch commit `19dcf169ffe36c7b5f64f560f1f22294fa8ee239`; Python CI #355 = `SUCCESS`.

Canonical MASTER savepoint:

`research/master/fusion_f2_2_geometry_convention_integration_freeze_0_1.md`

## Immediate next gate

Fusion F2.3 — Physical Geometry / Gradient / Wavenumber Parameter Freeze 0.1 is the only active scientific handoff.

It must freeze exactly one coherent source-supported numerical point for the frozen F2-R architecture and F2.2 geometry family. A CBC-compatible benchmark is preferred only if the required two-species trapped-electron quantities can be assigned coherently from supported conventions. Any material ambiguity must return `HOLD`; mixing incompatible benchmarks or tuning values for expected stability/transport/objective separation is forbidden.

Canonical instruction:

`research/master/prompts/fusion_f2_3_physical_parameter_freeze_0_1.md`

## Planned dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1 two-species local-GK candidate/balance — **COMPLETE / FROZEN**;
3. F2.2 geometry family / kinetic conventions — **COMPLETE / FROZEN**;
4. F2.3 physical geometry/gradient/wavenumber single-point freeze — **READY**;
5. kinetic admissible input geometry / input-cost freeze;
6. structure-preserving phase-space discretization and physical discrete-channel reconstruction;
7. numerical/free-energy/spectral qualification;
8. later pre-effect pilot specification/freeze before any finite-time execution;
9. fully kinetic/GENE-compatible reference validation only through separately released gates.

## Other branch states

- CORE: `STABLE / PARKED`
- Fusion: `F2.3 READY`
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

No parallel science is opened. The physical point must be frozen before kinetic input geometry, phase-space discretization or numerical qualification. MODES remains conditional on a later concrete high-dimensional representation issue; CONT remains premature before a parameter family, rather than one pilot point, is explicitly authorized.

## Branch-independent / branch-dependent distinction

Branch-independent CORE methodology remains

\[
\mathfrak C=(A,M,\{Q_\alpha\},B,R_{\rm in}).
\]

Branch-dependent F2 content now includes the continuous kinetic state, positive Helmholtz metric, physical ambipolar particle channel, distinct ion/electron heat channels, exact source balance and a fixed continuous circular `s-alpha` geometry/convention package. The numerical parameter point, kinetic input geometry and discrete representation remain unfrozen.

## Protected rollback chain

All first-paper savepoints remain protected. Latest post-paper savepoint:

\[
\boxed{\text{Fusion F2.2 Geometry / Kinetic-Convention Integration Freeze 0.1}}.
\]

## Decision record

- base through DEC-443;
- Addendum 0.1 through DEC-486;
- Addendum 0.2 through DEC-502;
- Addendum 0.3 through DEC-510;
- Addendum 0.4 through DEC-520;
- Addendum 0.5 through DEC-529;
- Addendum 0.6 through DEC-540;
- Addendum 0.7 through DEC-550.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_f2_3_physical_parameter_freeze_0_1.md`.

No parameter scans, spectra, phase-space discretization, GENE run, kinetic input optimization or finite-time effect inspection are authorized before F2.3 returns.
