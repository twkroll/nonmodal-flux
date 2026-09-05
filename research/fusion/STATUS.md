# Fusion Branch Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and the submission track remains parked.

B5.5, F1.2, F1.3, F1.4 and the R1 literature audit are complete and MASTER-integrated. F2.1 and F2.2 are also complete and MASTER-integrated.

## Frozen R1 control

The anisotropic-ZLR four-moment R1 minimal-curvature candidate remains a frozen structural/conservative control. Its exact collisionless one-channel balance and frozen `B=I_4`, `R_in=M_k` geometry imply

\[
2\frac{R_0}{L_T}K_q(T)=\mathcal E_M(T)-I,
\]

so cumulative ion heat and final free energy are affinely equivalent at every horizon. The R1 objective-separation pilot remains blocked. No damping, retuning or FLR-only rescue is permitted.

## Frozen F2.1 architecture

Primary reduced candidate:

\[
\boxed{
\text{finite-ion-FLR electrostatic local-GK ions}
+\text{collisionless bounce-averaged trapped electrons}
}
\]

with passing electrons adiabatic at leading order.

Higher-fidelity reference:

\[
\boxed{
\text{fully kinetic two-species electrostatic local GK}
+\text{H-theorem-compatible physical collisions}
}
\]

The reduced continuous balance remains

\[
\frac{dW}{dt}
=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr},
\]

so the R1 one-channel affine redundancy is not structurally forced. No finite-time objective has been inspected.

## Frozen F2.2 geometry/conventions

MASTER integration freeze:

`research/master/fusion_f2_2_geometry_convention_integration_freeze_0_1.md`

Primary geometry family:

\[
\boxed{
\text{large-aspect-ratio circular local tokamak}
+\hat s\text{-}\alpha_{\rm MHD}\text{ flux-tube geometry in ballooning space}
}
\]

Frozen continuous conventions include the Clebsch/Fourier orientation, circular `B(theta)` and `dl/dtheta`, `s-alpha` `k_perp(theta)` and twist sign, signed magnetic drifts, trapped/passing and bounce-point definitions, exact orbit-time bounce averages, finite ion FLR, the leading adiabatic-passing/bounce-averaged-trapped electron ordering, infinite ballooning line and no parity reduction.

No numerical `epsilon`, `q`, `shat`, `alpha_MHD`, gradients, temperature ratio, `ky`, `kx0/theta0` or discretization is frozen by F2.2.

F2.2 branch commit `19dcf169ffe36c7b5f64f560f1f22294fa8ee239`; Python CI #355 = `SUCCESS`.

## Active instruction

**Status:** `FUSION F2.3 PHYSICAL GEOMETRY / GRADIENT / WAVENUMBER PARAMETER FREEZE READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_f2_3_physical_parameter_freeze_0_1.md`

On a bare `GO`, first read this STATUS and execute only that committed instruction.

## F2.3 scope

Freeze exactly one coherent, source-supported physical geometry/gradient/wavenumber point for the already-frozen F2-R architecture and F2.2 geometry family. A CBC-compatible point is a leading benchmark only if the required two-species trapped-electron quantities are source-consistent. If the needed values cannot be justified without mixing incompatible benchmarks, return `HOLD` rather than inventing or tuning them.

## Forbidden until F2.3 returns

Do not scan geometry parameters, gradients, wavenumbers, trapped fractions or model variants. Do not calculate eigenvalues or stability, discretize phase space, define/optimize kinetic `B` or `R_in`, construct discrete `A/M/Q`, run GENE, perform transient/finite-time calculations or compute optimizers/angles/gaps. Do not select any parameter by expected objective-separation magnitude. Do not reopen R1, MODES, CONT, CASCADE, Power Grid, Photonics or Paper-1 work.

## Expected return state

One of:

- `F2.3 PASS — PHYSICAL GEOMETRY/GRADIENT/WAVENUMBER POINT FROZEN — RETURN TO MASTER`;
- `F2.3 HOLD — SOURCE-SUPPORTED PARAMETER DECISION REQUIRED — RETURN TO MASTER`;
- `F2.3 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Governance authority

- `research/master/fusion_f2_1_two_species_gk_balance_integration_freeze_0_1.md`
- `research/master/fusion_f2_2_geometry_convention_integration_freeze_0_1.md`
- `research/master/prompts/fusion_f2_3_physical_parameter_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / AWAIT GO.**
