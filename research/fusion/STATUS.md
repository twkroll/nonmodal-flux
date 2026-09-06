# Fusion Branch Status

**Last updated:** 2026-09-06  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit, F2.1, F2.2, F2.3, F2.4 and F2.5 are complete and MASTER-integrated.

F2.6 has returned `HOLD` before any spectral work.

## Frozen upstream lineage

The primary reduced F2-R candidate remains

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons, the frozen circular `s-alpha` ballooning geometry, the frozen F2.3 CBC-compatible point, and

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}}.
\]

The F2.5 K0/K1/K2 discretization ladder remains frozen and may not be retuned.

## F2.6 result

Canonical report:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_1.md`

Machine-readable diagnostics:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_1.json`

**Status:** `F2.6 HOLD — SPECIFIC DISCRETE ALGEBRA/IMPLEMENTATION DECISION REQUIRED — RETURN TO MASTER`

The blocker is a single ion-FLR convention conflict:

- F2.2/F2.5 evaluate
  \[
  J_{0i}=J_0(k_\perp v_\perp/\Omega_i(\theta))
  \]
  with local `B(theta)`;
- F2.3/F2.5 simultaneously use the reference gyroradius
  \[
  \rho_{i0}=v_{Ti}/\Omega_i(B_0)
  \]
  in
  \[
  b_i^{\rm frozen}=(k_\perp\rho_{i0})^2,
  \qquad
  \Gamma_{0i}=I_0(b_i)e^{-b_i}.
  \]

For the local `J0i`, the source-consistent Maxwellian identity instead requires

\[
\boxed{
b_i^{\rm local}(\theta)
=
(k_\perp\rho_{i0})^2
\left(\frac{B_0}{B(\theta)}\right)^2.
}
\]

The discrepancy is not numerical: at `theta=0`, `<J0^2>=0.8856850888548` while frozen `Gamma0=0.9157828330545`; at `theta=pi`, `<J0^2>=0.6741214459595` while frozen `Gamma0=0.5752843264774`. K1/K2 reproduce the local-B Maxwellian values to machine precision.

## MASTER decision required

MASTER must explicitly clarify/erratum the ion polarization convention before F2.6 can resume.

Preferred source-consistent option:

\[
b_i(\theta)=(k_\perp\rho_{i0})^2(B_0/B(\theta))^2
\]

while retaining the already frozen local `J0i`.

Alternative: retain reference-`B0` `b_i` but revise `J0i` to use `Omega_i(B0)`. F2.6 is not authorized to choose between these by itself.

## Active instruction

**Next instruction:** none in this branch.

A bare `GO` must not resume F2.6 or open spectral/numerical qualification until MASTER commits an explicit FLR convention resolution and a new handoff.

## Forbidden while HOLD remains

Do not inspect eigenvalues, growth rates, pseudospectra, eigenvectors, propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not change K0/K1/K2, F2.3, F2.4 or any other frozen branch object. Do not run GENE or add damping/collisions.

**STOP / RETURN TO MASTER.**
