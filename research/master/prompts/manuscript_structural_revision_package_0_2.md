# MASTER Prompt — Manuscript Structural Revision Package 0.2

**Authority:** `research/master/manuscript_draft_review_gate_0_1.md` and `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`.

**Target chat:** `00 – MASTER – Projektplan & Status` unless MASTER explicitly delegates writing-only work.

**Scope:** manuscript restructuring and reproducibility exposition only. No new theory, no new numerical execution, no parameter search, no retuning, no new application branch, no new novelty claim.

## Task

Produce Revision 0.2 of the integrated manuscript using only already frozen model/specification/result/literature sources.

Preserve exactly:

- Plasma/D10-ZF `P2-A` = strong primary domain anchor;
- Neuro/CMC `NEURO-STRONG` = strong cross-domain demonstrator;
- Climate/Ocean QG `CLIM-WEAK` = robust weak/contrast case;
- first-paper framing = methods/application paper on physics-informed objective-nonredundancy diagnostics;
- novelty = `N2+N3` with domain-specific `N1`, no mathematical novelty;
- all allowed/forbidden claim boundaries in the claim freeze and Draft Review Gate.

## Required revisions

### 1. Make each application self-contained

Use frozen source files only to expose compact defining equations and semantics in the manuscript.

**Plasma:** include the frozen D10-ZF linear model/operator definition sufficient for an external reader to understand state variables, free-energy metric `M`, radial particle-transport channel `Q_Gamma`, `B=I`, `R_in=M`, time normalization, horizon ladder and resolution definition. Do not alter the frozen point.

**Neuro:** include the frozen CMC state/filter structure sufficient to define synaptic-filter storage, the V1-SP -> V4-SS pathway contribution, `A=A_rest+A_{j->i}`, the formula

\[
Q_{j\to i}=\frac12(A_{j\to i}^\dagger M+MA_{j\to i}),
\]

and the construction/meaning of the rank-two two-pulse preparation map. State that pathway sign refers to increasing/decreasing the chosen storage rate, not excitatory/inhibitory sign.

**Climate/Ocean:** include the frozen two-layer Phillips-QG PV equations, physical state restriction/boundary conditions, QG perturbation-energy definition, signed heat-transport definition/sign convention, `B=I`, `R_in=M_K`, time normalization and frozen resolution ladder.

If full details are too long for the main text, create a clearly marked Supplement/Methods-appendix section in the Markdown draft. Do not omit the compact defining equations from the main manuscript.

### 2. Clarify study-design terminology

Default external wording:

- “pre-specified and frozen before objective-separation evaluation”, or
- “prospectively frozen in the version-controlled analysis record before effect inspection”.

Do not use “preregistered” as the default unless the text explicitly explains the commit/registration chronology and makes the intended meaning defensible.

### 3. State operational verdict criteria

Add a concise Methods table/subsection defining:

- optimizer/subspace angle;
- performance gap `Delta_Q`;
- study-specific strong criterion `theta >= 20 deg` and `Delta_Q >= 0.25` on at least two neighboring horizons;
- domain-specific numerical/robustness gates at the level needed to understand the verdicts;
- explicit statement that thresholds are operational rules for this study, not universal physical constants.

Do not change any frozen verdict rule.

### 4. Normalize notation

Resolve the `1/2 x^dagger M x` versus `K_M` factor convention explicitly. Preserve domain-specific language:

- Plasma = free energy;
- Neuro = synaptic-filter storage per input cost;
- Climate = QG perturbation energy.

Keep Neuro cumulative-negative-reachability restriction explicit.

### 5. Tighten Abstract and Introduction

- shorten Abstract and reduce operator detail;
- retain one compact quantitative witness per domain;
- keep the Climate 90-degree / 4.12% contrast;
- reduce repetitive statements in Introduction;
- keep established prior art visible before novelty/contribution language.

### 6. Strengthen Discussion

Add an explicit distinction between geometric nonidentity and decision/practical relevance. Define “physical channel” broadly enough to include transport channels and the Neuro pathway contribution without implying a common conserved-flux semantics.

### 7. Bibliographic normalization

Using only already approved literature sources, normalize full metadata/DOIs where available and clearly flag any entry whose final publication status still needs manual verification. This is not a new novelty search.

### 8. Preserve figure guardrails

Update the figure/evidence maps only if needed to match Revision 0.2 structure. No figure may require a rerun, new horizon, interpolation-based result, new eigensolve or new model calculation.

## Required outputs

Create:

`research/manuscript/manuscript_draft_0_2.md`

Update if necessary:

`research/manuscript/evidence_citation_map_0_1.md`

`research/manuscript/figure_source_map_0_1.md`

Update:

`research/manuscript/STATUS.md`

`research/master/STATUS.md`

and append decisions to:

`research/master/decision_branch_log.md`

After completion, set MASTER status to:

`MANUSCRIPT REVISION 0.2 COMPLETE — RETURN TO MASTER FOR STRUCTURE FREEZE`

and STOP.

## STOP boundary

Do not target a journal, submit, generate new scientific results, open protected branches, or change the frozen three-domain architecture in this task.