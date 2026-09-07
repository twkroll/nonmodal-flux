# Fusion Branch Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit, F2.1, F2.2, F2.3, F2.4 and F2.5 remain complete and MASTER-integrated.

F2.6 `0_1` historically returned `HOLD` on an ion-FLR convention conflict. MASTER resolved that conflict through the local-B ion-FLR erratum and re-released F2.6. The resumed F2.6 `0_2` now returns `FAIL` before any spectral work because the frozen F2.5 ion magnetic-moment quadrature does not resolve the corrected local-B FLR identity over the full K0/K1/K2 retained support.

## Controlling ion-FLR convention

MASTER erratum:

`research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`

The controlling convention is

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

This convention itself is no longer ambiguous.

## F2.6 resumed result

Canonical report:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_2.md`

Machine-readable diagnostics:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_2.json`

Reproducible pre-spectral check:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_0_2.py`

**Status:** `F2.6 FAIL — RETURN TO MASTER`

The representative local-B FLR checks at `theta=0` and `theta=pi` pass after the MASTER erratum. The failure is instead a full-support frozen-ladder error:

| level | `N_mu` | max `|<J0^2>_K-Gamma0|` | max relative error |
|---|---:|---:|---:|
| K0 | 8 | `8.3028e-05` | `3.6977e-04` |
| K1 | 12 | `1.7012e-03` | `1.3010e-02` |
| K2 | 16 | `2.3078e-02` | `3.0470e-01` |

Thus the required FLR manufactured identity is not convergent across the predeclared K0/K1/K2 ladder. At K2 the worst active-node discrepancy is approximately `30.5 %` relative.

The associated positive-Helmholtz versus `g`-form field-block defect also grows across the ladder, so the complete F2.1 discrete balance with the canonical independently constructed positive metric cannot be qualified on all three levels.

Other pre-spectral checks remain localized and satisfactory: quasineutrality residuals are at roundoff, Maxwellian moments converge, bounce quadrature is at roundoff for the fixed analytic tests, physical channel forms are Hermitian to roundoff, particle ambipolarity is at roundoff, and `max(k_perp rho_e)<0.1` remains satisfied.

## Why this is FAIL

The earlier `HOLD` ambiguity has been removed by MASTER. Repairing the remaining defect would require changing the frozen F2.5 ion magnetic-moment resolution/integration strategy or its coupling to the ballooning-window ladder.

F2.6 is explicitly forbidden to retune K0/K1/K2 or silently replace the quadrature. Therefore the frozen discretization cannot satisfy the required physical/algebraic qualification under the committed ladder.

## Active instruction

**Next instruction:** none in this branch.

A bare `GO` must not reopen or repair F2.5/F2.6, inspect spectra, or start finite-time work until MASTER commits an explicit new handoff.

## Forbidden while FAIL remains

Do not inspect eigenvalues, growth rates, pseudospectra, eigenvectors, propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not change F2.3, F2.4 or F2.5, add damping/collisions, run GENE, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

**STOP / RETURN TO MASTER.**
