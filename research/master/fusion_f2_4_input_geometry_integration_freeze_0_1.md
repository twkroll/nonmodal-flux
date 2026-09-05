# Fusion F2.4 Kinetic Input-Geometry / Input-Cost Integration Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER  
**Status:** `STABLE — F2.4 KINETIC INPUT GEOMETRY FROZEN / F2.5 DISCRETIZATION-SPECIFICATION GATE RELEASED`

## Scope

This MASTER freeze integrates only the completed `Fusion F2.4 — Kinetic Admissible Input Geometry / Input-Cost Freeze 0.1`. It performs no phase-space discretization, no discrete operator construction, no spectrum calculation, no GENE execution and no finite-time objective inspection.

Canonical branch result:

`research/fusion/fusion_f2_4_kinetic_input_geometry_input_cost_freeze_0_1.md`

Branch verdict:

\[
\boxed{\text{F2.4 PASS — KINETIC INPUT GEOMETRY / INPUT COST FROZEN — RETURN TO MASTER}}
\]

Branch commit:

`eabc44856458c7450946050c8ab04362904ef9ac`

Python CI #371 = `SUCCESS`.

## Frozen continuous admissible state space

The physically admissible input space is the full finite-Helmholtz-free-energy tangent space of the already reduced F2-R model,

\[
\mathcal H_{F2}=\overline{\mathcal D_0}^{\|\cdot\|_{F2}},
\qquad
\|x\|_{F2}^2=\langle x,\mathcal M_{F2}x\rangle=2W[x].
\]

`D0` already contains the physical reductions frozen upstream: the fixed nonzonal Fourier block, finite-FLR ion kinetic phase space, trapped nonadiabatic electron state only, leading-order `g_e^pass=0`, bounce/orbit regularity, ballooning-space conventions, and the quasineutrality-reconstructed electrostatic field.

Quasineutrality is a field-reconstruction map

\[
\phi=P_{\rm QN}(g_i,g_e^{\rm tr}),
\]

not a proper-subspace constraint on the reduced kinetic state. No extra particle-number, charge, momentum, energy-moment, gauge, parity or transport-neutral condition is required in the frozen nonzonal block.

## Frozen continuous input pair

The physically correct continuous CORE input pair is therefore

\[
\boxed{
B=I_{\mathcal H_{F2}},
\qquad
R_{\rm in}=\mathcal M_{F2}.
}
\]

The fixed input budget is initial Helmholtz free energy:

\[
\langle u,R_{\rm in}u\rangle=2W(0).
\]

This is a mathematical initial-value geometry on the reduced physical model. It is not a claim that arbitrary ion and trapped-electron distribution perturbations can be independently prepared by laboratory actuators.

## Discretization constraints inherited from F2.4

Any later discrete state space must approximate `H_F2` without changing physical admissibility. In particular it must preserve ion and trapped-electron directions, both ion orbit-sign branches where present, no parity reduction, no artificial moment-null constraints and no transport-neutral projection.

The electrostatic potential must remain a reconstructed/algebraically constrained field rather than an extra input coordinate. The discrete Helmholtz metric must satisfy

\[
M_K=M_K^\dagger\succ0
\]

on the physical discrete state after elimination of algebraic field variables and spurious null directions. No diagonal loading may be used to manufacture positivity.

For a conforming coefficient representation the discrete input pair must inherit

\[
B_K=I,
\qquad
R_{{\rm in},K}=M_K,
\]

or the congruent relation `R_in,K=B_K^\dagger M_K B_K` if a nontrivial inclusion/basis map is used.

Discrete particle and species heat channels must later be reconstructed from the already frozen physical radial flux integrals on the same state space and may not be used to prune the input space.

## MASTER gate-order decision

The next task is split into a pure discretization/convergence-specification gate before any discrete generator/channel construction.

Reason: the F2-R kinetic state is high-dimensional and contains ballooning-line truncation, ion velocity/orbit-sign structure, trapped-electron energy/pitch/well coordinates, bounce singularities and quasineutrality elimination. Freezing these numerical representation choices first provides a clean rollback point and prevents later operator algebra or spectral behavior from influencing cutoffs, quadrature or basis choices.

Thus the next gate may freeze the numerical state-space architecture and a resolution/convergence ladder, but it may not yet calculate spectra or finite-time objectives. Discrete operator/channel reconstruction and algebraic balance checks remain a subsequent gate.

## Next task released

**Fusion F2.5 — Structure-Preserving Phase-Space Discretization / Quadrature Specification Freeze 0.1**

Canonical handoff:

`research/master/prompts/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`

## Rollback / STOP

This file is a new protected post-paper rollback point after the F2.3 physical-parameter integration freeze.

R1 remains a frozen structural no-go control. F2.3 may not be retuned and the F2.4 input geometry may not be modified after later numerical or finite-time inspection.

**STOP — F2.4 INTEGRATED; F2.5 MAY PROCEED ONLY VIA THE COMMITTED HANDOFF.**
