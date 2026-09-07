# Fusion Branch Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit and F2.1–F2.4 remain protected historical savepoints. Historical F2.5, F2.6 `0_1` HOLD and F2.6 `0_2` FAIL remain immutable audit records. Historical F2.6 `0_3`, F2.7 `0_1` and F2.6A remain preserved audit/provenance records.

MASTER has integrated F2.6B and frozen its new provenance-clean source-level realization as the canonical executable operator for all downstream F2-R numerical work.

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

The repaired magnetic-moment ladder remains

\[
\boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.}
\]

All other F2.5/F2.5R objects remain unchanged.

## Frozen F2.6B source-level implementation

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

MASTER integration freeze:

`research/master/fusion_f2_6b_source_level_operator_pass_integration_freeze_0_1.md`

Branch commit `83f004412183d43a1653d3a3a2f9ad104482de7d`; Python CI #433 = `SUCCESS`.

F2.6B is explicitly a new source-level realization and does not claim exact source identity with historical F2.6 `0_3`.

The committed public interfaces are

- `build_operator(level)`;
- `apply_E(op,x)`;
- `apply_F(op,x)`;
- `solve_E(op,x)`.

The frozen NumPy C-order state layout is ion `h_i[theta,u,zeta]` followed by trapped-electron `h_e[well,energy,lambda]`, with

\[
\boxed{N_{\rm total}(K0,K1,K2)=(18608,\ 93204,\ 361152).}
\]

The complete pre-spectral algebraic requalification passes. Maximum complete-balance relative residuals are

\[
\boxed{1.29\times10^{-13},\qquad5.64\times10^{-13},\qquad5.87\times10^{-13}.}
\]

No spectrum or finite-time object was inspected.

## Active instruction

**Status:** `FUSION F2.7 0_2 NUMERICAL / SPECTRAL QUALIFICATION ON F2.6B OPERATOR READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_f2_7_rerun_on_f2_6b_source_operator_0_1.md`

On bare `GO`, first read this STATUS and execute only that committed instruction.

## F2.7 0_2 scope

Use the committed F2.6B source-level operator directly and determine the rightmost modal spectral edge / spectral abscissa on K0/K1/K2 with residual certification, an independent eigensolver repetition and frozen-ladder robustness.

All reported spectral quantities must be attributed to the F2.6B implementation, not to the unrecoverable historical F2.6 `0_3` source realization.

A robustly unstable point must be reported without damping or retuning. A marginal or unresolved edge returns HOLD. A new operator inconsistency returns FAIL rather than a silent repair.

## Forbidden until F2.7 0_2 returns

Do not modify the frozen F2.6B operator for spectral convenience. Do not construct propagators, matrix exponentials, Gramians, cumulative objectives, optimizers, angles, gaps or horizon curves. Do not change F2.1–F2.5R, the repaired ladder, physical channels, physical point or input geometry. Do not scan parameters or resolutions outside K0/K1/K2, run GENE, add collisions/damping, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Expected return

One of:

- `F2.7 PASS — SPECTRALLY STABLE / NUMERICALLY QUALIFIED — RETURN TO MASTER`;
- `F2.7 PASS — SPECTRALLY UNSTABLE / NUMERICALLY QUALIFIED — RETURN TO MASTER`;
- `F2.7 HOLD — MARGINAL OR SPECTRALLY INDETERMINATE — RETURN TO MASTER`;
- `F2.7 FAIL — RETURN TO MASTER`.

Create new versioned `0_2` outputs. Do not overwrite F2.7 `0_1`. No branch-side next gate is self-authorized.

**STOP / AWAIT GO.**
