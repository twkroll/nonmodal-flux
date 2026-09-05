# MASTER Decision & Branch Log — Addendum 0.10

**Date:** 2026-09-05  
**Base continuation:** `research/master/decision_branch_log_addendum_0_9.md` through DEC-570  
**Status:** `ACTIVE CANONICAL CONTINUATION`

## Fusion F2.5 integration / F2.6 release

- **DEC-571:** `Fusion F2.5 — Structure-Preserving Phase-Space Discretization / Quadrature Specification Freeze 0.1 = PASS` — STABLE PRE-EFFECT SCIENTIFIC SAVEPOINT.
- **DEC-572:** Primary F2-R numerical architecture is frozen as compact-support ballooning Galerkin/SBP spectral elements × Hermite–Laguerre ion velocity representation + regularized trapped-electron orbit quadrature, with continuous time left unfrozen — FROZEN NUMERICAL STATE-SPACE ARCHITECTURE.
- **DEC-573:** F2.5 freezes no boundary damping/filtering/hyperdiffusion/hypercollision, retains both ion velocity signs with no parity reduction, assigns no DOF to separatrix/turning sets, retains finite-ion FLR exactly, and algebraically reconstructs/eliminates `phi_K` from quasineutrality — FROZEN STRUCTURE-PRESERVING DISCRETIZATION RULES.
- **DEC-574:** The three-level ladder is frozen as K0/K1/K2 with `Theta_max=3pi/5pi/7pi`, 3/5/7 complete trapped-electron wells, `theta` LGL degrees 12/16/20, ion Hermite orders 16/24/32, ion Laguerre orders 8/12/16, trapped-electron energy/pitch orders 12/18/24 and bounce quadrature orders 24/36/48 — FROZEN PREDECLARED REFINEMENT LADDER.
- **DEC-575:** At the frozen F2.3 point the maximum retained-support `k_perp rho_e` values are approximately `0.03765/0.06241/0.08724` on K0/K1/K2. These are reduced-electron ordering checks only, not convergence/effect claims — FROZEN INTERPRETATION BOUNDARY.
- **DEC-576:** F2.5 requires later `M_K` to be derived directly from the positive Helmholtz functional and satisfy `M_K=M_K^dagger>0` without shifts/clipping; conforming input geometry must inherit `B_K=I`, `R_in,K=M_K`, and all physical particle/heat channels must use the same state space/quadratures — FROZEN DISCRETE PHYSICAL-GEOMETRY REQUIREMENTS.
- **DEC-577:** F2.5 branch commit `43de899b547b2ccc1d0c11ecb6788dfce6cb6b47`; Python CI #378 = `SUCCESS` — STABLE REPRODUCIBILITY CHECK.
- **DEC-578:** `Fusion F2.5 Discretization-Specification Integration Freeze 0.1 = STABLE — F2.5 DISCRETIZATION / QUADRATURE SPECIFICATION FROZEN / F2.6 DISCRETE OPERATOR-CHANNEL ALGEBRA GATE RELEASED` — NEW POST-PAPER ROLLBACK POINT.
- **DEC-579:** Next authorized task = `Fusion F2.6 — Discrete Generator / Helmholtz Metric / Physical Channel Reconstruction & Algebraic Balance Qualification Gate 0.1`. It must construct `A_K`, `M_K`, `Q_Gamma,K`, `Q_qi,K`, `Q_qe,K` on the frozen K0/K1/K2 ladder and test quasineutrality, positivity, Hermiticity, ambipolarity, conservative-advection adjoint structure and the complete F2.1 algebraic free-energy balance before any spectrum is inspected — ACTIVE SCIENTIFIC HANDOFF.
- **DEC-580:** F2.6 may not calculate eigenvalues/growth rates/pseudospectra, propagators/Gramians/cumulative objectives, optimizers/angles/gaps, scan parameters, run GENE, change F2.3/F2.4/F2.5 freezes, reopen R1, or open MODES/CONT/CASCADE/protected branches. Fusion remains the only active scientific branch; Paper-1 submission remains parked — ACTIVE / FROZEN PARALLELISM RULE.
