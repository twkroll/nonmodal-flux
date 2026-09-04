# MASTER Project Status

**Last updated:** 2026-09-04  
**Branch:** `main`

## Global scientific savepoints

- CORE Mathematical / Integration / Interpretation freezes: **STABLE**.
- Plasma/D10-ZF Pilot 0.2: **P2-A**, frozen.
- Neuro/CMC Pilot 0.1: **NEURO-STRONG**, frozen.
- Climate-A/Phillips-QG Pilot 0.1: **CLIM-WEAK**, frozen.
- Climate-B/Bickley-jet Pilot 0.1: **CLIM-B-FAIL — resolution robustness failure**, frozen.
- Manuscript Revision 0.4: **COMPLETE — PASS**.
- First Paper Scientific Content Freeze 0.1: **STABLE — SCIENTIFIC CONTENT BASELINE FROZEN / SUBMISSION TRACK PARKED**.
- Post-Paper Scientific Roadmap Gate 0.1: **COMPLETE — FUSION-F1 SELECTED**.
- Fusion B5.5 heat-flux observable: **PASS / INTEGRATED / FROZEN**.
- Fusion F1.2 input geometry / input cost: **PASS / INTEGRATED / FROZEN**.
- Fusion F1.3 candidate / convention freeze: **PASS / INTEGRATED / FROZEN**.
- Fusion F1.3 Candidate / Convention Integration Freeze 0.1: **STABLE — F1.4 RELEASED**.

## First-paper status

Paper 1 scientific content remains frozen. Draft 0.4 is a scientific-content baseline, not final prose. Submission preparation remains parked by user choice.

## Active post-paper program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

Planned fidelity sequence:

\[
\text{anisotropic ZLR four-moment gyrofluid}
\rightarrow
\text{FLR gyrofluid}
\rightarrow
\text{parallel/flux-tube or local gyrokinetic/GENE-compatible validation}.
\]

No finite-time Fusion objective-separation effect has yet been authorized or inspected.

## Frozen Fusion candidate after F1.3

Primary reduced candidate:

\[
\boxed{\text{anisotropic-ZLR four-moment R1 minimal-curvature branch}}
\]

The slab generator is only the exact `omega_d -> 0` analytic/limiting control.

State and electrostatic closure:

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad \Phi=\mathcal C_kN,
\qquad \mathcal C_k=(\tau_i+k_\perp^2\rho_i^2)^{-1}.
\]

Positive free-energy metric and input geometry:

\[
M_k=M_k^\dagger\succ0,
\qquad B=I_4,
\qquad R_{\rm in}=M_k.
\]

Physical signed heat channel remains the B5.5 `Q_{q_i,k}`, Hermitian, rank 2 and indefinite for `k_y!=0`, with `Q_{Gamma_i,k}=0` under the frozen adiabatic-electron closure.

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

The model remains collisionless/source-faithful with no artificial damping. The point may not be retuned or damped to rescue a spectrum.

Canonical F1.3 result:

`research/fusion/fusion_candidate_convention_freeze_0_1.md`

MASTER F1.3 savepoint:

`research/master/fusion_f1_3_candidate_convention_integration_freeze_0_1.md`

F1.3 commit `956115d805bd195148bfb3071449a2fabb606ea2`; Python CI #323 = `SUCCESS`.

## Immediate next gate

Fusion F1.4 — Numerical / Spectral Qualification Gate 0.1 is the only active scientific handoff.

It must reconstruct exactly the frozen single-point matrices and verify `M`, `Q`, `B`, `R_in`, the free-energy balance, physical heat-channel reconstruction, coordinate consistency, conditioning and the complete spectrum. It may not construct finite-time objective operators or inspect optimizer separation.

If the exact frozen point is clearly unstable, the required outcome is `HOLD — SPECTRALLY UNSTABLE FROZEN POINT`; no damping or retuning is allowed.

Canonical instruction:

`research/master/prompts/fusion_numerical_spectral_qualification_gate_0_1.md`

## Planned dependency chain

1. B5.5 heat-flux observable — **COMPLETE / FROZEN**;
2. F1.2 admissible input geometry / cost — **COMPLETE / FROZEN**;
3. F1.3 candidate / convention freeze — **COMPLETE / FROZEN**;
4. F1.4 numerical / spectral qualification — **READY**;
5. targeted exact-question Fusion literature positioning — blocked pending F1.4/regime acceptance;
6. pilot specification;
7. MASTER pilot freeze and one-shot execution;
8. result integration/freeze;
9. later FLR/GK fidelity progression based on physical/structural validity, not effect size.

## Other branch states

- CORE: `STABLE / PARKED`
- MODES: `PARKED / conditional Fusion companion`
- CONT: `PARKED`
- CASCADE: `PARKED`
- Neuro: frozen first result; extensions parked
- Climate: A/B frozen; no B repair or third-candidate rescue lineage
- Literature: no active Fusion task until F1.4 returns and MASTER accepts the spectral regime
- Manuscript/submission: parked
- Power Grids: `PROTECTED`
- Photonics/Waves: `PROTECTED`
- Fusion: `F1.4 NUMERICAL / SPECTRAL QUALIFICATION READY — AWAIT GO`

## Parallelism decision

No parallel science is opened. MODES remains conditional on a later high-dimensional Fusion representation problem; CONT remains parked. The frozen R1 parameter point now exists, but continuation is not opened before the base candidate passes or is explicitly accepted after spectral qualification.

## Branch-independent / branch-dependent distinction

Branch-independent methodology remains

\[
\mathfrak C=(A,M,Q,B,R_{\rm in}).
\]

Fusion branch-dependent semantics and the exact reduced candidate/conventions are now frozen through F1.3. Only numerical/spectral qualification remains before any literature/pilot progression.

## Protected rollback chain

All first-paper savepoints remain protected. Post-paper savepoints now include:

1. Post-Paper Scientific Roadmap Gate 0.1;
2. Fusion B5.5 Integration Freeze 0.1;
3. Fusion F1.2 Input Geometry / Input-Cost Integration Freeze 0.1;
4. Fusion F1.3 Candidate / Convention Integration Freeze 0.1.

## Decision record

- base through DEC-443;
- Addendum 0.1 through DEC-486;
- Addendum 0.2 through DEC-502;
- Addendum 0.3 through DEC-510.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_numerical_spectral_qualification_gate_0_1.md`.

No finite-time effect inspection, parameter rescue, FLR/GK extension, literature audit or parallel branch work is authorized before F1.4 returns.
