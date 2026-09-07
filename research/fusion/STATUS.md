# Fusion Branch Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit and F2.1–F2.4 remain protected historical savepoints. Historical F2.5, F2.6 `0_1` HOLD and F2.6 `0_2` FAIL remain immutable audit records.

MASTER integrated F2.5R and F2.6 `0_3`; their repaired discrete algebra remains qualified.

F2.7 has returned HOLD before any eigensolver run because the exact qualified F2.6 `0_3` operator is not canonically available as an executable/serialized numerical artifact.

## Controlling physical / numerical objects

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

All other F2.5 objects remain unchanged.

## Frozen F2.6 `0_3` qualification

Canonical report:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_3.md`

Canonical diagnostics:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_3.json`

F2.6 remains

\[
\boxed{\text{PASS — discrete operator/channel algebra qualified}.}
\]

No F2.6 conclusion is revoked by F2.7.

## F2.7 result

Canonical report:

`research/fusion/fusion_f2_7_numerical_spectral_qualification_gate_0_1.md`

Machine-readable diagnostics:

`research/fusion/fusion_f2_7_numerical_spectral_qualification_diagnostics_0_1.json`

**Status:** `F2.7 HOLD — MARGINAL OR SPECTRALLY INDETERMINATE — RETURN TO MASTER`

The blocker is one reproducibility object:

\[
\boxed{\text{no canonical executable/serialized F2.6 `0_3` realization of }(E_K,F_K).}
\]

The repository contains the `0_3` report and diagnostics, but no versioned operator implementation or serialized factor set sufficient to reproduce the exact qualified matrix-free maps

\[
x\mapsto E_Kx,\qquad
x\mapsto F_Kx,\qquad
x\mapsto E_K^{-1}x
\]

on K0/K1/K2 without making new implementation choices.

Therefore F2.7 did not request any Ritz pair and does not classify the point as stable or unstable.

## MASTER decision required

MASTER must decide whether to issue a narrow reproducibility/serialization repair that publishes and freezes the exact F2.6 `0_3` matrix-free operator implementation (or equivalent serialized factor set) and then re-release F2.7.

Such a repair must reproduce the already-frozen F2.6 `0_3` structural diagnostics and may not alter F2.1–F2.5R.

## Active instruction

**Next instruction:** none in this branch.

A bare `GO` must not resume F2.7, reconstruct a substitute operator, inspect spectra, or start finite-time work until MASTER commits an explicit new handoff.

## Forbidden while HOLD remains

Do not construct a replacement F2-R operator from prose. Do not inspect eigenvalues, growth rates or pseudospectra from a noncanonical implementation. Do not construct propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not change F2.3/F2.4/F2.5R, run GENE, add collisions/damping, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

**STOP / RETURN TO MASTER.**
