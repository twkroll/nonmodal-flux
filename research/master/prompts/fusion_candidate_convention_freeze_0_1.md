# Fusion F1.3 — Candidate / Convention Freeze 0.1

**Authority:** MASTER  
**Execution branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`  
**Mode:** pre-effect physical/convention freeze only.

## Objective

Freeze one exact reduced Fusion candidate and all conventions required for later numerical/spectral qualification, using only already-established physical/structural information. Do **not** inspect any finite-time free-energy-versus-heat objective separation.

The intended primary candidate is the already-derived **anisotropic-ZLR four-moment R1 minimal-curvature branch**, provided the full pre-effect derivation chain remains internally consistent. The slab R1 generator remains an analytic/limiting control and must not be selected as primary because of any prospective or inspected objective effect.

## Canonical inputs

Read and use the frozen lineage, including at minimum:

- `research/fusion/B5_1_source_convention.md`;
- the B5.2 slab/minimal-curvature linearizations;
- the B5.3 slab/minimal-curvature generators;
- `research/fusion/B5_4A_slab_free_energy_metric.md`;
- `research/fusion/B5_4B_curvature_free_energy_check.md`;
- `research/fusion/B5_5_ion_heat_flux_observable.md`;
- `research/fusion/fusion_admissible_input_geometry_input_cost_gate_0_1.md`;
- `research/master/fusion_b5_5_heat_flux_observable_integration_freeze_0_1.md`;
- `research/master/fusion_f1_2_input_geometry_integration_freeze_0_1.md`.

## Required freeze contents

Freeze explicitly, with all formulas and units/normalizations needed for exact reproducibility:

1. selected primary reduced candidate and role of the slab control;
2. state ordering and dimensional/nondimensional variable definitions;
3. Fourier convention and admissible nonzonal sector;
4. electrostatic/polarization closure and all coefficients entering it;
5. exact generator `A_k` for the selected primary candidate;
6. positive free-energy metric `M_k` and normalization of `W_k`;
7. physical signed heat-flux matrix `Q_{q_i,k}` with sign/prefactor convention;
8. `B=I_4`, `R_in=M_k`, and the state-admissibility—not actuator—interpretation;
9. equilibrium density/temperature-gradient convention and curvature-frequency convention;
10. parallel wavenumber convention and any retained/suppressed geometric terms;
11. dissipation/closure choice required for a later finite-dimensional stable/qualified pilot;
12. one physical parameter point selected on source/model grounds only, before finite-time effect inspection;
13. time normalization `tau_ref` and the dimensional mapping needed later;
14. all exact algebraic identities that must be checked at the qualification stage.

If a unique physically defensible value or convention is not already fixed by the lineage, choose it only from source convention, canonical benchmark usage, dimensional consistency, or minimal-model fidelity. Document the reason. Do not choose any value by inspecting or anticipating a large optimizer angle, heat-transport gap, transient growth, or cumulative flux.

## Mandatory anti-bias rule

No finite-time propagator/Gramian/channel calculation is allowed. Do not compute:

- `K_M(T)` or `K_q(T)`;
- cumulative extrema;
- energy or heat optimal vectors/subspaces;
- principal angles;
- performance gaps;
- horizon dependence;
- parameter scans or stability-rescue searches informed by finite-time effect size.

A purely spectral/algebraic check needed to verify that the frozen candidate is well-defined may be stated symbolically, but **numerical/spectral qualification belongs to the next gate** and must not be executed here unless required only to detect an invalid convention. Do not tune a parameter point for stability here if that would amount to a search; instead freeze a source-/benchmark-motivated point and leave qualification to F1.4.

## Required outcome classification

Return exactly one of:

- `F1.3 PASS — CANDIDATE/CONVENTION FROZEN — RETURN TO MASTER FOR NUMERICAL/SPECTRAL QUALIFICATION`;
- `F1.3 HOLD — RETURN TO MASTER FOR A SPECIFIC CONVENTION DECISION`;
- `F1.3 FAIL — RETURN TO MASTER`.

## Canonical output

Write the complete result to:

`research/fusion/fusion_candidate_convention_freeze_0_1.md`

Update:

`research/fusion/STATUS.md`

Commit the result and status. Report the canonical path, full commit hash, and CI status if available, then STOP.

## Forbidden branch expansion

Do not restore FLR/R2, kinetic electrons, six-moment GEM, GENE/local gyrokinetics, MODES, CONT, CASCADE, Power Grids, Photonics/Waves, or Paper-1 submission work. Do not create a second candidate from effect considerations.

**STOP after F1.3; no branch-side self-authorization of the next gate.**