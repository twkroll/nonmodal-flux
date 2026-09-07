# Fusion F2.6 — Rerun Discrete Operator / Channel Algebraic Qualification after F2.5R Repair 0.1

**Date:** 2026-09-07  
**Authority:** MASTER  
**Execution branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

## Objective

Rerun the F2.6 pre-spectral discrete operator/channel algebraic qualification using the MASTER-integrated F2.5R repaired ion magnetic-moment quadrature ladder.

This remains a **pre-spectral, pre-effect** gate.

## Mandatory controlling inputs

Read and preserve:

- `research/master/fusion_f2_5r_quadrature_repair_integration_freeze_0_1.md`;
- `research/fusion/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`;
- `research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`;
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_2.md` as historical FAIL record;
- `research/master/fusion_f2_6_discrete_algebra_failure_integration_freeze_0_1.md`;
- F2.1–F2.4 integration freezes and the unchanged portions of F2.5;
- the shared MASTER Prompt Handoff Protocol.

Historical F2.6 `0_1` and `0_2` files remain immutable audit records.

## Controlling numerical ladder

Use the unchanged K0/K1/K2 geometry/basis architecture with only the F2.5R ion magnetic-moment order supersession:

\[
\boxed{
N_{\mu,K0}=16,\qquad
N_{\mu,K1}=24,\qquad
N_{\mu,K2}=40.
}
\]

All other F2.5 orders, windows, quadratures and boundary treatments remain unchanged.

The controlling local-B ion-FLR convention remains

\[
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right),
\]

\[
\boxed{
b_i(\theta)=(k_\perp(\theta)\rho_{i0})^2\left(\frac{B_0}{B(\theta)}\right)^2,
\qquad
\Gamma_{0i}=I_0(b_i)e^{-b_i}.}
\]

Do not change any F2.3 physical parameter or F2.4 input geometry.

## Required work

On K0/K1/K2:

1. reconstruct all FLR-dependent quasineutrality, Helmholtz, generator and channel ingredients using the repaired `N_mu` ladder;
2. independently re-verify the active-node and between-node manufactured local-B FLR identity at the repaired orders;
3. construct canonical `M_K` directly from the positive F2 Helmholtz functional after field elimination and verify Hermiticity and strict positive definiteness without loading, clipping or nullspace deletion;
4. construct `A_K` directly from the frozen F2-R equations and unchanged weak/SBP discretization;
5. independently reconstruct `Q_Gamma,K`, `Q_qi,K`, `Q_qe,K` from the physical radial gyrocentre flux integrals using the same state space and quadratures;
6. verify quasineutrality residuals, `B_K=I`, `R_in,K=M_K`, physical-channel Hermiticity, particle ambipolarity, conservative phase-space adjoint/skew structure and the complete F2.1 discrete free-energy balance;
7. report K0/K1/K2 structural/convergence diagnostics and confirm that the F2.5R repair removes the specific field-block discrepancy diagnosed in F2.6 `0_2`.

The physical channels must remain logically independent of the balance identity. Do not define any `Q` backwards from `A_K^dagger M_K+M_K A_K`.

## Required outputs

Create new versioned files:

- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_3.md`;
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_3.json`;
- if a reproducible script is used, version it as `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_0_3.py`.

Update `research/fusion/STATUS.md` in the same work package.

Do not overwrite `0_1` or `0_2` files.

## Pass / hold / fail logic

Return exactly one of:

- `F2.6 PASS — DISCRETE OPERATOR/CHANNEL ALGEBRA QUALIFIED — RETURN TO MASTER`;
- `F2.6 HOLD — SPECIFIC DISCRETE ALGEBRA/IMPLEMENTATION DECISION REQUIRED — RETURN TO MASTER`;
- `F2.6 FAIL — RETURN TO MASTER`.

A HOLD must identify one specific unresolved object. A FAIL may not be repaired inside F2.6 by changing F2.3/F2.4, changing any F2.5 object beyond the already frozen F2.5R repair, adding damping/filtering/loading, deleting directions or redefining physical channels.

## Forbidden work

Do **not** calculate or inspect:

- eigenvalues, eigenvectors, growth rates, spectral abscissa or pseudospectra;
- matrix exponentials, propagators, Gramians or cumulative channel operators;
- finite-time energy/transport objectives;
- optimizer directions, principal angles, performance gaps or horizon dependence;
- physical parameter, wavenumber or input-subspace scans;
- resolutions outside the frozen repaired K0/K1/K2 ladder;
- GENE or another external GK solver.

Do not add collisions, hypercollision, viscosity, diffusion, filtering, absorbing layers, metric shifts or ad hoc regularization.

No branch-side next gate is self-authorized after the result.

**STOP / RETURN TO MASTER AFTER F2.6 0_3.**
