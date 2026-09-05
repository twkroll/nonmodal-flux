# Fusion F2.4 — Kinetic Admissible Input Geometry / Input-Cost Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER  
**Execution branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

## Objective

Freeze the physically admissible initial-condition geometry and initial perturbation cost for the already-frozen F2-R continuous kinetic model and F2.3 single physical point, before any phase-space discretization, spectrum calculation or finite-time objective construction.

This is a **pre-effect geometry gate**. It must determine the continuous input pair

\[
(B,R_{\rm in})
\]

from physical admissibility and preparation-cost semantics only.

## Canonical inputs

Read and preserve:

- `research/master/fusion_f2_1_two_species_gk_balance_integration_freeze_0_1.md`;
- `research/master/fusion_f2_2_geometry_convention_integration_freeze_0_1.md`;
- `research/master/fusion_f2_3_physical_parameter_integration_freeze_0_1.md`;
- `research/fusion/fusion_f2_1_two_species_local_gyrokinetic_balance_specification_gate_0_1.md`;
- `research/fusion/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`;
- `research/fusion/fusion_f2_3_physical_parameter_freeze_0_1.md`;
- `research/core_mathematical_freeze_0_1.md`;
- the shared MASTER Prompt Handoff Protocol.

The continuous reduced state is

\[
x=(g_i(l,E_i,\mu_i,\sigma),\,g_e^{\rm tr}(E_e,\lambda,w)),
\]

with `phi` reconstructed from quasineutrality and positive Helmholtz metric

\[
\mathcal M_{F2}\succ0.
\]

## Required work

Determine and freeze, in continuous/operator form only:

1. the physically admissible tangent-space of initial perturbations for the reduced F2-R initial-value problem;
2. whether arbitrary finite-free-energy `(g_i,g_e^tr)` perturbations consistent with quasineutrality are admissible, or whether exact physical constraints require a proper subspace;
3. the role of quasineutrality: distinguish reconstructed-field closure from any genuine restriction on the kinetic state;
4. whether particle-number, charge, momentum, energy, gauge, parity, ballooning-boundary or trapped/passing constraints impose linear restrictions on initial data in this local collisionless model;
5. the exact continuous input operator `B` (identity on the admissible Hilbert space if justified, otherwise a physically derived injection/projection map);
6. the exact initial cost `R_in`, with the Helmholtz free-energy metric restricted to the admissible input space as the leading candidate only if physically justified;
7. whether any null/gauge directions remain after quasineutrality elimination and how they are excluded without numerical regularization;
8. whether the admissible space preserves both ion and trapped-electron kinetic directions needed by the F2.1 multi-channel balance;
9. the physical meaning of the fixed-input budget and what it does **not** imply experimentally;
10. the exact requirements that the later discretization must preserve so that discrete `B_K` and `R_{in,K}` converge to this continuous geometry.

Explicitly evaluate, but do not force, the candidate

\[
B=I_{\mathcal H_{F2}},
\qquad
R_{\rm in}=\mathcal M_{F2}.
\]

If this pair is valid, state the admissible Hilbert space precisely rather than writing an unconstrained formal identity. If it is not valid, derive the minimal physically justified restriction.

## Anti-bias and forbidden work

Do **not**:

- choose an input subspace because it is expected to produce larger or smaller objective separation;
- impose transport neutrality or remove source-channel directions unless physically required;
- impose parity reduction;
- discretize `theta`, energy, pitch, sign or well coordinates;
- choose ballooning cutoffs or quadrature rules;
- construct discrete `A`, `M`, `Q_Gamma`, `Q_qi`, `Q_qe`;
- calculate eigenvalues, growth rates, propagators, Gramians, cumulative operators, optimizer directions, principal angles or performance gaps;
- scan initial-condition subspaces, parameters or wavenumbers;
- run GENE or another gyrokinetic solver;
- add collisions to F2-R;
- reopen or retune R1, F2.2 or F2.3;
- open MODES, CONT, CASCADE, Power Grid, Photonics or Paper-1 work.

## Required output

Create:

`research/fusion/fusion_f2_4_kinetic_input_geometry_input_cost_freeze_0_1.md`

Update `research/fusion/STATUS.md` in the same work package.

Return exactly one of:

- `F2.4 PASS — KINETIC INPUT GEOMETRY / INPUT COST FROZEN — RETURN TO MASTER`;
- `F2.4 HOLD — PHYSICAL INPUT-SPACE DECISION REQUIRED — RETURN TO MASTER`;
- `F2.4 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Expected next MASTER decision after PASS

If F2.4 passes, MASTER should normally release a structure-preserving phase-space discretization / discrete physical-channel reconstruction gate. That later gate must inherit the continuous `(B,R_in)` freeze and may not choose a basis to alter admissibility or objective behavior.

**STOP / RETURN TO MASTER AFTER F2.4.**
