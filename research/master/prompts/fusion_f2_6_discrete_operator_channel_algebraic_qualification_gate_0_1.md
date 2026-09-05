# Fusion F2.6 — Discrete Generator / Helmholtz Metric / Physical Channel Reconstruction & Algebraic Balance Qualification Gate 0.1

**Date:** 2026-09-05  
**Authority:** MASTER  
**Execution branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

## Objective

Instantiate the already-frozen F2.5 K0/K1/K2 numerical representation for the already-frozen F2-R physics and construct the discrete physical operators

\[
A_K,\qquad M_K,\qquad Q_{\Gamma,K},\qquad Q_{q_i,K},\qquad Q_{q_e,K}
\]

plus the discrete quasineutrality reconstruction, and qualify only their algebraic/physical structure **before any spectrum or finite-time objective is inspected**.

This is a pre-spectral, pre-effect gate.

## Canonical inputs

Read and preserve:

- `research/master/fusion_f2_5_discretization_specification_integration_freeze_0_1.md`;
- `research/fusion/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`;
- `research/master/fusion_f2_4_input_geometry_integration_freeze_0_1.md`;
- `research/master/fusion_f2_3_physical_parameter_integration_freeze_0_1.md`;
- `research/master/fusion_f2_2_geometry_convention_integration_freeze_0_1.md`;
- `research/master/fusion_f2_1_two_species_gk_balance_integration_freeze_0_1.md`;
- the shared MASTER Prompt Handoff Protocol.

R1 remains the frozen structural no-go control and must not be modified.

## Required construction

For each frozen level K0, K1, K2:

1. instantiate exactly the frozen ballooning/ion/trapped-electron basis and quadratures, without hidden extra resolution, changed cutoffs, filters or damping;
2. assemble the weak/algebraic quasineutrality system
   \[
   C_{\rm QN,K}\phi_K=S_{\rm QN,K}x_K,
   \qquad
   \phi_K=P_{\rm QN,K}x_K,
   \]
   and eliminate `phi_K` from the physical state;
3. construct `M_K` directly from the discrete positive F2 Helmholtz functional, not from `A_K` or a desired balance identity;
4. construct `A_K` directly from the frozen collisionless F2-R equations, including ion parallel/mirror dynamics, magnetic drifts, finite ion FLR, trapped-electron bounce-averaged dynamics and the frozen equilibrium drives;
5. independently reconstruct the physical particle, ion-heat and trapped-electron-heat forms from the frozen radial gyrocentre flux integrals and the same quadratures/state space, yielding Hermitian matrices `Q_Gamma,K`, `Q_qi,K`, `Q_qe,K`;
6. inherit the discrete input pair as `B_K=I`, `R_in,K=M_K` in the conforming representation, or the exactly congruent equivalent if an explicit inclusion map is unavoidable.

## Required algebraic qualification

Report at K0/K1/K2, before any spectral work:

### A. Geometry/quadrature and manufactured-function checks

- Maxwellian density/energy/heat-weight moment reproduction;
- `J0i`-weighted and `Gamma0i` polarization manufactured integrals;
- regularized bounce denominators and bounce averages for the frozen analytic test functions;
- trapped-electron charge projection consistency;
- `max(k_perp rho_e)` on the full retained support.

### B. Quasineutrality and metric

- residuals of `C_QN,K phi_K-S_QN,K x_K` on fixed manufactured/random states;
- invertibility/conditioning diagnostics of the physical quasineutrality solve, without pseudo-inverse cutoffs or diagonal loading;
- Hermiticity residual of `M_K`;
- strict positive-definite factorization of `M_K` with no shift, clipping or nullspace deletion;
- exact/congruent verification of `B_K=I`, `R_in,K=M_K`;
- free-energy convergence for fixed projected manufactured states across K0/K1/K2.

### C. Generator/channel algebra

- source-free collisionless adjoint/skew residual of the conservative ion phase-space advection in the physical mass/free-energy form;
- Hermiticity residuals of `Q_Gamma,K`, `Q_qi,K`, `Q_qe,K`;
- electrostatic particle-channel ambipolarity residual under the frozen hydrogenic conventions;
- complete discrete F2.1 balance residual
  \[
  A_K^\dagger M_K+M_KA_K
  =2\left(
  G_\Gamma Q_{\Gamma,K}
  +G_{T,i}Q_{q_i,K}
  +G_{T,e}Q_{q_e,K}
  \right)
  \]
  for the collisionless reduced F2-R model;
- consistency of the independently reconstructed channel forms with direct quadrature evaluation on fixed manufactured/random states;
- K0/K1/K2 convergence/robustness of the structural residuals.

Do not derive any `Q` backwards from the balance identity. The physical flux-integral reconstruction and the balance check must remain logically independent.

## Pass / hold / fail logic

Return `PASS` only if all three frozen levels can be instantiated and the physical/algebraic checks support a structure-preserving discrete representation without unapproved regularization.

Return `HOLD` if a specific implementation ambiguity or computational obstacle prevents a defensible qualification but does not falsify the frozen physical/numerical architecture. Identify the exact unresolved object and do not change it silently.

Return `FAIL` if the frozen discretization cannot preserve the required physical state geometry, positivity, quasineutrality, channel structure or F2.1 balance under the predeclared ladder.

A failure may not be repaired by changing F2.3 parameters, F2.4 input geometry, F2.5 cutoffs/bases/quadratures, adding damping, loading the metric, clipping eigenvalues, deleting physical directions or deriving channels from the desired balance.

## Forbidden work

Do **not**:

- calculate or inspect eigenvalues, growth rates, spectral abscissa, pseudospectra or eigenvectors;
- construct `exp(A_K t)`, propagators, Gramians, cumulative transport operators or finite-time energy operators;
- calculate optimizer directions, principal angles, performance gaps or horizon dependence;
- scan parameters, wavenumbers, resolutions beyond the frozen K0/K1/K2 ladder or input subspaces;
- run GENE or another GK solver;
- add collisions, hypercollision, viscosity, diffusion, filtering, absorbing layers or ad hoc regularization to F2-R;
- retune the frozen F2.3 physical point;
- alter `B/R_in` from F2.4;
- reopen R1, FLR-only rescue, MODES, CONT, CASCADE, Power Grid, Photonics or Paper-1 work.

## Required output

Create:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_1.md`

Store any necessary machine-readable structural diagnostics under `research/fusion/` with clearly versioned F2.6 filenames.

Update `research/fusion/STATUS.md` in the same work package.

Return exactly one of:

- `F2.6 PASS — DISCRETE OPERATOR/CHANNEL ALGEBRA QUALIFIED — RETURN TO MASTER`;
- `F2.6 HOLD — SPECIFIC DISCRETE ALGEBRA/IMPLEMENTATION DECISION REQUIRED — RETURN TO MASTER`;
- `F2.6 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Expected next MASTER decision after PASS

If F2.6 passes, MASTER should open a separate **numerical/spectral qualification gate** on the already qualified frozen operators. That later gate may inspect the complete spectrum and conditioning/convergence needed to decide whether a finite-time pilot is scientifically admissible, but finite-time objective calculations should still remain blocked until a subsequent explicit pilot specification/freeze.

**STOP / RETURN TO MASTER AFTER F2.6.**
