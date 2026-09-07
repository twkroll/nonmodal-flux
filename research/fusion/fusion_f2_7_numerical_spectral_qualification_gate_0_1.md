# Fusion F2.7 — Numerical / Spectral Qualification Gate 0.1

**Date:** 2026-09-07  
**Authority:** MASTER / `research/master/prompts/fusion_f2_7_numerical_spectral_qualification_gate_0_1.md`  
**Status:** `F2.7 HOLD — MARGINAL OR SPECTRALLY INDETERMINATE — RETURN TO MASTER`

## Executive verdict

F2.7 cannot defensibly classify the rightmost spectrum of the frozen repaired F2-R operator from the current canonical repository state.

The blocker is one specific reproducibility object:

\[
\boxed{\text{the executable/serialized F2.6 `0_3` matrix-free realization }(E_K,F_K)\text{ is not present canonically}.}
\]

F2.6 `0_3` freezes and qualifies

\[
E_K\dot x_K=F_Kx_K,\qquad A_K=E_K^{-1}F_K,
\]

and documents the low-rank quasineutrality/metric factorization, but the repository contains no versioned `0_3` implementation or serialized factor set from which the exact K0/K1/K2 maps

\[
x\mapsto E_Kx,\qquad x\mapsto F_Kx
\]

can be reproduced without making additional implementation choices.

Re-deriving weak/SBP streaming–mirror matrices, bounce projectors, quasineutrality couplings or field-drive maps from prose would create a new implementation. F2.7 explicitly requires the already-qualified operator and forbids replacing it by a differently implemented one.

Therefore no Ritz pair was requested and no stability sign is inferred from benchmark expectations or from the free-energy balance.

\[
\boxed{\text{F2.7 HOLD — MARGINAL OR SPECTRALLY INDETERMINATE — RETURN TO MASTER}.}
\]

## Frozen lineage preserved

No upstream object was changed. The F2.1–F2.4 physics/input geometry, local-`B` ion-FLR convention, and F2.5R repaired ladder

\[
N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40
\]

remain frozen. The repaired dimensions remain

\[
N_i=(18176,91584,357120),\qquad N_e=(432,1620,4032).
\]

## Canonical inputs actually available

The repository contains:

- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_3.md`;
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_3.json`;
- the historical `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_0_2.py`;
- the F2.5R quadrature-repair script.

It does **not** contain a versioned F2.6 `0_3` executable operator implementation or serialized arrays/factors sufficient to instantiate the exact qualified `E_K` and `F_K` applications.

The F2.6 `0_3` report gives the structural factorization

\[
C_K\phi_K=S_Kx_K,\qquad P_K=C_K^{-1}S_K,
\]

\[
R_K=D_K^{-1}S_K^\dagger,\qquad E_K=I-R_KC_K^{-1}S_K,
\]

with

\[
E_K^{-1}y=y+R_K(C_K-S_KR_K)^{-1}S_Ky,
\]

but does not serialize every numerical object needed by a reproducible eigensolver, notably the concrete weak/SBP ion streaming–mirror action and full orbit-projected trapped-electron coupling maps.

## Why no approximate spectral answer is reported

The F2.7 handoff requires rightmost Ritz values, eigen-residuals, independent solver repetition, K0/K1/K2 refinement robustness and conditioning information for the actual generalized/matrix-free solve. None of these can be certified for the **qualified** operator without its canonical executable realization.

A physical expectation that a Cyclone-Base-Case-like point is unstable is not a substitute for the requested spectrum. Likewise, the exact F2.6 free-energy balance does not determine the sign of the spectral abscissa.

## Exact MASTER action required

MASTER should release one narrow reproducibility repair:

\[
\boxed{\text{publish/freeze the exact F2.6 `0_3` matrix-free operator implementation or equivalent serialized factor set}.}
\]

A sufficient artifact must deterministically provide

\[
E_Kx,\qquad F_Kx,\qquad E_K^{-1}x
\]

for K0/K1/K2 and reproduce the already-frozen F2.6 `0_3` structural diagnostics before F2.7 is rerun. This is a serialization/reproducibility repair only; it need not reopen F2.1–F2.5R.

## Forbidden-work audit

F2.7 performed no eigenvalue/eigenvector calculation, spectral-abscissa estimate, pseudospectrum, propagator, Gramian, cumulative objective, finite-time optimization, parameter scan, GENE run, damping/filtering or replacement-operator construction.

## Verdict

The spectral regime remains indeterminate because the exact already-qualified discrete operator is not reproducibly instantiated by a canonical executable/serialized artifact.

\[
\boxed{\text{F2.7 HOLD — MARGINAL OR SPECTRALLY INDETERMINATE — RETURN TO MASTER}.}
\]

**STOP / RETURN TO MASTER.**
