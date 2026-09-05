# MASTER Decision & Branch Log — Addendum 0.9

**Date:** 2026-09-05  
**Base continuation:** `research/master/decision_branch_log_addendum_0_8.md` through DEC-560  
**Status:** `ACTIVE CANONICAL CONTINUATION`

## Fusion F2.4 integration / F2.5 release

- **DEC-561:** `Fusion F2.4 — Kinetic Admissible Input Geometry / Input-Cost Freeze 0.1 = PASS` — STABLE PRE-EFFECT SCIENTIFIC SAVEPOINT.
- **DEC-562:** The physically admissible continuous F2-R input space is frozen as the full finite-Helmholtz-free-energy tangent space of the already reduced model, `H_F2=closure(D0)`, where `D0` already contains the nonzonal, trapped-electron, bounce/orbit, ballooning and quasineutrality-reconstruction restrictions — FROZEN CONTINUOUS STATE-SPACE GEOMETRY.
- **DEC-563:** Quasineutrality is classified as a unique field-reconstruction map `phi=P_QN(g_i,g_e^tr)`, not a proper-subspace condition on the kinetic state; no additional zero-moment, gauge, parity, transport-neutral or effect-motivated restriction is required — FROZEN ADMISSIBILITY INTERPRETATION.
- **DEC-564:** The continuous input pair is frozen as `B=I_HF2`, `R_in=M_F2`; the fixed input budget is initial Helmholtz free energy, not laboratory actuator energy. This does not claim arbitrary independent experimental preparation of the kinetic distribution components — FROZEN INPUT SEMANTICS.
- **DEC-565:** Any discrete representation must inherit the full reduced physical input space, preserve quasineutrality as reconstruction/algebraic closure, and realize `B_K=I`, `R_in,K=M_K` or the congruent equivalent without parity/moment/transport-neutral pruning — FROZEN DISCRETIZATION CONSTRAINT.
- **DEC-566:** F2.4 branch commit `eabc44856458c7450946050c8ab04362904ef9ac`; Python CI #371 = `SUCCESS` — STABLE REPRODUCIBILITY CHECK.
- **DEC-567:** `Fusion F2.4 Kinetic Input-Geometry / Input-Cost Integration Freeze 0.1 = STABLE — F2.4 KINETIC INPUT GEOMETRY FROZEN / F2.5 DISCRETIZATION-SPECIFICATION GATE RELEASED` — NEW POST-PAPER ROLLBACK POINT.
- **DEC-568:** MASTER splits the next kinetic numerical stage: first freeze the structure-preserving phase-space representation, cutoffs/quadrature and predeclared refinement ladder; only afterward reconstruct discrete generator/metric/transport-channel operators and test the algebraic balance. This prevents spectral/operator behavior from influencing numerical representation choices — ACTIVE GATE-ORDER DECISION.
- **DEC-569:** Next authorized task = `Fusion F2.5 — Structure-Preserving Phase-Space Discretization / Quadrature Specification Freeze 0.1`. It may freeze ballooning/velocity-space representation, separatrix/turning-point handling, quasineutrality treatment and convergence ladder, but may not inspect spectra, transient growth, propagators, cumulative objectives or optimizer separation — ACTIVE SCIENTIFIC HANDOFF.
- **DEC-570:** Canonical F2.5 handoff = `research/master/prompts/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`. Fusion remains the only active scientific branch; Literature/MODES/CONT/CASCADE wait; Power Grid/Photonics remain protected; Paper-1 submission remains parked — ACTIVE / FROZEN PARALLELISM RULE.
