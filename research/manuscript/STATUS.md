# Manuscript Branch Status

**Last updated:** 2026-09-03  
**Branch:** `main`

## Current state

`Manuscript Structural Revision Package 0.2` is complete.

Revision 0.2 was produced from frozen evidence and model/specification sources only. It introduces no new simulation, parameter, horizon, objective, pathway, admissible geometry, or novelty claim.

The revision resolves the major Draft Review Gate 0.1 writing/reproducibility items:

- Plasma, Neuro and Climate/Ocean now contain compact self-contained defining physics in the manuscript;
- `A/M/Q/B/R_in`, state/admissible geometry and time normalization are exposed at manuscript level;
- default external terminology is “pre-specified and frozen before objective-separation evaluation” rather than unqualified “preregistered”;
- the study-specific strong criterion `theta >= 20 deg`, `Delta_Q >= 0.25` on two neighboring horizons is stated explicitly and labeled non-universal;
- the `1/2 x^dagger M x` versus `K_M` convention is made explicit;
- Neuro pathway-sign semantics and the no-negative-cumulative-reachability restriction remain explicit;
- Climate remains the main-text weak geometry-versus-performance contrast;
- bibliography metadata were normalized only from already approved literature sources, with Ogino 2026 flagged for final-status verification;
- evidence and figure maps were updated to match Revision 0.2 without authorizing new calculations.

Frozen manuscript architecture remains:

- Plasma/D10-ZF `P2-A` — strong primary domain anchor;
- Neuro/CMC `NEURO-STRONG` — strong cross-domain demonstrator;
- Climate/Ocean QG `CLIM-WEAK` — robust weak/contrast case.

## Canonical manuscript package

- `research/manuscript/manuscript_draft_0_2.md`
- `research/manuscript/evidence_citation_map_0_1.md`
- `research/manuscript/figure_source_map_0_1.md`
- this `STATUS.md`

Draft 0.1 is retained as the previous editorial rollback point.

## Active instruction

**Status:** `MANUSCRIPT REVISION 0.2 COMPLETE — RETURN TO MASTER FOR STRUCTURE FREEZE`

**Next instruction:** `RETURN TO MASTER FOR STRUCTURE FREEZE`

No bare `GO` in this branch may create a journal submission, new scientific calculation, new figure requiring simulation, new novelty claim, or protected-branch work until MASTER explicitly opens the next instruction.

## Authority

- `research/master/manuscript_draft_review_gate_0_1.md`
- `research/master/prompts/manuscript_structural_revision_package_0_2.md`
- `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`

**STOP.**