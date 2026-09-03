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
- **Climate Intra-Domain Contrast Pilot Specification 0.1: `COMPLETE`.**

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

The complete frozen resolution ladder is spectrally stable:

\[
\alpha(A_K)=-0.05787037037037=-0.1\,\mathrm d^{-1}<0
\]

at every rung. All structural/channel/quadrature/parity/sign-witness/eigenpair gates passed.

### Pilot Specification 0.1 freeze

Canonical specification:

`research/climate/climate_intra_domain_contrast_pilot_specification_0_1.md`

The inherited horizon ladder is now frozen before effect inspection:

\[
T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\},
\]

corresponding to

\[
T\in\{12500,25000,50000,100000,200000,400000\}\,\mathrm s.
\]

The specification freezes, before any effect calculation:

- definitions of `K_M(T)`, `K_shift(T)`, `G_M(T)`, and signed `J_shift^±(T)`;
- conservative vector/subspace angle and shift-performance-gap diagnostics;
- degeneracy threshold `delta_deg=1e-8`;
- safely-nonzero denominator rule for `Delta_shift`;
- blockwise scaling-and-squaring Padé propagation;
- quadrature-free Lyapunov-tail cumulative signed operator with an independent block-exponential cross-check;
- Hermiticity, PSD, eigenpair, normalization, Rayleigh and direct physical-trajectory tolerances;
- primary/confirmation/high-audit objective-value convergence threshold `<=2%`;
- common-space optimizer/subspace requirements `mu_c>=0.95` and maximum resolution principal angle `<=10 deg`;
- physical diagnostics for zonal wavenumber, meridional parity, streamfunction/velocity structure, Reynolds stress and jet-translation forcing;
- operational strong thresholds
  \[
  \vartheta\ge20^\circ,\qquad \Delta_{\rm shift}\ge0.25
  \]
  on at least two neighboring fixed horizons;
- inherited weak/null resolution thresholds `5 deg` / `0.05`;
- exactly four one-shot outcome classes: `CLIM-B-STRONG`, `CLIM-B-WEAK`, `CLIM-B-NULL`, `CLIM-B-FAIL`.

These are project-level operational rules, not universal atmospheric-physics constants.

No finite-time `K_M`, `K_shift`, `G_M`, `J_shift^±`, optimizer, angle, gap, horizon dependence, or Climate-B verdict has been computed or inspected.

## Active instruction

**Status:** `CLIMATE-B PILOT SPECIFICATION COMPLETE — RETURN TO MASTER FOR PILOT FREEZE`

**Next instruction:**

`RETURN TO MASTER FOR PILOT FREEZE`

This Climate chat must not self-authorize finite-time execution on a bare `GO` until MASTER commits a separate Pilot Freeze / execution instruction.

## Governance / manuscript dependency

Climate-B remains exactly one additional attempt. If a later frozen execution returns weak/null/fail, retain it; no third Climate candidate is authorized before the first manuscript.

`Manuscript Structure Freeze 0.2` remains on **HOLD** pending Climate-B resolution and is the mandatory return point afterward.

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
- `tests/test_climate_intra_domain_contrast_numerical_qualification_0_1.py`
- `research/climate/climate_intra_domain_contrast_pilot_specification_0_1.md`
- `research/master/prompts/climate_intra_domain_contrast_pilot_specification_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

\[
\boxed{\text{CLIMATE-B PILOT SPECIFICATION COMPLETE — RETURN TO MASTER FOR PILOT FREEZE}}
\]

**STOP.**