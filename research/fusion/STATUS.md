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

Canonical executable operator:

`research/fusion/fusion_f2_6b_operator_0_1.py`

F2.6B branch commit `83f004412183d43a1653d3a3a2f9ad104482de7d`; Python CI #433 = `SUCCESS`.

The frozen state dimensions are

\[
\boxed{N_{\rm total}(K0,K1,K2)=(18608,\ 93204,\ 361152).}
\]

## F2.7 `0_2` result

Canonical report:

`research/fusion/fusion_f2_7_numerical_spectral_qualification_gate_0_2.md`

Machine-readable diagnostics:

`research/fusion/fusion_f2_7_numerical_spectral_qualification_diagnostics_0_2.json`

Reproducible spectral driver:

`research/fusion/fusion_f2_7_numerical_spectral_qualification_0_2.py`

**Status:** `F2.7 PASS — SPECTRALLY UNSTABLE / NUMERICALLY QUALIFIED — RETURN TO MASTER`

All spectral quantities belong exclusively to the frozen F2.6B source-level realization. No claim is made about the unrecoverable historical F2.6 `0_3` source realization.

Residual-certified unstable eigenvalues are

\[
\lambda_{K0}=0.0221552877943+0.0463690913769\,i,
\]

\[
\lambda_{K1}=0.00730158359482590+0.0333949532678270\,i,
\]

\[
\lambda_{K2}=0.00621516166872793+0.0273172444169728\,i.
\]

Therefore

\[
\boxed{\alpha_{K0}>0,\qquad\alpha_{K1}>0,\qquad\alpha_{K2}>0.}
\]

The reported eigenvalues are certified positive lower bounds for the spectral abscissa, not claims of globally exact maximizers of `Re(lambda)`. One certified positive eigenvalue suffices to prove the unstable sign classification.

Direct canonical `D`-weighted residuals against the unmodified full F2.6B `apply_A` are

\[
9.16\times10^{-13},\qquad
6.93\times10^{-14},\qquad
5.21\times10^{-14}
\]

for K0/K1/K2.

For K2 the full 40-`zeta` dispersion matrix satisfies

\[
\sigma_{\min}/\sigma_{\max}=2.97\times10^{-16}.
\]

Independent offset-target repetitions converge to the same unstable branch. The K2 repeat is

\[
\lambda_{K2}^{\rm repeat}
=0.006215161668746496+0.027317244416965134\,i,
\]

only approximately `2.01e-14` from the primary K2 eigenvalue.

The unstable sign is robust under the complete frozen K0/K1/K2 refinement ladder.

No damping, collisions, filtering, parameter retuning, wavenumber scan, alternative resolution, propagator, matrix exponential, Gramian, cumulative transport objective, finite-time optimizer, angle, gap or horizon curve was constructed.

## Active instruction

**Next instruction:** none in this branch.

A bare `GO` must not open finite-time work or any later Fusion gate until MASTER integrates F2.7 `0_2` and commits an explicit new handoff.

## Forbidden while RETURN TO MASTER remains

Do not construct propagators, matrix exponentials, Gramians, cumulative objectives, optimizers, principal angles, performance gaps or horizon curves. Do not retune the F2.3 point, change the F2.4 input geometry, modify F2.1–F2.5R or the frozen F2.6B operator, scan parameters/resolutions, add collisions/damping/filters, run GENE, or reopen R1, MODES, CONT, CASCADE, Power Grid, Photonics or Paper-1 work.

**STOP / RETURN TO MASTER.**
