# Fusion Branch Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit, F2.1, F2.2 and F2.3 are complete and MASTER-integrated. F2.4 is now complete in this Fusion branch.

## Frozen R1 control

R1 remains the structural/conservative no-go control. Its one-channel collisionless balance with `B=I4`, `R_in=M_k` makes cumulative ion heat and final free energy affinely equivalent at every horizon. No damping, retuning or FLR-only rescue is permitted.

## Frozen F2-R architecture

Primary reduced candidate:

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons.

The continuous balance is

\[
\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr},
\]

so the R1 affine redundancy is not structurally forced. No finite-time F2 objective has been inspected.

## Frozen F2.2 geometry

Primary family:

\[
\boxed{\text{large-aspect-ratio circular local tokamak}+\hat s\text{-}\alpha_{\rm MHD}\text{ ballooning-space flux tube}}
\]

with the previously frozen Clebsch/Fourier, drift, trapping, bounce-average, FLR and ballooning-space conventions.

## Frozen F2.3 physical point

The single CBC-compatible point remains

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

with `v_Ti=sqrt(T_i/m_i)`, `rho_i=v_Ti/Omega_i`, and `tau_ref=R0/v_Ti`.

## F2.4 completed kinetic input geometry / input cost

Canonical result:

`research/fusion/fusion_f2_4_kinetic_input_geometry_input_cost_freeze_0_1.md`

The physically admissible continuous input space is the full finite-Helmholtz-free-energy tangent space of the **already reduced** F2-R model,

\[
\mathcal H_{F2}=\overline{\mathcal D_0}^{\|\cdot\|_{F2}},
\qquad
\|x\|_{F2}^2=\langle x,\mathcal M_{F2}x\rangle=2W[x].
\]

Here `D0` already incorporates the frozen physical model restrictions: fixed nonzonal sector, finite-free-energy ion kinetic phase space, trapped nonadiabatic electrons only, `g_e^pass=0` at leading order, bounce/orbit regularity, inherited ballooning conventions and reconstructed quasineutral electrostatic field.

Quasineutrality is a unique field-reconstruction map,

\[
\phi=P_{\rm QN}(g_i,g_e^{\rm tr}),
\]

not a proper-subspace condition on the kinetic state. No additional particle-number, charge, momentum, energy-moment, gauge, parity or transport-neutral input restriction is physically required in the fixed `k_alpha != 0` block.

Therefore the frozen continuous input pair is

\[
\boxed{
B=I_{\mathcal H_{F2}},
\qquad
R_{\rm in}=\mathcal M_{F2}.
}
\]

The fixed input budget is initial Helmholtz free energy, not laboratory actuator energy. This does not claim arbitrary independent experimental preparation of ion and trapped-electron distribution perturbations.

The full reduced input geometry preserves both ion and trapped-electron directions from the F2.1 multichannel balance. No later objective-separation result is implied.

## Active instruction

**Status:** `F2.4 PASS — KINETIC INPUT GEOMETRY / INPUT COST FROZEN — RETURN TO MASTER`

**Next instruction:** none in this branch.

A bare `GO` must not open phase-space discretization, discrete quasineutrality/channel reconstruction, numerical/spectral qualification, GENE work or finite-time objective calculations while this status remains `RETURN TO MASTER`. MASTER must integrate F2.4 and commit any later handoff explicitly.

## Remaining pre-effect objects

Before any finite-time execution, MASTER must separately authorize and freeze, as applicable:

- structure-preserving ballooning/velocity-space discretization and quadrature;
- trapped/passing separatrix and ion turning-point treatment;
- discrete quasineutrality elimination;
- discrete Helmholtz metric and physical particle/ion-heat/electron-heat channel reconstruction;
- numerical/free-energy/balance/spectral qualification;
- later finite-time pilot specification;
- fully kinetic collisional-reference and GENE mapping details.

## Forbidden until MASTER returns a new committed handoff

Do not discretize phase space, choose cutoffs/quadrature, construct discrete `A/M/Q`, calculate spectra, propagators, Gramians, optimizers, angles or gaps, scan input subspaces or parameters, run GENE, add collisions to F2-R, retune F2.3, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Governance authority

- `research/master/fusion_f2_1_two_species_gk_balance_integration_freeze_0_1.md`
- `research/master/fusion_f2_2_geometry_convention_integration_freeze_0_1.md`
- `research/master/fusion_f2_3_physical_parameter_integration_freeze_0_1.md`
- `research/master/prompts/fusion_f2_4_kinetic_input_geometry_input_cost_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / RETURN TO MASTER.**
