# Fusion Branch Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and the submission track remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit, F2.1 and F2.2 are complete and MASTER-integrated. F2.3 is now complete in this Fusion branch.

## Frozen R1 control

The anisotropic-ZLR four-moment R1 minimal-curvature candidate remains a structural/conservative no-go control. Its one-channel collisionless balance with `B=I4`, `R_in=M_k` makes cumulative ion heat and final free energy affinely equivalent at every horizon. The R1 objective-separation pilot remains blocked; no damping, retuning or FLR-only rescue is permitted.

## Frozen F2 architecture and geometry

Primary reduced candidate:

\[
\boxed{
\text{finite-ion-FLR electrostatic local-GK ions}
+\text{collisionless bounce-averaged trapped electrons}
}
\]

with leading adiabatic passing electrons.

Primary geometry family:

\[
\boxed{
\text{large-aspect-ratio circular local tokamak}
+\hat s\text{-}\alpha_{\rm MHD}\text{ ballooning-space flux tube}
}
\]

The continuous F2.1 balance remains

\[
\frac{dW}{dt}
=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr},
\]

so the R1 one-channel affine redundancy is not structurally forced. No finite-time F2 objective has been inspected.

## F2.3 completed physical parameter freeze

Canonical result:

`research/fusion/fusion_f2_3_physical_parameter_freeze_0_1.md`

Frozen single CBC-compatible point:

\[
\boxed{
\begin{gathered}
R_0/a=2.77778,
\quad r_0/a=0.5,
\quad \epsilon=0.18,
\quad q=1.4,
\quad \hat s=0.8,
\quad \alpha_{\rm MHD}=0,\\
Z_i=+1,
\quad Z_e=-1,
\quad m_i/m_e=3672,
\quad T_i/T_e=1,
\quad n_i=n_e,\\
a/L_n=0.8,
\quad a/L_{T_i}=a/L_{T_e}=2.49,\\
k_y\rho_i=+0.3,
\quad \theta_0=0,
\quad k_{x0}=0.
\end{gathered}
}
\]

Equivalent major-radius gradients are

\[
R_0/L_n=2.222224,
\qquad
R_0/L_{T_i}=R_0/L_{T_e}=6.9166722.
\]

Normalization:

\[
v_{Ti}=\sqrt{T_i/m_i},
\qquad
\rho_i=v_{Ti}/\Omega_i,
\qquad
\tau_{\rm ref}=R_0/v_{Ti}.
\]

All three F2.1 supply coefficients are nonzero at the frozen point: `G_Gamma`, `G_Ti`, `G_Te`.

The trapped region is not a free knob. From `epsilon=0.18`, with `lambda_hat=lambda B0`,

\[
0.82<\widehat\lambda<1.18,
\]

and the outboard-midplane local trapped pitch fraction is approximately `0.5523`. For the deuterium/electron mass ratio, `rho_e/rho_i ~= 0.01650`, giving `k_perp(0) rho_e ~= 0.00495`.

No spectrum, phase-space grid, discrete operator, kinetic input map or finite-time objective was constructed.

## Active instruction

**Status:** `F2.3 PASS — PHYSICAL GEOMETRY/GRADIENT/WAVENUMBER POINT FROZEN — RETURN TO MASTER`

**Next instruction:** none in this branch.

A bare `GO` must not open kinetic input geometry, input-cost selection, phase-space discretization, numerical/spectral qualification, GENE work or finite-time objective calculations while this status remains `RETURN TO MASTER`. MASTER must integrate F2.3 and commit any later handoff explicitly.

## Remaining pre-effect objects

Before any numerical execution, MASTER must separately authorize and freeze, as applicable:

- kinetic admissible initial-condition map `B` and physical input cost `R_in`;
- ballooning/velocity-space discretization and separatrix treatment;
- discrete quasineutrality and physical particle/heat-channel reconstruction;
- structure-preserving numerical/free-energy/spectral qualification;
- later fully kinetic collisional-reference and GENE mapping details.

## Forbidden until MASTER returns a new committed handoff

Do not scan parameters or model variants. Do not construct discrete `A/M/Q`, eigenvalues, propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not run GENE, add collisions to F2-R, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Governance authority

- `research/master/fusion_f2_1_two_species_gk_balance_integration_freeze_0_1.md`
- `research/master/fusion_f2_2_geometry_convention_integration_freeze_0_1.md`
- `research/master/prompts/fusion_f2_3_physical_parameter_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / RETURN TO MASTER.**
