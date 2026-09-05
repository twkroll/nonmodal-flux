# MASTER Project Status

**Last updated:** 2026-09-05  
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
- Fusion F1.2 input geometry / cost: **PASS / INTEGRATED / FROZEN**.
- Fusion F1.3 candidate / convention: **PASS / INTEGRATED / FROZEN**.
- Fusion F1.4 numerical / spectral qualification: **HOLD — MARGINAL SPECTRUM / INTEGRATED**.
- Fusion F1.4 Marginal / Structural Integration Freeze 0.1: **STABLE — R1 STRUCTURAL CONTROL FROZEN / R1 OBJECTIVE-SEPARATION PILOT BLOCKED / LIT AUDIT RELEASED**.

## First-paper status

Paper 1 scientific content remains frozen. Draft 0.4 is a scientific-content baseline, not final prose. Submission preparation remains parked by user choice.

## Active post-paper program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

The current scientific question has sharpened from “does R1 show objective separation?” to “which physically necessary fidelity additions first make free-energy and signed heat-transport objectives non-affine?”

## Qualified R1 baseline

The frozen primary R1 candidate is the anisotropic-ZLR four-moment minimal-curvature branch at

\[
\tau_i=1,
\quad R_0/L_n=2.2,
\quad R_0/L_T=6.9,
\quad q=1.4,
\quad k_x\rho_i=0,
\quad k_y\rho_i=0.3,
\quad \tau_{\rm ref}=R_0/c_s.
\]

F1.4 reconstructed the exact single-point matrices and passed all required metric/channel/balance/coordinate/conditioning checks. The complete spectrum is purely imaginary with four distinct eigenvalues, confirmed independently by exact-rational/high-precision reproduction. The point is marginal and diagonalizable.

F1.4 branch commit `f2562061e79c67a5ccdc6a3d809ae0f655594319`; Python CI #330 = `SUCCESS`.

## Structural R1 no-go result

For the frozen collisionless one-channel R1 balance,

\[
\widetilde A^\dagger M_k+M_k\widetilde A
=2\frac{R_0}{L_T}\widehat Q_q,
\]

with

\[
B=I_4,\qquad R_{\rm in}=M_k,
\]

and no dissipation term, the already-frozen CORE integral identity gives

\[
2\frac{R_0}{L_T}K_q(T)=\mathcal E_M(T)-I.
\]

Thus cumulative signed ion-heat transport and final free-energy optimization are affinely equivalent for every horizon and have identical optimizer eigenspaces. The R1 finite-time objective-separation pilot is therefore blocked as structurally redundant, not because an unfavorable numerical effect was observed.

R1 is retained as a no-go / structural-collapse baseline for the fidelity ladder.

Canonical MASTER savepoint:

`research/master/fusion_f1_4_marginal_structural_integration_freeze_0_1.md`

## Immediate next task

The next authorized task is

**Fusion R1 Structural Redundancy & Fidelity-Breaking Literature Audit 0.1**

in the Literature branch.

Its purpose is to determine how the R1 structural-collapse result sits in the gyrofluid/gyrokinetic literature and which physically justified additions alter the free-energy balance through independent supply channels and/or positive dissipation. The audit must not select models because they are expected to produce large optimizer separation.

Canonical instruction:

`research/master/prompts/fusion_r1_structural_redundancy_fidelity_breaking_literature_audit_0_1.md`

## Revised dependency chain

1. B5.5 heat-flux observable — **COMPLETE / FROZEN**;
2. F1.2 input geometry / cost — **COMPLETE / FROZEN**;
3. F1.3 candidate / convention — **COMPLETE / FROZEN**;
4. F1.4 numerical / spectral qualification — **COMPLETE / MARGINAL / INTEGRATED**;
5. R1 structural affine-equivalence consequence — **FROZEN / R1 PILOT BLOCKED**;
6. targeted structural-redundancy / fidelity-breaking literature audit — **READY**;
7. MASTER higher-fidelity gate selection from physics/balance completeness;
8. only then higher-fidelity candidate derivation/qualification;
9. finite-time execution only after a later pre-effect pilot freeze.

## Other branch states

- CORE: `STABLE / PARKED`
- Fusion: `WAIT LITERATURE AUDIT`
- Literature: `ACTIVE NEXT HANDOFF`
- MODES: `PARKED / conditional Fusion companion`
- CONT: `PARKED`
- CASCADE: `PARKED`
- Neuro: frozen first result; extensions parked
- Climate: A/B frozen; no B repair or third-candidate rescue lineage
- Manuscript/submission: parked
- Power Grids: `PROTECTED`
- Photonics/Waves: `PROTECTED`

## Parallelism decision

No additional scientific branch is opened in parallel. MODES remains conditional on a later high-dimensional representation issue. CONT remains parked despite the existence of a frozen R1 point because continuation cannot resolve the exact one-channel balance equivalence and would be premature before the fidelity audit.

## Branch-independent / branch-dependent distinction

Branch-independent CORE balance identity supplies the affine-equivalence criterion when `D=0`, `B=I`, `R_in=M`, and the Hermitian injection is exhausted by one physical channel.

Fusion branch-dependent content is the R1 realization of those conditions: the physical ion-heat channel, adiabatic-electron closure, full-state input geometry, collisionless balance and marginal CBC-projected point.

## Protected rollback chain

All first-paper savepoints remain protected. Post-paper savepoints now include:

1. Post-Paper Scientific Roadmap Gate 0.1;
2. Fusion B5.5 Integration Freeze 0.1;
3. Fusion F1.2 Input Geometry / Input-Cost Integration Freeze 0.1;
4. Fusion F1.3 Candidate / Convention Integration Freeze 0.1;
5. Fusion F1.4 Marginal / Structural Integration Freeze 0.1.

## Decision record

- base through DEC-443;
- Addendum 0.1 through DEC-486;
- Addendum 0.2 through DEC-502;
- Addendum 0.3 through DEC-510;
- Addendum 0.4 through DEC-520.

## Current next action

In `80 – LIT – Literatur & Lernpfad`, issue bare `GO`. The branch must read `research/literature/STATUS.md` and execute only `research/master/prompts/fusion_r1_structural_redundancy_fidelity_breaking_literature_audit_0_1.md`.

No R1 finite-time optimizer calculation, parameter rescue, FLR/GK execution, MODES/CONT/CASCADE work, protected collaboration work or Paper-1 submission reactivation is authorized before the literature audit returns.
