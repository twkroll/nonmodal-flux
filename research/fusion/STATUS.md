# Fusion Branch Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit, F2.1, F2.2, F2.3 and F2.4 are complete and MASTER-integrated.

## Frozen R1 control

R1 remains the structural/conservative no-go control. Its one-channel collisionless balance with `B=I4`, `R_in=M_k` makes cumulative ion heat and final free energy affinely equivalent at every horizon. No damping, retuning or FLR-only rescue is permitted.

## Frozen F2-R architecture and point

Primary reduced candidate:

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons.

Primary geometry family:

\[
\boxed{\text{large-aspect-ratio circular local tokamak}+\hat s\text{-}\alpha_{\rm MHD}\text{ ballooning-space flux tube}}
\]

The F2.3 CBC-compatible single point remains frozen with `R0/a=2.77778`, `r0/a=0.5`, `epsilon=0.18`, `q=1.4`, `shat=0.8`, `alpha_MHD=0`, deuterium/electron `mi/me=3672`, `Ti/Te=1`, equal density, `a/Ln=0.8`, `a/LTi=a/LTe=2.49`, `ky rho_i=+0.3`, `theta0=0`, `kx0=0`. No retuning is permitted.

## Frozen F2.4 input geometry

The physically admissible continuous state/input space is the full finite-Helmholtz-free-energy tangent space of the already reduced F2-R model,

\[
\mathcal H_{F2}=\overline{\mathcal D_0}^{\|\cdot\|_{F2}},
\qquad
\|x\|_{F2}^2=\langle x,\mathcal M_{F2}x\rangle=2W[x].
\]

Quasineutrality is a field-reconstruction map and not an additional kinetic-state constraint. The continuous input pair is frozen as

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}}.
\]

The budget is initial Helmholtz free energy, not laboratory actuator energy. No parity, moment-null, transport-neutral or effect-motivated input restriction is authorized.

Canonical F2.4 result:

`research/fusion/fusion_f2_4_kinetic_input_geometry_input_cost_freeze_0_1.md`

MASTER integration freeze:

`research/master/fusion_f2_4_input_geometry_integration_freeze_0_1.md`

F2.4 branch commit `eabc44856458c7450946050c8ab04362904ef9ac`; Python CI #371 = `SUCCESS`.

## Active instruction

**Status:** `FUSION F2.5 STRUCTURE-PRESERVING DISCRETIZATION / QUADRATURE SPECIFICATION FREEZE READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`

On bare `GO`, first read this STATUS and execute only that committed instruction.

## F2.5 scope

Freeze one structure-preserving numerical representation and predeclared convergence ladder for the F2-R kinetic state before any spectrum or finite-time objective is inspected. Cover ballooning-line truncation, ion parallel/velocity representation, trapped-electron energy/pitch/well quadrature, turning-point/separatrix treatment, bounce integration, finite ion FLR, quasineutrality handling, free-energy positivity targets, and inheritance of `B_K/R_in,K`.

F2.5 is a discretization-specification gate, not a spectral or CORE-effect gate. A later separate gate will reconstruct discrete `A/M/Q` and check algebraic balance before spectral qualification.

## Forbidden until F2.5 returns

Do not choose cutoffs/bases by eigenvalues, stability, nonnormality, transport magnitude or expected optimizer separation. Do not calculate spectra, propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not run GENE, scan parameters, add collisions to F2-R, retune F2.3, alter F2.4 input geometry, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Expected return

One of:

- `F2.5 PASS — STRUCTURE-PRESERVING DISCRETIZATION / QUADRATURE SPECIFICATION FROZEN — RETURN TO MASTER`;
- `F2.5 HOLD — DISCRETIZATION/STRUCTURE DECISION REQUIRED — RETURN TO MASTER`;
- `F2.5 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

**STOP / AWAIT GO.**
