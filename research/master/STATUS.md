# MASTER Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

All first-paper savepoints remain intact and the submission track remains parked by user choice. Post-paper science remains focused on Fusion.

Stable first-paper lineage:

- CORE Mathematical / Integration / Interpretation freezes: `STABLE`;
- Plasma/D10-ZF: `P2-A`, `FROZEN`;
- Neuro/CMC: `NEURO-STRONG`, `FROZEN`;
- Climate-A: `CLIM-WEAK`, `FROZEN`;
- Climate-B: `CLIM-B-FAIL — resolution robustness failure`, `RESULT FROZEN`;
- Manuscript Revision 0.4: `COMPLETE — PASS`;
- Submission Readiness Gate 0.1: `PASS WITH AUTHOR/METADATA ITEMS — SCIENTIFIC PACKAGE READY`;
- First Paper Scientific Content Freeze 0.1: `STABLE — SCIENTIFIC CONTENT BASELINE FROZEN / SUBMISSION TRACK PARKED`.

Post-paper Fusion lineage:

- Post-Paper Scientific Roadmap Gate 0.1: `COMPLETE — FUSION-F1 SELECTED`;
- B5.5 physical ion heat-flux observable: `PASS / MASTER-INTEGRATED / FROZEN`;
- F1.2 admissible input geometry / cost: `PASS / MASTER-INTEGRATED / FROZEN`;
- F1.3 candidate / convention freeze: `PASS / MASTER-INTEGRATED / FROZEN`;
- F1.4 numerical / spectral qualification: `HOLD — MARGINAL SPECTRUM / MASTER-INTEGRATED`;
- F1.4 Marginal / Structural Integration Freeze 0.1: `STABLE — R1 STRUCTURAL CONTROL FROZEN / R1 OBJECTIVE-SEPARATION PILOT BLOCKED`;
- Fusion R1 structural-redundancy literature audit: `COMPLETE / MASTER-INTEGRATED`;
- Fusion R1 Structural-Redundancy Literature Integration Freeze 0.1: `STABLE`;
- Fusion F2.1 two-species local-GK candidate/balance specification: `PASS / MASTER-INTEGRATED / FROZEN`;
- Fusion F2.1 Two-Species GK Balance Integration Freeze 0.1: `STABLE — F2.2 RELEASED`.

## Frozen R1 conclusion

For the collisionless R1 lineage,

\[
2\frac{R_0}{L_T}K_q(T)=\mathcal E_M(T)-I
\]

for every horizon under the frozen `B=I_4`, `R_in=M_k` geometry. R1 remains a structural no-go / conservative control; its objective-separation pilot is blocked and no retuning or FLR-only rescue is allowed.

## Frozen F2.1 higher-fidelity architecture

Primary reduced candidate:

\[
\boxed{
\text{finite-ion-FLR electrostatic local-GK ions}
+\text{collisionless bounce-averaged trapped electrons}
}
\]

with passing electrons adiabatic at leading order.

Higher-fidelity reference:

\[
\boxed{
\text{fully kinetic two-species electrostatic local GK}
+\text{H-theorem-compatible physical collisions}
}
\]

The reduced continuous state is

\[
x=(g_i(l,E_i,\mu_i,\sigma),\,g_e^{\rm tr}(E_e,\lambda,w)),
\]

with quasineutrality-reconstructed electrostatic potential and positive continuous Helmholtz metric

\[
\mathcal M_{F2}\succ0.
\]

The source-faithful reduced collisionless balance is

\[
\boxed{
\frac{dW}{dt}
=G_\Gamma\Gamma
+G_{T,i}q_i
+G_{T,e}q_e^{\rm tr}.
}
\]

Electrostatic ambipolarity reduces the species particle fluxes to one particle channel for hydrogen, but no closure identity forces ion and trapped-electron heat fluxes to coincide. Therefore the R1 two-operator affine redundancy is no longer structurally forced in F2.1. This is only a possibility-in-principle statement; no finite-time objective separation has been inspected.

Canonical F2.1 result:

`research/fusion/fusion_f2_1_two_species_local_gyrokinetic_balance_specification_gate_0_1.md`

MASTER integration freeze:

`research/master/fusion_f2_1_two_species_gk_balance_integration_freeze_0_1.md`

F2.1 branch commit `93e855b1618a92a6a20724a09549897112b23b7d`; Python CI #347 = `SUCCESS`.

## Current dependency chain

1. R1 structural no-go and literature positioning — **COMPLETE / FROZEN**;
2. F2.1 two-species local-GK candidate/balance specification — **COMPLETE / FROZEN**;
3. F2.2 local magnetic-geometry family / kinetic convention freeze — **READY**;
4. later physical geometry/gradient/wavenumber parameter freeze;
5. later kinetic input geometry / input-cost freeze;
6. later structure-preserving phase-space discretization and discrete-channel reconstruction;
7. later numerical/spectral qualification and only then any finite-time pilot decision;
8. fully kinetic/GENE-compatible reference mapping only after the reduced lineage is independently qualified.

## Parallelism / parked branches

- Fusion: active next handoff;
- Literature: `WAIT`;
- MODES: parked / conditional companion only after a concrete high-dimensional representation issue exists;
- CONT: parked;
- CASCADE: parked;
- CORE 0.2: parked;
- Neuro and higher-fidelity Climate: parked;
- Power Grids and Photonics/Waves: `PROTECTED`;
- Paper-1 submission: parked.

No parallel scientific branch is opened while F2.2 freezes the geometry/convention package.

## Decision record

- base log through DEC-443;
- Addendum 0.1 through DEC-486;
- Addendum 0.2 through DEC-502;
- Addendum 0.3 through DEC-510;
- Addendum 0.4 through DEC-520;
- Addendum 0.5 through DEC-529;
- Addendum 0.6 through DEC-540.

## Rollback points

The protected post-paper rollback chain is now

\[
\text{Post-Paper Roadmap}
\rightarrow
\text{B5.5 Integration Freeze}
\rightarrow
\text{F1.2 Input Geometry Integration Freeze}
\rightarrow
\text{F1.3 Candidate / Convention Integration Freeze}
\rightarrow
\text{F1.4 Marginal / Structural Integration Freeze}
\rightarrow
\text{R1 Literature Integration Freeze}
\rightarrow
\boxed{\text{F2.1 Two-Species GK Balance Integration Freeze}}.
\]

All first-paper savepoints remain separately protected.

## Active instruction

**Status:** `FUSION F2.2 LOCAL MAGNETIC-GEOMETRY FAMILY / KINETIC CONVENTION FREEZE READY — AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Branch status:**

`research/fusion/STATUS.md`

**Next instruction:**

`research/master/prompts/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

## STOP boundary

Do not choose geometry by spectral or finite-time effect. Do not scan geometry parameters, gradients or wavenumbers; discretize phase space; define kinetic `B/R_in`; run GENE; perform spectral/transient/finite-time objective calculations; reopen R1/FLR-only rescue; or open MODES/CONT/CASCADE/protected branches. Paper-1 submission remains parked unless explicitly reactivated.

**STOP — AWAIT FUSION `GO`.**
