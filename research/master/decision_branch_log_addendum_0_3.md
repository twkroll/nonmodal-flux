# MASTER Decision & Branch Log — Addendum 0.3

**Date:** 2026-09-04  
**Base continuation:** `research/master/decision_branch_log_addendum_0_2.md` through DEC-502  
**Status:** `ACTIVE CANONICAL CONTINUATION`

## Fusion F1.3 integration / F1.4 release

- **DEC-503:** `Fusion F1.3 — Candidate / Convention Freeze 0.1 = PASS — CANDIDATE/CONVENTION FROZEN` — STABLE PRE-EFFECT SCIENTIFIC SAVEPOINT.
- **DEC-504:** Primary reduced candidate is the anisotropic-ZLR four-moment R1 minimal-curvature branch; the slab R1 generator remains only the exact `omega_d -> 0` analytic/limiting control — FROZEN CANDIDATE ROLE.
- **DEC-505:** Frozen CBC-projected R1 point is `tau_i=1`, `R0/L_n=2.2`, `R0/L_T=6.9`, `q=1.4`, `k_x rho_i=0`, `k_y rho_i=0.3`, with `tau_ref=R0/c_s`, `k_y>0`, `k_parallel=1/(qR0)>0`, and the previously frozen curvature/gradient sign conventions — STABLE PRE-EFFECT PARAMETER/CONVENTION FREEZE.
- **DEC-506:** The F1.3 dissipation/closure choice is collisionless and source-faithful: no artificial damping, viscosity/diffusion, Landau-fluid term, kinetic-electron response, FLR/R2 restoration, six-moment GEM or GENE layer is added. The frozen point may not be retuned or damped to rescue the spectrum or later effect — FROZEN ANTI-RETUNING RULE.
- **DEC-507:** F1.3 branch commit `956115d805bd195148bfb3071449a2fabb606ea2`; Python CI #323 = `SUCCESS` — STABLE REPRODUCIBILITY CHECK.
- **DEC-508:** `Fusion F1.3 Candidate / Convention Integration Freeze 0.1 = STABLE — F1.3 CANDIDATE/CONVENTION FROZEN / F1.4 RELEASED` — NEW POST-PAPER ROLLBACK POINT.
- **DEC-509:** Next authorized task = `Fusion F1.4 — Numerical / Spectral Qualification Gate 0.1`. It may reconstruct the exact frozen matrices, verify algebraic/balance/physical-channel identities, conditioning and complete spectrum, but may not construct or inspect finite-time objective separation — ACTIVE SCIENTIFIC HANDOFF.
- **DEC-510:** If the exact frozen point is clearly spectrally unstable, F1.4 must return `HOLD — SPECTRALLY UNSTABLE FROZEN POINT`; no damping or parameter retuning is allowed. Canonical handoff is `research/master/prompts/fusion_numerical_spectral_qualification_gate_0_1.md`. No parallel MODES/CONT/CASCADE or protected collaboration work is opened before F1.4 returns — ACTIVE / FROZEN PARALLELISM RULE.
