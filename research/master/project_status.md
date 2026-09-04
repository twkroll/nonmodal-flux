# MASTER Project Status

**Last updated:** 2026-09-04  
**Branch:** `main`

## Global scientific savepoints

- CORE Mathematical / Integration / Interpretation freezes: **STABLE**.
- Plasma/D10-ZF Pilot 0.2: **P2-A**, strong primary domain anchor.
- Neuro/CMC Pilot 0.1: **NEURO-STRONG**, strong cross-domain demonstrator.
- Climate-A/Phillips-QG Pilot 0.1: **CLIM-WEAK**, robust weak/contrast case.
- Climate-B/Bickley-jet one-shot Pilot 0.1: **CLIM-B-FAIL — resolution robustness failure**, result frozen.
- Cross-Domain Result Integration & Freeze 0.1: **STABLE**.
- Cross-Domain Application Literature Positioning Audit 0.1: **COMPLETE**.
- Cross-Domain Manuscript Positioning & Claim Freeze 0.1: **STABLE**.
- Manuscript Structure Freeze 0.2: **STABLE**.
- Manuscript Revision 0.4: **COMPLETE — PASS**.
- Submission Readiness Gate 0.1: **PASS WITH AUTHOR/METADATA ITEMS — SCIENTIFIC PACKAGE READY**.
- First Paper Scientific Content Freeze 0.1: **STABLE — SCIENTIFIC CONTENT BASELINE FROZEN / SUBMISSION TRACK PARKED**.
- Post-Paper Scientific Roadmap Gate 0.1: **COMPLETE — FUSION-F1 SELECTED**.

## First-paper status

The scientific content of Paper 1 is frozen. Draft 0.4 is the current scientific-content baseline but not final prose. The user intends to revise the text personally before any eventual submission.

Submission preparation is parked. No APS portal, cover letter, author-list, OA/APC, archive DOI/release/license, or production-formatting work is active.

## New primary scientific program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

The program asks whether finite-horizon signed ion heat-transport optimality differs meaningfully from free-energy optimality in an energy-consistent fusion hierarchy and whether any distinction survives controlled increases in physical fidelity.

Planned hierarchy:

\[
\text{anisotropic ZLR four-moment gyrofluid}
\rightarrow
\text{FLR gyrofluid}
\rightarrow
\text{parallel/flux-tube or local gyrokinetic/GENE-compatible validation}.
\]

This is not selected because Paper 1 showed a large effect. It is selected because the Fusion branch already has a strong pre-effect physical derivation chain and the next unresolved object is a primitive physical heat-flux operator that can pass or fail before any finite-time effect is inspected.

## Fusion pre-effect groundwork already present

- `research/fusion/observable_dictionary.md`;
- `research/fusion/model_audit.md`;
- `research/fusion/minimal_model_derivation_audit.md`;
- `research/fusion/four_moment_reduction_audit.md`;
- B5.1 source convention;
- B5.2 slab/minimal-curvature linearizations;
- B5.3 slab/minimal-curvature generators;
- B5.4A positive perturbation free-energy metric;
- B5.4B curvature free-energy consistency check.

B5.4B leaves the physical ion radial heat-flux normalization/sign and Hermitian matrix explicitly open. No finite-time heat-transport optimization has been authorized.

## Immediate selected gate

B5.5 must derive independently

\[
q_{i,k}=z_k^\dagger Q_{q_i,k}z_k
\]

from the physical radial `E×B` heat/thermal-energy flux, including exact thermodynamic combination, sign, prefactor, Fourier convention and Hermitian matrix, and only then compare it with the free-energy injection identity.

Canonical instruction:

`research/master/prompts/fusion_ion_heat_flux_observable_derivation_gate_0_1.md`

Branch status:

`research/fusion/STATUS.md`

## Planned dependency chain

1. B5.5 heat-flux observable derivation;
2. admissible-input geometry / input-cost gate;
3. Fusion candidate/convention freeze;
4. numerical/spectral qualification;
5. targeted Fusion literature positioning for the exact frozen question;
6. pilot specification;
7. MASTER pilot freeze and one-shot execution;
8. result integration/freeze;
9. later FLR/GK fidelity progression based on physical/structural validity, not effect size.

## Other branch states

- CORE: `STABLE / PARKED`
- MODES: `PARKED / conditional Fusion companion`
- CONT: `PARKED`
- CASCADE: `PARKED`
- Neuro: first result frozen; higher-fidelity extensions parked
- Climate: A/B frozen; no B repair or third-candidate rescue lineage
- Literature: prior Paper-1 audit complete; no new task until Fusion candidate/channel freeze
- Manuscript: Paper-1 content frozen; submission parked
- Power Grids: `PROTECTED`
- Photonics/Waves: `PROTECTED`
- Fusion: `B5.5 READY — AWAIT GO`

## Parallelism decision

No immediate parallel science is opened. `MODES` may later support Fusion if high-dimensional representation/reduction robustness becomes a concrete issue. `CONT` may become natural after a physical parameter family is frozen. Neither is active now.

## Branch-independent methodology

The reusable framework remains

\[
\mathfrak C=(A,M,Q,B,R_{\rm in}),
\]

with finite-time positive/signed operators, signed extrema, optimizer/subspace geometry, performance gap, physical reconstruction, robustness and anti-retuning discipline.

Fusion must preserve its own physical semantics rather than treating Paper-1 observables as interchangeable templates.

## Protected rollback chain

All first-paper savepoints remain protected through `First Paper Scientific Content Freeze 0.1`. The new post-paper roadmap savepoint is

`research/master/post_paper_scientific_roadmap_gate_0_1.md`.

New Fusion results cannot silently revise the first-paper baseline.

## Decision record

- base: `research/master/decision_branch_log.md` through DEC-443;
- continuation: `research/master/decision_branch_log_addendum_0_1.md` through DEC-486.

## Current next action

Use the Fusion branch/chat `60 – FUSION – Gyrofluid/Gyrokinetic Transport` and issue bare `GO` after it has read `research/fusion/STATUS.md`.

No finite-time Fusion effect inspection or parallel branch work is authorized before B5.5 returns to MASTER.
