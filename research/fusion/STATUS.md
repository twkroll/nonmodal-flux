# Fusion Branch Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and the submission track remains parked.

B5.5, F1.2, F1.3 and F1.4 are complete. MASTER has integrated F1.4 and redirected the next task to the Literature branch.

## Frozen R1 lineage

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

Frozen physical/input objects:

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

## F1.4 integrated result

Canonical branch result:

`research/fusion/fusion_numerical_spectral_qualification_gate_0_1.md`

Transparent reproduction code:

`research/fusion/fusion_numerical_spectral_qualification_0_1.py`

Branch verdict:

\[
\boxed{\text{F1.4 HOLD — MARGINAL SPECTRUM — RETURN TO MASTER}}
\]

All algebraic/physical reconstruction checks passed. The complete dimensionless spectrum is purely imaginary with four distinct eigenvalues, so the frozen R1 point is marginal and diagonalizable, not asymptotically stable and not clearly unstable.

F1.4 commit `f2562061e79c67a5ccdc6a3d809ae0f655594319`; Python CI #330 = `SUCCESS`.

MASTER integration freeze:

`research/master/fusion_f1_4_marginal_structural_integration_freeze_0_1.md`

## Structural R1 consequence

Because the frozen collisionless R1 balance contains no dissipation term,

\[
\widetilde A^\dagger M_k+M_k\widetilde A
=2\frac{R_0}{L_T}\widehat Q_q,
\]

and because F1.2 froze

\[
B=I_4,\qquad R_{\rm in}=M_k,
\]

the standard CORE integral identity gives

\[
2\frac{R_0}{L_T}K_q(T)=\mathcal E_M(T)-I.
\]

Therefore cumulative signed ion-heat optimization and final free-energy optimization are affinely equivalent at every horizon for this R1 lineage. Their optimizer eigenspaces cannot provide the intended objective-nonredundancy demonstration.

This is a structural balance consequence, not a finite-time effect calculation.

## Current branch status

**Status:** `F1.4 MASTER-INTEGRATED — R1 STRUCTURAL CONTROL FROZEN / R1 OBJECTIVE-SEPARATION PILOT BLOCKED / WAIT LITERATURE AUDIT`

**Next instruction:** none in this branch.

A bare `GO` must not open a new Fusion task while this status remains `WAIT LITERATURE AUDIT`.

The active cross-branch handoff is:

`research/master/prompts/fusion_r1_structural_redundancy_fidelity_breaking_literature_audit_0_1.md`

and must be executed in `80 – LIT – Literatur & Lernpfad`.

## Forbidden until MASTER returns a new Fusion handoff

Do not compute finite-time energy/heat objective operators, cumulative extrema, optimizer directions/subspaces, principal angles, performance gaps, horizon dependence or transient-growth curves. Do not retune R1 or add damping/collisions/closure terms. Do not restore FLR/R2, kinetic electrons, six-moment GEM or GENE. Do not open MODES/CONT/CASCADE, Power Grid/Photonics work, or modify the frozen first paper.

**STOP / WAIT LITERATURE AUDIT.**