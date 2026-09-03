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
- Climate Intra-Domain Contrast Numerical Qualification 0.1: **`QUALIFIED`**.

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

### Numerical Qualification result

Canonical:

- `research/climate/climate_intra_domain_contrast_numerical_qualification_0_1.md`
- `research/climate/climate_intra_domain_contrast_numerical_qualification_0_1_data.csv`
- `tests/test_climate_intra_domain_contrast_numerical_qualification_0_1.py`

All frozen qualification gates passed. In particular,

\[
\alpha(A_K)=-0.05787037037037=-0.1\,\mathrm d^{-1}<0
\]

on every frozen rung. Worst 512-vs-1024 assembly defect was `2.92e-14`, worst normalized eigenpair residual `6.42e-15`, and the rightmost spectral boundary is resolution-robust. Local qualification regression tests: `3 passed`.

No finite-time `K_M`, `K_shift`, `G_M`, `J_shift^±`, optimizer, angle, gap, horizon dependence, or objective-separation quantity has yet been computed or inspected.

## Active instruction

**Status:** `CLIMATE-B PILOT SPECIFICATION READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/climate_intra_domain_contrast_pilot_specification_0_1.md`

On a bare `GO`, first read this STATUS and execute only that committed prompt.

The Pilot Specification must freeze the inherited dimensionless horizon ladder, finite-time operator definitions, diagnostics, numerical execution/robustness rules, and one-shot verdict logic. It must not execute or inspect any Climate-B finite-time effect.

## Governance / manuscript dependency

Climate-B remains exactly one additional attempt. If a later frozen execution returns weak/null/fail, retain it; no third Climate candidate is authorized before the first manuscript.

`Manuscript Structure Freeze 0.2` remains on **HOLD** pending Climate-B resolution and is the mandatory return point afterward.

No other application/theory branch is authorized while Climate-B is active.

\[
\boxed{\text{CLIMATE-B PILOT SPECIFICATION READY — AWAIT GO}}
\]

**STOP / AWAIT GO.**