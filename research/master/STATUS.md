# MASTER Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

All first-paper savepoints remain intact and the submission track remains parked by user choice. Post-paper science remains focused on Fusion.

Stable first-paper lineage remains unchanged: CORE `STABLE`; Plasma `P2-A` frozen; Neuro `NEURO-STRONG` frozen; Climate-A `CLIM-WEAK` frozen; Climate-B `CLIM-B-FAIL` frozen; Manuscript Revision 0.4 `COMPLETE — PASS`; First Paper Scientific Content Freeze 0.1 `STABLE`.

Post-paper Fusion lineage now includes:

- R1 structural no-go / literature positioning: frozen;
- F2.1 two-species local-GK candidate/balance specification: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.2 local magnetic-geometry family / kinetic convention freeze: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.2 Geometry / Kinetic-Convention Integration Freeze 0.1: `STABLE — F2.3 RELEASED`.

## Frozen F2-R architecture and balance

Primary reduced candidate:

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with passing electrons adiabatic at leading order. Higher-fidelity reference remains fully kinetic two-species electrostatic local GK with H-theorem-compatible physical collisions.

The reduced continuous balance is

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

The R1 one-channel affine redundancy is therefore not structurally forced, but no finite-time objective separation has been inspected.

## Frozen F2.2 geometry package

Primary geometry family:

\[
\boxed{\text{large-aspect-ratio circular local tokamak}+\hat s\text{-}\alpha_{\rm MHD}\text{ flux-tube geometry in ballooning space}}
\]

F2.2 freezes the Clebsch/Fourier orientation, circular field-strength and line metric, `s-alpha` perpendicular metric and twist sign, signed curvature/grad-B magnetic-drift convention, trapped/passing and bounce-point definitions, exact orbit-time bounce averaging, finite ion FLR, `k_perp rho_e << 1` reduced-electron ordering, infinite ballooning line and no parity reduction.

No numerical geometry values, gradients, temperature ratio, wavenumbers or discretization were frozen or scanned.

Canonical branch result:

`research/fusion/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`

MASTER savepoint:

`research/master/fusion_f2_2_geometry_convention_integration_freeze_0_1.md`

F2.2 branch commit `19dcf169ffe36c7b5f64f560f1f22294fa8ee239`; Python CI #355 = `SUCCESS`.

## Current dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1 two-species local-GK candidate/balance — **COMPLETE / FROZEN**;
3. F2.2 geometry family / kinetic conventions — **COMPLETE / FROZEN**;
4. F2.3 physical geometry/gradient/wavenumber single-point freeze — **READY**;
5. kinetic admissible input geometry / input-cost freeze;
6. structure-preserving phase-space discretization and discrete physical-channel reconstruction;
7. numerical/free-energy/spectral qualification;
8. only then a later pre-effect finite-time pilot specification/freeze;
9. fully kinetic/GENE-compatible reference validation through separately released gates.

## Parallelism / parked branches

Fusion is the only active scientific branch. Literature, MODES, CONT, CASCADE, CORE 0.2, Neuro extensions and higher-fidelity Climate remain parked. Power Grids and Photonics/Waves remain `PROTECTED`. Paper-1 submission remains parked.

No parallel branch is opened while the single F2-R physical point is frozen.

## Decision record

- base through DEC-443;
- Addendum 0.1 through DEC-486;
- Addendum 0.2 through DEC-502;
- Addendum 0.3 through DEC-510;
- Addendum 0.4 through DEC-520;
- Addendum 0.5 through DEC-529;
- Addendum 0.6 through DEC-540;
- Addendum 0.7 through DEC-550.

## Rollback points

The latest protected post-paper rollback point is

\[
\boxed{\text{Fusion F2.2 Geometry / Kinetic-Convention Integration Freeze 0.1}}.
\]

All previous post-paper and first-paper savepoints remain protected.

## Active instruction

**Status:** `FUSION F2.3 PHYSICAL GEOMETRY / GRADIENT / WAVENUMBER PARAMETER FREEZE READY — AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Next instruction:**

`research/master/prompts/fusion_f2_3_physical_parameter_freeze_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

## STOP boundary

Do not scan or select parameters by spectrum, stability, nonnormality, transport magnitude or optimizer separation. Do not calculate eigenvalues, discretize phase space, define kinetic `B/R_in`, run GENE or inspect finite-time objectives before F2.3 returns. Do not open MODES/CONT/CASCADE or protected branches. Paper-1 submission remains parked unless explicitly reactivated.

**STOP — AWAIT FUSION `GO`.**
