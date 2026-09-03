# MASTER Project Status

**Last updated:** 2026-09-03  
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
- Manuscript Structure Freeze 0.2: **STABLE — MANUSCRIPT ARCHITECTURE FROZEN**.
- **Manuscript Structural Revision Package 0.3: COMPLETE.**

## Canonical manuscript package

The current manuscript savepoint is:

- `research/manuscript/manuscript_draft_0_3.md`;
- `research/manuscript/evidence_citation_map_0_2.md`;
- `research/manuscript/figure_source_map_0_2.md`.

Draft 0.2 and maps 0.1 remain editorial rollback points. Revision 0.3 changed no scientific result and implemented the frozen Structure Freeze 0.2 architecture. Python CI #253 on the Revision-0.3 return commit completed successfully.

## Frozen evidence base

The robust main-paper application sequence remains:

- Plasma `P2-A` — strong;
- Neuro `NEURO-STRONG` — strong;
- Climate-A `CLIM-WEAK` — weak but robust and scientifically informative.

Climate-B remains a frozen negative robustness result. At fixed truncation it showed large separation and `Delta_shift=1` to roundoff, but zero of six frozen horizons passed the full refinement protocol. It is therefore excluded from the main positive evidence sequence and retained only as qualified robustness-rejection evidence in brief main text + Supplement S5.

## Manuscript architecture

The paper remains a methods/application paper on physics-informed objective-nonredundancy diagnostics in stable linear dynamics. Novelty remains `N2+N3` with domain-specific `N1`; no mathematical novelty claim is authorized.

Frozen main-text architecture:

1. Introduction
2. Common finite-time framework and study design
3. Application methods: Plasma, Neuro, Climate-A
4. Results: Plasma, Neuro, Climate-A
5. Cross-domain synthesis and robustness lessons
   - geometry versus target performance
   - Climate-B robustness rejection
6. Discussion and limitations
7. Conclusion

Supplement S1-S6 contains detailed reproducibility material, with the full Climate-B rejection case in S5.

## Figure/table readiness

The scientific content of all figures/tables is now frozen in `figure_source_map_0_2.md`.

Main figures:

- Fig. 1 workflow/domain semantics;
- Fig. 2 Plasma;
- Fig. 3 Neuro;
- Fig. 4 Climate-A;
- Fig. 5 non-inferential robust-domain geometry/performance summary.

Main Table 1 remains the three-domain model/objective/admissible-geometry table. The operational rules/outcome table is Supplement material. Climate-B gets a Supplement robustness figure/table only from stored frozen artifacts.

No figure has yet been produced. No new scientific computation is needed for figure production.

## Claims and title

The central claim remains:

\[
\boxed{\text{storage/state-optimal and signed physical-channel-optimal perturbations need not be redundant,}}
\]

with magnitude and practical consequence dependent on system, horizon, observable, admissible geometry, and robustness.

Climate-B adds only the methodological lesson

\[
\boxed{\text{large fixed-resolution objective separation does not imply a robust physical demonstration}.}
\]

The canonical working title remains:

`Diagnosing objective nonredundancy in stable linear dynamics: a physics-informed finite-time workflow across plasma, neural and geophysical models`

Exact title shortening remains deferred to journal/audience positioning.

Default external terminology remains `pre-specified and frozen before objective-separation evaluation`; unqualified `preregistered` remains disallowed absent defensible chronology.

## Branch states

- CORE: `STABLE / WAIT`
- Plasma: `P2-A / FROZEN`
- Neuro: `NEURO-STRONG / FROZEN / WAIT`
- Climate-A: `CLIM-WEAK / FROZEN`
- Climate-B: `CLIM-B-FAIL / RESULT FROZEN / STOP`
- Literature: `COMPLETE / WAIT`
- Manuscript: `REVISION 0.3 COMPLETE / RETURNED TO MASTER`
- MODES / CONT / CASCADE: `WAIT`
- Power Grids: `PROTECTED`
- Photonics/Waves: `PROTECTED`
- realistic Fusion: `PROTECTED`
- delayed Neuro / higher-fidelity Climate: `PROTECTED`

## Freeze check

All scientific and manuscript-architecture freezes are current. There is no active scientific blocker and no scientifically required new calculation before the first manuscript proceeds.

No Climate-B repair or third Climate candidate is allowed before the first manuscript. Opening protected scientific branches now would be premature.

## Branch-independent methodology

\[
\mathfrak C=(A,M,Q,B,R_{\rm in})
\]

with common finite-time positive-objective and signed-channel operators, signed extrema, optimizer/subspace geometry, target-performance gap, physical reconstruction, robustness, and anti-retuning discipline.

## Branch-dependent semantics

- Plasma: free energy / signed particle transport.
- Neuro: synaptic-filter storage / signed pathway contribution.
- Climate-A: QG perturbation energy / signed poleward heat transport.
- Climate-B: barotropic perturbation kinetic energy / signed jet-translation forcing; frozen robustness failure.

These meanings remain distinct.

## Rollback points

1. Plasma `P2-A` result freeze.
2. Neuro `NEURO-STRONG` result freeze.
3. Climate-A `CLIM-WEAK` result freeze.
4. Cross-Domain Result Integration & Freeze 0.1.
5. Manuscript Claim Freeze / Draft 0.2.
6. Climate-B Candidate / Numerical Qualification / Pilot freezes.
7. Climate-B Execution / Result Integration & Freeze 0.1.
8. Manuscript Structure Freeze 0.2.
9. **Manuscript Revision 0.3 package.**

## Current dependency

There is no scientific dependency. The sole active project dependency is publication-format positioning:

\[
\boxed{\text{Journal & Audience Positioning Gate 0.1}.}
\]

Canonical instruction:

`research/master/prompts/journal_audience_positioning_gate_0_1.md`

This gate should use current official journal/publisher sources and rank a primary target plus backups without changing frozen science. Figure production remains WAIT until this gate resolves title/format/figure packaging implications.

## Next global step

Run in MASTER:

`Journal & Audience Positioning Gate 0.1`

No new scientific calculation or protected-branch work is authorized before that gate resolves.
