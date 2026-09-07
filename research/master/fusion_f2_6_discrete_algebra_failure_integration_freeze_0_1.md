# Fusion F2.6 Discrete-Algebra Failure Integration Freeze 0.1

**Date:** 2026-09-07  
**Authority:** MASTER  
**Status:** `STABLE — F2.6 FAIL INTEGRATED / F2.5R ION-FLR QUADRATURE REPAIR RELEASED`

## Scope

This MASTER freeze integrates only the resumed

`Fusion F2.6 — Discrete Generator / Helmholtz Metric / Physical Channel Reconstruction & Algebraic Balance Qualification Gate 0.2`.

It performs no spectrum, eigenvalue, propagator, Gramian, finite-time objective, optimizer, parameter scan or GENE calculation.

Canonical branch result:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_2.md`

Machine-readable diagnostics:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_2.json`

Reproducible pre-spectral diagnostic:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_0_2.py`

Branch verdict:

\[
\boxed{\text{F2.6 FAIL — RETURN TO MASTER}.}
\]

Branch commit:

`78db3e41c2cce29d505f13401f6f0878cb40f854`

Python CI #398 = `SUCCESS`.

## Integrated factual result

The MASTER ion-FLR erratum remains correct and controlling:

\[
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right),
\qquad
b_i(\theta)=(k_\perp\rho_{i0})^2\left(\frac{B_0}{B(\theta)}\right)^2,
\qquad
\Gamma_{0i}=I_0(b_i)e^{-b_i}.
\]

Representative checks at `theta=0` and `theta=pi` now pass, so the historical F2.6 `0_1` convention ambiguity is resolved.

The resumed gate instead exposes a genuine numerical qualification failure of the frozen F2.5 ion magnetic-moment quadrature on the expanding K0/K1/K2 ballooning windows. With the frozen

\[
N_\mu=8,12,16,
\]

the full-support manufactured identity

\[
\langle J_{0i}^2\rangle_K=\Gamma_{0i}(b_i)
\]

has maximum relative errors approximately

\[
3.70\times10^{-4},\qquad 1.30\times10^{-2},\qquad 3.05\times10^{-1}
\]

on K0/K1/K2 respectively. The error worsens rather than converges. The corresponding positive-Helmholtz versus `g`-form field-block defect also grows across the ladder.

Therefore the complete F2.1 discrete balance cannot be certified with the canonical independently constructed positive Helmholtz metric on all three frozen levels.

## Interpretation boundary

This is a **discretization / FLR-resolution failure**, not a failure of the F2-R continuous physical model, the local-B ion-FLR convention, the F2.3 benchmark point or the F2.4 input geometry.

Other regenerated pre-spectral checks remain satisfactory: quasineutrality residuals, basic Maxwellian moments, bounce quadrature, channel Hermiticity, hydrogenic particle ambipolarity and the reduced-electron ordering.

No spectral or finite-time quantity has been inspected. Consequently a narrowly versioned numerical repair remains scientifically admissible without effect-selection bias, provided it is qualified solely against predeclared algebraic/manufactured criteria before F2.6 is rerun.

## MASTER repair decision

MASTER reopens **only** the ion magnetic-moment quadrature order inside the F2.5 numerical specification. The numerical representation family remains Gauss--Laguerre in the ion magnetic-moment coordinate; the ballooning basis/window, ion Hermite representation, trapped-electron representation, bounce quadrature, quasineutrality treatment, physical parameters, input geometry and all physical channel definitions remain frozen.

The repair gate is

\[
\boxed{\text{F2.5R — Ion-FLR Magnetic-Moment Quadrature Repair / Discretization Requalification Gate 0.1}.}
\]

Its purpose is to choose a new monotone K0/K1/K2 `N_mu` ladder using **only** the analytic local-B FLR manufactured identity and related positive-metric field-block diagnostics. No `A_K` spectrum or finite-time quantity may be inspected.

The repaired ladder must be frozen before F2.6 is rerun again. F2.6 itself may not be resumed directly from the current FAIL state.

Canonical handoff:

`research/master/prompts/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`

## Rollback / STOP

This integration freeze is a new protected post-paper savepoint. Historical F2.5, F2.6 `0_1`, the ion-FLR erratum and F2.6 `0_2` remain immutable audit records.

Do not inspect spectra, propagators or finite-time effects; do not retune F2.3/F2.4; do not alter any F2.5 object other than the explicitly released ion magnetic-moment quadrature order; do not open MODES/CONT/CASCADE or protected branches.

**STOP — F2.6 FAIL INTEGRATED; F2.5R MAY PROCEED ONLY THROUGH THE COMMITTED HANDOFF.**
