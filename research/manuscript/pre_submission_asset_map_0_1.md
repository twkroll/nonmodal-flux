# Pre-Submission Asset Map 0.1

**Status:** CANONICAL ASSET/CONSISTENCY MAP FOR MANUSCRIPT REVISION 0.4  
**Authority:** `research/master/prompts/manuscript_pre_submission_integration_revision_0_4.md`  
**Primary target:** Physical Review E — Regular Article  
**Rule:** frozen evidence/assets only; this map performs no submission action and introduces no scientific result.

## 1. Main manuscript

- Main manuscript: `research/manuscript/manuscript_draft_0_4.md`
- Scientific/textual rollback point: `research/manuscript/manuscript_draft_0_3.md`
- Target-specific title: `Physics-informed diagnosis of objective nonredundancy in stable linear dynamics across plasma, neural and geophysical models`

## 2. Supplement

- Submission-oriented companion: `research/manuscript/manuscript_supplement_0_1.md`
- Architecture: S1–S6 copied/reorganized from the frozen inline Supplement in Draft 0.3.
- Supplement Table S1 is integrated in S6.1 from the produced canonical table asset.
- Supplement Fig. S5 is referenced in S5 and remains the Climate-B robustness-rejection display only.

## 3. Main figures

| Figure | Vector master | Preview | Manuscript role |
|---|---|---|---|
| Fig. 1 | `research/manuscript/figures/main/fig1_common_workflow.svg` | `research/manuscript/figures/main/fig1_common_workflow.png` | common workflow/domain semantics |
| Fig. 2 | `research/manuscript/figures/main/fig2_plasma_strong_anchor.svg` | `research/manuscript/figures/main/fig2_plasma_strong_anchor.png` | Plasma `P2-A` strong anchor |
| Fig. 3 | `research/manuscript/figures/main/fig3_neuro_two_pulse.svg` | `research/manuscript/figures/main/fig3_neuro_two_pulse.png` | Neuro `NEURO-STRONG` two-pulse result |
| Fig. 4 | `research/manuscript/figures/main/fig4_climate_a_weak_contrast.svg` | `research/manuscript/figures/main/fig4_climate_a_weak_contrast.png` | Climate-A `CLIM-WEAK` geometry/performance contrast |
| Fig. 5 | `research/manuscript/figures/main/fig5_cross_domain_summary.svg` | `research/manuscript/figures/main/fig5_cross_domain_summary.png` | non-inferential robust-domain summary; Climate-B excluded |

## 4. Main table

- Markdown: `research/manuscript/figures/tables/main_table_1.md`
- LaTeX-compatible: `research/manuscript/figures/tables/main_table_1.tex`
- Draft 0.4 reproduces the canonical table content rather than the earlier hand-entered duplicate.
- Rows: Plasma, Neuro, Climate-A only.

## 5. Supplement assets

### Supplement Table S1

- Markdown: `research/manuscript/figures/tables/supplement_table_s1_operational_rules_outcomes.md`
- LaTeX-compatible: `research/manuscript/figures/tables/supplement_table_s1_operational_rules_outcomes.tex`
- Study-specific `theta >= 20 deg` / `Delta_Q >= 0.25` rule remains explicitly operational and non-universal.
- Climate-B row remains failure-qualified.

### Supplement Fig. S5

- Vector master: `research/manuscript/figures/supplement/figS5_climate_b_robustness_rejection.svg`
- Preview: `research/manuscript/figures/supplement/figS5_climate_b_robustness_rejection.png`
- Required frozen verdict: `CLIM-B-FAIL — resolution robustness failure`
- Required robustness summary: `0/6` frozen horizons robust.

## 6. Captions and scientific presentation authority

- Approved captions: `research/manuscript/figures/captions_0_1.md`
- Figure validation: `research/manuscript/figures/validation_0_1.md`
- Figure manifest: `research/manuscript/figures/figure_manifest_0_1.md`
- Figure source map: `research/manuscript/figure_source_map_0_2.md`
- Evidence/citation map: `research/manuscript/evidence_citation_map_0_2.md`
- Figure-package report: `research/manuscript/frozen_data_figure_production_package_0_1.md`
- MASTER integration freeze: `research/master/frozen_data_figure_production_integration_freeze_0_1.md`

## 7. Frozen machine-readable data paths

- Plasma: `research/d10_zf_pilot_0_2_execution_data.csv`
- Neuro: `research/neuro/neuro_pilot_0_1_execution_data.csv`
- Climate-A: `research/climate/climate_ocean_pilot_0_1_execution_data.csv`
- Climate-B robustness-rejection case: `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv`

The associated frozen specifications/results remain the scientific authority identified by `research/manuscript/evidence_citation_map_0_2.md` and `research/manuscript/figure_source_map_0_2.md`.

## 8. Code / analysis-record paths

- Figure generation: `research/manuscript/figures/src/generate_frozen_data_figures_0_1.py`
- Figure validation: `research/manuscript/figures/src/validate_frozen_data_figures_0_1.py`
- Repository source tree present at: `src/`
- Version-controlled analysis/specification/result record: `research/`

Revision 0.4 does not make a new claim about a software license, archival preservation policy, or completeness of code beyond the paths explicitly present in the public repository.

## 9. Data/Code Availability wording basis

The repository is public and version controlled. Draft 0.4 therefore states that frozen machine-readable result data and the presentation-only figure generation/validation scripts are available in `twkroll/nonmodal-flux`.

An in-repository editorial metadata check found no Zenodo/CITATION/archival-DOI entry from the queried terms, and the repository root listing contains no root `LICENSE` or `CITATION.cff` file. Revision 0.4 therefore does **not** invent:
- an archival DOI or permanent archival repository identifier;
- a software-license claim;
- an institutional preservation commitment.

Any archival deposition, persistent identifier, and journal-facing license wording remain submission-readiness items.

## 10. Unresolved submission-only metadata/items

The following are intentionally unresolved in Revision 0.4:

- author list, author order, affiliations, corresponding-author designation, and ORCID metadata;
- final manuscript submission metadata and APS portal fields;
- cover letter and any presubmission correspondence;
- final Data Availability wording after any archival deposition/tag/release decision;
- archival DOI/persistent identifier, if one is created later;
- journal-facing software/data license wording after repository/license verification;
- final publication-status verification for `Ogino2026`;
- final bibliography style/APS formatting;
- final journal production sizing/placement of figures and tables;
- Data Availability Statement placement required by the selected APS production workflow.

None of these items authorizes scientific recomputation, novelty search, or protected-branch work.

**STOP — asset map only; no submission action performed.**
