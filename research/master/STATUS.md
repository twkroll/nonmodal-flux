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
- F2.7 `0_1`: `HOLD — SPECTRALLY INDETERMINATE BECAUSE CANONICAL EXECUTABLE OPERATOR ARTIFACT IS MISSING`, MASTER-integrated;
- Fusion F2.7 HOLD / Canonical Operator-Artifact Integration Freeze 0.1: `STABLE — F2.6A RELEASED`.

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

F2.6 `0_3` remains fully qualified. In particular, the complete discrete balance

\[
A_K^\dagger M_K+M_KA_K
=2\left(G_\Gamma Q_{\Gamma,K}+G_{T,i}Q_{q_i,K}+G_{T,e}Q_{q_e,K}\right)
\]

remains frozen on K0/K1/K2 with maximum reported relative residuals approximately `1.92e-14 / 3.15e-13 / 1.61e-13`.

## F2.7 HOLD integrated result

Canonical result:

`research/fusion/fusion_f2_7_numerical_spectral_qualification_gate_0_1.md`

Branch commit `e4453080cae805a4e50d019975f6722130e88903`; Python CI #419 = `SUCCESS`.

F2.7 ran no eigensolver and reports no eigenvalues or spectral abscissa. The blocker is exactly:

\[
\boxed{\text{no canonical executable/serialized F2.6 `0_3` realization of }(E_K,F_K).}
\]

The repository contains the qualified report/diagnostics but not a versioned artifact sufficient to reproduce without new choices

\[
E_Kx,\qquad F_Kx,\qquad E_K^{-1}x
\]

for K0/K1/K2. The current point is therefore **spectrally indeterminate**, not established marginal, stable or unstable.

MASTER savepoint:

`research/master/fusion_f2_7_hold_operator_artifact_integration_freeze_0_1.md`

## Current dependency chain

1. F2.1–F2.4 — **COMPLETE / FROZEN**;
2. historical F2.5/F2.6 failure lineage — **PRESERVED AUDIT RECORDS**;
3. F2.5R quadrature repair — **PASS / FROZEN**;
4. F2.6 `0_3` algebraic qualification — **PASS / FROZEN**;
5. F2.7 `0_1` spectral qualification — **HOLD / MASTER-INTEGRATED**;
6. F2.6A canonical matrix-free operator artifact / reproducibility freeze — **READY**;
7. only after F2.6A PASS and MASTER integration may F2.7 be rerun;
8. finite-time pilot work remains blocked until a later explicit spectral-regime acceptance and pilot freeze.

## F2.6A repair boundary

F2.6A may only publish/freeze a versioned executable matrix-free realization or equivalent serialized factor set for the already-qualified F2.6 `0_3` maps `E_K`, `F_K`, `E_K^{-1}` and verify that it reproduces the frozen F2.6 structural diagnostics.

If exact equivalence cannot be established without introducing new implementation choices, F2.6A must return HOLD. It may not canonize a replacement operator.

No eigensolver, Ritz pair, spectral abscissa, growth rate, pseudospectrum, propagator, Gramian, cumulative objective, optimizer, angle, performance gap, physical-parameter scan, GENE, damping/collision or retuning work is authorized.

## Parallelism / parked branches

Fusion is the only active scientific branch. Literature, MODES, CONT, CASCADE, CORE 0.2, Neuro extensions and higher-fidelity Climate remain parked. Power Grids and Photonics/Waves remain `PROTECTED`. Paper-1 submission remains parked.

No parallel scientific branch is opened during F2.6A. MODES remains conditional on a genuine representation/reduction issue after the canonical operator artifact exists; CONT remains premature without an authorized physical parameter family.

## Decision record

Canonical continuation now reaches **DEC-630** in `research/master/decision_branch_log_addendum_0_15.md`.

## Rollback points

The latest protected post-paper savepoint is

\[
\boxed{\text{Fusion F2.7 HOLD / Canonical Operator-Artifact Integration Freeze 0.1}}.
\]

All prior F2.5/F2.6/F2.5R savepoints remain preserved.

## Active instruction

**Status:** `FUSION F2.6A CANONICAL MATRIX-FREE OPERATOR ARTIFACT / REPRODUCIBILITY FREEZE READY — AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Next instruction:**

`research/master/prompts/fusion_f2_6a_canonical_operator_artifact_reproducibility_gate_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

## STOP boundary

Do not resume F2.7 directly, reconstruct a substitute operator for spectral work, inspect eigenvalues or finite-time effects, retune F2.3/F2.4/F2.5R, run GENE or open parked/protected branches.

**STOP — AWAIT FUSION F2.6A `GO`.**
