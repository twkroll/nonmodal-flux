# Fusion Branch Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit, F2.1, F2.2, F2.3 and F2.4 are complete and MASTER-integrated. F2.5 is now complete in this Fusion branch.

## Frozen R1 control

R1 remains the structural/conservative no-go control. Its one-channel collisionless balance with `B=I4`, `R_in=M_k` makes cumulative ion heat and final free energy affinely equivalent at every horizon. No damping, retuning or FLR-only rescue is permitted.

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

No parity, moment-null, transport-neutral or effect-motivated input restriction is authorized.

## F2.5 completed discretization / quadrature specification

Canonical result:

`research/fusion/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`

Frozen numerical package:

\[
\boxed{
\text{compact-support ballooning Galerkin/SBP spectral elements}
\times\text{ Hermite--Laguerre ion velocity representation}
+\text{ regularized trapped-electron orbit quadrature}
}
\]

Key conventions:

- ballooning windows end at magnetic maxima and use compact-support LGL spectral elements;
- no boundary damping, filtering, hyperdiffusion or hypercollision;
- ions use symmetric Gauss--Hermite `v_parallel` and Gauss--Laguerre magnetic-moment quadrature, retaining both `sigma` signs with no parity reduction;
- ion turning set `v_parallel=0` is measure zero and not an extra DOF;
- trapped electrons use generalized Gauss--Laguerre energy, interior Gauss--Legendre pitch, explicit well labels and analytic bounce-singularity regularization;
- the trapped/passing separatrix has no state DOF;
- finite ion `J0i` and `Gamma0i` are retained without small-argument expansion;
- `phi_K` is reconstructed and algebraically eliminated from quasineutrality, never added as an input direction;
- later `M_K` must come directly from the positive Helmholtz quadratic form and satisfy `M_K=M_K^dagger>0` without shifts/clipping;
- conforming discrete input geometry inherits `B_K=I`, `R_in,K=M_K`;
- later particle/ion-heat/electron-heat channels must use the same state space and physical quadratures.

Frozen three-level refinement ladder:

| quantity | K0 primary | K1 | K2 |
|---|---:|---:|---:|
| `Theta_max` | `3 pi` | `5 pi` | `7 pi` |
| complete electron wells | 3 | 5 | 7 |
| `theta` elements | 6 | 10 | 14 |
| LGL degree `p_theta` | 12 | 16 | 20 |
| interior `theta` DOF | 71 | 159 | 279 |
| ion Hermite order | 16 | 24 | 32 |
| ion Laguerre order | 8 | 12 | 16 |
| trapped-e energy order | 12 | 18 | 24 |
| trapped-e pitch order | 12 | 18 | 24 |
| bounce quadrature order | 24 | 36 | 48 |

At the frozen F2.3 point, the maximum retained-support electron-FLR ordering parameters are approximately `0.03765`, `0.06241`, `0.08724` on K0/K1/K2 respectively.

F2.5 constructs no discrete `A/M/Q`, spectrum or finite-time quantity. A later gate must first reconstruct the discrete generator/metric/physical channels and verify quasineutrality, positivity, Hermiticity, ambipolarity and the F2.1 algebraic free-energy balance.

## Active instruction

**Status:** `F2.5 PASS — STRUCTURE-PRESERVING DISCRETIZATION / QUADRATURE SPECIFICATION FROZEN — RETURN TO MASTER`

**Next instruction:** none in this branch.

A bare `GO` must not open discrete operator/channel construction, algebraic qualification, spectrum, GENE work or finite-time objectives while this status remains `RETURN TO MASTER`. MASTER must integrate F2.5 and commit any later handoff explicitly.

## Remaining pre-effect objects

Before any finite-time execution, MASTER must separately authorize and freeze, as applicable:

- discrete `A_K`, `M_K`, `Q_Gamma,K`, `Q_qi,K`, `Q_qe,K` construction on the frozen ladder;
- quasineutrality/free-energy/channel algebraic balance qualification;
- spectral qualification only after the algebraic gate passes;
- later finite-time pilot specification;
- fully kinetic collisional-reference / GENE mapping details.

## Forbidden until MASTER returns a new committed handoff

Do not change cutoffs or quadratures, construct/inspect spectra, propagators, Gramians, cumulative objectives, optimizers, angles or gaps, scan parameters, run GENE, add collisions/damping to F2-R, retune F2.3, alter F2.4 input geometry, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Governance authority

- `research/master/fusion_f2_4_input_geometry_integration_freeze_0_1.md`
- `research/master/prompts/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / RETURN TO MASTER.**
