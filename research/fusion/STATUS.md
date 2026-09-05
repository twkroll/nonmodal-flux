# Fusion Branch Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit, F2.1, F2.2 and F2.3 are complete and MASTER-integrated.

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

Canonical result:

`research/fusion/fusion_f2_3_physical_parameter_freeze_0_1.md`

MASTER integration freeze:

`research/master/fusion_f2_3_physical_parameter_integration_freeze_0_1.md`

Frozen point:

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

Normalization:

\[
v_{Ti}=\sqrt{T_i/m_i},
\qquad
\rho_i=v_{Ti}/\Omega_i,
\qquad
\tau_{\rm ref}=R_0/v_{Ti}.
\]

All three continuous supply coefficients are nonzero at this point, but this does not establish later discrete channel independence or optimizer separation.

F2.3 branch commit `fcd012219427ce0243151d2cfb7796236778d966`; Python CI #362 = `SUCCESS`.

## Active instruction

**Status:** `FUSION F2.4 KINETIC INPUT GEOMETRY / INPUT-COST FREEZE READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_f2_4_kinetic_input_geometry_input_cost_freeze_0_1.md`

On bare `GO`, first read this STATUS and execute only that committed instruction.

## F2.4 scope

Freeze the continuous physical initial-condition pair `(B,R_in)` before any discretization. Determine whether the full finite-free-energy F2-R tangent space is physically admissible or whether exact local-GK/quasineutrality/invariant constraints require a proper subspace. Evaluate `B=I` and `R_in=M_F2` only on physical grounds; do not force them.

## Forbidden until F2.4 returns

Do not discretize phase space, choose ballooning cutoffs/quadrature, construct discrete `A/M/Q`, calculate spectra, propagators, Gramians, optimizers, angles or gaps, scan input subspaces, run GENE, add collisions to F2-R, retune F2.3, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Expected return

One of:

- `F2.4 PASS — KINETIC INPUT GEOMETRY / INPUT COST FROZEN — RETURN TO MASTER`;
- `F2.4 HOLD — PHYSICAL INPUT-SPACE DECISION REQUIRED — RETURN TO MASTER`;
- `F2.4 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

**STOP / AWAIT GO.**
