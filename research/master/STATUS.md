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
- F2.5 structure-preserving discretization / quadrature specification: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.5 Discretization-Specification Integration Freeze 0.1: `STABLE — F2.6 RELEASED`.

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

The R1 affine redundancy is not structurally forced in F2-R, but no finite-time F2 objective separation has been inspected.

## Frozen physical point and input geometry

The F2.3 single CBC-compatible point remains fixed: `R0/a=2.77778`, `r0/a=0.5`, `epsilon=0.18`, `q=1.4`, `shat=0.8`, `alpha_MHD=0`, deuterium/electron `mi/me=3672`, `Ti/Te=1`, equal density, `a/Ln=0.8`, `a/LTi=a/LTe=2.49`, `ky rho_i=+0.3`, `theta0=0`, `kx0=0`. No retuning is allowed.

The continuous input pair remains

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}}.
\]

No parity, zero-moment, transport-neutral or effect-motivated input restriction is authorized.

## Frozen F2.5 numerical representation

The numerical package is frozen as

\[
\boxed{
\text{compact-support ballooning Galerkin/SBP spectral elements}
\times\text{ Hermite--Laguerre ion velocity representation}
+\text{ regularized trapped-electron orbit quadrature}
}
\]

with no boundary damping/filtering/hyperdiffusion/hypercollision, exact finite-ion FLR, algebraic quasineutrality elimination of `phi_K`, both ion velocity signs retained, no parity reduction and no separatrix/turning-set state DOF.

The predeclared K0/K1/K2 ladder is frozen with `Theta_max=3pi/5pi/7pi`, 3/5/7 complete trapped-electron wells, `theta` degrees 12/16/20, ion Hermite orders 16/24/32, ion Laguerre orders 8/12/16, trapped-electron energy/pitch orders 12/18/24 and bounce quadrature orders 24/36/48.

F2.5 branch commit `43de899b547b2ccc1d0c11ecb6788dfce6cb6b47`; Python CI #378 = `SUCCESS`.

Canonical result:

`research/fusion/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`

MASTER savepoint:

`research/master/fusion_f2_5_discretization_specification_integration_freeze_0_1.md`

## Current dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1 candidate/balance — **COMPLETE / FROZEN**;
3. F2.2 geometry/conventions — **COMPLETE / FROZEN**;
4. F2.3 physical single point — **COMPLETE / FROZEN**;
5. F2.4 kinetic input geometry / input cost — **COMPLETE / FROZEN**;
6. F2.5 structure-preserving discretization / quadrature specification — **COMPLETE / FROZEN**;
7. F2.6 discrete generator/metric/physical-channel reconstruction and algebraic balance qualification — **READY**;
8. later numerical/free-energy/spectral qualification;
9. only then a pre-effect finite-time pilot specification/freeze;
10. fully kinetic/GENE-compatible reference validation through separately released gates.

## Parallelism / parked branches

Fusion is the only active scientific branch. Literature, MODES, CONT, CASCADE, CORE 0.2, Neuro extensions and higher-fidelity Climate remain parked. Power Grids and Photonics/Waves remain `PROTECTED`. Paper-1 submission remains parked.

No parallel scientific branch is opened while F2.6 qualifies the discrete physical algebra. MODES remains conditional on a concrete representation/reduction problem after a qualified high-dimensional operator exists; CONT remains premature without an authorized parameter family.

## Decision record

Canonical continuation now reaches **DEC-580** in `research/master/decision_branch_log_addendum_0_10.md`.

## Rollback points

The latest protected post-paper rollback point is

\[
\boxed{\text{Fusion F2.5 Discretization-Specification Integration Freeze 0.1}}.
\]

All previous post-paper and first-paper savepoints remain protected.

## Active instruction

**Status:** `FUSION F2.6 DISCRETE OPERATOR / CHANNEL ALGEBRAIC QUALIFICATION READY — AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Next instruction:**

`research/master/prompts/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

## STOP boundary

Do not inspect eigenvalues/growth rates/pseudospectra, construct finite-time propagators/Gramians/cumulative objectives, compute optimizers/angles/gaps, scan parameters, run GENE, add damping/collisions, change F2.3/F2.4/F2.5 freezes, reopen R1/FLR-only rescue or open MODES/CONT/CASCADE/protected branches. Paper-1 submission remains parked unless explicitly reactivated.

**STOP — AWAIT FUSION `GO`.**
