# Fusion F1.2 — Admissible Input Geometry / Input-Cost Gate 0.1

**Authority:** MASTER / `research/master/fusion_b5_5_heat_flux_observable_integration_freeze_0_1.md`  
**Branch:** `research/fusion/`  
**Scope:** determine the physically admissible initial-perturbation geometry and input-cost metric for the already-frozen R1 Fusion state/channel. This is a pre-effect gate only.

## Read first

- `research/fusion/STATUS.md`;
- `research/master/post_paper_scientific_roadmap_gate_0_1.md`;
- `research/master/fusion_b5_5_heat_flux_observable_integration_freeze_0_1.md`;
- `research/fusion/B5_1_source_convention.md`;
- `research/fusion/B5_3A_slab_generator.md` and `B5_3B_curvature_generator.md` as needed for state meaning only;
- `research/fusion/B5_4A_slab_free_energy_metric.md`;
- `research/fusion/B5_4B_curvature_free_energy_check.md`;
- `research/fusion/B5_5_ion_heat_flux_observable.md`;
- `research/master/prompt_handoff_protocol_0_1.md`.

## Absolute prohibitions

Do not:

- compute any finite-time energy or heat-transport operator;
- compute optimizers, principal angles, performance gaps, horizon dependence or cumulative transport extrema;
- search parameter values, horizons, wavenumbers or closures for a large separation effect;
- restore FLR, kinetic electrons, six-moment GEM, GENE, extra channels or new model fidelity;
- modify the frozen heat-flux operator `Q_{q_i,k}` or free-energy metric `M_k` merely to simplify the input geometry;
- force `B^\dagger Q_{q_i,k}B=0` unless a physical preparation argument independently requires it;
- assume `B=I` or `R_in=M` without explicitly justifying the physical interpretation of an admissible initial perturbation and its cost;
- open Power Grid/Photonics collaboration work or modify Paper 1.

## Scientific question

For the already-fixed R1 tangent state

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad \Phi=\mathcal C_kN,
\]

and positive free-energy metric `M_k`, determine what initial perturbations are physically admissible and how their input amplitude/cost should be measured before any finite-time objective comparison is allowed.

The gate must distinguish clearly between:

1. **state-space initial-condition admissibility** — a mathematical/physical ensemble of allowed perturbations at `t=0`; and
2. **actuator/preparation realizability** — a narrower experimentally imposed input mechanism, if such a mechanism is actually part of the proposed Fusion question.

Do not conflate these two meanings.

## Required analyses

### 1. State and constraint geometry

Document the physical meaning and units/normalization of all four state components and the eliminated electrostatic constraint. Determine whether the frozen closure/polarization relation imposes any additional linear constraint on the four-component perturbation state beyond `Phi=C_k N` already used in the model.

### 2. Candidate admissible spaces

Identify only physically defensible candidate initial-condition spaces. At minimum test whether the following interpretation is legitimate:

- arbitrary perturbations in the closed R1 tangent state subject to the already-eliminated field constraint, represented by `B=I` in the frozen state coordinates.

If full-state admissibility is not physically defensible, derive the minimal physically motivated lower-rank `B` instead. Every column of `B` must have a stated physical preparation meaning; do not select columns from eigenvectors or effect metrics.

If more than one physically plausible geometry remains, compare them only using pre-effect physical/structural criteria and either select uniquely or return `HOLD` to MASTER. Do not carry multiple geometries forward merely to choose later from effect size.

### 3. Input-cost metric

For each defensible `B`, derive a positive input metric `R_in` from the physical meaning of the admissible perturbation budget.

Explicitly test whether the natural free-energy budget implies

\[
R_{\rm in}=B^\dagger M_k B
\]

(or `R_in=M_k` when `B=I`) in the frozen coordinate convention. If a different cost is physically required, derive it and explain why it is not an effect-oriented choice.

Require

\[
R_{\rm in}=R_{\rm in}^\dagger\succ0
\]

on the admitted input coordinates.

### 4. Rank and nontriviality

Report `rank(B)`. A rank-one geometry cannot support a nontrivial comparison of distinct optimal input directions. If the only physically defensible geometry has rank one, return `HOLD` or `FAIL` for the intended FUSION-F1 objective-comparison pilot rather than enlarging it ad hoc.

### 5. Instantaneous channel geometry as diagnostic only

Compute only the algebraic instantaneous restriction

\[
B^\dagger Q_{q_i,k}B
\]

needed to classify whether the admissible space is transport-neutral, indefinite, semidefinite or otherwise restricted. This is allowed because it is an instantaneous structural property of the already-frozen physical channel, not a finite-time effect.

Do not choose or alter `B` to manufacture neutrality or indefiniteness.

If `B^\dagger Q B=0`, record the resulting generation-order question for later; do not compute the finite-time hierarchy here unless already directly implied by frozen algebra.

### 6. Coordinate/basis consistency

Show that the physical admissible subspace and input cost are invariant under a change of basis within `range(B)`: `B -> B S` with the corresponding transformed input metric. Distinguish this from changing the physical admissible subspace itself.

### 7. Slab versus minimal-curvature applicability

State whether the same `B,R_in` interpretation applies to both already-derived slab and minimal-curvature R1 generators. If not, explain the physical reason and return to MASTER before selecting one based on any effect.

## PASS / HOLD / FAIL criteria

Return **PASS** only if all of the following are established without finite-time effect inspection:

- one physical admissible perturbation space is selected or uniquely justified;
- `B` is explicit in the frozen state ordering;
- `R_in` is explicit, Hermitian and positive definite;
- `rank(B)>=2` for the intended objective-comparison program;
- field/closure constraints are respected;
- no choice depends on optimizer separation or finite-time performance;
- slab/minimal-curvature applicability is clear;
- instantaneous `B^\dagger Q B` geometry is documented but not used for cherry-picking.

Return **HOLD** if a scientifically consequential choice between multiple input geometries/costs remains unresolved. Return **FAIL** if no physically defensible rank-at-least-two geometry/cost exists for the intended FUSION-F1 pilot.

## Required output

Create and commit:

`research/fusion/fusion_admissible_input_geometry_input_cost_gate_0_1.md`

The document must include:

- scope and forbidden actions;
- state/constraint geometry;
- candidate admissible spaces considered;
- selected `B` and `R_in` or explicit unresolved alternatives;
- rank and positivity checks;
- instantaneous restricted-channel classification;
- coordinate/basis consistency;
- slab/curvature applicability;
- PASS/HOLD/FAIL verdict;
- allowed and forbidden interpretations;
- exact open issues;
- final STOP.

Update `research/fusion/STATUS.md` and commit both result and status. Report the canonical path, full commit hash and CI status if available.

Expected return state:

- `F1.2 PASS — RETURN TO MASTER FOR FUSION CANDIDATE/CONVENTION FREEZE`;
- `F1.2 HOLD — RETURN TO MASTER FOR INPUT-GEOMETRY DECISION`;
- `F1.2 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

**STOP — PRE-EFFECT INPUT-GEOMETRY GATE ONLY.**