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
- **Climate Intra-Domain Contrast Candidate Freeze 0.1: `STABLE`.**

Frozen candidate:

\[
\boxed{\text{equivalent-barotropic midlatitude Bickley jet}}
\]

with

- positive objective metric: barotropic perturbation kinetic energy;
- signed physical channel: eddy-induced forcing of the infinitesimal poleward jet-translation coordinate;
- translation tangent: \(g(y)=-U'(y)\), unchanged from feasibility;
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

Candidate Freeze analytically established \(M_K\succ0\), a Hermitian signed/indefinite \(Q_{{\rm shift},K}\), physical consistency of \(B=I,R_{\rm in}=M_K\), and the Rayleigh-Kuo pre-effect stability criterion. Exact finite-dimensional spectral stability remains for Numerical Qualification.

No finite-time `K_M`, `K_shift`, optimizer, angle, gap, horizon dependence or objective-separation quantity has been computed or inspected for Climate-B.

Hard rule: Climate-B remains one additional attempt only. If Numerical Qualification fails or a later frozen execution is weak/null, no third Climate candidate is authorized before the first manuscript.

## Active instruction

**Status:** `CLIMATE-B CANDIDATE FROZEN — RETURN TO MASTER FOR NUMERICAL QUALIFICATION`

**Next instruction:**

`RETURN TO MASTER FOR NUMERICAL QUALIFICATION`

This Climate chat must not self-authorize Numerical Qualification on a bare `GO` until MASTER commits a new instruction.

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
- `research/master/prompts/climate_intra_domain_contrast_candidate_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

\[
\boxed{\text{CLIMATE-B CANDIDATE FROZEN — RETURN TO MASTER FOR NUMERICAL QUALIFICATION}}
\]

**STOP.**
