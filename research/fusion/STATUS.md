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

MASTER integrated F2.5R, freezing the repaired ion magnetic-moment quadrature ladder, and released F2.6 `0_3`. The rerun now passes the complete pre-spectral discrete operator/channel algebraic qualification.

## Controlling physical / FLR objects

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

The controlling repaired magnetic-moment ladder is

\[
\boxed{
N_{\mu,K0}=16,\qquad
N_{\mu,K1}=24,\qquad
N_{\mu,K2}=40.
}
\]

All other F2.5 numerical objects remain unchanged.

## F2.6 `0_3` result

Canonical report:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_3.md`

Machine-readable diagnostics:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_3.json`

**Status:** `F2.6 PASS — DISCRETE OPERATOR/CHANNEL ALGEBRA QUALIFIED — RETURN TO MASTER`

The repaired full-support local-B FLR identity passes on active LGL nodes and on the independent between-node geometry envelope. Quasineutrality residuals are at roundoff. The canonical positive Helmholtz metric is Hermitian and strictly positive without loading or clipping, with

\[
B_K=I,\qquad R_{{\rm in},K}=M_K.
\]

The ion streaming/mirror and full conservative phase-space operators satisfy the required discrete adjoint/skew structure to approximately `1e-14` or better. The physical particle and species-heat channels are independently reconstructed from the radial gyrocentre flux integrals, are Hermitian to roundoff, and hydrogenic particle ambipolarity is satisfied to roundoff.

The complete F2.1 discrete balance is qualified on K0/K1/K2. Maximum reported relative residuals over deterministic probes are approximately

\[
1.92\times10^{-14},\qquad
3.15\times10^{-13},\qquad
1.61\times10^{-13}.
\]

No eigenvalue, eigenvector, growth rate, pseudospectrum, propagator, Gramian, finite-time objective, optimizer, angle, performance gap, physical parameter scan or GENE result was inspected.

## Active instruction

**Next instruction:** none in this branch.

A bare `GO` must not open spectral qualification, finite-time propagation, objective comparison or any new repair until MASTER integrates F2.6 `0_3` and commits an explicit new handoff.

## Forbidden while RETURN TO MASTER remains

Do not inspect eigenvalues, growth rates, pseudospectra, eigenvectors, propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not change F2.3/F2.4, the repaired F2.5R ladder or any other F2.5 object. Do not run GENE, add collisions/damping, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

**STOP / RETURN TO MASTER.**
