# Fusion F1.3 Candidate / Convention Integration Freeze 0.1

**Date:** 2026-09-04  
**Authority:** MASTER  
**Status:** `STABLE — F1.3 CANDIDATE/CONVENTION FROZEN / F1.4 RELEASED`

## Scope

This MASTER freeze integrates only the completed Fusion F1.3 candidate/convention freeze. It performs no finite-time optimization, no effect inspection, no parameter or horizon scan, no FLR/GK extension, and no modification of the frozen first-paper content.

## Integrated F1.3 result

Canonical branch result:

`research/fusion/fusion_candidate_convention_freeze_0_1.md`

Branch verdict:

\[
\boxed{\text{F1.3 PASS — CANDIDATE/CONVENTION FROZEN — RETURN TO MASTER FOR NUMERICAL/SPECTRAL QUALIFICATION}}
\]

The primary reduced candidate is now frozen as

\[
\boxed{\text{anisotropic-ZLR four-moment R1 minimal-curvature branch}}
\]

with the slab R1 generator retained only as the exact `omega_d -> 0` analytic/limiting control.

Frozen state, closure and physical objects:

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad
\Phi=\mathcal C_kN,
\qquad
\mathcal C_k=(\tau_i+k_\perp^2\rho_i^2)^{-1},
\]

\[
M_k=M_k^\dagger\succ0,
\qquad
q_{i,k}=z_k^\dagger Q_{q_i,k}z_k,
\qquad
B=I_4,
\qquad
R_{\rm in}=M_k.
\]

The physical heat channel remains Hermitian, rank 2 and indefinite for `k_y!=0`; `Q_{Gamma_i,k}=0` remains a frozen consequence of the adiabatic-electron closure.

Frozen geometry/sign conventions use outward `+x`, `k_y>0`,

\[
L_n^{-1}=-\partial_x\ln n_0>0,
\qquad
L_T^{-1}=-\partial_x\ln T_{i0}>0,
\]

\[
\widehat{\mathcal K}f_k=-2i\omega_df_k,
\qquad
\omega_d=\frac{k_y\rho_i c_s}{R_0}>0,
\qquad
k_\parallel=\frac{1}{qR_0}>0.
\]

No artificial damping, viscosity/diffusion, Landau-fluid term, kinetic-electron response, FLR/R2 operator, six-moment GEM closure or GENE layer is included.

The unique frozen CBC-projected R1 point is

\[
\boxed{
\tau_i=1,
\quad R_0/L_n=2.2,
\quad R_0/L_T=6.9,
\quad q=1.4,
\quad k_x\rho_i=0,
\quad k_y\rho_i=0.3.
}
\]

Time normalization is

\[
\boxed{\tau_{\rm ref}=R_0/c_s.}
\]

The point is a CBC projection onto the reduced R1 model, not a claim that R1 reproduces the full CBC flux-tube geometry.

## Anti-retuning rule

The frozen parameter point may not be changed in F1.4 to obtain stability, larger nonnormality, a larger objective separation, or any preferred spectrum. No damping may be added as a spectral rescue. If the exact frozen point is spectrally unstable or otherwise fails qualification, F1.4 must report that fact and return to MASTER.

## Reproducibility

F1.3 branch commit:

`956115d805bd195148bfb3071449a2fabb606ea2`

Python CI #323 = `SUCCESS`.

## Next gate released

The next authorized scientific task is **Fusion F1.4 — Numerical / Spectral Qualification Gate 0.1**.

It must reconstruct exactly the frozen single-block R1 candidate at the frozen CBC-projected point and verify matrix identities, physical-channel reconstruction, conditioning and the complete spectrum without constructing any finite-time energy/heat objective operator or inspecting objective separation.

Canonical handoff:

`research/master/prompts/fusion_numerical_spectral_qualification_gate_0_1.md`

If the spectral abscissa is clearly positive, F1.4 must return `HOLD — SPECTRALLY UNSTABLE FROZEN POINT` rather than adding damping or retuning. MASTER will then decide explicitly whether an unstable-regime finite-time program is scientifically acceptable or whether the reduced candidate lineage should stop/redirect.

## Rollback and STOP

This file is a new post-paper rollback point after the F1.2 Integration Freeze and F1.3 branch result. It does not modify any first-paper savepoint.

**STOP — F1.3 INTEGRATED; F1.4 MAY PROCEED ONLY VIA THE COMMITTED HANDOFF.**