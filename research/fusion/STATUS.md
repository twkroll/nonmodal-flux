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

F2.7 `0_1` remains HOLD / spectrally indeterminate because the exact qualified F2.6 `0_3` operator is not canonically executable.

MASTER released F2.6A solely to recover and freeze an exact reproducible operator artifact. F2.6A has now audited the canonical repository and CI provenance and cannot establish exact source-level equivalence without introducing new implementation choices.

## F2.6A result

Canonical report:

`research/fusion/fusion_f2_6a_canonical_operator_artifact_reproducibility_gate_0_1.md`

Machine-readable manifest:

`research/fusion/fusion_f2_6a_canonical_operator_artifact_reproducibility_manifest_0_1.json`

**Status:** `F2.6A HOLD — EXACT OPERATOR EQUIVALENCE NOT ESTABLISHED — RETURN TO MASTER`

The target remains

\[
E_K\dot x_K=F_Kx_K,
\qquad
A_K=E_K^{-1}F_K,
\]

with the frozen repaired ladder

\[
\boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.}
\]

The canonical F2.6 `0_3` report and diagnostics contain the abstract factorization and structural residuals but do not contain the exact coefficient-level weak/SBP streaming-mirror implementation, trapped-electron orbit projection maps, complete serialized `D_K/S_K/C_K/R_K` factors and state layouts, or the exact `F_K` source-level action.

F2.6 `0_3` CI #412 checked out the exact PASS commit, ran the generic pytest suite (`210 passed`) and published no artifacts. No missing operator source or factor archive can be recovered from that run.

Accordingly F2.6A commits no substitute `apply_E/apply_F/solve_E` implementation. Doing so from prose would create a new numerical realization and violate the exact-equivalence requirement.

## MASTER decision required

MASTER must choose one of two provenance-clean paths:

1. recover/publish the original source-level F2.6 `0_3` builder or an exact serialized factor set tied unambiguously to its diagnostics, then re-release F2.6A; or
2. if that provenance object does not exist, authorize a new versioned operator-implementation freeze and complete algebraic requalification on that implementation before any F2.7 rerun.

No F2.6 `0_3` scientific conclusion is revoked by this reproducibility HOLD.

## Active instruction

**Next instruction:** none in this branch.

A bare `GO` must not construct a replacement operator, resume F2.7, inspect spectra or start finite-time work until MASTER commits an explicit new handoff.

## Forbidden while HOLD remains

Do not construct a substitute F2-R operator from prose and label it F2.6 `0_3`. Do not inspect eigenvalues, Ritz pairs, spectral abscissa, growth rates, pseudospectra or eigenvectors. Do not construct propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not change F2.1–F2.5R, the repaired ladder, physical channels, weak/SBP convention, bounce/quasineutrality treatment or physical point. Do not run GENE, add collisions/damping, reopen R1 or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

**STOP / RETURN TO MASTER.**
