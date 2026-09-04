# MASTER Status

**Last updated:** 2026-09-04  
**Branch:** `main`

## Current state

All first-paper savepoints remain intact and the submission track remains parked by user choice. Post-paper science is active only in Fusion.

Stable first-paper lineage:

- CORE Mathematical / Integration / Interpretation freezes: `STABLE`;
- Plasma/D10-ZF: `P2-A`, `FROZEN`;
- Neuro/CMC: `NEURO-STRONG`, `FROZEN`;
- Climate-A: `CLIM-WEAK`, `FROZEN`;
- Climate-B: `CLIM-B-FAIL — resolution robustness failure`, `RESULT FROZEN`;
- Manuscript Revision 0.4: `COMPLETE — PASS`;
- Submission Readiness Gate 0.1: `PASS WITH AUTHOR/METADATA ITEMS — SCIENTIFIC PACKAGE READY`;
- First Paper Scientific Content Freeze 0.1: `STABLE — SCIENTIFIC CONTENT BASELINE FROZEN / SUBMISSION TRACK PARKED`.

Post-paper Fusion lineage:

- Post-Paper Scientific Roadmap Gate 0.1: `COMPLETE — FUSION-F1 SELECTED`;
- B5.5 physical ion heat-flux observable: `PASS / MASTER-INTEGRATED`;
- F1.2 admissible input geometry / cost: `PASS / MASTER-INTEGRATED`;
- F1.3 candidate / convention freeze: `PASS / MASTER-INTEGRATED`;
- F1.3 Candidate / Convention Integration Freeze 0.1: `STABLE — F1.4 RELEASED`.

## Frozen F1.3 candidate

Primary reduced candidate:

\[
\boxed{\text{anisotropic-ZLR four-moment R1 minimal-curvature branch}}
\]

with slab R1 only as the exact `omega_d -> 0` analytic/limiting control.

Frozen state/closure/physical objects:

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad \Phi=\mathcal C_kN,
\qquad M_k=M_k^\dagger\succ0,
\]

\[
q_{i,k}=z_k^\dagger Q_{q_i,k}z_k,
\qquad B=I_4,
\qquad R_{\rm in}=M_k.
\]

Frozen CBC-projected point:

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

No artificial damping or spectral rescue is allowed. The point may not be retuned if the exact spectrum is unstable.

Canonical F1.3 result:

`research/fusion/fusion_candidate_convention_freeze_0_1.md`

MASTER integration freeze:

`research/master/fusion_f1_3_candidate_convention_integration_freeze_0_1.md`

F1.3 branch commit `956115d805bd195148bfb3071449a2fabb606ea2`; Python CI #323 = `SUCCESS`.

## Parallelism / parked branches

No parallel scientific branch is active.

- `MODES`: parked / conditional Fusion companion later;
- `CONT`: parked until a physical parameter family is scientifically needed;
- `CASCADE`: parked;
- `CORE 0.2`: parked;
- Neuro and higher-fidelity Climate: parked;
- Power Grids and Photonics/Waves: `PROTECTED`;
- Paper-1 submission: parked.

## Selected dependency chain

1. B5.5 physical ion heat-flux derivation — **COMPLETE / FROZEN**;
2. F1.2 admissible input geometry / cost — **COMPLETE / FROZEN**;
3. F1.3 candidate / convention freeze — **COMPLETE / FROZEN**;
4. F1.4 numerical / spectral qualification — **READY**;
5. targeted exact-question Fusion literature audit — blocked until F1.4 returns and MASTER accepts the regime;
6. pilot specification;
7. MASTER pilot freeze / one-shot execution;
8. result freeze;
9. later FLR/GK fidelity progression by physical validity, not effect size.

## Decision record

- base log through DEC-443;
- Addendum 0.1 through DEC-486;
- Addendum 0.2 through DEC-502;
- Addendum 0.3 through DEC-510.

## Rollback points

The protected post-paper rollback chain is now

\[
\text{Post-Paper Roadmap}
\rightarrow
\text{B5.5 Integration Freeze}
\rightarrow
\text{F1.2 Input Geometry Integration Freeze}
\rightarrow
\boxed{\text{F1.3 Candidate / Convention Integration Freeze}}.
\]

All first-paper savepoints remain separately protected.

## Active instruction

**Status:** `FUSION F1.3 INTEGRATED — F1.4 NUMERICAL / SPECTRAL QUALIFICATION READY / AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Branch status:**

`research/fusion/STATUS.md`

**Next instruction:**

`research/master/prompts/fusion_numerical_spectral_qualification_gate_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

If the exact frozen point is clearly unstable, the branch must return `HOLD — SPECTRALLY UNSTABLE FROZEN POINT`; it must not add damping or retune.

## STOP boundary

Do not perform finite-time Fusion objective optimization, horizon/parameter scans, FLR/GK extensions, literature positioning, pilot specification, or parallel branch work before F1.4 returns. Do not reactivate submission work unless explicitly requested.

**STOP — AWAIT FUSION `GO`.**