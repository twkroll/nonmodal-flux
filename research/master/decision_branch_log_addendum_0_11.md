# MASTER Decision & Branch Log — Addendum 0.11

**Date:** 2026-09-06  
**Base continuation:** `research/master/decision_branch_log_addendum_0_10.md` through DEC-580  
**Status:** `ACTIVE CANONICAL CONTINUATION`

## Fusion F2.6 HOLD integration / ion-FLR convention resolution / F2.6 resumption

- **DEC-581:** `Fusion F2.6 — Discrete Generator / Helmholtz Metric / Physical Channel Reconstruction & Algebraic Balance Qualification Gate 0.1 = HOLD` before any spectral work — STABLE FACTUAL HOLD INTEGRATION.
- **DEC-582:** The F2.6 blocker is localized to one ion-FLR convention inconsistency: frozen local `J0i=J0(k_perp v_perp/Omega_i(theta))` was paired with a reference-`B0` polarization argument `b_i=(k_perp rho_i0)^2`; K0/K1/K2 manufactured Maxwellian checks show the discrepancy is not a quadrature/convergence error — FROZEN DIAGNOSTIC INTERPRETATION.
- **DEC-583:** F2.6 branch HOLD commit `ef5a20e728a5a6ca0dfb1cd2cd012f4003a4c0f1`; Python CI #385 = `SUCCESS` — STABLE REPRODUCIBILITY CHECK.
- **DEC-584:** MASTER selects the source-consistent local-B ion-FLR convention while preserving the existing local gyroaverage: `rho_i(theta)=rho_i0 B0/B(theta)` and `b_i(theta)=(k_perp rho_i0)^2(B0/B(theta))^2` — FROZEN FLR ERRATUM DECISION.
- **DEC-585:** The F2.3 reference normalization and benchmark remain unchanged: `rho_i0=vTi/Omega_i(B0)` and `k_y rho_i0=0.3`; the correction applies only to the local polarization/free-energy FLR argument and does not retune geometry, gradients, wavenumbers, input geometry, state-space basis, quadrature or K0/K1/K2 — FROZEN NO-RETUNING BOUNDARY.
- **DEC-586:** `Gamma0i(theta)=I0(b_i(theta)) exp[-b_i(theta)]` is henceforth required to satisfy the standard Maxwellian identity `Gamma0i=<J0i^2>_Fi0` consistently with the already-frozen local `J0i`; the alternative reference-`B0` gyroaverage is rejected — FROZEN ALGEBRA/PHYSICAL-CONSISTENCY DECISION.
- **DEC-587:** Historical F2.1/F2.3/F2.5/F2.6-0.1 files remain immutable savepoints; `research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md` supersedes only the inconsistent varying-`B` implementation reading of `b_i` and becomes the controlling downstream convention — NEW PROTECTED POST-PAPER SAVEPOINT.
- **DEC-588:** F2.6 is re-released only through `research/master/prompts/fusion_f2_6_resume_after_ion_flr_erratum_0_1.md`; the resumed branch must create versioned `0_2` result/diagnostic files and rerun all affected algebraic checks on K0/K1/K2 — ACTIVE SCIENTIFIC HANDOFF.
- **DEC-589:** Spectra/eigenvalues/pseudospectra, propagators/Gramians/cumulative objectives, optimizers/angles/gaps, parameter scans, GENE, damping/collisions and any F2.3/F2.4/F2.5 retuning remain forbidden until F2.6 returns again — FROZEN PRE-SPECTRAL BOUNDARY.
- **DEC-590:** Fusion remains the only active scientific branch; Literature, MODES, CONT, CASCADE and CORE 0.2 remain parked; Power Grid/Photonics remain protected; Paper-1 submission remains parked — ACTIVE / FROZEN PARALLELISM RULE.
