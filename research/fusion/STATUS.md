# Fusion Branch Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit and F2.1–F2.4 remain protected historical savepoints. Historical F2.5, F2.6 `0_1` HOLD and F2.6 `0_2` FAIL remain immutable audit records. F2.5R and historical F2.6 `0_3` remain MASTER-integrated qualified savepoints.

F2.7 `0_1` remains a historical HOLD / spectrally indeterminate result because the historical F2.6 `0_3` source realization was not canonically executable. F2.6A remains a historical HOLD because exact source-level identity to that historical realization cannot be proven.

MASTER then authorized F2.6B to create a new provenance-clean source-level realization of the unchanged frozen F2-R numerical model and re-run the complete pre-spectral algebraic qualification. F2.6B has now completed PASS.

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

## F2.6B result

Canonical report:

`research/fusion/fusion_f2_6b_source_level_operator_implementation_requalification_gate_0_1.md`

Canonical executable operator:

`research/fusion/fusion_f2_6b_operator_0_1.py`

Canonical requalification driver:

`research/fusion/fusion_f2_6b_requalification_0_1.py`

Machine-readable diagnostics:

`research/fusion/fusion_f2_6b_requalification_diagnostics_0_1.json`

Focused regression test:

`tests/test_fusion_f2_6b_operator_0_1.py`

**Status:** `F2.6B PASS — SOURCE-LEVEL MATRIX-FREE OPERATOR IMPLEMENTATION FROZEN / ALGEBRA REQUALIFIED — RETURN TO MASTER`

This F2.6B realization is explicitly new and does not claim source identity with historical F2.6 `0_3`.

The committed public generalized-operator interfaces are

- `build_operator(level)`;
- `apply_E(op,x)`;
- `apply_F(op,x)`;
- `solve_E(op,x)`.

The frozen state layout is ion `h_i[theta,u,zeta]` followed by trapped-electron `h_e[well,energy,lambda]`, NumPy C-order.

The resulting dimensions are

\[
N_{\rm total}(K0,K1,K2)=(18608,\ 93204,\ 361152).
\]

The complete K0/K1/K2 requalification passes:

- repaired full-support local-`B` FLR identity;
- positive Maxwellian/orbit weights and moment checks;
- quasineutrality and exact Woodbury/Schur `solve_E`;
- canonical positive Helmholtz metric \(M_K=M_K^\dagger\succ0\);
- \(B_K=I,\ R_{{\rm in},K}=M_K\);
- ion streaming/mirror and full conservative phase-space skew structure;
- independently constructed particle/ion-heat/trapped-electron-heat channel Hermiticity;
- hydrogenic particle ambipolarity;
- complete F2.1 discrete free-energy balance.

Maximum complete-balance relative residuals are

\[
1.29\times10^{-13},\qquad
5.64\times10^{-13},\qquad
5.87\times10^{-13}
\]

for K0/K1/K2.

A fixed manufactured state gives

\[
2W_K=8.5835647932,\quad8.5972174967,\quad8.6039815033,
\]

with decreasing successive relative changes.

No spectral or finite-time object was inspected.

## Active instruction

**Next instruction:** none in this branch.

A bare `GO` must not start F2.7, inspect spectra or open finite-time work until MASTER integrates F2.6B and commits an explicit new handoff.

## Forbidden while RETURN TO MASTER remains

Do not compute eigenvalues, Ritz values, spectral abscissa, growth rates, pseudospectra or eigenvectors. Do not construct propagators, Gramians, cumulative objectives, optimizers, angles, gaps or horizon curves. Do not change F2.1–F2.5R, the repaired ladder, physical channels, physical point or input geometry. Do not run GENE, add collisions/damping, reopen R1 or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

**STOP / RETURN TO MASTER.**
