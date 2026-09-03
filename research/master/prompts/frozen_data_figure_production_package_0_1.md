# Frozen-Data Figure Production Package 0.1 — Manuscript Instruction

**Authority:** MASTER / `research/master/journal_audience_positioning_gate_0_1.md`  
**Primary publication target:** Physical Review E, Regular Article  
**Scientific authority:** `research/manuscript/figure_source_map_0_2.md`  
**Scope:** figure/table production and purely presentational manuscript assets from frozen evidence only.

## Absolute prohibitions

Do **not**:

- instantiate or rerun any Plasma, Neuro, Climate-A, or Climate-B model;
- solve a new eigenproblem, singular-value problem, matrix exponential, Lyapunov equation, trajectory, optimization, continuation, or parameter search;
- add/interpolate/smooth/extrapolate horizons, resolutions, optimizer values, objective values, angles, gaps, or physical diagnostics;
- alter any verdict, claim, physical semantic, admissible geometry, objective, channel, parameter, normalization, or evidence ordering;
- repair Climate-B or add a third Climate candidate;
- perform a new novelty/literature search;
- submit the paper, draft a cover letter, or modify the author list.

If a desired panel is not directly supported by stored frozen data, **simplify or omit the panel** rather than recomputing it.

## Inputs

Read first:

- `research/manuscript/STATUS.md`;
- `research/master/journal_audience_positioning_gate_0_1.md`;
- `research/master/manuscript_structure_freeze_0_2.md`;
- `research/manuscript/manuscript_draft_0_3.md`;
- `research/manuscript/figure_source_map_0_2.md`;
- `research/manuscript/evidence_citation_map_0_2.md`.

Then use only the frozen CSV/result/specification files explicitly authorized by `figure_source_map_0_2.md`.

## PRE packaging rule

Use Physical Review E / APS Regular-Article presentation conventions as the primary packaging target, but do not let journal style change scientific content.

Target-specific working title for metadata only:

`Physics-informed diagnosis of objective nonredundancy in stable linear dynamics across plasma, neural and geophysical models`

Draft 0.3 remains the manuscript rollback point; do not rewrite the manuscript body in this package except for figure/table references or captions strictly needed to match produced assets.

Graphics should be vector-first where practical and remain interpretable without reliance on color alone. Use readable domain labels and define specialist symbols in captions.

## Required main figures

Produce, subject to direct frozen-data support:

1. **Main Figure 1 — Common workflow and domain semantics**
   - `(A,M,Q,B,R_in)` workflow;
   - positive-objective versus signed-channel finite-time operators;
   - geometry versus target-performance diagnostics;
   - robustness as a separate evidentiary gate;
   - Plasma/Neuro/Climate-A semantics only in principal domain panel.

2. **Main Figure 2 — Plasma strong anchor**
   - frozen horizon quantities and/or signed extrema;
   - `theta(T)` and `Delta_Gamma(T)`;
   - frozen T=1 structural information only if directly stored;
   - representative witness `T=1`, `Delta_Gamma≈0.5043`, `theta≈53.40 deg`.

3. **Main Figure 3 — Neuro constrained two-pulse result**
   - frozen six-horizon geometry/performance;
   - two-pulse preparation-coordinate comparison at 112/224 ms;
   - preserve pulse signs;
   - do not depict a reachable negative cumulative pathway branch.

4. **Main Figure 4 — Climate-A robust weak contrast**
   - frozen six-horizon geometry/performance;
   - longest-horizon `(3,2)` energy versus `(4,2)` heat modal support where directly stored;
   - make `90 deg` geometry and `Delta_heat≈0.0412` / 95.88% retained performance visible together.

5. **Main Figure 5 — Cross-domain robust geometry/performance summary**
   - non-inferential paired summary only;
   - Plasma, Neuro, Climate-A robust evidence only;
   - no trend line, regression, decision region, phase diagram, universal threshold visualization, or common physical-objective scale;
   - Climate-B fixed-resolution points excluded.

## Required main table

Produce **Main Table 1** for Plasma, Neuro, Climate-A only:

- defining model;
- positive metric;
- signed channel;
- admissible geometry/input cost;
- time normalization if space permits;
- frozen role/verdict.

Preserve distinct physical semantics.

## Required Supplement assets

Produce:

- Supplement operational-rules / representative-outcomes table, including the study-specific strong rule and clearly labeling it non-universal;
- at least one compact **Climate-B robustness-rejection figure/table** if directly supported by stored frozen execution data.

Climate-B display must:

- separate local numerical/direct PASS gates from cross-resolution FAIL gates;
- state `CLIM-B-FAIL — resolution robustness failure` prominently;
- state `0/6` frozen horizons robust where shown;
- show objective convergence/common-space mass/principal-angle failure only from stored data;
- mention `Delta_shift=1` or large fixed-resolution angle only in the same visual/caption context as the failed refinement result.

## Source scripts and reproducibility

Create transparent plotting/table-generation source scripts that:

- read only frozen files;
- perform only unit-preserving selection, reshaping, labeling, and plotting/presentation transformations;
- contain assertions preventing unsupported horizons/resolutions from being introduced;
- record input file paths and, where practical, checksums/commit identifiers in a manifest.

Recommended repository layout (adapt only if an existing canonical layout already exists):

- `research/manuscript/figures/`
- `research/manuscript/figures/src/`
- `research/manuscript/figures/main/`
- `research/manuscript/figures/supplement/`
- `research/manuscript/figures/figure_manifest_0_1.md`

Do not include font files.

## Output formats

For each figure, provide a vector publication asset where technically suitable (PDF and/or SVG) and a PNG preview for inspection. Tables should be available in manuscript-ready text/LaTeX-compatible form in addition to any visual preview.

Do not rasterize equations unnecessarily.

## Validation

Before committing:

1. verify every plotted numeric point against its frozen source file;
2. verify no interpolation/smoothing/recalculation occurred;
3. verify Climate-B failure qualification is inseparable from any attractive fixed-resolution quantity;
4. verify Main Fig. 5 excludes Climate-B;
5. verify Neuro semantics and reachable-sign restriction;
6. verify Climate-A angle/performance pairing;
7. verify all text remains readable at intended journal display size;
8. inspect every rendered figure visually for clipping, overlap, illegible labels, and misleading visual encoding.

## Required canonical report

Create:

`research/manuscript/frozen_data_figure_production_package_0_1.md`

Document:

- scope and forbidden actions;
- exact frozen source files used by each figure/table;
- output file inventory;
- validation results;
- omitted/simplified panels and why;
- PRE packaging notes;
- remaining editorial-only issues;
- final PASS/FAIL/STOP.

Update `research/manuscript/STATUS.md` and return to MASTER after committing all outputs.

## STOP

After figure/table production and validation:

**STOP — RETURN TO MASTER.**

Do not start journal submission preparation or manuscript polishing on the same `GO`.
