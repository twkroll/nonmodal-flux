# Fusion F2.5R — Ion-FLR Magnetic-Moment Quadrature Repair / Discretization Requalification Gate 0.1

**Date:** 2026-09-07  
**Authority:** MASTER  
**Execution branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

## Objective

Repair only the ion magnetic-moment quadrature order that caused the pre-spectral F2.6 `0_2` failure, while preserving every other frozen physical and numerical choice.

This is a **pre-spectral, pre-effect numerical-structure gate**. Its output is a revised, versioned K0/K1/K2 `N_mu` ladder and its structural qualification. It must not construct or inspect any generator spectrum or finite-time quantity.

## Mandatory controlling inputs

Read and preserve:

- `research/master/fusion_f2_6_discrete_algebra_failure_integration_freeze_0_1.md`;
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_2.md`;
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_2.json`;
- `research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`;
- `research/master/fusion_f2_5_discretization_specification_integration_freeze_0_1.md`;
- `research/fusion/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`;
- F2.1–F2.4 integration freezes;
- the shared MASTER Prompt Handoff Protocol.

## Objects that remain frozen

Do **not** change:

- F2.1 reduced physics or physical transport-channel definitions;
- F2.2 geometry, ballooning conventions or local gyroaverage;
- F2.3 physical parameters, including `k_y rho_i0=0.3`;
- F2.4 admissible input space or input cost;
- the local-B ion-FLR erratum;
- K0/K1/K2 ballooning windows, theta elements, LGL polynomial degrees or compact-support boundary treatment;
- ion Hermite orders;
- trapped-electron energy/pitch/well representation;
- bounce quadrature;
- algebraic quasineutrality elimination;
- absence of damping, filtering, hypercollision, loading, clipping or physical-direction deletion.

The only released numerical object is the **ion Gauss--Laguerre magnetic-moment order `N_mu` on K0/K1/K2**.

The representation family itself remains Gauss--Laguerre in

\[
\zeta=\mu_iB_0/T_i\in[0,\infty).
\]

Do not switch to a different basis/integration family in this gate. If Gauss--Laguerre cannot satisfy the criteria below at computationally defensible orders, return `HOLD` to MASTER rather than silently changing representation family.

## Controlling FLR identity

Use throughout

\[
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right),
\qquad
b_i(\theta)=(k_\perp(\theta)\rho_{i0})^2\left(\frac{B_0}{B(\theta)}\right)^2,
\]

\[
\Gamma_{0i}(\theta)=I_0(b_i)e^{-b_i}.
\]

For every frozen K-level, the repaired magnetic-moment quadrature must resolve the Maxwellian manufactured identity

\[
\langle J_{0i}^2\rangle_K=\Gamma_{0i}(b_i)
\]

uniformly over the entire retained ballooning support.

## Authorized numerical search

A search over candidate **quadrature orders only** is explicitly authorized because the failed object is numerical resolution and no spectrum/effect has been inspected.

Use a deterministic monotone candidate sequence, document it before evaluating the candidates, and choose the **smallest** order at each K-level that satisfies the predeclared structural tolerances. The resulting repaired ladder must be monotone,

\[
N_{\mu,K0}\le N_{\mu,K1}\le N_{\mu,K2}.
\]

Do not optimize for runtime, spectral behavior, transport amplitude, nonnormality or objective separation.

## Required qualification criteria

At each K0/K1/K2 level, using the unchanged ballooning window and active LGL nodes, require all of the following:

1. maximum absolute full-support FLR identity error
   \[
   \max_\theta|\langle J_0^2\rangle_K-\Gamma_0|\le10^{-10};
   \]
2. maximum relative full-support error wherever `Gamma0>=1e-6`
   \[
   \max_\theta\frac{|\langle J_0^2\rangle_K-\Gamma_0|}{\Gamma_0}\le10^{-8};
   \]
3. normalized positive-Helmholtz versus `g`-form ion field-block defect no larger than `1e-10` in both the weighted Frobenius diagnostic and maximum local diagnostic;
4. the representative `theta=0` and `theta=pi` checks remain consistent with the same tolerance target;
5. standard Maxwellian density/energy/heat-weight moment reproduction does not degrade relative to the original F2.5/F2.6 checks;
6. positive Gauss--Laguerre weights and the physical phase-space measure remain intact.

In addition, perform a deterministic geometry-only envelope check between LGL nodes on each frozen theta interval to demonstrate that the selected order is not accidentally fitted only to the active nodal set. This check may use the analytic local-B geometry and manufactured FLR identity only; it may not use `A_K` or physical transport effects.

## Required output

Create:

- `research/fusion/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`;
- `research/fusion/fusion_f2_5r_ion_flr_quadrature_repair_diagnostics_0_1.json`;
- if a reproducible script is needed, `research/fusion/fusion_f2_5r_ion_flr_quadrature_repair_0_1.py`.

Update `research/fusion/STATUS.md` in the same work package.

The result must freeze the repaired K0/K1/K2 `N_mu` values if successful and record the resulting total ion-state dimensions.

## Pass / hold / fail logic

Return exactly one of:

- `F2.5R PASS — ION-FLR MAGNETIC-MOMENT QUADRATURE REPAIRED / LADDER FROZEN — RETURN TO MASTER`;
- `F2.5R HOLD — GAUSS-LAGUERRE REPAIR NOT COMPUTATIONALLY/STRUCTURALLY DEFENSIBLE — RETURN TO MASTER`;
- `F2.5R FAIL — RETURN TO MASTER`.

`PASS` requires all three frozen K-levels to satisfy the predeclared criteria with one explicit monotone order ladder.

`HOLD` is appropriate if the required order becomes so large that the unchanged tensor-product architecture is no longer computationally credible, or if Gauss--Laguerre cannot satisfy the envelope criteria cleanly. Identify the exact obstacle; do not switch representation family.

`FAIL` is appropriate if the released quadrature-order repair cannot restore the required source-consistent manufactured structure without violating another frozen constraint.

## Forbidden work

Do **not** calculate or inspect:

- `A_K` eigenvalues/eigenvectors, growth rates, spectral abscissa or pseudospectra;
- matrix exponentials, propagators, Gramians or cumulative channel operators;
- finite-time free-energy or transport objectives;
- optimizers, principal angles, performance gaps or horizon dependence;
- physical parameter, wavenumber, input-subspace or ballooning-window scans;
- resolutions outside the existing K0/K1/K2 geometry ladder except the explicitly authorized `N_mu` candidate-order search;
- GENE or another external GK run.

Do not alter any upstream physical freeze, add collisions/damping/filtering, or open MODES/CONT/CASCADE/protected branches.

No branch-side next gate is self-authorized after the result. If F2.5R passes, MASTER must integrate the repaired ladder and explicitly re-release F2.6 as a new versioned algebraic qualification.

**STOP / RETURN TO MASTER AFTER F2.5R.**
