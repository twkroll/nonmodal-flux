# MASTER Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Current state

All first-paper savepoints remain intact and the submission track remains parked by user choice. Post-paper science remains focused on Fusion.

Stable first-paper lineage remains unchanged: CORE `STABLE`; Plasma `P2-A` frozen; Neuro `NEURO-STRONG` frozen; Climate-A `CLIM-WEAK` frozen; Climate-B `CLIM-B-FAIL` frozen; Manuscript Revision 0.4 `COMPLETE — PASS`; First Paper Scientific Content Freeze 0.1 `STABLE`.

Post-paper Fusion lineage:

- R1 structural no-go / literature positioning: frozen;
- F2.1–F2.4: `PASS / MASTER-INTEGRATED / FROZEN`;
- historical F2.5 and F2.6 `0_1`/`0_2`: immutable audit records;
- local-B Ion-FLR Erratum 0.1: `STABLE`;
- F2.5R repaired `N_mu=(16,24,40)`: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.6 `0_3`: `PASS / MASTER-INTEGRATED — DISCRETE OPERATOR/CHANNEL ALGEBRA QUALIFIED`;
- F2.7 `0_1`: `HOLD / MASTER-INTEGRATED — SPECTRALLY INDETERMINATE BECAUSE NO CANONICAL EXECUTABLE OPERATOR ARTIFACT EXISTS`;
- F2.6A: `HOLD / MASTER-INTEGRATED — EXACT HISTORICAL OPERATOR EQUIVALENCE NOT ESTABLISHED`;
- Fusion F2.6A Reproducibility HOLD Integration Freeze 0.1: `STABLE — F2.6B RELEASED`.

## Frozen F2-R structure

The reduced model remains

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons and collisionless balance

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

The F2.3 physical point, F2.4 input geometry and local-B ion-FLR convention remain frozen. The controlling repaired magnetic-moment orders remain

\[
\boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.}
\]

All other F2.5/F2.5R numerical objects remain frozen.

F2.6 `0_3` remains a qualified historical algebraic result. In particular, its complete discrete balance

\[
A_K^\dagger M_K+M_KA_K
=2\left(G_\Gamma Q_{\Gamma,K}+G_{T,i}Q_{q_i,K}+G_{T,e}Q_{q_e,K}\right)
\]

remains frozen with reported maximum relative residuals approximately `1.92e-14 / 3.15e-13 / 1.61e-13` on K0/K1/K2.

## F2.6A HOLD integrated result

Canonical result:

`research/fusion/fusion_f2_6a_canonical_operator_artifact_reproducibility_gate_0_1.md`

Manifest:

`research/fusion/fusion_f2_6a_canonical_operator_artifact_reproducibility_manifest_0_1.json`

Branch commit `1ac71cd2ad0d5e9c7388c5b21229629484323aa2`; Python CI #426 = `SUCCESS`.

F2.6A established that the canonical repository and F2.6 `0_3` CI provenance do not contain a source-level builder or serialized factor set sufficient to prove exact identity of

\[
E_Kx,\qquad F_Kx,\qquad E_K^{-1}x
\]

for the historical qualified realization. The F2.6 `0_3` CI run #412 published no artifacts. The report/diagnostics constrain the implementation but do not uniquely determine coefficient-level weak/SBP streaming-mirror assembly, trapped-electron orbit maps, complete `D/S/C/R` factors/layouts or the full source-level `F_K` action.

F2.6A correctly created no substitute operator. F2.7 therefore remains spectrally indeterminate and blocked.

MASTER savepoint:

`research/master/fusion_f2_6a_reproducibility_hold_integration_freeze_0_1.md`

## MASTER provenance decision

MASTER selects the provenance-clean new-version path:

\[
\boxed{\text{F2.6B — Source-Level Matrix-Free Operator Implementation Freeze / Algebraic Requalification Gate 0.1}.}
\]

F2.6B may make only previously implicit coefficient-level implementation choices explicit and source-controlled. It must preserve all frozen F2.1–F2.5R physics/numerics and implement deterministic matrix-free interfaces for `apply_E`, `apply_F` and `solve_E` on K0/K1/K2.

It must then rerun the complete F2.6 algebraic qualification on that new versioned implementation. It may not claim exact historical source identity with F2.6 `0_3`.

## Current dependency chain

1. F2.1–F2.4 — **COMPLETE / FROZEN**;
2. historical F2.5/F2.6 failure lineage — **PRESERVED AUDIT RECORDS**;
3. F2.5R quadrature repair — **PASS / FROZEN**;
4. F2.6 `0_3` algebraic qualification — **PASS / HISTORICAL QUALIFIED RESULT**;
5. F2.7 `0_1` spectral qualification — **HOLD / MASTER-INTEGRATED**;
6. F2.6A exact-artifact reproducibility gate — **HOLD / MASTER-INTEGRATED**;
7. F2.6B source-level operator implementation + algebraic requalification — **READY**;
8. only after F2.6B PASS + MASTER integration may a new versioned F2.7 rerun be released;
9. finite-time pilot work remains blocked until later explicit spectral-regime acceptance and pilot freeze.

## F2.6B boundary

Authorized: explicit source-level state layout/indexing, weak/SBP split/skew assembly, trapped-electron orbit projections, `D/S/C/R` constructors, drift/gradient-drive `F_K` action, physical-channel implementation, stable `apply_E/apply_F/solve_E` interfaces, regression metadata and full algebraic requalification.

Not authorized: changes to F2.1–F2.5R; eigenvalues/Ritz/spectral abscissa/pseudospectrum; propagators/Gramians/cumulative objectives; optimizers/angles/gaps; physical parameter scans; resolutions outside frozen K0/K1/K2; GENE; damping/collisions; retuning.

If a source-level choice remains genuinely underdetermined by frozen physics/structure-preserving criteria, F2.6B must return HOLD rather than use desired spectral/effect behavior to choose it.

## Parallelism / parked branches

Fusion is the only active scientific branch. Literature, MODES, CONT, CASCADE, CORE 0.2, Neuro extensions and higher-fidelity Climate remain parked. Power Grids and Photonics/Waves remain `PROTECTED`. Paper-1 submission remains parked.

No parallel science is opened during F2.6B. The present blocker is source-level numerical provenance/reproducibility, not a reason to open MODES or CONT.

## Decision record

Canonical continuation now reaches **DEC-640** in `research/master/decision_branch_log_addendum_0_16.md`.

## Rollback points

The latest protected post-paper savepoint is

\[
\boxed{\text{Fusion F2.6A Reproducibility HOLD Integration Freeze 0.1}}.
\]

F2.7 HOLD, F2.6 `0_3`, F2.5R and all historical F2.5/F2.6 savepoints remain preserved.

## Active instruction

**Status:** `FUSION F2.6B SOURCE-LEVEL MATRIX-FREE OPERATOR IMPLEMENTATION / ALGEBRAIC REQUALIFICATION READY — AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Next instruction:**

`research/master/prompts/fusion_f2_6b_source_level_operator_implementation_requalification_gate_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

## STOP boundary

Do not resume F2.7 directly, inspect spectra or finite-time effects, claim unverifiable historical source identity, retune F2.1–F2.5R, run GENE or open parked/protected branches.

**STOP — AWAIT FUSION F2.6B `GO`.**
