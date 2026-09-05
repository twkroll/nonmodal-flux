# Fusion Branch Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and the submission track remains parked.

B5.5, F1.2 and F1.3 are complete and MASTER-integrated. F1.4 numerical/spectral qualification is now complete in this branch.

## Frozen F1.3 candidate

Primary reduced candidate:

\[
\boxed{\text{anisotropic-ZLR four-moment R1 minimal-curvature branch}}
\]

with slab retained only as the exact `omega_d -> 0` analytic control.

Frozen point:

\[
\tau_i=1,
\quad R_0/L_n=2.2,
\quad R_0/L_T=6.9,
\quad q=1.4,
\quad k_x\rho_i=0,
\quad k_y\rho_i=0.3,
\quad \tau_{\rm ref}=R_0/c_s.
\]

Frozen physical/input objects remain

\[
M_k=M_k^\dagger\succ0,
\qquad
q_{i,k}=z_k^\dagger Q_{q_i,k}z_k,
\qquad
B=I_4,
\qquad
R_{\rm in}=M_k.
\]

No artificial damping or spectral rescue is allowed.

## F1.4 qualification result

Canonical result:

`research/fusion/fusion_numerical_spectral_qualification_gate_0_1.md`

Transparent single-point reproduction code:

`research/fusion/fusion_numerical_spectral_qualification_0_1.py`

The exact frozen dimensionless matrix passes all required algebraic and physical reconstruction checks:

- `M_k` Hermitian positive definite;
- `Q_q` Hermitian, rank 2, signature `(1,1,2)`;
- `rank(B)=4`, `R_in=M_k` positive definite;
- free-energy balance residual at roundoff;
- source-free minimal-curvature/parallel part `M_k`-skew-adjoint at roundoff;
- deterministic heat-flux cross-phase reconstruction at roundoff;
- coordinate congruence verified;
- implementation conditioning acceptable for the 4x4 block.

The complete dimensionless spectrum is

\[
\lambda\tau_{\rm ref}
\approx
\{-3.592939609690i,\,-1.563190668779i,\,-0.276482492169i,\,+0.076649467886i\}.
\]

With scale-aware tolerance

\[
\varepsilon_{\rm spec}=1.0850\times10^{-13},
\]

the computed spectral abscissa is

\[
\alpha(\widetilde A)=7.34\times10^{-17},
\]

and an independent exact-rational/high-precision reproduction confirms four distinct purely imaginary eigenvalues.

Therefore the frozen point is **marginal**, not asymptotically stable and not clearly unstable.

## Active instruction

**Status:** `F1.4 HOLD — MARGINAL SPECTRUM — RETURN TO MASTER`

**Next instruction:** none in this branch.

A bare `GO` must not open a literature audit, pilot specification, finite-time objective calculation or any new Fusion gate while this status remains `RETURN TO MASTER`. MASTER must explicitly decide whether the marginal conservative regime is scientifically acceptable and commit any later handoff.

## Forbidden until MASTER returns a new committed handoff

Do not compute finite-time energy/heat objective operators, propagator/Gramian objectives, cumulative extrema, optimizer directions/subspaces, principal angles, performance gaps, horizon dependence, transient-growth curves or parameter scans. Do not retune the frozen point or add damping/collisions/closure terms to obtain stability. Do not restore FLR/R2, kinetic electrons, six-moment GEM or GENE. Do not open MODES/CONT/CASCADE, Power Grid/Photonics work, or modify the frozen first paper.

## Governance authority

- `research/master/first_paper_scientific_content_freeze_0_1.md`
- `research/master/post_paper_scientific_roadmap_gate_0_1.md`
- `research/master/fusion_b5_5_heat_flux_observable_integration_freeze_0_1.md`
- `research/master/fusion_f1_2_input_geometry_integration_freeze_0_1.md`
- `research/master/fusion_f1_3_candidate_convention_integration_freeze_0_1.md`
- `research/master/prompts/fusion_numerical_spectral_qualification_gate_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / RETURN TO MASTER.**
