# MASTER Status

**Last updated:** 2026-09-03  
**Branch:** `main`

## Current state

The established scientific and manuscript savepoints remain intact:

- CORE Mathematical / Integration / Interpretation freezes: `STABLE`;
- Plasma/D10-ZF: `P2-A` — strong primary domain anchor, `FROZEN`;
- Neuro/CMC: `NEURO-STRONG` — strong cross-domain demonstrator, `FROZEN`;
- Climate-A/Phillips-QG heat transport: `CLIM-WEAK` — permanent weak/contrast result, `FROZEN`;
- Cross-Domain Result Integration & Freeze 0.1: `STABLE`;
- application literature positioning: `COMPLETE`;
- manuscript claim freeze: `STABLE`;
- Manuscript Structural Revision Package 0.2: `COMPLETE`.

The one-shot Climate-B branch has now completed all pre-effect gates:

- Climate Intra-Domain Contrast Feasibility Gate 0.1: `PASS`;
- Climate Intra-Domain Contrast Candidate Freeze 0.1: `STABLE`;
- Climate Intra-Domain Contrast Numerical Qualification 0.1: `QUALIFIED`;
- Climate Intra-Domain Contrast Pilot Specification 0.1: `COMPLETE`;
- **Climate Intra-Domain Contrast Pilot Freeze 0.1: `STABLE — EXECUTION RELEASED`.**

Climate-B remains the frozen equivalent-barotropic Bickley jet with perturbation kinetic energy and signed eddy forcing of the infinitesimal poleward jet-translation coordinate `g=-U'`, with `B=I`, `R_in=M_K`.

The complete frozen resolution ladder is spectrally stable,

\[
\alpha(A_K)=-0.05787037037037=-0.1\,\mathrm d^{-1}<0,
\]

and the specification return commit `495b53819c8b6b2cca0cb6e061898ad2efe73e1d` passed Python CI #228.

The final pre-effect Pilot Freeze now fixes the six-horizon ladder

\[
T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\},
\]

finite-time operators, signed extrema, degeneracy-aware optimizer/subspace diagnostics, `Delta_shift` denominator rule, numerical propagation/integral cross-checks, physical-trajectory reproduction, resolution robustness, physical diagnostics, and one-shot `STRONG/WEAK/NULL/FAIL` logic.

At execution release, no Climate-B finite-time objective value, optimizer, angle, performance gap, horizon dependence, or verdict had been inspected.

## Governance consequence

Exactly one Climate-B execution is now authorized. It must execute all frozen horizons and mandatory resolution roles without retuning or early stopping.

Climate-A may not be retuned, replaced, or relabeled. Climate-B is the only additional Climate attempt authorized before the first manuscript. No third Climate candidate is permitted.

`Manuscript Structure Freeze 0.2` remains on **HOLD**, not canceled. It is the mandatory return point after Climate-B execution/result integration.

No other scientific/application branch should proceed while Climate-B is active.

## Active instruction

**Status:** `CLIMATE-B PILOT FROZEN — EXECUTION READY / AWAIT CLIMATE GO`

**Next instruction:**

`research/master/prompts/climate_intra_domain_contrast_pilot_execution_0_1.md`

Execute it in the existing Climate chat under the shared prompt handoff protocol. A bare `GO` there must first read `research/climate/STATUS.md` and execute only the committed Next instruction.

## Freeze check

No prior freeze is invalidated or overdue. Climate-B Pilot Specification 0.1 and Pilot Freeze 0.1 are new pre-effect rollback/savepoints.

Execution is now timely: an additional pre-effect freeze would be redundant, while manuscript structure freeze before Climate-B resolves would be premature.

Parallel branch work is not recommended. CORE, Plasma, Neuro, Literature, MODES, CONT, CASCADE, Power Grids, Photonics/Waves, realistic Fusion, delayed Neuro, and higher-fidelity Climate remain WAIT/PROTECTED.

## Rollback points

The protected rollback chain is:

1. Plasma `P2-A` result freeze;
2. Neuro `NEURO-STRONG` result freeze;
3. Climate-A `CLIM-WEAK` result freeze;
4. Cross-Domain Result Integration & Freeze 0.1;
5. Manuscript Claim Freeze / Draft 0.2;
6. Climate-B Candidate Freeze 0.1;
7. Climate-B Numerical Qualification 0.1;
8. Climate-B Pilot Specification 0.1;
9. Climate-B Pilot Freeze 0.1.

Climate-B execution may add evidence but may not rewrite any earlier savepoint.

## Branch-independent / branch-dependent distinction

Branch-independent methodology remains

\[
\mathfrak C=(A,M,Q,B,R_{\rm in})
\]

with common finite-time positive-objective and signed-channel operators, signed extrema, optimizer/subspace geometry, target-performance gap, physical reconstruction, robustness, and anti-retuning discipline.

Branch-dependent semantics remain distinct:

- Plasma: free energy / signed particle transport;
- Neuro: synaptic-filter storage / signed pathway contribution;
- Climate-A: QG perturbation energy / signed poleward heat transport;
- Climate-B: barotropic perturbation kinetic energy / signed jet-translation forcing.

## STOP boundary

Do not run `Manuscript Structure Freeze 0.2` yet. Do not target a journal, submit, open another protected branch, alter any Climate-B frozen choice, or authorize a third Climate candidate. The only active scientific action is the frozen one-shot Climate-B execution.