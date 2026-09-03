# Frozen-Data Figure Production Package 0.1

**Status:** `COMPLETE — PASS / STOP / RETURN TO MASTER`  
**Primary publication target:** Physical Review E — Regular Article  
**Scientific authority:** `research/manuscript/figure_source_map_0_2.md`  
**Manuscript rollback point:** `research/manuscript/manuscript_draft_0_3.md`

## 1. Scope

This package performs figure/table production only from already frozen stored evidence. It does not instantiate or rerun any Plasma, Neuro, Climate-A, or Climate-B model and does not solve any new eigenproblem, singular-value problem, matrix exponential, Lyapunov equation, trajectory, optimization, continuation, or parameter search. No horizon, resolution, scientific value, physical interpretation, verdict, or claim is added, interpolated, smoothed, extrapolated, fitted, or retuned.

The package also performs no novelty search, journal submission, cover-letter drafting, author-list work, journal-transfer preparation, protected-branch work, Climate-B repair, or third Climate-candidate work.

## 2. Frozen sources used

### Figure 1

- `research/manuscript/manuscript_draft_0_3.md`, Sec. 2;
- `research/manuscript/figure_source_map_0_2.md`;
- `research/master/manuscript_structure_freeze_0_2.md`;
- `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`.

### Figure 2 — Plasma

- `research/d10_zf_pilot_0_2_execution_data.csv`;
- `research/d10_zf_pilot_0_2_execution_results.md`;
- `research/d10_zf_pilot_0_1_specification.md` for definitions only.

### Figure 3 — Neuro

- `research/neuro/neuro_pilot_0_1_execution_data.csv`;
- `research/neuro/neuro_pilot_0_1_execution_results.md`;
- `research/neuro/neuro_pilot_specification_0_1.md` for pathway/preparation definitions only.

### Figure 4 — Climate-A

- `research/climate/climate_ocean_pilot_0_1_execution_data.csv`;
- `research/climate/climate_ocean_pilot_0_1_execution_results.md`;
- `research/climate/climate_ocean_numerical_qualification_0_1.md` and `research/climate/climate_ocean_pilot_specification_0_1.md` for definitions only.

### Figure 5

- the same frozen Plasma, Neuro, and Climate-A execution data/result sources above;
- `research/master/manuscript_structure_freeze_0_2.md` and Draft 0.3 Sec. 5.1 for role/wording authority.

Climate-B fixed-resolution points are excluded.

### Supplement Fig. S5 — Climate-B

- `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv`;
- `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_results.md`;
- `research/climate/climate_intra_domain_contrast_pilot_specification_0_1.md` for frozen criteria;
- `research/climate/climate_intra_domain_contrast_numerical_qualification_0_1.md` for passed pre-effect gates;
- `research/master/climate_intra_domain_contrast_result_integration_freeze_0_1.md` for the frozen verdict.

### Tables

Main Table 1 uses the frozen application specifications/qualification files authorized by `figure_source_map_0_2.md`. Supplement Table S1 uses Draft 0.3 Sec. 2.5/S6, the frozen pilot specifications/results, and Structure Freeze 0.2.

## 3. Output inventory

### Main figures

- `research/manuscript/figures/main/fig1_common_workflow.svg`
- `research/manuscript/figures/main/fig1_common_workflow.png`
- `research/manuscript/figures/main/fig2_plasma_strong_anchor.svg`
- `research/manuscript/figures/main/fig2_plasma_strong_anchor.png`
- `research/manuscript/figures/main/fig3_neuro_two_pulse.svg`
- `research/manuscript/figures/main/fig3_neuro_two_pulse.png`
- `research/manuscript/figures/main/fig4_climate_a_weak_contrast.svg`
- `research/manuscript/figures/main/fig4_climate_a_weak_contrast.png`
- `research/manuscript/figures/main/fig5_cross_domain_summary.svg`
- `research/manuscript/figures/main/fig5_cross_domain_summary.png`

### Supplement

- `research/manuscript/figures/supplement/figS5_climate_b_robustness_rejection.svg`
- `research/manuscript/figures/supplement/figS5_climate_b_robustness_rejection.png`

### Tables

- `research/manuscript/figures/tables/main_table_1.md`
- `research/manuscript/figures/tables/main_table_1.tex`
- `research/manuscript/figures/tables/supplement_table_s1_operational_rules_outcomes.md`
- `research/manuscript/figures/tables/supplement_table_s1_operational_rules_outcomes.tex`

### Source / reproducibility / captions

- `research/manuscript/figures/src/generate_frozen_data_figures_0_1.py`
- `research/manuscript/figures/src/validate_frozen_data_figures_0_1.py`
- `research/manuscript/figures/figure_manifest_0_1.md`
- `research/manuscript/figures/validation_0_1.md`
- `research/manuscript/figures/captions_0_1.md`

No font files are included. SVG is the vector master; PNGs are inspection previews. A separate PDF duplicate is not required because the instruction permits PDF **and/or** SVG for vector publication assets.

## 4. Required-content implementation

- **Fig. 1:** common `(A,M,Q,B,R_in)` workflow, separate geometry/performance diagnostics, robustness gate, and distinct Plasma/Neuro/Climate-A semantics; Climate-B excluded as a robust principal domain.
- **Fig. 2:** six frozen Plasma horizons, signed extrema, `theta(T)`/`Delta_Gamma(T)`, and frozen `T=1` witness (`Delta_Gamma≈0.5043`, `theta≈53.40 deg`).
- **Fig. 3:** six frozen Neuro horizons and signed two-pulse preparation-coordinate directions at 112/224 ms; negative pathway-optimal second pulse coordinate preserved; no reachable negative cumulative pathway branch depicted.
- **Fig. 4:** six frozen Climate-A geometry/performance values; longest-horizon `(3,2)` versus `(4,2)` support; `90 deg` geometry paired with `Delta_heat≈0.0412` and 95.88% retained target performance.
- **Fig. 5:** non-inferential paired robust-domain summary only; no threshold regions, phase diagram, fit, trend, regression, or Climate-B point.
- **Main Table 1:** Plasma, Neuro, Climate-A only with distinct physical semantics.
- **Supplement Table S1:** study-specific strong rule explicitly labeled non-universal plus representative frozen outcomes and a failure-qualified Climate-B row.
- **Supplement Fig. S5:** local PASS gates visually separated from cross-resolution FAIL gates; exact `CLIM-B-FAIL — resolution robustness failure`, `0/6`, objective-value discrepancy and common-space mass evidence; `Delta_shift=1` appears only in the same rejection context.

## 5. Validation

Automated and visual validation is recorded in `research/manuscript/figures/validation_0_1.md`.

PASS checks include:

- exact stored horizon/resolution selections;
- representative frozen values reproduced from stored CSV fields;
- no interpolation/smoothing/fitting or unsupported values;
- Main Fig. 5 excludes Climate-B;
- Neuro signed-preparation and reachable-sign restrictions preserved;
- Climate-A angle/performance pairing preserved;
- Climate-B fixed-resolution attraction inseparable from failure qualification;
- no scientific solver calls/imports in the generator;
- SVG renderer inspection for clipping, overlap, readable labels, and non-color-dependent encoding.

## 6. Simplifications / omissions

Panels requiring reconstructed time series, physical fields, or modal distributions not directly necessary for the frozen manuscript message were omitted rather than recomputed. In particular, no Plasma trajectory, Neuro state trajectory, Climate-A reconstructed field, or Climate-B repair/comparison is generated.

## 7. PRE packaging notes

The package uses broad-physics labels, monochrome-safe line/marker distinctions, SVG vector masters, and concise captions. PRE Regular Article targeting changes presentation only and does not change the evidence order or scientific claims. The PRE target-specific working title remains metadata only; Draft 0.3 is not substantively rewritten here.

## 8. Remaining editorial-only issues

- final APS production sizing and caption placement;
- final manuscript insertion/reference numbering;
- any later data-availability/code-availability wording authorized by MASTER;
- journal submission metadata and author-list decisions, which remain outside this package.

## 9. Verdict

\[
\boxed{\text{Frozen-Data Figure Production Package 0.1 = PASS}}
\]

All required main figures, main table, supplement operational table, Climate-B robustness-rejection display, source scripts, manifest, captions, and validation records are prepared from frozen evidence only.

**STOP — RETURN TO MASTER.**
