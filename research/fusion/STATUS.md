# Fusion Branch Status

**Last updated:** 2026-09-04  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and the submission track remains parked.

B5.5, F1.2 and F1.3 are complete and MASTER-integrated.

## Frozen F1.3 candidate / convention

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

Frozen CBC-projected R1 point:

\[
\boxed{
\tau_i=1,
\quad R_0/L_n=2.2,
\quad R_0/L_T=6.9,
\quad q=1.4,
\quad k_x\rho_i=0,
\quad k_y\rho_i=0.3,
\quad \tau_{\rm ref}=R_0/c_s.
}
\]

No artificial damping, viscosity/diffusion, Landau-fluid term, FLR/R2, kinetic electrons, six-moment GEM or GENE layer is included. The frozen point may not be retuned to rescue its spectrum or change any later effect.

Canonical F1.3 result:

`research/fusion/fusion_candidate_convention_freeze_0_1.md`

MASTER F1.3 integration freeze:

`research/master/fusion_f1_3_candidate_convention_integration_freeze_0_1.md`

F1.3 branch commit `956115d805bd195148bfb3071449a2fabb606ea2`; Python CI #323 = `SUCCESS`.

## Active instruction

**Status:** `FUSION F1.4 NUMERICAL / SPECTRAL QUALIFICATION READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_numerical_spectral_qualification_gate_0_1.md`

On a bare `GO`, first read this STATUS and execute only that committed instruction.

## F1.4 scope

Reconstruct exactly the frozen single-point minimal-curvature R1 matrices and qualify algebraic identities, physical heat-channel reconstruction, conditioning and the complete spectrum. No finite-time objective separation may be constructed or inspected.

If the frozen point is clearly spectrally unstable, return `HOLD — SPECTRALLY UNSTABLE FROZEN POINT`; do not add damping or retune. MASTER will decide whether that spectral regime is scientifically acceptable.

## Forbidden until F1.4 returns

Do not compute finite-time energy/heat objective operators, cumulative extrema, optimizer directions/subspaces, principal angles, performance gaps, horizon scans or parameter scans. Do not change the frozen point or add spectral rescue. Do not restore FLR/GK fidelity or open MODES/CONT/CASCADE, Power Grid/Photonics work, or Paper-1 submission.

## Expected return state

One of:

- `F1.4 PASS — SPECTRALLY STABLE / NUMERICALLY QUALIFIED — RETURN TO MASTER`;
- `F1.4 HOLD — MARGINAL SPECTRUM — RETURN TO MASTER`;
- `F1.4 HOLD — SPECTRALLY UNSTABLE FROZEN POINT — RETURN TO MASTER`;
- `F1.4 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Governance authority

- `research/master/first_paper_scientific_content_freeze_0_1.md`
- `research/master/post_paper_scientific_roadmap_gate_0_1.md`
- `research/master/fusion_b5_5_heat_flux_observable_integration_freeze_0_1.md`
- `research/master/fusion_f1_2_input_geometry_integration_freeze_0_1.md`
- `research/master/fusion_f1_3_candidate_convention_integration_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / AWAIT GO.**