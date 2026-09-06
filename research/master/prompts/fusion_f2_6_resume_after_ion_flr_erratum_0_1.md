# Fusion F2.6 — Resume Discrete Operator / Channel Algebraic Qualification after Ion-FLR Erratum 0.1

**Date:** 2026-09-06  
**Authority:** MASTER  
**Execution branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

## Objective

Resume the previously held F2.6 algebraic qualification and resolve only the ion-FLR blocker using the MASTER erratum

`research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`.

This remains a **pre-spectral, pre-effect** gate.

## Mandatory controlling inputs

Read and preserve:

- `research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`;
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_1.md` as the historical HOLD record;
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_1.json` as historical diagnostics;
- `research/master/fusion_f2_5_discretization_specification_integration_freeze_0_1.md`;
- `research/fusion/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`;
- F2.1–F2.4 integration freezes;
- the shared MASTER Prompt Handoff Protocol.

## Frozen ion-FLR convention

Keep

\[
\rho_{i0}=v_{Ti}/\Omega_i(B_0),
\qquad
k_y\rho_{i0}=0.3,
\]

and the local gyroaverage

\[
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right).
\]

Use everywhere in polarization/free-energy FLR factors

\[
\boxed{
 b_i(\theta)
 =(k_\perp(\theta)\rho_{i0})^2
 \left(\frac{B_0}{B(\theta)}\right)^2,
\qquad
\Gamma_{0i}=I_0(b_i)e^{-b_i}.
}
\]

Do not change any F2.3 physical parameter, F2.4 input geometry or F2.5 numerical resolution/basis/quadrature.

## Required resumption work

On the frozen K0/K1/K2 ladder:

1. rebuild all FLR-dependent quasineutrality, Helmholtz and generator/channel ingredients using the controlling local-B `b_i(theta)` convention;
2. re-run the manufactured Maxwellian identity and confirm numerically that `Gamma0i=<J0i^2>` to the expected quadrature accuracy;
3. construct the canonical `M_K` directly from the positive Helmholtz functional after field elimination and verify Hermiticity and strict positive definiteness without loading, clipping or nullspace deletion;
4. construct `A_K` directly from the frozen F2-R equations and the frozen F2.5 weak/SBP phase-space discretization;
5. independently reconstruct `Q_Gamma,K`, `Q_qi,K`, `Q_qe,K` from the physical radial gyrocentre flux integrals using the same frozen state space and quadratures;
6. verify quasineutrality residuals, `B_K=I`, `R_in,K=M_K`, physical-channel Hermiticity, particle ambipolarity, conservative phase-space adjoint/skew structure and the complete F2.1 discrete free-energy balance;
7. report K0/K1/K2 structural/convergence diagnostics specified by the original F2.6 handoff.

The physical channel matrices must remain logically independent of the balance identity. Do not define any `Q` backwards from `A_K^dagger M_K+M_K A_K`.

## Historical/provisional data rule

The `0_1` F2.6 metric/channel probes were explicitly provisional under the unresolved FLR convention. They may be used only as debugging comparisons. The resumed calculation must regenerate canonical diagnostics under the MASTER erratum.

## Required outputs

Create new versioned files:

- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_2.md`;
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_2.json`.

Update `research/fusion/STATUS.md` in the same work package.

Do not overwrite the `0_1` HOLD report or diagnostics.

## Pass / hold / fail logic

Return exactly one of:

- `F2.6 PASS — DISCRETE OPERATOR/CHANNEL ALGEBRA QUALIFIED — RETURN TO MASTER`;
- `F2.6 HOLD — SPECIFIC DISCRETE ALGEBRA/IMPLEMENTATION DECISION REQUIRED — RETURN TO MASTER`;
- `F2.6 FAIL — RETURN TO MASTER`.

A new HOLD must identify a specific remaining unresolved object. A FAIL may not be repaired by retuning F2.3, altering F2.4/F2.5, adding damping/filtering/loading or changing the physical channel definitions.

## Forbidden work

Do **not** calculate or inspect:

- eigenvalues, eigenvectors, growth rates, spectral abscissa or pseudospectra;
- matrix exponentials, propagators, Gramians or cumulative channel operators;
- finite-time energy/transport objectives;
- optimizer directions, principal angles, performance gaps or horizon dependence;
- parameter/wavenumber/input-subspace scans;
- resolutions beyond K0/K1/K2;
- GENE or another external GK run.

Do not add collisions, hypercollision, viscosity, diffusion, filtering, absorbing layers, metric shifts or ad hoc regularization.

No branch-side next gate is self-authorized after the result.

**STOP / RETURN TO MASTER AFTER F2.6 RESUMPTION.**
