# Climate/Ocean Branch Status

## Current state

### Climate-A — existing frozen pilot

- Feasibility Gate 0.1: `PASSED`.
- Pilot Candidate Freeze 0.1: `STABLE`.
- Numerical Qualification 0.1: `QUALIFIED`.
- Cross-Domain Integration Gate 0.1: `PASSED`.
- Pilot Specification 0.1: `COMPLETE`.
- Cross-Domain Pilot Freeze 0.1: `STABLE`.
- Pilot Execution 0.1: `COMPLETE`.
- Cross-Domain Result Integration & Freeze 0.1: `STABLE`.
- Frozen verdict: `CLIM-WEAK`.

Climate-A remains the damped two-layer Phillips-QG heat-transport pilot and is permanently frozen against retuning.

At `T/tau_ref=8`,

\[
(|m|,n)_E=(3,2),\qquad (|m|,n)_{heat}=(4,2),
\]

\[
\vartheta_{sub}=90^\circ,\qquad \Delta_{heat}=0.04118455338,
\]

so the energy-optimal subspace retains approximately 95.88% of maximum cumulative poleward heat transport.

### Climate-B — one-shot intra-domain contrast branch

- Climate Intra-Domain Contrast Feasibility Gate 0.1: `PASSED`.
- Climate Intra-Domain Contrast Candidate Freeze 0.1: `STABLE`.
- **Climate Intra-Domain Contrast Numerical Qualification 0.1: `QUALIFIED`.**

Frozen candidate:

\[
\boxed{\text{equivalent-barotropic midlatitude Bickley jet}}
\]

with

- positive objective metric: barotropic perturbation kinetic energy;
- signed physical channel: eddy-induced forcing of the infinitesimal poleward jet-translation coordinate;
- translation tangent: \(g(y)=-U'(y)\);
- admissible eddy geometry: \(B=I\), \(R_{\rm in}=M_K\);
- frozen physical point
  \[
  \beta=1.6\times10^{-11}\,\mathrm{m^{-1}s^{-1}},\quad
  U_0=20\,\mathrm{m\,s^{-1}},\quad
  L=1000\,\mathrm{km},\quad
  r=(10\,\mathrm d)^{-1};
  \]
- domain: \(L_x=20000\,\mathrm{km}\), \(L_y=10000\,\mathrm{km}\), centered jet;
- time normalization:
  \[
  \tau_{\rm ref}=L/U_0=50000\,\mathrm s=0.5787037037\,\mathrm d;
  \]
- structure-preserving representation: positive zonal Fourier modes plus centered meridional sine Galerkin basis, with exact conjugate reconstruction of real fields;
- frozen nested resolution roles:
  `(8,16)` structural smoke, `(12,24)` coarse audit, `(16,32)` primary, `(20,40)` confirmation, `(24,48)` high-resolution audit.

## Climate-B Numerical Qualification 0.1 result

Canonical qualification report:

`research/climate/climate_intra_domain_contrast_numerical_qualification_0_1.md`

Machine-readable data:

`research/climate/climate_intra_domain_contrast_numerical_qualification_0_1_data.csv`

Regression test:

`tests/test_climate_intra_domain_contrast_numerical_qualification_0_1.py`

All frozen structural and spectral gates passed:

- 512-versus-1024 Gauss-Legendre assembly audit: PASS; worst relative defect `2.92e-14`;
- \(M_K=M_K^\dagger\succ0\): PASS, with \(\lambda_{\min}(M_K)=7.895683520871486\);
- \(Q_{{\rm shift},K}=Q_{{\rm shift},K}^\dagger\), nontrivial and indefinite: PASS;
- parity selection rules: PASS to quadrature/roundoff precision;
- fixed `m=1, c_11=1, c_12=±i` signed-channel witness: PASS;
- complete frozen spectra: PASS;
- spectral stability at every rung:
  \[
  \alpha(A_K)=-0.05787037037037=-0.1\,\mathrm d^{-1}<0
  \]
  to double-precision roundoff;
- maximum deviation of any computed spectral real part from \(-r^*\): `1.13e-14`;
- worst normalized eigenpair residual: `6.42e-15`;
- rightmost spectral boundary is resolution-robust from smoke through high-resolution audit.

Local qualification-only regression tests: `3 passed`.

No finite-time `K_M`, `K_shift`, `G_M`, `J_shift^±`, optimizer, angle, gap, horizon dependence, or objective-separation quantity has been computed or inspected for Climate-B. No horizon ladder has been selected.

Hard rule: Climate-B remains one additional attempt only. Qualification success does not authorize execution. No third Climate candidate is authorized before the first manuscript.

## Active instruction

**Status:** `CLIMATE-B NUMERICAL QUALIFICATION COMPLETE — RETURN TO MASTER`

**Next instruction:**

`RETURN TO MASTER`

This Climate chat must not self-authorize Pilot Specification, finite-time execution, horizon selection, or any further Climate analysis on a bare `GO` until MASTER commits a new instruction.

## Manuscript dependency

`Manuscript Structure Freeze 0.2` remains on HOLD pending resolution of this one-shot Climate-B branch. It is not canceled and remains the mandatory return point.

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
- `tests/test_climate_intra_domain_contrast_numerical_qualification_0_1.py`
- `research/master/prompts/climate_intra_domain_contrast_numerical_qualification_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

\[
\boxed{\text{CLIMATE-B NUMERICAL QUALIFICATION COMPLETE — RETURN TO MASTER}}
\]

**STOP.**