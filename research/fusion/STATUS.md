# Fusion Branch Status

**Last updated:** 2026-09-04  
**Branch:** `main`

## Current state

The post-paper roadmap has selected the Fusion branch as the next scientific program:

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

The first-paper scientific content remains frozen and is not part of this branch.

Existing Fusion derivation work is retained as pre-effect groundwork. In particular:

- `research/fusion/observable_dictionary.md` identifies gyrokinetic/free-energy and physical transport observables;
- `research/fusion/model_audit.md` ranks the reduced gyrofluid/gyrokinetic hierarchy;
- `research/fusion/minimal_model_derivation_audit.md` selects the Strintzi–Scott–Brizard electrostatic four-moment family as the preferred minimal derivation target;
- `research/fusion/four_moment_reduction_audit.md` selects anisotropic ZLR `R1` as the first derivation target, with FLR `R2` as a later validation deformation;
- B5.1–B5.3 derive source convention and closed slab/minimal-curvature generators;
- B5.4A derives a positive perturbation free-energy metric;
- B5.4B verifies that minimal curvature is conservative in the same metric and that the gradient-drive Hermitian part selects the ion-temperature-gradient thermal channel.

No finite-time Fusion objective-separation effect has been authorized by this status.

## Current unresolved primitive

The next safe scientific object is the independently derived physical ion radial heat/thermal-energy flux operator

\[
q_{i,k}=z_k^\dagger Q_{q_i,k}z_k.
\]

Its exact physical definition, sign, normalization, Fourier-pair convention and Hermitian matrix must be derived from the physical radial `E×B` heat/thermal-energy transport and then checked against the B5.4 free-energy balance.

It must **not** be defined retrospectively from `A^\dagger M+MA`.

## Active instruction

**Status:** `FUSION B5.5 ION HEAT-FLUX OBSERVABLE DERIVATION READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_ion_heat_flux_observable_derivation_gate_0_1.md`

On a bare `GO`, first read this STATUS and then execute only that committed instruction.

## Forbidden on this GO

Do not compute finite-time energy/heat operators, cumulative effect metrics, optimizer directions, angles, gaps, horizon dependence or parameter scans. Do not restore FLR, kinetic electrons, six-moment GEM or GENE in B5.5. Do not open Power Grid/Photonics collaboration work or modify the frozen first paper.

## Expected return state

One of:

- `B5.5 PASS — RETURN TO MASTER FOR ADMISSIBLE INPUT GEOMETRY / INPUT-COST GATE`;
- `B5.5 HOLD — RETURN TO MASTER FOR SOURCE/CONVENTION DECISION`;
- `B5.5 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Governance authority

- `research/master/first_paper_scientific_content_freeze_0_1.md`
- `research/master/post_paper_scientific_roadmap_gate_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / AWAIT GO.**