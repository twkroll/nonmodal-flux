# MASTER Decision & Branch Log — Addendum 0.17

**Date:** 2026-09-07  
**Base continuation:** `research/master/decision_branch_log_addendum_0_16.md` through DEC-640  
**Status:** `ACTIVE CANONICAL CONTINUATION`

## Fusion F2.6B PASS integration / executable-operator freeze / F2.7 0_2 release

- **DEC-641:** `Fusion F2.6B — Source-Level Matrix-Free Operator Implementation Freeze / Algebraic Requalification Gate 0.1 = PASS` before any spectral or finite-time work — STABLE FACTUAL RESULT INTEGRATION.
- **DEC-642:** F2.6B is a new provenance-clean executable realization of the unchanged frozen F2-R model/numerical architecture and does **not** claim source identity with historical F2.6 `0_3`; historical F2.6 `0_3`, F2.6A HOLD and F2.7 `0_1` HOLD remain immutable audit records — FROZEN PROVENANCE BOUNDARY.
- **DEC-643:** The canonical downstream generalized-operator interface is frozen as `build_operator(level)`, `apply_E(op,x)`, `apply_F(op,x)`, `solve_E(op,x)` with NumPy C-order state layout ion `h_i[theta,u,zeta]` followed by trapped-electron `h_e[well,energy,lambda]`; total dimensions are `18608 / 93204 / 361152` on K0/K1/K2 — FROZEN SOURCE-LEVEL IMPLEMENTATION SPECIFICATION.
- **DEC-644:** The repaired `N_mu=16/24/40` ladder and every F2.1–F2.5R physical/numerical object remain unchanged; the F2.6B implementation passes full-support FLR, quasineutrality, positive metric, conservative adjoint/skew structure, independently reconstructed physical-channel Hermiticity, ambipolarity and complete F2.1 balance on K0/K1/K2 — FROZEN UPSTREAM-INTEGRITY / ALGEBRAIC REQUALIFICATION RESULT.
- **DEC-645:** F2.6B complete-balance maximum relative residuals are approximately `1.29e-13 / 5.64e-13 / 5.87e-13`; deterministic regression metadata and hashes are committed; no spectral or finite-time quantity entered the implementation/requalification — FROZEN PRE-SPECTRAL QUALIFICATION RESULT.
- **DEC-646:** F2.6B branch commit `83f004412183d43a1653d3a3a2f9ad104482de7d`; Python CI #433 = `SUCCESS` — STABLE REPRODUCIBILITY CHECK.
- **DEC-647:** `Fusion F2.6B Source-Level Operator PASS Integration Freeze 0.1 = STABLE — F2.6B PASS INTEGRATED / SOURCE-LEVEL OPERATOR FROZEN / F2.7 0_2 RELEASED` — NEW PROTECTED POST-PAPER SAVEPOINT.
- **DEC-648:** All downstream numerical work must use the committed F2.6B source-level realization unless MASTER explicitly opens a new version; no future result may be attributed to the unrecoverable historical F2.6 `0_3` source realization — FROZEN DOWNSTREAM-PROVENANCE RULE.
- **DEC-649:** MASTER releases `F2.7 0_2 — Numerical / Spectral Qualification on the F2.6B Source-Level Operator` solely to determine the rightmost spectrum/spectral abscissa with residual certification, independent numerical repetition and K0/K1/K2 robustness. A robustly unstable point is reported without rescue; marginal/indeterminate returns HOLD. No propagator/Gramian/cumulative-objective/optimizer/angle/gap work is authorized — FROZEN SPECTRAL-GATE BOUNDARY.
- **DEC-650:** Canonical next handoff = `research/master/prompts/fusion_f2_7_rerun_on_f2_6b_source_operator_0_1.md`. Fusion remains the sole active scientific branch; Literature/MODES/CONT/CASCADE/CORE 0.2 remain parked; Power Grid/Photonics remain protected; Paper-1 submission remains parked. MASTER must explicitly accept the F2.7 spectral regime before any finite-time pilot specification — ACTIVE HANDOFF / PARALLELISM RULE.
