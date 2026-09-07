# MASTER Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Current state

All first-paper savepoints remain intact and the submission track remains parked by user choice. Post-paper science remains focused on Fusion.

Stable first-paper lineage remains unchanged: CORE `STABLE`; Plasma `P2-A` frozen; Neuro `NEURO-STRONG` frozen; Climate-A `CLIM-WEAK` frozen; Climate-B `CLIM-B-FAIL` frozen; Manuscript Revision 0.4 `COMPLETE — PASS`; First Paper Scientific Content Freeze 0.1 `STABLE`.

Post-paper Fusion lineage now includes:

- R1 structural no-go / literature positioning: frozen;
- F2.1–F2.4: `PASS / MASTER-INTEGRATED / FROZEN`;
- historical F2.5 and F2.6 `0_1`/`0_2`: immutable audit records;
- local-B Ion-FLR Erratum 0.1: `STABLE`;
- F2.5R repaired `N_mu=(16,24,40)`: `PASS / MASTER-INTEGRATED / FROZEN`;
- historical F2.6 `0_3`: `PASS / MASTER-INTEGRATED — ALGEBRAICALLY QUALIFIED HISTORICAL RESULT`;
- historical F2.7 `0_1`: `HOLD / MASTER-INTEGRATED — SPECTRALLY INDETERMINATE FROM MISSING EXECUTABLE PROVENANCE`;
- F2.6A: `HOLD / MASTER-INTEGRATED — EXACT HISTORICAL SOURCE IDENTITY NOT ESTABLISHED`;
- F2.6B: `PASS / MASTER-INTEGRATED — NEW SOURCE-LEVEL MATRIX-FREE OPERATOR FROZEN / ALGEBRA REQUALIFIED`;
- Fusion F2.6B Source-Level Operator PASS Integration Freeze 0.1: `STABLE — F2.7 0_2 RELEASED`.

## Frozen F2-R structure

The reduced model remains

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons and collisionless balance

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

The F2.3 physical point, F2.4 input geometry and local-B ion-FLR convention remain frozen. The repaired magnetic-moment orders remain

\[
\boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.}
\]

All other F2.5/F2.5R numerical objects remain frozen.

## F2.6B integrated result

Canonical report:

`research/fusion/fusion_f2_6b_source_level_operator_implementation_requalification_gate_0_1.md`

Canonical executable operator:

`research/fusion/fusion_f2_6b_operator_0_1.py`

Requalification driver / diagnostics / regression test:

- `research/fusion/fusion_f2_6b_requalification_0_1.py`;
- `research/fusion/fusion_f2_6b_requalification_diagnostics_0_1.json`;
- `tests/test_fusion_f2_6b_operator_0_1.py`.

Branch commit `83f004412183d43a1653d3a3a2f9ad104482de7d`; Python CI #433 = `SUCCESS`.

F2.6B is explicitly a new provenance-clean realization and does not claim source identity with historical F2.6 `0_3`.

The frozen public interfaces are

- `build_operator(level)`;
- `apply_E(op,x)`;
- `apply_F(op,x)`;
- `solve_E(op,x)`.

The frozen NumPy C-order state layout is ion `h_i[theta,u,zeta]` followed by trapped-electron `h_e[well,energy,lambda]`, with

\[
\boxed{N_{\rm total}(K0,K1,K2)=(18608,\ 93204,\ 361152).}
\]

The complete pre-spectral algebraic requalification passes on K0/K1/K2. Maximum complete-balance relative residuals are

\[
\boxed{1.29\times10^{-13},\qquad5.64\times10^{-13},\qquad5.87\times10^{-13}.}
\]

No eigenvalue, Ritz value, spectral abscissa, pseudospectrum, propagator, Gramian or finite-time objective was inspected.

MASTER savepoint:

`research/master/fusion_f2_6b_source_level_operator_pass_integration_freeze_0_1.md`

## Current dependency chain

1. F2.1–F2.4 — **COMPLETE / FROZEN**;
2. historical F2.5/F2.6 failure lineage — **PRESERVED AUDIT RECORDS**;
3. F2.5R quadrature repair — **PASS / FROZEN**;
4. historical F2.6 `0_3` algebraic qualification — **PASS / QUALIFIED AUDIT RESULT**;
5. historical F2.7 `0_1` — **HOLD / INTEGRATED**;
6. F2.6A provenance recovery — **HOLD / INTEGRATED**;
7. F2.6B source-level executable implementation + algebraic requalification — **PASS / MASTER-INTEGRATED / FROZEN**;
8. F2.7 `0_2` numerical / spectral qualification on the F2.6B operator — **READY**;
9. after F2.7 `0_2`, MASTER must explicitly accept the spectral regime;
10. only then may targeted Fusion literature positioning and a pre-effect finite-time pilot specification be considered;
11. finite-time execution remains blocked until a later explicit pilot freeze.

## Parallelism / parked branches

Fusion is the only active scientific branch. Literature, MODES, CONT, CASCADE, CORE 0.2, Neuro extensions and higher-fidelity Climate remain parked. Power Grids and Photonics/Waves remain `PROTECTED`. Paper-1 submission remains parked.

No parallel scientific branch is opened during F2.7 `0_2`. MODES remains conditional on a concrete representation/reduction problem; CONT remains premature without an authorized physical parameter family.

## Decision record

Canonical continuation now reaches **DEC-650** in `research/master/decision_branch_log_addendum_0_17.md`.

## Rollback points

The latest protected post-paper savepoint is

\[
\boxed{\text{Fusion F2.6B Source-Level Operator PASS Integration Freeze 0.1}}.
\]

F2.6A HOLD, F2.7 `0_1` HOLD, historical F2.6 `0_3`, F2.5R and all earlier F2.5/F2.6 records remain preserved.

## Active instruction

**Status:** `FUSION F2.7 0_2 NUMERICAL / SPECTRAL QUALIFICATION ON F2.6B OPERATOR READY — AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Next instruction:**

`research/master/prompts/fusion_f2_7_rerun_on_f2_6b_source_operator_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

## STOP boundary

F2.7 `0_2` may inspect only the rightmost modal spectrum of the frozen F2.6B operator. Do not construct propagators, Gramians, cumulative objectives, optimizers, angles or gaps; do not retune F2.1–F2.5R, scan physical parameters, run GENE, add damping/collisions or open parked/protected branches.

**STOP — AWAIT FUSION F2.7 `0_2` `GO`.**
