# Climate/Ocean Branch Status

**Last updated:** 2026-09-03  
**Branch:** `main`

## Climate-A — existing frozen pilot

Climate-A remains permanently frozen as the damped two-layer Phillips-QG heat-transport pilot.

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
\vartheta_{\rm sub}=90^\circ,\qquad \Delta_{\rm heat}=0.04118455338.
\]

Climate-A is not reopened, retuned, replaced, or relabeled.

## Climate-B — one-shot intra-domain contrast branch

- Feasibility Gate 0.1: `PASSED`.
- Candidate Freeze 0.1: `STABLE`.
- Numerical Qualification 0.1: `QUALIFIED`.
- Pilot Specification 0.1: `COMPLETE`.
- Pilot Freeze 0.1: `STABLE — EXECUTION RELEASED`.
- Pilot Execution 0.1: `COMPLETE`.
- MASTER Result Integration & Freeze 0.1: `STABLE`.
- **Frozen one-shot verdict: `CLIM-B-FAIL`.**
- **Failure reason: resolution robustness.**

Climate-B is the frozen equivalent-barotropic Bickley jet with perturbation kinetic energy versus signed cumulative eddy forcing of the infinitesimal poleward jet-translation tangent `g=-U'`.

All six frozen horizons and mandatory primary/confirmation/high-audit resolutions were executed without retuning. All algebraic and direct numerical gates passed.

At individual fixed truncations the Energy-vs-Shift separation is large and

\[
\Delta_{\rm shift}=1
\]

to roundoff. However, **zero of the six frozen horizons is resolution robust** under the frozen refinement rules. Objective values and optimizer/subspace geometry do not converge sufficiently from primary through high audit.

Therefore the result is permanently

\[
\boxed{\text{CLIM-B-FAIL — resolution robustness failure}}.
\]

The large fixed-resolution angles and `Delta_shift=1` may only be cited with the resolution-failure qualification and may not support a robust strong Climate-B claim.

No Climate-B repair, retuning, extra resolution, alternative channel, or third Climate candidate is authorized before the first manuscript.

## Canonical Climate-B artifacts

- `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_results.md`
- `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv`
- `tests/test_climate_intra_domain_contrast_pilot_0_1.py`
- `research/master/climate_intra_domain_contrast_result_integration_freeze_0_1.md`

## Active instruction

**Status:** `CLIMATE-B RESULT FROZEN — STOP / WAIT`

**Next instruction:**

`WAIT — RETURN TO MASTER`

No bare `GO` in this Climate chat may open a repair, third Climate candidate, extra horizon/resolution, manuscript change, or new scientific analysis.

## Manuscript dependency

The Climate-B one-shot branch is resolved. `Manuscript Structure Freeze 0.2` is now the mandatory MASTER task.

\[
\boxed{\text{CLIMATE-B RESULT FROZEN — STOP}}
\]

**STOP / WAIT.**
