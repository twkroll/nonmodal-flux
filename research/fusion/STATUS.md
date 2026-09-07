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

MASTER has integrated F2.5R and F2.6 `0_3`. The repaired discrete operator/channel algebra is now frozen as qualified, and F2.7 is released solely for numerical/spectral-regime qualification.

## Controlling physical / FLR / numerical objects

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
\boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.}
\]

All other F2.5 numerical objects remain unchanged.

## Frozen F2.6 0_3 algebraic qualification

Canonical report:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_3.md`

MASTER integration freeze:

`research/master/fusion_f2_6_discrete_algebra_pass_integration_freeze_0_1.md`

F2.6 `0_3` branch commit `4db62c37d3465726be061dc7b49cbc3a81d87a55`; Python CI #412 = `SUCCESS`.

The repaired full-support local-B FLR identity, quasineutrality, canonical positive Helmholtz metric, conservative phase-space adjoint/skew structure, independently reconstructed physical particle/ion-heat/trapped-electron-heat channels, ambipolarity and the complete F2.1 discrete free-energy balance all qualify on K0/K1/K2.

Maximum reported complete-balance relative residuals are approximately

\[
1.92\times10^{-14},\qquad3.15\times10^{-13},\qquad1.61\times10^{-13}.
\]

No spectrum or finite-time object was inspected in F2.6.

## Active instruction

**Status:** `FUSION F2.7 NUMERICAL / SPECTRAL QUALIFICATION READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_f2_7_numerical_spectral_qualification_gate_0_1.md`

On bare `GO`, first read this STATUS and execute only that committed instruction.

## F2.7 scope

Use the frozen repaired K0/K1/K2 operators to determine the rightmost modal spectral edge and spectral abscissa with reproducible matrix-free eigensolver methods, residual certification, independent numerical repetition and refinement-robustness checks.

Classify the frozen point as spectrally stable, unstable or marginal/indeterminate. A robustly unstable point must be reported factually and may not be rescued by damping or parameter retuning.

A full dense spectrum is not required at K1/K2. A defensible rightmost-spectrum classification is required.

## Forbidden until F2.7 returns

Do not construct propagators, Gramians, cumulative objectives, finite-time energy/transport operators, optimizers, principal angles, performance gaps or horizon curves. Do not scan physical parameters, wavenumbers, input subspaces or resolutions outside K0/K1/K2. Do not change F2.3/F2.4/F2.5R, run GENE, add collisions/damping, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Expected return

One of:

- `F2.7 PASS — SPECTRALLY STABLE / NUMERICALLY QUALIFIED — RETURN TO MASTER`;
- `F2.7 PASS — SPECTRALLY UNSTABLE / NUMERICALLY QUALIFIED — RETURN TO MASTER`;
- `F2.7 HOLD — MARGINAL OR SPECTRALLY INDETERMINATE — RETURN TO MASTER`;
- `F2.7 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

**STOP / AWAIT GO.**
