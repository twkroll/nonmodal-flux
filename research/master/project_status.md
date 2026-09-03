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
- Manuscript Structural Revision Package 0.2: **COMPLETE**.
- **Manuscript Structure Freeze 0.2: STABLE — MANUSCRIPT ARCHITECTURE FROZEN.**

## Frozen evidence base

The robust main-paper application evidence remains:

- Plasma `P2-A` — strong;
- Neuro `NEURO-STRONG` — strong;
- Climate-A `CLIM-WEAK` — weak but robust and scientifically informative.

Climate-B remains a frozen negative robustness result. At fixed truncation it showed large separation and `Delta_shift=1` to roundoff, but zero of six frozen horizons passed the full refinement protocol. It is therefore excluded from the main positive evidence sequence and retained only as qualified robustness-rejection evidence.

## Manuscript architecture

The paper remains a methods/application paper on physics-informed objective-nonredundancy diagnostics in stable linear dynamics. Novelty remains `N2+N3` with domain-specific `N1`; no mathematical novelty claim is authorized.

Frozen main-text architecture:

1. Introduction
2. Common finite-time framework and study design
3. Application methods: Plasma, Neuro, Climate-A
4. Results: Plasma, Neuro, Climate-A
5. Cross-domain synthesis and robustness lessons
   - geometry versus target performance
   - brief Climate-B robustness rejection
6. Discussion and limitations
7. Conclusion

Climate-B receives full treatment in Supplement S5, not as a fourth main results section.

## Main-text / Supplement split

Main text keeps compact defining physics, the common finite-time operators/diagnostics, study-specific strong criterion, the three robust-domain results, cross-domain synthesis, and a brief Climate-B rejection lesson.

Supplement holds detailed matrices/parameter ledgers/tolerances/freeze chronology and full domain reproducibility material. Climate-B S5 records the complete one-shot workflow, passed local numerical/direct gates, failed cross-resolution gates, parity mechanism, and frozen `CLIM-B-FAIL` verdict.

## Figure/table architecture

Main figures are frozen to:

- Fig. 1 workflow/domain semantics;
- Fig. 2 Plasma;
- Fig. 3 Neuro;
- Fig. 4 Climate-A;
- Fig. 5 simplified non-inferential robust-domain geometry/performance summary, with no phase-diagram framing.

Main Table 1 remains model/objective/admissible-geometry definitions for Plasma/Neuro/Climate-A.

The detailed operational rules/outcome table moves to Supplement and may include Climate-B only as a failed robustness case. Climate-B receives at least one Supplement robustness figure/table if directly supported by frozen artifacts.

## Claims and title

The central claim remains:

\[
\boxed{\text{storage/state-optimal and signed physical-channel-optimal perturbations need not be redundant,}}
\]

but the magnitude and practical consequence of separation depend on system, horizon, observable, admissible geometry, and robustness.

The Climate-B failure adds only the methodological lesson

\[
\boxed{\text{large fixed-resolution objective separation does not imply a robust physical demonstration}.}
\]

Current Draft-0.2 title remains the canonical working title. Exact title shortening is deferred to journal/audience targeting after Draft 0.3.

Default external terminology remains `pre-specified and frozen before objective-separation evaluation`; unqualified `preregistered` remains disallowed absent defensible registration chronology.

## Branch states

- CORE: `STABLE / WAIT`
- Plasma: `P2-A / FROZEN`
- Neuro: `NEURO-STRONG / FROZEN / WAIT`
- Climate-A: `CLIM-WEAK / FROZEN`
- Climate-B: `CLIM-B-FAIL / RESULT FROZEN / STOP`
- Literature: `COMPLETE / WAIT`
- Manuscript: `STRUCTURE FREEZE 0.2 STABLE / REVISION 0.3 READY`
- MODES / CONT / CASCADE: `WAIT`
- Power Grids: `PROTECTED`
- Photonics/Waves: `PROTECTED`
- realistic Fusion: `PROTECTED`
- delayed Neuro / higher-fidelity Climate: `PROTECTED`

## Freeze check

All scientific freezes are current. There is no active scientific blocker and no scientifically required new calculation before the first manuscript proceeds.

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

These meanings must remain distinct.

## Rollback points

1. Plasma `P2-A` result freeze.
2. Neuro `NEURO-STRONG` result freeze.
3. Climate-A `CLIM-WEAK` result freeze.
4. Cross-Domain Result Integration & Freeze 0.1.
5. Manuscript Claim Freeze / Draft 0.2.
6. Climate-B Candidate / Numerical Qualification / Pilot freezes.
7. Climate-B Execution / Result Integration & Freeze 0.1.
8. **Manuscript Structure Freeze 0.2.**

## Current dependency

The only active task is editorial implementation:

\[
\boxed{\text{Manuscript Structural Revision Package 0.3}.}
\]

Canonical instruction:

`research/master/prompts/manuscript_structural_revision_package_0_3.md`

After Revision 0.3 returns, MASTER should decide between frozen-data figure production and journal/audience positioning. No new science is authorized in Revision 0.3.
