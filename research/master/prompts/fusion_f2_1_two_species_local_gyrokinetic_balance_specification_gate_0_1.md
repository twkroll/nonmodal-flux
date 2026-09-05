# Fusion F2.1 — Balance-Complete Two-Species Local-Gyrokinetic Candidate / Balance Specification Gate 0.1

**Date:** 2026-09-05  
**Authority:** MASTER  
**Execution branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

## Purpose

Open the first higher-fidelity Fusion gate after the frozen R1 structural no-go. Select and specify one physically justified **two-species local gyrokinetic** lineage using balance completeness, source fidelity and tractability only.

This gate exists because the completed literature audit established that:

- the R1 one-channel collisionless affine collapse is a recognizable standard-balance limit;
- physical collisions can add a positive free-energy sink;
- nonadiabatic electrons can add an independent electron free-energy drive;
- conservative FLR corrections alone do not generically create an independent source/sink and must not be used as an effect-motivated rescue.

No finite-time objective-separation effect has yet been authorized in the higher-fidelity lineage.

## Required inputs

Read and use as canonical authority:

- `research/master/fusion_f1_4_marginal_structural_integration_freeze_0_1.md`;
- `research/literature/fusion_r1_structural_redundancy_fidelity_breaking_literature_audit_0_1.md`;
- `research/master/fusion_r1_structural_redundancy_literature_integration_freeze_0_1.md`;
- `research/core_mathematical_freeze_0_1.md`;
- the earlier frozen Fusion model/free-energy/observable derivation files needed for notation and provenance.

## Task

Create a single canonical report:

`research/fusion/fusion_f2_1_two_species_local_gyrokinetic_balance_specification_gate_0_1.md`

The report must do all of the following.

### 1. Select the fidelity architecture

Choose one primary reduced two-species local-gyrokinetic candidate using only physical/source criteria. The leading candidate from the frozen audit is a finite-ion-FLR gyrokinetic ion model coupled to nonadiabatic bounce-averaged/trapped-electron dynamics, with fully kinetic two-species local gyrokinetics retained as the higher-fidelity reference.

You may accept this hierarchy if it closes consistently, or return `HOLD` with a specific physical reason if a different choice is required. Do not compare candidates by expected optimizer separation, nonnormality or effect size.

### 2. Specify state variables and phase-space representation

Define the exact perturbation variables for ions and electrons, including velocity-space coordinates, gyroaveraging/bounce averaging, quasineutrality/electrostatic closure and the local geometry assumptions needed for the reduced candidate.

State clearly which variables are dynamical and which are reconstructed.

### 3. Derive the exact free-energy functional

Write the positive free-energy/Helmholtz functional for the chosen reduced candidate and identify the corresponding positive metric/operator conceptually. If the state remains continuous in velocity space, keep the operator in functional form; do not discretize it numerically in F2.1.

Establish positivity under the stated admissible sector and conventions.

### 4. Derive the balance decomposition

Derive the exact linear free-energy balance in a form that explicitly separates all physically independent terms, schematically

\[
\frac{dW}{dt}
=\sum_s\big(g_{n,s}\,\Gamma_s+g_{T,s}\,q_s\big)-D_{\rm coll}
\]

or the correct source-faithful analogue for the selected model.

For every term, freeze:

- sign convention;
- physical meaning;
- normalization;
- whether it is a particle-flux, heat-flux, species-exchange, conservative redistribution, or positive dissipation contribution;
- whether it is independent or constrained by quasineutrality/closure.

Do not infer channel operators backwards solely from `A^dagger M + M A`; use the physical transport definitions and then verify the balance.

### 5. Collision treatment

Choose a physically justified collision treatment for the candidate architecture.

Preferred if feasible: an H-theorem-compatible linearized gyrokinetic/Fokker–Planck collision operator with explicit conservation properties and nonnegative entropy/free-energy dissipation.

If a collisionless reduced candidate is scientifically preferable, justify this on physical/model grounds and state explicitly which balance-changing mechanism remains through nonadiabatic electrons. Do not choose collisions merely to break the R1 identity.

### 6. FLR role

Specify the finite-ion-FLR operators required by the chosen gyrokinetic model and state exactly whether they modify only conservative geometry/free energy or also participate in the physical transport/supply definitions. Preserve the literature-audit conclusion that FLR alone is not assumed to break the R1 affine identity.

### 7. Reduced candidate vs higher-fidelity reference

Define a strict hierarchy:

- primary reduced candidate for subsequent qualification;
- higher-fidelity fully kinetic two-species local-GK/GENE-compatible reference;
- any conservative FLR-only/R1 limit retained only as control.

State which reductions connect the levels and what balance terms disappear in each limit.

### 8. Determine whether structural nonredundancy is now *possible in principle*

Using only the derived balance structure, classify whether the chosen F2.1 model has at least one independent source/sink beyond the single R1 ion-heat term, so that the exact R1 two-operator affine identity is no longer forced.

This is a structural possibility test only. Do **not** calculate finite-time objectives, optimizers, angles or performance gaps and do not claim that the objectives will be substantially different.

### 9. List the next unresolved pre-effect objects

Identify exactly what must still be frozen before any numerical execution, including as applicable:

- local geometry / magnetic configuration;
- equilibrium gradients and physical parameter point;
- phase-space discretization;
- collision frequencies/operator parameters;
- admissible initial-condition geometry `B` and input cost `R_in` for the kinetic state;
- numerical/spectral qualification;
- transport-channel operator reconstruction after discretization.

Do not solve these later gates in F2.1 unless they are unavoidable for internal consistency.

## Absolute prohibitions

Do not:

- compute `e^{At}`, finite-time Gramians or cumulative CORE operators;
- compute energy/heat/particle optimizers, principal angles, objective gaps or transient-growth curves;
- scan parameters, wavenumbers, collision rates, trapped-particle fractions or model variants;
- choose a model or closure because it is expected to maximize objective separation;
- retune or repair the frozen R1 candidate;
- run GENE or any gyrokinetic simulation;
- discretize velocity space for numerical optimization;
- open MODES, CONT, CASCADE, Power Grids or Photonics;
- modify Paper 1.

## Required verdict

Return exactly one of:

- `F2.1 PASS — TWO-SPECIES GK CANDIDATE/BALANCE SPECIFIED — RETURN TO MASTER`;
- `F2.1 HOLD — SPECIFIC MODEL/BALANCE DECISION REQUIRED — RETURN TO MASTER`;
- `F2.1 FAIL — RETURN TO MASTER`.

Update `research/fusion/STATUS.md` in the same work package so that it contains no branch-side self-authorized next gate.

Commit the result and STATUS, report the canonical path and full commit SHA, then:

**STOP / RETURN TO MASTER.**
