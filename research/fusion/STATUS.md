# Fusion Branch Status

**Last updated:** 2026-09-04  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and the submission track remains parked.

B5.5 and F1.2 are complete and MASTER-integrated. F1.3 is now complete in this branch.

## F1.3 frozen candidate / convention

Primary reduced candidate:

\[
\boxed{\text{anisotropic-ZLR four-moment R1 minimal-curvature branch}}
\]

with the slab R1 generator retained only as the exact `omega_d -> 0` analytic/limiting control.

Frozen state and closure:

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad
\Phi=\mathcal C_kN,
\qquad
\mathcal C_k=(\tau_i+k_\perp^2\rho_i^2)^{-1}.
\]

Frozen physical objects:

\[
M_k=M_k^\dagger\succ0,
\qquad
q_{i,k}=z_k^\dagger Q_{q_i,k}z_k,
\qquad
B=I_4,
\qquad
R_{\rm in}=M_k.
\]

The physical heat channel remains Hermitian, rank 2 and indefinite for `k_y!=0`; the ion particle-flux channel remains `Q_{Gamma_i,k}=0` under the frozen adiabatic-electron closure.

Frozen gradient/geometry conventions use outward `+x`, `k_y>0`,

\[
L_n^{-1}=-\partial_x\ln n_0>0,
\qquad
L_T^{-1}=-\partial_x\ln T_{i0}>0,
\]

\[
\widehat{\mathcal K}f_k=-2i\omega_df_k,
\qquad
\omega_d=\frac{k_y\rho_ic_s}{R_0}>0,
\qquad
k_\parallel=\frac{1}{qR_0}>0.
\]

The dissipation/closure choice is source-faithful and collisionless: no artificial damping, viscosity/diffusion or Landau-fluid term is added; electrons remain adiabatic.

Frozen CBC-projected R1 parameter point:

\[
\boxed{
\tau_i=1,
\quad
R_0/L_n=2.2,
\quad
R_0/L_T=6.9,
\quad
q=1.4,
\quad
k_x\rho_i=0,
\quad
k_y\rho_i=0.3.
}
\]

Time normalization:

\[
\boxed{\tau_{\rm ref}=R_0/c_s.}
\]

Canonical F1.3 result:

`research/fusion/fusion_candidate_convention_freeze_0_1.md`

## Active instruction

**Status:** `F1.3 PASS — CANDIDATE/CONVENTION FROZEN — RETURN TO MASTER FOR NUMERICAL/SPECTRAL QUALIFICATION`

**Next instruction:** none in this branch.

A bare `GO` must not open F1.4 while this status remains `RETURN TO MASTER`. MASTER must integrate F1.3 and commit a new explicit handoff before further Fusion work.

## Forbidden until MASTER returns a new committed handoff

Do not compute finite-time energy/heat operators, propagators/Gramians for objective comparison, cumulative extrema, optimizer vectors/subspaces, principal angles, performance gaps, horizon dependence or effect-guided parameter scans. Do not retune the frozen CBC-projected point or add damping to rescue a spectrum. Do not restore FLR/R2, kinetic electrons, six-moment GEM or GENE. Do not open MODES/CONT/CASCADE, Power Grid/Photonics work, or modify the frozen first paper.

## Expected MASTER action

If MASTER accepts the F1.3 freeze, the roadmap-designated next stage is numerical/spectral qualification of exactly the frozen candidate and point. This branch does not self-authorize that gate.

## Governance authority

- `research/master/first_paper_scientific_content_freeze_0_1.md`
- `research/master/post_paper_scientific_roadmap_gate_0_1.md`
- `research/master/fusion_b5_5_heat_flux_observable_integration_freeze_0_1.md`
- `research/master/fusion_f1_2_input_geometry_integration_freeze_0_1.md`
- `research/master/prompts/fusion_candidate_convention_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / RETURN TO MASTER.**
