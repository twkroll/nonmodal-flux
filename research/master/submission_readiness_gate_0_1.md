# Submission Readiness Gate 0.1

**Date:** 2026-09-04  
**Authority:** MASTER  
**Primary target:** Physical Review E — Regular Article  
**Scope:** readiness audit only; no submission action and no new science.

## Overall verdict

\[
\boxed{\text{PASS WITH AUTHOR/METADATA ITEMS — SCIENTIFIC PACKAGE READY}}
\]

The frozen Revision-0.4 scientific/manuscript package is sufficiently complete to enter a later final-submission-preparation stage. It is **not** ready for literal upload without author/editorial work, and no submission action is authorized here.

This verdict is deliberately compatible with a later author-led prose revision: scientific readiness does not mean the present wording must be submitted unchanged.

## 1. Official PRE/APS requirements checked

Current official APS/PRE author guidance was checked only for submission/readiness requirements, not for scientific novelty.

Relevant official sources:

- Physical Review E — Information for Authors: `https://journals.aps.org/pre/authors`
- APS Web Submission Guidelines: `https://journals.aps.org/authors/web-submission-guidelines-physical-review`
- APS Data Availability Guidelines: `https://journals.aps.org/authors/data-availability-statements`
- APS Style Basics: `https://journals.aps.org/authors/style-basics`
- APS Supplemental Material Instructions: `https://journals.aps.org/authors/supplemental-material-instructions`
- APS Editorial Policies and Practices: `https://journals.aps.org/authors/editorial-policies`
- APS Appropriate Use of AI Tools: `https://journals.aps.org/authors/appropriate-use-ai-tools`

Current PRE guidance confirms that Regular Articles have no stated length limit; a PDF manuscript is sufficient for peer review, while LaTeX/REVTeX source is preferred for efficient processing. Published Physical Review articles require a Data Availability Statement. The submission server requires author/contact metadata and a designated corresponding author; ORCID is required for the corresponding author and strongly encouraged for all authors. APS currently requires disclosure of substantive AI use in research/manuscript preparation.

## 2. Readiness matrix

| Category | Item | Classification | Gate finding |
|---|---|---|---|
| Scientific integrity | Frozen evidence order: Plasma → Neuro → Climate-A; Climate-B rejection only | `READY` | Preserved exactly. |
| Scientific integrity | No universality or mathematical-novelty overclaim | `READY` | Draft 0.4 explicitly limits contribution to methodological integration/physical interpretation. |
| Scientific integrity | Domain semantics | `READY` | Plasma free energy/particle transport; Neuro synaptic-filter storage/pathway contribution; Climate-A QG energy/heat transport; Climate-B kinetic energy/jet-translation forcing remain distinct. |
| Scientific integrity | Climate-A `90 deg` geometry + `Delta_heat≈0.0412` | `READY` | Presented together with 95.88% retained heat performance. |
| Scientific integrity | Climate-B failure qualification | `READY` | `CLIM-B-FAIL — resolution robustness failure`, `0/6`; excluded from Main Fig. 5. |
| Scientific integrity | Strong threshold non-universal | `READY` | Explicitly study-specific/operational. |
| Scientific integrity | Freeze chronology wording | `READY` | Uses `pre-specified and frozen before objective-separation evaluation`; unqualified `preregistered` absent. |
| Main manuscript | Title, Abstract, 1–7 architecture, conclusion | `READY` | Complete and internally coherent for PRE-style broad readership baseline. |
| Main manuscript | Equations/symbols and representative values | `READY` | Frozen values retained in Revision 0.4 validation. |
| Main manuscript | Fig. 1–5 and Main Table 1 callouts/captions | `READY` | Called out in order and matched to frozen assets. |
| Main manuscript | Supplement references | `READY` for science; `EDITORIAL FIX REQUIRED` for final APS packaging | Content references S1–S6 are present; final APS-style Supplemental Material citation/reference packaging should be normalized during final preparation. |
| Main manuscript | Data/Code Availability text | `READY` as truthful interim wording; `EXTERNAL METADATA CHECK REQUIRED` before publication | Public repository paths are real; no DOI/license is invented. APS asks publicly shared data/software to be cited in the DAS/reference list, so a final citable repository/data reference or approved URL/persistent identifier must be chosen. |
| Supplement | S1–S6 completeness | `READY` | Separate supplement reproduces frozen content without new science. |
| Supplement | Table S1 and Fig. S5 placement | `READY` | Correctly integrated and failure-qualified. |
| Supplement | Publication-ready file form | `EDITORIAL FIX REQUIRED` | APS recommends PDF for text Supplemental Material. Current canonical source is Markdown; final PDF/typeset companion must be produced later from frozen content. |
| Figures/tables | Scientific content and numbering | `READY` | Main Fig. 5 excludes Climate-B; captions agree with Draft 0.4. |
| Figures/tables | Vector masters | `READY` as internal masters; `EDITORIAL FIX REQUIRED` for final APS upload if needed | SVG masters + PNG previews exist. Final PRE-compatible figure/source packaging can be converted presentation-only without scientific rerendering. |
| Bibliography | Already-cited reference set | `READY` scientifically | No new prior art needed for readiness. |
| Bibliography | `Ogino2026` status | `EXTERNAL METADATA CHECK REQUIRED` resolved at gate | Official eLife record on 2026-09-04: Reviewed Preprint v1, March 9 2026, **Not revised**, DOI `10.7554/eLife.110030.1`; do not describe it as a conventional final Version of Record unless status changes. |
| Bibliography | Remaining DOI/page/article-number normalization | `EXTERNAL METADATA CHECK REQUIRED` | Farrell 1982/1985, Farrell & Ioannou 1994, Kim & Morgan 2002, Kuang 2004 and complete Sevellec 2008 pagination/article metadata should be normalized before literal submission. This is metadata cleanup only. |
| Author metadata | Author list/order, affiliations, corresponding author, author emails | `AUTHOR INPUT REQUIRED` | Must be supplied/approved by authors; no inference permitted. |
| Author metadata | ORCIDs | `AUTHOR INPUT REQUIRED` | Corresponding-author ORCID required by APS; others strongly encouraged. |
| Author metadata | Acknowledgments, funding, conflicts, contributions | `AUTHOR INPUT REQUIRED` | Author facts/decisions only. |
| Submission metadata | PhySH/section, cover-letter choices, referee suggestions/exclusions, submission history | `AUTHOR INPUT REQUIRED` | To be decided only when submission track is reactivated. |
| OA | Subscription/hybrid OA route, APC/institutional agreement | `AUTHOR INPUT REQUIRED` | No choice made. |
| AI policy | APS substantive-AI-use disclosure | `AUTHOR INPUT REQUIRED` and mandatory before submission if substantive use remains applicable | Current APS policy requires disclosure of substantive AI use, including scientific reasoning, claims/explanations, literature synthesis, figure generation, derivations/calculations, or materially result-affecting code. Exact author-approved disclosure wording must be prepared before submission; AI cannot be an author. |
| Repository | Public data/result/code paths | `READY` | `twkroll/nonmodal-flux` contains frozen CSVs, result/specification records, evidence maps, and figure-generation/validation scripts. |
| Repository | Tagged release / archive DOI / CITATION / license | `AUTHOR INPUT REQUIRED` / `EXTERNAL METADATA CHECK REQUIRED` | Not currently documented; absence is not a scientific blocker. No release, DOI, CITATION file, or license is created by this gate. |

## 3. Mandatory work before an actual submission

No new science is required. Before literal PRE submission, the following must be completed in a separate, explicitly authorized final-preparation phase:

1. authors must perform and approve the final prose pass;
2. author list/order, affiliations, corresponding author, emails and ORCIDs must be supplied;
3. acknowledgments/funding/conflicts/contributions must be supplied or explicitly declared not applicable;
4. final APS-compliant Data Availability / software availability citation must be chosen, ideally with a stable citable release/archive if the authors elect to create one;
5. the supplement must be rendered as a publication-ready PDF and cited in APS style;
6. final manuscript/source/figure packaging should be converted to accepted PRE/APS formats without changing scientific content;
7. bibliography metadata must be normalized, including the verified eLife Reviewed Preprint status of `Ogino2026`;
8. authors must review APS's current AI-use policy and include an author-approved disclosure for any substantive AI use that applies;
9. OA route/APC/institutional agreement and portal-only metadata must be chosen;
10. only after these items are resolved may a cover letter or APS portal submission be authorized.

## 4. Author-input checklist

- author names and order;
- affiliations where the research was performed;
- designated corresponding author and active email;
- ORCID for corresponding author; optional/encouraged ORCIDs for all others;
- acknowledgments and funding identifiers;
- conflict-of-interest statement;
- author-contribution statement if desired/required;
- exact author-approved AI-use disclosure;
- OA/subscription preference and institutional agreement information;
- suggested/excluded referees, if used;
- repository release/archive/DOI/license preference;
- final prose and title approval.

## 5. External metadata checklist

- keep `Ogino2026` as eLife Reviewed Preprint v1, March 9 2026, Not revised, DOI `10.7554/eLife.110030.1`, unless its official status later changes;
- normalize incomplete DOI/page/article-number metadata for the already-cited atmospheric/ocean references;
- verify final APS citation style/titles in references;
- verify accepted upload formats at the time the submission track is reactivated;
- if a repository release/archive is created later, update the Data Availability citation accordingly.

## 6. Canonical scientific/manuscript package assessed

Main content:

- `research/manuscript/manuscript_draft_0_4.md`
- `research/manuscript/manuscript_supplement_0_1.md`
- `research/manuscript/pre_submission_asset_map_0_1.md`
- `research/manuscript/manuscript_pre_submission_integration_revision_0_4.md`

Main display assets:

- `research/manuscript/figures/main/fig1_common_workflow.svg` + PNG preview
- `research/manuscript/figures/main/fig2_plasma_strong_anchor.svg` + PNG preview
- `research/manuscript/figures/main/fig3_neuro_two_pulse.svg` + PNG preview
- `research/manuscript/figures/main/fig4_climate_a_weak_contrast.svg` + PNG preview
- `research/manuscript/figures/main/fig5_cross_domain_summary.svg` + PNG preview
- Main Table 1 Markdown + LaTeX asset

Supplement display assets:

- `research/manuscript/figures/supplement/figS5_climate_b_robustness_rejection.svg` + PNG preview
- Supplement Table S1 Markdown + LaTeX asset

Presentation/reproducibility authority:

- `research/manuscript/figures/captions_0_1.md`
- `research/manuscript/figures/figure_manifest_0_1.md`
- `research/manuscript/figures/validation_0_1.md`
- `research/manuscript/evidence_citation_map_0_2.md`
- `research/manuscript/figure_source_map_0_2.md`

## 7. No-new-science confirmation

This gate performed no model rerun, scientific calculation, eigenproblem, matrix exponential, optimization, parameter/horizon/resolution change, new application, Climate-B repair, novelty search, or change to any scientific claim/verdict. The only web checks were current APS/PRE submission requirements and metadata for references already cited.

## 8. Is another scientific/editorial revision required now?

**No scientific revision is required.** A later author-led prose pass and a narrowly scoped final-submission-formatting pass are required before literal submission, but they need not block resumption of the scientific program.

The scientific content of the first paper can therefore be frozen as a stable baseline while submission preparation remains parked until the authors explicitly reactivate it.

## Final gate decision

\[
\boxed{\text{PASS WITH AUTHOR/METADATA ITEMS — SCIENTIFIC PACKAGE READY}}
\]

**STOP — GATE COMPLETE; NO SUBMISSION ACTION PERFORMED.**