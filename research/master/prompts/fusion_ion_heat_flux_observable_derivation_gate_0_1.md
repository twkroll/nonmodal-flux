# Fusion Ion Heat-Flux Observable Derivation Gate 0.1 — Branch Instruction

**Authority:** MASTER / `research/master/post_paper_scientific_roadmap_gate_0_1.md`  
**Branch:** Fusion  
**Scope:** B5.5 physical observable derivation only; no finite-time objective calculation.

## Read first

Read, in this order:

1. `research/fusion/STATUS.md`;
2. `research/master/post_paper_scientific_roadmap_gate_0_1.md`;
3. `research/fusion/B5_1_source_convention.md`;
4. `research/fusion/B5_2A_slab_linearization.md`;
5. `research/fusion/B5_2B_curvature_linearization.md` and the B5.2B source-audit notes;
6. `research/fusion/B5_3A_slab_generator.md`;
7. `research/fusion/B5_3B_curvature_generator.md`;
8. `research/fusion/B5_4A_slab_free_energy_metric.md`;
9. `research/fusion/B5_4B_curvature_free_energy_check.md`;
10. `research/fusion/observable_dictionary.md` and the prior B3/B4 audits only as supporting provenance.

Git is the canonical source of truth.

## Scientific objective

Complete B5.5 by deriving the **physical signed ion radial heat/thermal-energy transport observable** for the already-fixed anisotropic-ZLR four-moment R1 reduction.

The target must come directly from the physical radial `E×B` transport of the thermodynamic ion energy/heat quantity appropriate to the frozen source convention. Do not guess a pressure combination from the desired matrix structure.

Derive an exact Fourier-space form

\[
q_{i,k}=z_k^\dagger Q_{q_i,k}z_k,
\qquad
Q_{q_i,k}=Q_{q_i,k}^\dagger,
\]

for the frozen state

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\]

including all sign, normalization and Fourier-pair factors.

## Required derivation content

Document explicitly:

1. the dimensional physical heat/thermal-energy flux definition being used and why it is the correct observable for this reduced ion model;
2. the radial `E×B` velocity under the frozen coordinate/sign convention;
3. the exact thermodynamic combination of `N`, `P_parallel`, `P_perp` or `Theta_parallel`, `Theta_perp` entering the flux;
4. the complex single-`k` and real conjugate-pair conventions;
5. the dimensional and nondimensional prefactors;
6. the final Hermitian matrix `Q_{q_i,k}` in the frozen state ordering;
7. whether the same `Q_{q_i,k}` applies to both slab and minimal-curvature generators, and why;
8. its rank/signature/indefiniteness or, if it is not indefinite, the exact algebraic reason;
9. the relation to the already-established B5.4B free-energy injection identity;
10. the status of the particle-flux channel under the same adiabatic-electron closure: confirm the previously identified collapse/non-independence without inventing a new particle channel.

## Mandatory consistency gate

Using only the already-derived `A_k` and `M_k`, verify algebraically that the profile-drive Hermitian part can be written with the newly derived physical heat-flux matrix and the correct thermodynamic-force coefficient/sign. The goal is an identity of the form

\[
A_k^\dagger M_k+M_kA_k
=g_T\,Q_{q_i,k}
\]

or the convention-correct equivalent, with any common factor from the project `1/2` quadratic-form convention made explicit.

Do **not** force the identity by redefining `Q_{q_i,k}` from `A^\dagger M+MA`. The observable must be independently derived first from the physical flux and only then compared with the balance.

If the direct physical derivation and the energy-balance coefficient cannot be reconciled exactly under one transparent convention, the gate is `FAIL/STOP`; report the mismatch and return to MASTER.

## Structural checks

Check and report:

- `Q_{q_i,k}=Q_{q_i,k}^\dagger`;
- nontriviality;
- signature / signed character;
- coordinate/state-order consistency;
- invariance of the physical value under the permitted real-field conjugate reconstruction;
- slab/curvature consistency;
- dimensional units and nondimensionalization.

A small hand-constructed algebraic sign witness may be used **only** to validate the derived instantaneous flux sign. It must not be a finite-time optimizer or parameter search.

## Absolute prohibitions

Do not:

- compute `K_M(T)`, `K_q(T)`, cumulative Gramians for an effect study, optimizer directions, principal angles, performance gaps or finite-time gains;
- choose or tune a parameter point from any objective-separation result;
- run a parameter sweep, horizon scan or stability search;
- introduce FLR/R2 physics, kinetic electrons, six-moment GEM, GENE, new closures or a new model branch;
- change the already-derived `A_k` or `M_k` merely to make the flux identity work;
- perform a new novelty/prior-art search;
- reopen Paper 1, Climate-B, Power Grids or Photonics;
- silently promote a balance term into a primitive physical flux without the independent derivation required above.

## Gate outcomes

Use exactly one:

- `PASS — PHYSICAL ION HEAT-FLUX OPERATOR DERIVED AND BALANCE-CONSISTENT`;
- `HOLD — SOURCE/CONVENTION AMBIGUITY REQUIRES MASTER DECISION`;
- `FAIL — PHYSICAL HEAT-FLUX/BALANCE CONSISTENCY NOT ESTABLISHED`.

A weak/null signed structure is not a failure if it is the correct physical result. Do not modify the model to obtain an indefinite or stronger channel.

## Required files

Create:

`research/fusion/B5_5_ion_heat_flux_observable.md`

Update:

`research/fusion/STATUS.md`

If PASS, `STATUS.md` must return to MASTER and must **not** self-authorize finite-time execution. The recommended next step may be an admissible-input geometry/input-cost gate, but MASTER must release it separately.

Commit the result and updated status, report the canonical path and full commit hash, then STOP.

**STOP — B5.5 ONLY; NO FINITE-TIME EFFECT INSPECTION.**