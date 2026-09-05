# Fusion Branch Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and the submission track remains parked.

B5.5, F1.2, F1.3, F1.4 and the R1 literature audit are complete and MASTER-integrated. F2.1 is complete and MASTER-integrated. F2.2 is now complete in this Fusion branch.

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

## F2.2 completed geometry/convention freeze

Canonical result:

`research/fusion/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`

Selected primary geometry family:

\[
\boxed{
\text{large-aspect-ratio circular local tokamak}
+\hat s\text{-}\alpha_{\rm MHD}\text{ flux-tube geometry in ballooning space}
}
\]

Frozen continuous conventions include:

- Clebsch `B = grad psi x grad alpha`, outward `psi`, `l` along `B`;
- `theta=0` at the outboard midplane and ballooning-space `theta in R`;
- Fourier factor `exp[i(k_psi psi+k_alpha alpha)]`, `k_alpha != 0`;
- `B(theta)=B0/[1+epsilon cos(theta)]`;
- `dl/dtheta=q R0[1+epsilon cos(theta)]`;
- `dV=dpsi dalpha dl/B`;
- `Lambda(theta)=kx0/ky + shat theta - alpha_MHD sin(theta)`;
- `k_perp^2=ky^2[1+Lambda^2]` and twist sign `kx(theta+2pi)-kx(theta)=+2pi shat ky`;
- signed magnetic drift `omega_da=k_perp dot v_da` with source term `+i omega_da g_a`;
- explicit curvature plus grad-B drift decomposition;
- trapped/passing classification from `lambda B(theta)`;
- circular bounce points and exact orbit-time bounce-average measure;
- trapped-electron well label `w`, adiabatic leading passing electrons;
- finite ion FLR and `k_perp rho_e << 1` on the retained electron-support region;
- no parity reduction.

The geometry family is CBC/GENE-compatible only as a later mapping/parameterization target. No CBC numerical values, gradients, `q`, shear, aspect ratio, `alpha_MHD`, wavenumbers, ballooning angle or discretization are frozen by F2.2.

## Active instruction

**Status:** `F2.2 PASS — LOCAL MAGNETIC-GEOMETRY / KINETIC CONVENTIONS FROZEN — RETURN TO MASTER`

**Next instruction:** none in this branch.

A bare `GO` must not open a physical parameter point, kinetic input geometry, phase-space discretization, numerical/spectral qualification, GENE work or finite-time objective calculation while this status remains `RETURN TO MASTER`. MASTER must integrate F2.2 and commit any later handoff explicitly.

## Unresolved pre-effect objects

Before any numerical execution, MASTER must separately authorize and freeze, as applicable:

- one physical geometry/gradient/wavenumber point;
- kinetic admissible input map `B` and physical input cost `R_in`;
- phase-space discretization, quadrature and bounce/separatrix handling;
- discrete particle and ion/electron heat-channel reconstruction;
- numerical/free-energy/spectral qualification;
- fully kinetic reference collision parameters and GENE-compatible mapping.

## Forbidden until MASTER returns a new committed handoff

Do not scan geometry parameters, gradients, wavenumbers, trapped fractions or model variants. Do not discretize phase space, define/optimize kinetic `B` or `R_in`, construct discrete `A/M/Q`, run GENE, perform spectral/transient/finite-time calculations, compute optimizers/angles/gaps, or choose later conventions by expected objective-separation magnitude. Do not reopen R1, MODES, CONT, CASCADE, Power Grid, Photonics or Paper-1 work.

## Governance authority

- `research/master/fusion_f2_1_two_species_gk_balance_integration_freeze_0_1.md`
- `research/master/prompts/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / RETURN TO MASTER.**
