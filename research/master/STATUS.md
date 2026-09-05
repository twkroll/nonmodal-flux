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
- F2.4 kinetic admissible input geometry / input-cost freeze: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.4 Kinetic Input-Geometry / Input-Cost Integration Freeze 0.1: `STABLE — F2.5 RELEASED`.

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

## Frozen geometry and physical point

Primary geometry family:

\[
\boxed{\text{large-aspect-ratio circular local tokamak}+\hat s\text{-}\alpha_{\rm MHD}\text{ flux-tube geometry in ballooning space}}
\]

The F2.3 single CBC-compatible point remains

\[
\boxed{
\begin{gathered}
R_0/a=2.77778,\ r_0/a=0.5,\ \epsilon=0.18,\ q=1.4,\ \hat s=0.8,\ \alpha_{\rm MHD}=0,\\
Z_i=+1,\ Z_e=-1,\ m_i/m_e=3672,\ T_i/T_e=1,\ n_i=n_e,\\
a/L_n=0.8,\ a/L_{T_i}=a/L_{T_e}=2.49,\\
k_y\rho_i=+0.3,\ \theta_0=0,\ k_{x0}=0.
\end{gathered}}
\]

with `vTi=sqrt(Ti/mi)`, `rho_i=vTi/Omega_i`, `tau_ref=R0/vTi`. No retuning is allowed.

## Frozen F2.4 continuous input geometry

The physically admissible continuous state/input space is the full finite-Helmholtz-free-energy tangent space of the already reduced F2-R model,

\[
\mathcal H_{F2}=\overline{\mathcal D_0}^{\|\cdot\|_{F2}},
\qquad
\|x\|_{F2}^2=\langle x,\mathcal M_{F2}x\rangle=2W[x].
\]

Quasineutrality is a field-reconstruction map

\[
\phi=P_{\rm QN}(g_i,g_e^{\rm tr}),
\]

not an extra proper-subspace constraint. No additional particle-number, charge, momentum, energy-moment, gauge, parity or transport-neutral restriction is required in the frozen nonzonal block.

The continuous input pair is therefore

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}}.
\]

The input budget is initial Helmholtz free energy, not laboratory actuator energy. This does not claim arbitrary independent experimental preparation of all kinetic components.

Canonical F2.4 result:

`research/fusion/fusion_f2_4_kinetic_input_geometry_input_cost_freeze_0_1.md`

MASTER savepoint:

`research/master/fusion_f2_4_input_geometry_integration_freeze_0_1.md`

F2.4 branch commit `eabc44856458c7450946050c8ab04362904ef9ac`; Python CI #371 = `SUCCESS`.

## Current dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1 two-species local-GK candidate/balance — **COMPLETE / FROZEN**;
3. F2.2 geometry family / kinetic conventions — **COMPLETE / FROZEN**;
4. F2.3 physical single point — **COMPLETE / FROZEN**;
5. F2.4 kinetic input geometry / input cost — **COMPLETE / FROZEN**;
6. F2.5 structure-preserving phase-space discretization / quadrature specification — **READY**;
7. later discrete generator/metric/transport-channel reconstruction and algebraic balance qualification;
8. later numerical/free-energy/spectral qualification;
9. only then a pre-effect finite-time pilot specification/freeze;
10. fully kinetic/GENE-compatible reference validation through separately released gates.

## Parallelism / parked branches

Fusion is the only active scientific branch. Literature, MODES, CONT, CASCADE, CORE 0.2, Neuro extensions and higher-fidelity Climate remain parked. Power Grids and Photonics/Waves remain `PROTECTED`. Paper-1 submission remains parked.

No parallel scientific branch is opened while the F2-R numerical representation is frozen.

## Decision record

- base through DEC-443;
- Addendum 0.1 through DEC-486;
- Addendum 0.2 through DEC-502;
- Addendum 0.3 through DEC-510;
- Addendum 0.4 through DEC-520;
- Addendum 0.5 through DEC-529;
- Addendum 0.6 through DEC-540;
- Addendum 0.7 through DEC-550;
- Addendum 0.8 through DEC-560;
- Addendum 0.9 through DEC-570.

## Rollback points

The latest protected post-paper rollback point is

\[
\boxed{\text{Fusion F2.4 Kinetic Input-Geometry / Input-Cost Integration Freeze 0.1}}.
\]

All previous post-paper and first-paper savepoints remain protected.

## Active instruction

**Status:** `FUSION F2.5 STRUCTURE-PRESERVING DISCRETIZATION / QUADRATURE SPECIFICATION FREEZE READY — AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Next instruction:**

`research/master/prompts/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

## STOP boundary

Do not select numerical cutoffs/bases by spectrum or effect, construct finite-time propagators/Gramians/optimizers, scan parameters, run GENE, add collisions to F2-R, retune F2.3, alter F2.4 input geometry, reopen R1/FLR-only rescue, or open MODES/CONT/CASCADE/protected branches. Paper-1 submission remains parked unless explicitly reactivated.

**STOP — AWAIT FUSION `GO`.**
