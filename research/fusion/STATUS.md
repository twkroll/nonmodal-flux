# Fusion Branch Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and the submission track remains parked.

B5.5, F1.2, F1.3 and F1.4 are complete and MASTER-integrated. The targeted R1 structural-redundancy / fidelity-breaking literature audit is complete and MASTER-integrated. F2.1 is now complete in this Fusion branch.

## Frozen R1 control

The anisotropic-ZLR four-moment R1 minimal-curvature candidate remains a frozen structural/conservative control. Its exact collisionless one-channel balance and frozen `B=I_4`, `R_in=M_k` geometry imply

\[
2\frac{R_0}{L_T}K_q(T)=\mathcal E_M(T)-I,
\]

so cumulative ion-heat and final free-energy optimization are affinely equivalent at every horizon. The R1 objective-separation pilot remains blocked. No damping, retuning or FLR-only rescue is permitted.

## F2.1 completed result

Primary reduced higher-fidelity candidate:

\[
\boxed{
\text{finite-ion-FLR local GK ions}
+\text{collisionless bounce-averaged trapped electrons}
}
\]

with passing electrons adiabatic at leading order in the slow-electron-transit ordering.

Higher-fidelity reference:

\[
\boxed{
\text{fully kinetic two-species electrostatic local GK}
+\text{H-theorem-compatible physical collisions}
}
\]

The reduced dynamic state is continuous in phase space,

\[
x=(g_i(l,E_i,\mu_i,\sigma),\,g_e^{\rm tr}(E_e,\lambda,w)),
\]

with the electrostatic potential reconstructed from quasineutrality.

The positive continuous Helmholtz free energy defines a kinetic metric

\[
\mathcal M_{F2}\succ0.
\]

The source-faithful reduced collisionless balance is

\[
\frac{dW}{dt}
=D_i+D_e^{\rm tr},
\]

or, after decomposing the physical transport work and using electrostatic ambipolarity,

\[
\boxed{
\frac{dW}{dt}
=G_\Gamma\Gamma
+G_{T,i}q_i
+G_{T,e}q_e^{\rm tr}.
}
\]

Quasineutrality constrains the particle fluxes by

\[
\sum_a e_a\Gamma_a=0,
\]

so for hydrogen `Gamma_i=Gamma_e^tr`, but no closure identity forces `q_i=q_e^tr`.

Therefore the exact R1 two-operator affine redundancy is **not structurally forced** in F2.1. This is only a possibility-in-principle result; no finite-time objective or optimizer separation has been inspected.

The reduced candidate remains collisionless because the bounce-averaged source model is derived in that ordering. Adding collisions there would require a separate trapped/passing collision model. The fully kinetic reference must use an H-theorem-compatible collision operator with nonnegative total free-energy dissipation.

Finite ion FLR is retained in gyroaveraging, polarization/free-energy geometry and the physical transport kernels, but is not classified as an independent source/sink or redundancy-breaking mechanism by itself.

Canonical F2.1 result:

`research/fusion/fusion_f2_1_two_species_local_gyrokinetic_balance_specification_gate_0_1.md`

## Active instruction

**Status:** `F2.1 PASS — TWO-SPECIES GK CANDIDATE/BALANCE SPECIFIED — RETURN TO MASTER`

**Next instruction:** none in this branch.

A bare `GO` must not open phase-space discretization, parameter/convention selection, kinetic input geometry, numerical/spectral qualification, GENE work or any finite-time objective calculation while this status remains `RETURN TO MASTER`. MASTER must integrate F2.1 and commit any later handoff explicitly.

## Unresolved pre-effect objects

Before any numerical execution, MASTER must separately authorize and freeze, as applicable:

- exact local magnetic geometry and trapped-particle structure;
- physical parameter/gradient point and wavenumbers;
- phase-space discretization and quadrature;
- kinetic admissible input map `B` and input cost `R_in`;
- physical collision parameters/operator implementation for the fully kinetic reference;
- discrete particle/heat channel reconstruction from the physical flux integrals;
- numerical/spectral and structure-preserving qualification;
- later GENE-compatible normalization/diagnostic mapping.

## Forbidden until MASTER returns a new committed handoff

Do not discretize velocity space for optimization, scan parameters or model variants, run GENE, construct finite-time propagators/Gramians/cumulative operators, compute optimizers/angles/gaps, choose gradients/collisions/trapped fractions by effect size, retune R1, or open MODES/CONT/CASCADE, Power Grid/Photonics work or Paper-1 work.

## Governance authority

- `research/master/fusion_f1_4_marginal_structural_integration_freeze_0_1.md`
- `research/literature/fusion_r1_structural_redundancy_fidelity_breaking_literature_audit_0_1.md`
- `research/master/fusion_r1_structural_redundancy_literature_integration_freeze_0_1.md`
- `research/master/prompts/fusion_f2_1_two_species_local_gyrokinetic_balance_specification_gate_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / RETURN TO MASTER.**
