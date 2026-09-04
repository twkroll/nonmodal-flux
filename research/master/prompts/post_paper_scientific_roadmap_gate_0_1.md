# Post-Paper Scientific Roadmap Gate 0.1 — MASTER Instruction

**Authority:** MASTER / `research/master/first_paper_scientific_content_freeze_0_1.md`  
**Scope:** choose the next scientific program after the first-paper scientific-content baseline has been frozen. This is a roadmap/branch-selection gate only; do not yet execute new simulations, theory derivations, parameter searches, or application pilots.

## Read first

- `research/master/STATUS.md`;
- `research/master/first_paper_scientific_content_freeze_0_1.md`;
- `research/master/submission_readiness_gate_0_1.md`;
- `research/master/project_status.md`;
- `research/master/decision_branch_log.md`;
- `research/master/decision_branch_log_addendum_0_1.md`;
- relevant branch `STATUS.md` files for CORE, MODES, CONT, CASCADE, Neuro, Climate, Power Grids, Photonics/Waves, Fusion, Literature, and Manuscript.

## Absolute prohibitions

Do not:

- alter the frozen first-paper scientific content baseline;
- resume submission preparation, cover-letter work, APS portal work, author-list work, OA/APC decisions, or publication formatting;
- perform new scientific calculations, numerical execution, parameter sweeps, theory proofs, or novelty searches in this gate;
- open Power Grids or Photonics/Waves for execution without preserving their protected-collaboration status and obtaining explicit MASTER/user authorization;
- silently reactivate Climate-B or authorize a third Climate candidate;
- use effect size from the first paper as a post-hoc reason to choose/tune a new model or parameter point.

## Gate objective

Select and justify the most sensible next scientific branch or tightly coupled pair of branches after the first paper, while preserving rollback points and avoiding premature parallel branching.

## Candidate program families to assess

At minimum compare:

1. **CORE 0.2 / theory consolidation** — only if there is a concrete unresolved mathematical/structural question not already demoted as known theory;
2. **MODES** — structure-preserving modal/reduction diagnostics, dynamic jet/Krylov mechanisms, and representation robustness;
3. **CONT** — continuation of finite-time signed objectives, optimizer/subspace switches, parameter dependence, and degeneracy-aware tracking without overstating bifurcation language;
4. **CASCADE** — scale-to-scale signed channels and multichannel transfer where a physically defined quadratic flux is available;
5. **Neuro next-step** — delayed/pathway-expanded or higher-fidelity admissible-input geometry, only if it creates a scientifically distinct question rather than repeating the first-paper witness;
6. **Higher-fidelity Climate/Ocean** — only as a new scientific program, not as a repair of Climate-A/B;
7. **realistic Fusion** — protected high-value application branch requiring domain-specific physical channel definition and qualification;
8. **Power Grids** — protected collaboration branch: storage/transient-response objective versus directed transfer/corridor-loading channel;
9. **Photonics/Waves** — protected collaboration branch: stored electromagnetic energy versus directed Poynting-flux/channel objective.

## Required evaluation criteria

For each candidate family classify:

- scientific question;
- novelty potential (`N0`–`N4`) without performing a new literature search;
- dependence on existing CORE machinery;
- need for new theory versus application work;
- expected falsifiability / possibility of weak/null/fail result;
- computational and implementation cost;
- domain-risk / semantic-risk;
- collaboration/protection constraints;
- whether it can produce a genuinely new paper rather than a minor extension of Paper 1;
- whether it should be run alone or in parallel with another branch;
- minimum next Gate/Freeze needed before any effect inspection.

## Selection rules

Prefer a program that:

- asks a question not already answered by Paper 1;
- can fail cleanly under pre-effect gates;
- does not require retuning old pilots;
- uses the integrated framework where useful but does not force every future project into the same paper structure;
- preserves Power Grid/Photonics collaboration protections;
- keeps a clear rollback boundary from the frozen first paper.

Do not select a branch merely because it is likely to give a large objective-separation effect.

## Required output

Create:

`research/master/post_paper_scientific_roadmap_gate_0_1.md`

with:

- current post-paper baseline;
- comparison matrix of all candidate program families;
- recommended primary next program;
- optional secondary/parallel program only if clearly justified;
- branches that must remain parked;
- exact dependency chain and Gate → Freeze → Execution sequence for the selected program;
- whether a literature-positioning check is needed before or after the first scientific gate;
- exact next branch/chat and exact command/handoff prompt;
- rollback/STOP conditions.

Update MASTER status and decision log. If the selected next step requires more than bare `GO`, create a committed handoff prompt under `research/master/prompts/` and point the selected branch `STATUS.md` to it.

## STOP

**STOP — ROADMAP SELECTION ONLY; DO NOT EXECUTE THE NEW SCIENTIFIC PROGRAM IN THE SAME GATE.**