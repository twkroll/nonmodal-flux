# Fusion F2.5 — Structure-Preserving Phase-Space Discretization / Quadrature Specification Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER  
**Execution branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

## Objective

Freeze one structure-preserving numerical representation and convergence ladder for the already-frozen F2-R continuous model before any discrete spectrum, finite-time objective, optimizer or effect-size calculation is opened.

The frozen continuous inputs are:

- F2.1 two-species local-GK architecture and Helmholtz/transport balance;
- F2.2 circular `s-alpha` ballooning-space geometry and trapping/bounce conventions;
- F2.3 single CBC-compatible physical point;
- F2.4 full finite-free-energy input space with `B=I_HF2` and `R_in=M_F2`.

This gate is numerical-architecture-only. It must not select cutoffs, grids or basis functions by spectral stability, growth rate, nonnormality, transport magnitude or expected objective separation.

## Required work

Freeze and document exactly one primary discretization package, plus a predeclared refinement ladder, covering:

1. ballooning-line truncation and boundary treatment consistent with the finite-free-energy `theta in R` domain;
2. parallel-coordinate grid/basis and differentiation strategy for ions;
3. ion velocity-space coordinates, energy/speed and pitch/magnetic-moment quadrature, both `sigma` branches, and turning-point treatment;
4. trapped-electron energy/pitch/well representation, bounce-point/separatrix handling and orbit-time-weighted bounce quadrature;
5. treatment of the measure-zero trapped/passing separatrix without inserting a spurious degree of freedom;
6. discrete representation of finite ion FLR `J0i(theta,v_perp)` and polarization terms;
7. quasineutrality elimination or exact algebraic constraint handling so `phi` never becomes an independent input direction;
8. discrete free-energy inner-product construction target and conditions required for `M_K=M_K^dagger>0` after physical-state elimination;
9. inheritance of the F2.4 input geometry: `B_K=I`, `R_in,K=M_K` for a conforming basis, or the congruent equivalent for a nontrivial inclusion map;
10. a primary resolution and at least two refinement levels chosen before any spectrum/effect inspection, with explicit convergence observables for later qualification;
11. checks of the reduced-electron ordering `k_perp rho_e << 1` on the retained numerical support;
12. exact bookkeeping needed later to reconstruct `Q_Gamma`, `Q_qi`, and `Q_qe` from the physical flux integrals on the same discrete state space.

The result must distinguish clearly between:

- frozen numerical representation choices;
- primary/refinement resolutions;
- algebraic verification targets for the later discrete-operator gate;
- quantities still forbidden until later qualification.

## Anti-bias / forbidden work

Do not:

- scan or compare discretizations by eigenvalues, growth rates, transient growth, pseudospectra, nonnormality, transport output or objective separation;
- change the F2.3 physical point;
- change F2.4 `B` or `R_in`;
- add collisions or damping to F2-R;
- construct finite-time propagators, Gramians, cumulative CORE operators, optimizer directions, angles or performance gaps;
- run GENE or another GK solver;
- reopen R1, FLR-only rescue, MODES, CONT, CASCADE, Power Grid, Photonics or Paper-1 work.

A minimal algebraic prototype may be used only if needed to verify that the proposed representation is internally well-defined; it must not be used to inspect the spectrum or finite-time behavior. If a representation cannot preserve the physical state space or quasineutrality/free-energy structure without ad hoc regularization, return `HOLD` rather than tuning it.

## Required output

Create:

`research/fusion/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`

Update `research/fusion/STATUS.md` in the same work package.

Return exactly one of:

- `F2.5 PASS — STRUCTURE-PRESERVING DISCRETIZATION / QUADRATURE SPECIFICATION FROZEN — RETURN TO MASTER`;
- `F2.5 HOLD — DISCRETIZATION/STRUCTURE DECISION REQUIRED — RETURN TO MASTER`;
- `F2.5 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Expected next MASTER decision after PASS

If F2.5 passes, MASTER should release a separate discrete operator/channel reconstruction and algebraic balance qualification gate before any spectral or finite-time calculation.

**STOP / RETURN TO MASTER AFTER F2.5.**
