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
- F2.3 physical geometry/gradient/wavenumber single-point freeze: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.3 Physical-Parameter Integration Freeze 0.1: `STABLE — F2.4 RELEASED`.

## Frozen F2-R architecture and balance

Primary reduced candidate:

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons. Higher-fidelity reference remains fully kinetic two-species electrostatic local GK with H-theorem-compatible physical collisions.

The reduced continuous balance is

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

The R1 one-channel affine redundancy is not structurally forced, but no finite-time F2 objective separation has been inspected.

## Frozen F2.2 geometry package

Primary geometry family:

\[
\boxed{\text{large-aspect-ratio circular local tokamak}+\hat s\text{-}\alpha_{\rm MHD}\text{ flux-tube geometry in ballooning space}}
\]

The Clebsch/Fourier orientation, circular field/line metric, `s-alpha` perpendicular metric and twist sign, magnetic-drift convention, trapped/passing and bounce definitions, exact orbit-time bounce average, finite ion FLR, reduced-electron ordering, infinite ballooning line and no-parity rule are frozen.

## Frozen F2.3 physical point

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

Equivalent major-radius gradients are `R0/Ln=2.222224` and `R0/LTi=R0/LTe=6.9166722`. Normalization is `vTi=sqrt(Ti/mi)`, `rho_i=vTi/Omega_i`, `tau_ref=R0/vTi`.

All three continuous F2.1 supply coefficients are nonzero at the frozen point. This does not prove later discrete channel independence or finite-time objective separation.

Canonical branch result:

`research/fusion/fusion_f2_3_physical_parameter_freeze_0_1.md`

MASTER savepoint:

`research/master/fusion_f2_3_physical_parameter_integration_freeze_0_1.md`

F2.3 branch commit `fcd012219427ce0243151d2cfb7796236778d966`; Python CI #362 = `SUCCESS`.

## Current dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1 two-species local-GK candidate/balance — **COMPLETE / FROZEN**;
3. F2.2 geometry family / kinetic conventions — **COMPLETE / FROZEN**;
4. F2.3 physical geometry/gradient/wavenumber single point — **COMPLETE / FROZEN**;
5. F2.4 kinetic admissible input geometry / input-cost freeze — **READY**;
6. structure-preserving phase-space discretization and discrete physical-channel reconstruction;
7. numerical/free-energy/spectral qualification;
8. only then a later pre-effect finite-time pilot specification/freeze;
9. fully kinetic/GENE-compatible reference validation through separately released gates.

## Parallelism / parked branches

Fusion is the only active scientific branch. Literature, MODES, CONT, CASCADE, CORE 0.2, Neuro extensions and higher-fidelity Climate remain parked. Power Grids and Photonics/Waves remain `PROTECTED`. Paper-1 submission remains parked.

No parallel scientific branch is opened while F2.4 fixes the continuous kinetic input geometry.

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

## Rollback points

The latest protected post-paper rollback point is

\[
\boxed{\text{Fusion F2.3 Physical-Parameter Integration Freeze 0.1}}.
\]

All previous post-paper and first-paper savepoints remain protected.

## Active instruction

**Status:** `FUSION F2.4 KINETIC INPUT GEOMETRY / INPUT-COST FREEZE READY — AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Next instruction:**

`research/master/prompts/fusion_f2_4_kinetic_input_geometry_input_cost_freeze_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

## STOP boundary

Do not discretize phase space, choose numerical basis/cutoffs, construct discrete `A/M/Q`, calculate eigenvalues, propagators, Gramians, cumulative objectives or optimizers, scan input subspaces, run GENE, add collisions to F2-R, retune F2.3, reopen R1/FLR-only rescue or open MODES/CONT/CASCADE/protected branches. Paper-1 submission remains parked unless explicitly reactivated.

**STOP — AWAIT FUSION `GO`.**
