# MASTER Decision & Branch Log — Addendum 0.8

**Date:** 2026-09-05  
**Base continuation:** `research/master/decision_branch_log_addendum_0_7.md` through DEC-550  
**Status:** `ACTIVE CANONICAL CONTINUATION`

## Fusion F2.3 integration / F2.4 release

- **DEC-551:** `Fusion F2.3 — Physical Geometry / Gradient / Wavenumber Parameter Freeze 0.1 = PASS` — STABLE PRE-EFFECT SCIENTIFIC SAVEPOINT.
- **DEC-552:** The single F2-R physical point is frozen as CBC-compatible large-aspect-ratio circular `s-alpha` geometry with `R0/a=2.77778`, `r0/a=0.5`, `epsilon=0.18`, `q=1.4`, `shat=0.8`, `alpha_MHD=0`, deuterium/electron `mi/me=3672`, `Ti/Te=1`, equal densities, `a/Ln=0.8`, `a/LTi=a/LTe=2.49`, `ky rho_i=+0.3`, `theta0=0`, `kx0=0` — FROZEN SINGLE PHYSICAL POINT.
- **DEC-553:** F2.3 normalization is frozen as `vTi=sqrt(Ti/mi)`, `rho_i=vTi/Omega_i`, `tau_ref=R0/vTi`; equivalent major-radius gradients are `R0/Ln=2.222224`, `R0/LTi=R0/LTe=6.9166722` — FROZEN NORMALIZATION/GRADIENT CONVENTION.
- **DEC-554:** All three continuous F2.1 supply coefficients are nonzero at the frozen point, while no claim is made that later discrete channel operators are linearly independent or yield optimizer separation — FROZEN INTERPRETATION BOUNDARY.
- **DEC-555:** The trapped-electron interval and local trapped pitch fraction follow from the frozen geometry rather than being independent knobs; the reduced-electron `k_perp rho_e << 1` ordering is plausible at the ballooning centre but must be rechecked on the retained numerical support — STABLE ORDERING/ANTI-RETUNING RULE.
- **DEC-556:** F2.3 branch commit `fcd012219427ce0243151d2cfb7796236778d966`; Python CI #362 = `SUCCESS` — STABLE REPRODUCIBILITY CHECK.
- **DEC-557:** `Fusion F2.3 Physical-Parameter Integration Freeze 0.1 = STABLE — F2.3 PHYSICAL POINT FROZEN / F2.4 KINETIC INPUT-GEOMETRY GATE RELEASED` — NEW POST-PAPER ROLLBACK POINT.
- **DEC-558:** MASTER orders the kinetic admissible-input geometry / input-cost freeze before phase-space discretization, because discretization must inherit rather than define the physical admissible state space and fixed initial budget — ACTIVE GATE-ORDER DECISION.
- **DEC-559:** Next authorized task = `Fusion F2.4 — Kinetic Admissible Input Geometry / Input-Cost Freeze 0.1`. It must derive continuous `(B,R_in)` from physical admissibility and Helmholtz/preparation-cost semantics only, and may not impose transport neutrality, parity reduction, effect-guided subspaces, discretization, spectral calculations or finite-time objectives — ACTIVE SCIENTIFIC HANDOFF.
- **DEC-560:** Canonical F2.4 handoff = `research/master/prompts/fusion_f2_4_kinetic_input_geometry_input_cost_freeze_0_1.md`. Fusion remains the only active scientific branch; Literature/MODES/CONT/CASCADE wait; Power Grid/Photonics remain protected; Paper-1 submission remains parked — ACTIVE / FROZEN PARALLELISM RULE.
