# Manuscript Pre-Submission Integration Revision 0.4

**Status:** COMPLETE — PASS / RETURN TO MASTER  
**Primary target:** Physical Review E — Regular Article  
**Authority:** `research/master/prompts/manuscript_pre_submission_integration_revision_0_4.md`  
**Scientific rollback point:** `research/manuscript/manuscript_draft_0_3.md`

## 1. Scope

Revision 0.4 performs editorial integration only. It promotes the frozen PRE working title, integrates the completed figure/table package into the manuscript, separates the existing Supplement S1–S6 into a submission-oriented companion file, adds evidence-grounded Data Availability and Code Availability wording, adds a compact reproducibility/analysis-record statement, and records a pre-submission asset map.

No scientific result, equation meaning, parameter, model, horizon, objective, signed channel, admissible geometry, evidence ordering, novelty class, or verdict is changed.

## 2. Forbidden actions respected

Revision 0.4 did **not**:

- rerun any model or scientific solver;
- calculate any new horizon, resolution, optimizer, eigensystem, trajectory, transport value, gap, angle, or robustness metric;
- change a physical semantic, verdict, parameter, objective, signed channel, admissible geometry, or evidence order;
- conduct a new novelty/prior-art search;
- repair Climate-B or open a third Climate case;
- open protected Power Grid, Photonics, realistic Fusion, delayed Neuro, higher-fidelity Climate, MODES, CONT, CASCADE, or CORE work;
- submit the manuscript or send a presubmission inquiry;
- draft a cover letter;
- decide or change the author list.

## 3. Files created / updated

Created:

- `research/manuscript/manuscript_draft_0_4.md`
- `research/manuscript/manuscript_supplement_0_1.md`
- `research/manuscript/pre_submission_asset_map_0_1.md`
- `research/manuscript/manuscript_pre_submission_integration_revision_0_4.md`

Updated:

- `research/manuscript/STATUS.md`

No frozen scientific result/specification/data file was modified.

## 4. Editorial changes made

### Title

Draft 0.4 uses the frozen PRE target-specific title:

`Physics-informed diagnosis of objective nonredundancy in stable linear dynamics across plasma, neural and geophysical models`

### Submission-oriented main-text compression

To keep the main manuscript submission-oriented while preserving the frozen section architecture, detailed model matrices, numerical-gate ledgers, and bibliography metadata remain in the separate Supplement S1–S6. The main text retains the shared framework, domain definitions, all canonical representative witnesses, verdicts, limitations, figure/table callouts, and availability statements. This is editorial compression only; no scientific value, equation meaning, evidence order, or robustness interpretation is changed.

### Figure/table callouts

- Fig. 1 is called out in Sec. 2 before the common framework details.
- Main Table 1 is called out and reproduced canonically in Sec. 2.6.
- Fig. 2 is called out in Plasma Results, Sec. 4.1.
- Fig. 3 is called out in Neuro Results, Sec. 4.2.
- Fig. 4 is called out in Climate-A Results, Sec. 4.3.
- Fig. 5 is called out in Sec. 5.1 as a non-inferential robust-domain summary.

The callout order is therefore Fig. 1 -> Main Table 1 -> Fig. 2 -> Fig. 3 -> Fig. 4 -> Fig. 5.

### Captions

The approved caption content from `research/manuscript/figures/captions_0_1.md` is integrated into Draft 0.4. Specialist symbols are expanded where needed for a broad PRE reader, without changing any scientific meaning or value.

### Main Table 1

The hand-entered Draft-0.3 table is replaced by the canonical produced table content from:

`research/manuscript/figures/tables/main_table_1.md`

The distinct Plasma/Neuro/Climate-A physical semantics are preserved.

### Supplement references

Draft 0.4 contains explicit references to:

- Supplement S1 for analysis freeze chronology/reproducibility;
- Supplement S2 for Plasma details;
- Supplement S3 for Neuro details;
- Supplement S4 for Climate-A details;
- Supplement S5 and Supplement Fig. S5 for the Climate-B robustness rejection;
- Supplement S6 for frozen data paths and citation-metadata notes.

The inline Draft-0.3 Supplement is separated into `research/manuscript/manuscript_supplement_0_1.md`. Supplement Table S1 is reproduced from the produced canonical asset and Supplement Fig. S5 is referenced in the Climate-B section.

## 5. Data Availability wording chosen

Draft 0.4 states that the machine-readable frozen execution data supporting the reported values and figures are available in the public version-controlled repository `twkroll/nonmodal-flux`, with source paths listed in Supplement S6 and the pre-submission asset map.

No archival DOI, permanent archival repository identifier, or institutional preservation commitment is invented. Archival deposition and/or assignment of a persistent identifier is explicitly left as a submission-readiness item.

## 6. Code Availability wording chosen

Draft 0.4 states that the presentation-only figure-generation and validation scripts are available under:

`research/manuscript/figures/src/`

It also identifies the version-controlled specification/result/data/evidence record in the same public repository. Revision 0.4 makes no new software-license assertion and does not invent an archival DOI or preservation commitment.

## 7. Reproducibility / analysis-record wording

Draft 0.4 uses the approved terminology:

**pre-specified and frozen before objective-separation evaluation**

and explains that failed frozen gates are retained rather than repaired by post-effect retuning. The unqualified term `preregistered` is not used.

## 8. Figure/table integration check

PASS:

- Main Fig. 1–5 are called out in numerical order.
- Main Table 1 is integrated from the canonical produced asset.
- Main Fig. 5 contains only Plasma, Neuro, and Climate-A robust evidence.
- Climate-B fixed-resolution points remain excluded from Main Fig. 5.
- Fig. 4 and its manuscript text keep `90 deg` geometry paired with `Delta_heat≈0.0412` and the 95.88% retained-performance interpretation.
- Fig. 3/caption preserve signed two-pulse coordinates and explicitly avoid claiming a reachable negative cumulative pathway branch.
- Fig. S5 remains inseparable from `CLIM-B-FAIL — resolution robustness failure` and `0/6` robust horizons.

## 9. Supplement integration check

PASS:

- S1–S6 remain the frozen supplement architecture.
- No new supplement science is introduced.
- Supplement Table S1 uses the canonical produced content and labels the strong thresholds operational/non-universal.
- Climate-B remains full Supplement S5 plus a brief main-text Sec. 5.2 robustness-rejection case only.
- Supplement Fig. S5 is explicitly referenced in S5 and the main text.

## 10. Consistency / scientific-value validation

PASS checks performed on Draft 0.4 and the companion supplement include:

- Plasma `T=1` retains `G_E=1.8782758`, `J_Gamma^+=0.3535169`, `J_Gamma^-=-0.1462216`, `J_Gamma(w_E^*)=0.1752252`, `Delta_Gamma=0.5043372`, and `theta=53.396 deg`.
- Neuro retains the frozen 112/224-ms angles, performance gaps, and signed two-pulse coordinates; the reachable cumulative minimum remains described as positive.
- Climate-A retains `(|m|,n)_E=(3,2)`, `(|m|,n)_heat=(4,2)`, `90 deg`, `J_heat^+=1.54448995`, `J_heat|E^best=1.48088082`, `Delta_heat=0.04118455`, and 95.88% retained performance.
- Climate-B remains `CLIM-B-FAIL — resolution robustness failure`; `Delta_shift=1` is mentioned only in the same failure-qualified context; zero of six horizons remains the robustness result.
- The study-specific `20 deg` / `0.25` criterion is explicitly non-universal.
- Neuro is described as model-internal synaptic-filter storage, not metabolic/thermodynamic brain energy.
- No unsupported archival DOI or OA/license claim is made.
- No cover letter, author-list decision, submission action, or protected-branch work is included.

## 11. Unresolved author/submission metadata items

Still unresolved and intentionally deferred to MASTER / a later Submission Readiness Gate:

- author list, order, affiliations, corresponding author, ORCID data;
- cover letter;
- APS submission portal metadata;
- final archival deposition / persistent identifier decision;
- final journal-facing data/software license wording;
- final publication-status metadata verification for `Ogino2026`;
- final APS bibliography styling and production formatting;
- final figure/table production sizing and placement;
- any OA-route/APC/institutional agreement decision.

These are editorial/submission items only and do not authorize new science.

## 12. Verdict

\[
\boxed{\text{MANUSCRIPT PRE-SUBMISSION INTEGRATION REVISION 0.4 = PASS}}
\]

Revision 0.4 is ready to return to MASTER for a separate Submission Readiness Gate.

**STOP — RETURN TO MASTER.**
