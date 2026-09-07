# Fusion Branch Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit and F2.1–F2.5 remain historical frozen savepoints. F2.6 `0_1` returned HOLD on the ion-FLR convention conflict; MASTER resolved that conflict with the local-B erratum. The resumed F2.6 `0_2` returned FAIL before any spectral work because the historical F2.5 ion magnetic-moment quadrature does not resolve the corrected local-B FLR identity over the full retained support.

MASTER has integrated that failure and released one narrowly scoped repair gate, F2.5R.

## Controlling physical / FLR objects

The F2-R physical model, F2.3 point and F2.4 input geometry remain frozen. The controlling ion-FLR convention remains

\[
\rho_{i0}=v_{Ti}/\Omega_i(B_0),
\qquad
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right),
\]

\[
\boxed{
b_i(\theta)=(k_\perp(\theta)\rho_{i0})^2\left(\frac{B_0}{B(\theta)}\right)^2,
\qquad
\Gamma_{0i}=I_0(b_i)e^{-b_i}.
}
\]

No physical parameter or input-space change is authorized.

## Historical F2.6 `0_2` failure

Canonical result:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_2.md`

Diagnostics:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_2.json`

Reproducible check:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_0_2.py`

Branch verdict:

\[
\boxed{\text{F2.6 FAIL — RETURN TO MASTER}.}
\]

Branch commit `78db3e41c2cce29d505f13401f6f0878cb40f854`; Python CI #398 = `SUCCESS`.

The representative local-B FLR checks at `theta=0` and `theta=pi` pass. The remaining defect is full-support magnetic-moment resolution: the historical `N_mu=8/12/16` ladder yields maximum relative `Gamma0i=<J0i^2>` errors approximately `3.70e-4 / 1.30e-2 / 3.05e-1` on K0/K1/K2, with a growing positive-Helmholtz versus `g`-form field-block defect. Thus the canonical complete F2.1 discrete balance cannot be certified on all historical levels.

Other pre-spectral checks remain satisfactory and no spectrum or finite-time quantity was inspected.

MASTER integration freeze:

`research/master/fusion_f2_6_discrete_algebra_failure_integration_freeze_0_1.md`

## Active instruction

**Status:** `FUSION F2.5R ION-FLR MAGNETIC-MOMENT QUADRATURE REPAIR READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`

On bare `GO`, first read this STATUS and execute only that committed instruction.

## F2.5R scope

Only the ion Gauss--Laguerre magnetic-moment order `N_mu` is reopened. The Gauss--Laguerre representation family remains fixed. All other F2.5 numerical objects and all upstream physical freezes remain unchanged.

F2.5R may search deterministic candidate `N_mu` orders solely against predeclared manufactured local-B FLR and positive-metric structural tolerances, choose the smallest monotone K0/K1/K2 ladder that passes, and freeze it. It may not inspect `A_K` spectra, transport effects or finite-time objectives.

If Gauss--Laguerre cannot meet the structural criteria at a computationally defensible order, return `HOLD` to MASTER rather than changing representation family.

## Forbidden until F2.5R returns

Do not rerun F2.6 directly. Do not inspect eigenvalues, growth rates, pseudospectra, eigenvectors, propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not change F2.3/F2.4, ballooning windows/basis, ion Hermite representation, trapped-electron representation, bounce quadrature or quasineutrality treatment. Do not run GENE, add collisions/damping, reopen R1 or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Governance authority

- `research/master/fusion_f2_6_discrete_algebra_failure_integration_freeze_0_1.md`
- `research/master/prompts/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`
- `research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / AWAIT GO.**
