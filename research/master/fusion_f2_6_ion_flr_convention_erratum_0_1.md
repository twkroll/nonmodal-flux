# Fusion F2.6 Ion-FLR Convention Clarification / Erratum 0.1

**Date:** 2026-09-06  
**Authority:** MASTER  
**Status:** `STABLE — LOCAL-B ION-FLR CONVENTION SELECTED / F2.6 RESUMPTION RELEASED`

## Scope

This MASTER erratum resolves the single ion-FLR convention conflict reported by

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_1.md`.

It changes no physical benchmark parameter, no admissible input geometry, no K0/K1/K2 resolution, no state-space basis, no quadrature order, no transport-channel definition and no spectral or finite-time quantity. The historical F2.6 HOLD report remains canonical as the diagnostic record that exposed the inconsistency.

## MASTER decision

MASTER selects the source-consistent **local-B ion-FLR convention**.

The reference normalization remains

\[
\rho_{i0}=\frac{v_{Ti}}{\Omega_i(B_0)},
\qquad
v_{Ti}=\sqrt{T_i/m_i},
\]

and the frozen F2.3 benchmark label remains

\[
\boxed{k_y\rho_{i0}=0.3}.
\]

The local cyclotron frequency remains

\[
\Omega_i(\theta)=\frac{eB(\theta)}{m_i},
\]

so the already-frozen gyroaverage remains

\[
\boxed{
J_{0i}(\theta,v_\perp)
=J_0\!\left(\frac{k_\perp(\theta)v_\perp}{\Omega_i(\theta)}\right).
}
\]

Define the local thermal gyroradius

\[
\rho_i(\theta)
=\frac{v_{Ti}}{\Omega_i(\theta)}
=\rho_{i0}\frac{B_0}{B(\theta)}.
\]

The ion polarization/free-energy argument is therefore frozen from this erratum onward as

\[
\boxed{
 b_i(\theta)
 =k_\perp^2(\theta)\rho_i^2(\theta)
 =(k_\perp(\theta)\rho_{i0})^2
 \left(\frac{B_0}{B(\theta)}\right)^2.
}
\]

and

\[
\boxed{
\Gamma_{0i}(\theta)=I_0(b_i(\theta))e^{-b_i(\theta)}.
}
\]

## Exact supersession rule

Where any earlier F2.1/F2.3/F2.5 downstream implementation statement in the varying-`B` toroidal geometry was read as

\[
b_i(\theta)=(k_\perp(\theta)\rho_{i0})^2
\]

with the reference gyroradius held fixed while `J0i` used local `Omega_i(theta)`, that implementation reading is superseded by the boxed local-B definition above.

This is a convention clarification/erratum, not a retuning of `k_y rho_i0`, geometry, gradients or any other F2.3 parameter. Historical frozen files are not overwritten; this file is the controlling clarification for all subsequent F2-R numerical work.

No change is made to the reduced-electron ordering:

\[
J_{0e}=1,
\qquad
\Gamma_{0e}=1.
\]

## Rationale

F2.6 demonstrated on the frozen K0/K1/K2 quadratures that the local gyroaverage satisfies the Maxwellian identity

\[
\left\langle
J_0^2\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right)
\right\rangle_{F_{i0}}
=
I_0(b_i^{\rm local})e^{-b_i^{\rm local}}
\]

with

\[
b_i^{\rm local}=(k_\perp\rho_{i0})^2(B_0/B)^2,
\]

while the reference-`B0` polarization argument produced percent-level to order-10-percent discrepancies at representative ballooning locations that did not decrease from K0 to K2. The discrepancy was therefore a convention inconsistency, not a quadrature or convergence error.

Selecting the local-B polarization argument preserves the already-frozen local physical gyroaverage and restores the standard identity

\[
\boxed{\Gamma_{0i}=\langle J_{0i}^2\rangle_{F_{i0}}}
\]

needed for equivalence of the gyrokinetic `g`-form and the positive `delta F + polarization` Helmholtz representation used by F2.1/F2.4/F2.5.

The alternative of redefining `J0i` with `Omega_i(B0)` is rejected because it would replace the already-frozen local gyroaverage rather than correcting the inconsistent derived polarization argument.

## Consequences for F2.6

F2.6 may now resume only as a pre-spectral algebraic qualification on the unchanged K0/K1/K2 ladder. It must reconstruct all FLR-dependent quasineutrality, Helmholtz and generator/channel objects using the local-B `b_i(theta)` above and re-run the required algebraic checks.

The prior `0_1` F2.6 report and diagnostics remain historical HOLD records. The resumed branch must create versioned `0_2` result/diagnostic files rather than overwriting them.

No eigenvalues, growth rates, pseudospectra, propagators, Gramians, cumulative objectives, optimizers, angles, gaps, parameter scans or GENE runs are authorized by this erratum.

## Canonical resumption handoff

`research/master/prompts/fusion_f2_6_resume_after_ion_flr_erratum_0_1.md`

**STOP — ION-FLR CONVENTION RESOLVED; F2.6 MAY RESUME ONLY THROUGH THE COMMITTED HANDOFF.**
