# Fusion Branch Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit and F2.1–F2.4 remain protected historical savepoints. Historical F2.5, F2.6 `0_1` HOLD and F2.6 `0_2` FAIL remain immutable audit records. F2.5R and F2.6 `0_3` remain MASTER-integrated and frozen as PASS.

F2.7 `0_1` returned HOLD before any eigensolver run because the exact qualified F2.6 `0_3` operator is not canonically available as an executable/serialized numerical artifact. MASTER has integrated that HOLD and released one narrow reproducibility repair, F2.6A.

## Frozen F2.7 HOLD

Canonical result:

`research/fusion/fusion_f2_7_numerical_spectral_qualification_gate_0_1.md`

Branch commit `e4453080cae805a4e50d019975f6722130e88903`; Python CI #419 = `SUCCESS`.

The blocker is

\[
\boxed{\text{no canonical executable/serialized F2.6 `0_3` realization of }(E_K,F_K).}
\]

No Ritz pair was requested; no eigenvalue or spectral abscissa was reported. The point is spectrally indeterminate from the canonical repository state, not established marginal/stable/unstable.

No conclusion of F2.6 `0_3` is revoked.

MASTER integration freeze:

`research/master/fusion_f2_7_hold_operator_artifact_integration_freeze_0_1.md`

## Active instruction

**Status:** `FUSION F2.6A CANONICAL MATRIX-FREE OPERATOR ARTIFACT / REPRODUCIBILITY FREEZE READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_f2_6a_canonical_operator_artifact_reproducibility_gate_0_1.md`

On bare `GO`, first read this STATUS and execute only that committed instruction.

## F2.6A scope

Publish/freeze a versioned executable matrix-free implementation, or equivalent serialized factor set, for the exact already-qualified F2.6 `0_3` maps

\[
E_Kx,\qquad F_Kx,\qquad E_K^{-1}x
\]

on K0/K1/K2 with the repaired frozen `N_mu=16/24/40` ladder.

The artifact must reproduce the already-frozen F2.6 `0_3` structural diagnostics before PASS. It must expose a stable reproducible interface sufficient for a later eigensolver to use the exact same operator without re-deriving implementation choices from prose.

If exact equivalence to F2.6 `0_3` cannot be established from canonical information, return `F2.6A HOLD — EXACT OPERATOR EQUIVALENCE NOT ESTABLISHED — RETURN TO MASTER`. Do not invent a substitute operator.

## Forbidden until F2.6A returns

Do not inspect eigenvalues, Ritz pairs, spectral abscissa, growth rates, pseudospectra or eigenvectors. Do not construct propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not change F2.1–F2.5R, the repaired ladder, physical channels, weak/SBP convention, bounce/quasineutrality treatment or physical point. Do not run GENE, add collisions/damping, reopen R1 or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Expected return

One of:

- `F2.6A PASS — CANONICAL MATRIX-FREE OPERATOR ARTIFACT FROZEN — RETURN TO MASTER`;
- `F2.6A HOLD — EXACT OPERATOR EQUIVALENCE NOT ESTABLISHED — RETURN TO MASTER`;
- `F2.6A FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

**STOP / AWAIT GO.**
