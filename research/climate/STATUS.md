# Climate/Ocean Branch Status

**Last updated:** 2026-09-03  
**Branch:** `main`

## Climate-A — existing frozen pilot

Climate-A remains the damped two-layer Phillips-QG heat-transport pilot.

- Feasibility Gate 0.1: `PASSED`.
- Candidate Freeze 0.1: `STABLE`.
- Numerical Qualification 0.1: `QUALIFIED`.
- Pilot Specification 0.1: `COMPLETE`.
- Pilot Execution 0.1: `COMPLETE`.
- Frozen verdict: `CLIM-WEAK`.

At `T/tau_ref=8`,

\[
(|m|,n)_E=(3,2),\qquad (|m|,n)_{\rm heat}=(4,2),
\]

\[
\vartheta_{\rm sub}=90^\circ,\qquad \Delta_{\rm heat}=0.04118455338,
\]

so the energy-optimal subspace retains approximately 95.88% of maximum cumulative poleward heat transport.

Climate-A is permanently frozen against retuning, replacement, or relabeling.

## Climate-B — one-shot intra-domain contrast branch

- Climate Intra-Domain Contrast Feasibility Gate 0.1: `PASSED`.
- Climate Intra-Domain Contrast Candidate Freeze 0.1: `STABLE`.
- Climate Intra-Domain Contrast Numerical Qualification 0.1: `QUALIFIED`.
- Climate Intra-Domain Contrast Pilot Specification 0.1: `COMPLETE`.
- **Climate Intra-Domain Contrast Pilot Freeze 0.1: `STABLE — EXECUTION RELEASED`.**

Frozen candidate:

\[
\boxed{\text{equivalent-barotropic midlatitude Bickley jet}}
\]

with

- `M_K` = barotropic perturbation kinetic-energy metric;
- `Q_shift,K` = signed eddy-induced forcing of the infinitesimal poleward jet-translation coordinate;
- translation tangent `g(y)=-U'(y)`;
- `B=I`, `R_in=M_K`;
- `beta=1.6e-11 m^-1 s^-1`, `U0=20 m/s`, `L=1000 km`, `r=(10 d)^-1`;
- `Lx=20000 km`, `Ly=10000 km`;
- `tau_ref=L/U0=50000 s=0.5787037037 d`;
- positive zonal Fourier modes plus centered meridional sine Galerkin basis with exact conjugate real-field reconstruction;
- frozen resolution roles `(8,16)` smoke, `(12,24)` coarse, `(16,32)` primary, `(20,40)` confirmation, `(24,48)` high audit.

Numerical Qualification established robust spectral stability on the full frozen ladder,

\[
\alpha(A_K)=-0.05787037037037=-0.1\,\mathrm d^{-1}<0,
\]

with all frozen structural/channel/quadrature/parity/sign-witness/eigenpair gates passing.

Pilot Specification 0.1 froze before effect inspection the complete finite-time protocol, including

\[
T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\},
\]

`K_M`, `K_shift`, signed extrema, degeneracy-aware angle/subspace diagnostics, `Delta_shift` denominator rule, numerical cross-checks, direct physical reconstruction, resolution-robustness gates, and one-shot verdict logic.

MASTER has now completed the final pre-effect Pilot Freeze. No Climate-B finite-time effect has yet been inspected at the time of release.

## Active instruction

**Status:** `CLIMATE-B PILOT FROZEN — EXECUTION READY / AWAIT GO`

**Next instruction:**

`research/master/prompts/climate_intra_domain_contrast_pilot_execution_0_1.md`

On a bare `GO`, first read this STATUS and execute only that committed instruction exactly.

Execution must report all six frozen horizons and all mandatory primary/confirmation/high-audit diagnostics, then assign exactly one frozen outcome class: `CLIM-B-FAIL`, `CLIM-B-NULL`, `CLIM-B-STRONG`, or `CLIM-B-WEAK`.

No retuning, extra horizon, extra resolution, alternative channel, alternative jet, or third Climate candidate is authorized.

## Governance / manuscript dependency

Climate-B remains exactly one additional attempt. Weak/null/fail is retained as valid one-shot evidence.

`Manuscript Structure Freeze 0.2` remains on HOLD pending Climate-B execution/result integration and is the mandatory return point afterward.

No other application/theory branch is authorized while Climate-B is active.

## Canonical documents

Climate-A:

- `research/climate/climate_ocean_numerical_qualification_0_1.md`
- `research/climate/climate_ocean_pilot_specification_0_1.md`
- `research/climate/climate_ocean_pilot_0_1_execution_results.md`
- `research/climate/climate_ocean_pilot_0_1_execution_data.csv`

Climate-B:

- `research/master/climate_intra_domain_contrast_feasibility_gate_0_1.md`
- `research/climate/climate_intra_domain_contrast_candidate_freeze_0_1.md`
- `research/climate/climate_intra_domain_contrast_numerical_qualification_0_1.md`
- `research/climate/climate_intra_domain_contrast_numerical_qualification_0_1_data.csv`
- `research/climate/climate_intra_domain_contrast_pilot_specification_0_1.md`
- `research/master/climate_intra_domain_contrast_pilot_freeze_0_1.md`
- `research/master/prompts/climate_intra_domain_contrast_pilot_execution_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

\[
\boxed{\text{CLIMATE-B PILOT FROZEN — EXECUTION READY}}
\]

**STOP / AWAIT GO.**