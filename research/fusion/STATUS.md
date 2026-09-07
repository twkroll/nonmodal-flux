# Fusion Branch Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit and F2.1–F2.4 remain protected historical savepoints. Historical F2.5, F2.6 `0_1` HOLD and F2.6 `0_2` FAIL remain immutable audit records. F2.5R and F2.6 `0_3` remain MASTER-integrated and frozen as PASS/historical qualification.

F2.7 `0_1` remains HOLD / spectrally indeterminate because the historical qualified operator is not canonically executable. F2.6A then returned HOLD because exact source-level identity to the historical F2.6 `0_3` realization cannot be established from canonical repository/CI provenance.

MASTER has integrated F2.6A and selected a new provenance-clean path: build and freeze a **new versioned source-level implementation** of the frozen F2-R numerical model, then rerun the complete pre-spectral algebraic qualification before any spectral work.

## Frozen physical / numerical objects

The F2-R physical model, F2.3 point and F2.4 input geometry remain frozen.

\[
\rho_{i0}=v_{Ti}/\Omega_i(B_0),
\qquad
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right),
\]

\[
\boxed{
b_i(\theta)
=(k_\perp(\theta)\rho_{i0})^2
\left(\frac{B_0}{B(\theta)}\right)^2,
\qquad
\Gamma_{0i}=I_0(b_i)e^{-b_i}.
}
\]

The controlling repaired magnetic-moment ladder remains

\[
\boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.}
\]

All other F2.5/F2.5R objects remain unchanged.

## F2.6A integrated HOLD

Canonical report:

`research/fusion/fusion_f2_6a_canonical_operator_artifact_reproducibility_gate_0_1.md`

Manifest:

`research/fusion/fusion_f2_6a_canonical_operator_artifact_reproducibility_manifest_0_1.json`

Branch commit `1ac71cd2ad0d5e9c7388c5b21229629484323aa2`; Python CI #426 = `SUCCESS`.

**Status:** `F2.6A HOLD — EXACT OPERATOR EQUIVALENCE NOT ESTABLISHED — MASTER-INTEGRATED`.

The canonical F2.6 `0_3` report/diagnostics do not uniquely identify the coefficient-level weak/SBP streaming-mirror assembly, trapped-electron orbit maps, complete `D_K/S_K/C_K/R_K` factor/state layout or full source-level `F_K` action. F2.6 `0_3` CI #412 published no artifacts. No original builder or exact serialized factor archive is canonically recoverable.

F2.6A correctly committed no substitute operator. No F2.6 `0_3` scientific conclusion is revoked.

MASTER integration freeze:

`research/master/fusion_f2_6a_reproducibility_hold_integration_freeze_0_1.md`

## Active instruction

**Status:** `FUSION F2.6B SOURCE-LEVEL MATRIX-FREE OPERATOR IMPLEMENTATION / ALGEBRAIC REQUALIFICATION READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_f2_6b_source_level_operator_implementation_requalification_gate_0_1.md`

On bare `GO`, first read this STATUS and execute only that committed instruction.

## F2.6B scope

Create a **new versioned** source-level matrix-free implementation of the frozen F2-R numerical model. Do not claim it is the exact historical F2.6 `0_3` source realization.

Freeze and publish all implementation choices required for reproducibility, including exact state layout/indexing, weak/SBP streaming-mirror split/skew assembly, trapped-electron orbit projection maps, quasineutrality/field factors or deterministic constructors, drift/gradient-drive `F_K` action, independently constructed physical channels and stable `apply_E/apply_F/solve_E` interfaces.

Then rerun the complete F2.6 pre-spectral algebraic qualification on K0/K1/K2. The new implementation must satisfy the frozen full-support FLR, quasineutrality, positive canonical metric, conservative adjoint/skew, physical-channel Hermiticity, ambipolarity and complete F2.1 balance requirements and must be reproducible directly from committed source/metadata.

If a source-level choice cannot be resolved from frozen physics/structure-preserving/reproducibility criteria alone, return HOLD. If the implementation cannot qualify without changing frozen upstream objects, return FAIL.

## Forbidden until F2.6B returns

Do not inspect eigenvalues, Ritz values, spectral abscissa, growth rates, pseudospectra or eigenvectors. Do not construct propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not change F2.1–F2.5R, the repaired ladder, physical channels, physical point or input geometry. Do not use resolutions outside frozen K0/K1/K2. Do not run GENE, add collisions/damping, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Expected return

One of:

- `F2.6B PASS — SOURCE-LEVEL MATRIX-FREE OPERATOR IMPLEMENTATION FROZEN / ALGEBRA REQUALIFIED — RETURN TO MASTER`;
- `F2.6B HOLD — SPECIFIC SOURCE-LEVEL IMPLEMENTATION DECISION REQUIRED — RETURN TO MASTER`;
- `F2.6B FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

**STOP / AWAIT GO.**
