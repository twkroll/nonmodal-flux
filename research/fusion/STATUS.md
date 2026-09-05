# Fusion Branch Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit, F2.1, F2.2, F2.3, F2.4 and F2.5 are complete and MASTER-integrated.

## Frozen F2-R architecture / point / input geometry

Primary reduced candidate:

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons, in the frozen large-aspect-ratio circular `s-alpha` ballooning-space flux tube.

The F2.3 single CBC-compatible point remains fixed: `R0/a=2.77778`, `r0/a=0.5`, `epsilon=0.18`, `q=1.4`, `shat=0.8`, `alpha_MHD=0`, deuterium/electron `mi/me=3672`, `Ti/Te=1`, equal density, `a/Ln=0.8`, `a/LTi=a/LTe=2.49`, `ky rho_i=+0.3`, `theta0=0`, `kx0=0`.

The continuous physical input pair remains

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}}.
\]

## Frozen F2.5 discretization / quadrature specification

Canonical result:

`research/fusion/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`

MASTER integration freeze:

`research/master/fusion_f2_5_discretization_specification_integration_freeze_0_1.md`

Frozen package:

\[
\boxed{
\text{compact-support ballooning Galerkin/SBP spectral elements}
\times\text{ Hermite--Laguerre ion velocity representation}
+\text{ regularized trapped-electron orbit quadrature}
}
\]

with no artificial damping/filtering, exact finite-ion FLR, algebraic quasineutrality elimination, both ion velocity signs retained, no parity reduction and no extra separatrix/turning-point state DOF.

The K0/K1/K2 refinement ladder is frozen exactly as specified in F2.5. F2.5 branch commit `43de899b547b2ccc1d0c11ecb6788dfce6cb6b47`; Python CI #378 = `SUCCESS`.

No discrete `A/M/Q`, spectrum or finite-time objective was constructed in F2.5.

## Active instruction

**Status:** `FUSION F2.6 DISCRETE OPERATOR / CHANNEL ALGEBRAIC QUALIFICATION READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_1.md`

On bare `GO`, first read this STATUS and execute only that committed instruction.

## F2.6 scope

Instantiate the frozen K0/K1/K2 numerical representation and construct `A_K`, `M_K`, `Q_Gamma,K`, `Q_qi,K`, `Q_qe,K` plus the discrete quasineutrality reconstruction directly from the frozen physical equations/quadratures. Qualify only structural algebra: quasineutrality residuals, `M_K>0`, Hermiticity, `B_K=I`, `R_in,K=M_K`, physical-channel Hermiticity, ambipolarity, conservative-advection adjoint/skew structure and the complete F2.1 discrete free-energy balance.

The physical channel matrices must be reconstructed independently from the radial gyrocentre flux integrals; they may not be derived backwards from the desired balance identity.

## Forbidden until F2.6 returns

Do not inspect eigenvalues, growth rates, pseudospectra or eigenvectors. Do not construct propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not scan parameters/resolutions beyond K0/K1/K2, run GENE, add collisions/damping, retune F2.3, alter F2.4/F2.5, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Expected return

One of:

- `F2.6 PASS — DISCRETE OPERATOR/CHANNEL ALGEBRA QUALIFIED — RETURN TO MASTER`;
- `F2.6 HOLD — SPECIFIC DISCRETE ALGEBRA/IMPLEMENTATION DECISION REQUIRED — RETURN TO MASTER`;
- `F2.6 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

**STOP / AWAIT GO.**
