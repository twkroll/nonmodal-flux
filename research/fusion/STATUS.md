# Fusion Branch Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and the submission track remains parked.

B5.5, F1.2, F1.3 and F1.4 are complete and MASTER-integrated. The targeted R1 literature audit is complete and MASTER-integrated. F2.1 is now also complete and MASTER-integrated.

## Frozen R1 control

The anisotropic-ZLR four-moment R1 minimal-curvature candidate remains a frozen structural/conservative control. Its exact collisionless one-channel balance and frozen `B=I_4`, `R_in=M_k` geometry imply

\[
2\frac{R_0}{L_T}K_q(T)=\mathcal E_M(T)-I,
\]

so cumulative ion-heat and final free-energy optimization are affinely equivalent at every horizon. The R1 objective-separation pilot remains blocked. No damping, retuning or FLR-only rescue is permitted.

## Frozen F2.1 balance-complete architecture

Primary reduced candidate:

\[
\boxed{
\text{finite-ion-FLR electrostatic local-GK ions}
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

The reduced continuous state is

\[
x=(g_i(l,E_i,\mu_i,\sigma),\,g_e^{\rm tr}(E_e,\lambda,w)),
\]

with the electrostatic field reconstructed from quasineutrality and with positive continuous Helmholtz free-energy metric

\[
\mathcal M_{F2}\succ0.
\]

The frozen reduced collisionless balance is

\[
\boxed{
\frac{dW}{dt}
=G_\Gamma\Gamma
+G_{T,i}q_i
+G_{T,e}q_e^{\rm tr}.
}
\]

Electrostatic ambipolarity gives one particle channel for hydrogen,

\[
\Gamma_i=\Gamma_e^{\rm tr}\equiv\Gamma,
\]

but no closure identity forces `q_i=q_e^tr`. Therefore the exact R1 two-operator affine redundancy is no longer structurally forced. No finite-time objective or optimizer separation has been inspected.

Canonical F2.1 result:

`research/fusion/fusion_f2_1_two_species_local_gyrokinetic_balance_specification_gate_0_1.md`

MASTER F2.1 integration freeze:

`research/master/fusion_f2_1_two_species_gk_balance_integration_freeze_0_1.md`

F2.1 branch commit `93e855b1618a92a6a20724a09549897112b23b7d`; Python CI #347 = `SUCCESS`.

## Active instruction

**Status:** `FUSION F2.2 LOCAL MAGNETIC-GEOMETRY FAMILY / KINETIC CONVENTION FREEZE READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`

On a bare `GO`, first read this STATUS and execute only that committed instruction.

## F2.2 scope

Freeze one source-faithful local toroidal magnetic-geometry family and all continuous coordinate, Fourier/ballooning, magnetic-drift, trapped/passing and bounce-average conventions required by F2-R before any numerical geometry/gradient/wavenumber point or phase-space discretization is chosen.

A standard circular-concentric / s-alpha / Cyclone-Base-Case-compatible local tokamak geometry is only a leading candidate and may be selected solely if source-consistent with the F2-R equations and justified by physical transparency, trapped-particle structure, tractability and later local-GK/GENE mapping.

## Forbidden until F2.2 returns

Do not scan geometry parameters, gradients, wavenumbers, trapped fractions or model variants. Do not discretize phase space, define/optimize kinetic `B` or `R_in`, construct discrete `A/M/Q`, run GENE, perform spectral/transient/finite-time calculations, compute optimizers/angles/gaps, or select geometry by expected objective-separation magnitude. Do not reopen R1, MODES, CONT, CASCADE, Power Grid, Photonics or Paper-1 work.

## Expected return state

One of:

- `F2.2 PASS — LOCAL MAGNETIC-GEOMETRY / KINETIC CONVENTIONS FROZEN — RETURN TO MASTER`;
- `F2.2 HOLD — SPECIFIC GEOMETRY/SOURCE DECISION REQUIRED — RETURN TO MASTER`;
- `F2.2 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Governance authority

- `research/master/fusion_f2_1_two_species_gk_balance_integration_freeze_0_1.md`
- `research/master/prompts/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / AWAIT GO.**
