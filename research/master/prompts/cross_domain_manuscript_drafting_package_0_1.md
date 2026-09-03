# MASTER Prompt — Cross-Domain Manuscript Drafting Package 0.1

**Authority:** `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`.

**Target chat:** `00 – MASTER – Projektplan & Status` unless MASTER explicitly delegates a writing-only subtask.

**Scope:** manuscript drafting and evidence organization only. No new theory, no new numerical execution, no parameter search, no retuning, no new application branch, no new novelty claim.

## Task

Construct the first integrated manuscript package from the frozen evidence and claim boundaries.

Preserve exactly:

- Plasma/D10-ZF `P2-A` = strong primary domain anchor;
- Neuro/CMC `NEURO-STRONG` = strong cross-domain demonstrator;
- Climate/Ocean QG `CLIM-WEAK` = robust weak/contrast case;
- manuscript novelty = `N2 + N3` with domain-specific `N1`, not mathematical novelty;
- the canonical claim and all allowed/forbidden language in `cross_domain_manuscript_positioning_claim_freeze_0_1.md`.

## Required outputs

Create:

`research/manuscript/manuscript_draft_0_1.md`

`research/manuscript/evidence_citation_map_0_1.md`

`research/manuscript/figure_source_map_0_1.md`

`research/manuscript/STATUS.md`

The draft must include at minimum:

1. working title;
2. structured abstract;
3. Introduction;
4. common framework/method section;
5. Plasma result section;
6. Neuro result section;
7. Climate contrast section;
8. cross-domain synthesis;
9. Discussion/limitations;
10. Conclusion;
11. placeholder bibliography with the required prior-art anchors from the claim freeze.

## Evidence discipline

Every quantitative statement must be traceable to a frozen canonical result file. The evidence map must pair each manuscript claim with:

- source file;
- section/table/quantity;
- allowed wording;
- required literature citation where applicable;
- restriction/forbidden wording.

The figure-source map must specify for each planned figure:

- exact frozen data source(s);
- panels;
- quantities shown;
- whether data transformation is purely presentational;
- caption-level claim guardrails.

No figure may depend on a new simulation or unregistered horizon.

## Style / positioning

Write as a methods/application paper about physics-informed objective-nonredundancy diagnostics. Do not write as a new general theory.

Use the preferred working title from the claim freeze unless the report itself gives a clearly safer equivalent.

Use `to our knowledge` only for the narrow application-specific absence claims already approved. Do not infer novelty from absence.

Preserve the semantic distinction among Plasma free energy, Climate QG perturbation energy and Neuro synaptic-filter storage/input cost.

## STOP boundary

Do not submit, target a journal, generate new scientific results, or open protected branches in this task.

After writing and committing all four files, update `research/master/STATUS.md` to `DRAFT PACKAGE COMPLETE — RETURN TO MASTER FOR DRAFT REVIEW`, report commit hash/CI status, and STOP.
