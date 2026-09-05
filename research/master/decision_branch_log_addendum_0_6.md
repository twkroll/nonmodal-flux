# MASTER Decision & Branch Log — Addendum 0.6

**Date:** 2026-09-05  
**Base continuation:** `research/master/decision_branch_log_addendum_0_5.md` through DEC-529  
**Status:** `ACTIVE CANONICAL CONTINUATION`

## Fusion F2.1 integration / F2.2 release

- **DEC-530:** `Fusion F2.1 — Balance-Complete Two-Species Local-Gyrokinetic Candidate / Balance Specification Gate 0.1 = PASS` — STABLE PRE-EFFECT SCIENTIFIC SAVEPOINT.
- **DEC-531:** Primary reduced higher-fidelity candidate is frozen as finite-ion-FLR electrostatic local-GK ions plus collisionless nonadiabatic bounce-averaged trapped electrons, with passing electrons adiabatic at leading order in the slow-electron-transit ordering — FROZEN F2-R ARCHITECTURE.
- **DEC-532:** Higher-fidelity reference is frozen as fully kinetic two-species electrostatic local gyrokinetics with an H-theorem-compatible physical collision operator, subject to later explicit normalization, collision and numerical-reference gates — FROZEN F2-K REFERENCE ROLE.
- **DEC-533:** F2.1 freezes a positive continuous Helmholtz free-energy metric `M_F2 > 0` and independently defined physical particle/heat channels from radial gyrocentre flux integrals. No discrete operator representation is yet authorized — FROZEN CONTINUOUS PHYSICAL STRUCTURE.
- **DEC-534:** Electrostatic quasineutrality imposes charge-flux ambipolarity, reducing the two species particle fluxes to one ambipolar particle channel for hydrogen, while no closure identity forces ion and trapped-electron heat fluxes to coincide — FROZEN CHANNEL-DEPENDENCE CLASSIFICATION.
- **DEC-535:** The reduced collisionless balance `dW/dt = G_Gamma Gamma + G_Ti q_i + G_Te q_e^tr` contains multiple physically independent source forms, so the exact R1 cumulative-ion-heat/final-free-energy affine redundancy is no longer structurally forced. This is only a possibility-in-principle statement and does not establish optimizer separation or effect magnitude — FROZEN INTERPRETATION BOUNDARY.
- **DEC-536:** F2-R remains collisionless by source ordering; finite ion FLR is retained consistently but is not promoted as an independent source/sink. F2-K collisions must be H-theorem-compatible; no ad hoc damping or R1 rescue is allowed — FROZEN FIDELITY RESTRICTIONS.
- **DEC-537:** F2.1 branch commit `93e855b1618a92a6a20724a09549897112b23b7d`; Python CI #347 = `SUCCESS` — STABLE REPRODUCIBILITY CHECK.
- **DEC-538:** `Fusion F2.1 Two-Species GK Balance Integration Freeze 0.1 = STABLE — F2.1 TWO-SPECIES GK BALANCE FROZEN / F2.2 GEOMETRY-CONVENTION GATE RELEASED` — NEW POST-PAPER ROLLBACK POINT.
- **DEC-539:** Next authorized task = `Fusion F2.2 — Local Magnetic-Geometry Family / Kinetic Convention Freeze 0.1`. It must freeze one source-faithful local toroidal geometry family and coordinate/trapping/bounce-average conventions without parameter scans, phase-space discretization, kinetic input optimization, GENE execution or finite-time objective inspection — ACTIVE SCIENTIFIC HANDOFF.
- **DEC-540:** Canonical F2.2 handoff = `research/master/prompts/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`. Fusion is the only active scientific branch. Literature returns to WAIT; MODES/CONT/CASCADE and protected collaboration branches remain closed; Paper-1 submission remains parked — ACTIVE / FROZEN PARALLELISM RULE.
