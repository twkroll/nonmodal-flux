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
- **Pilot Execution 0.1: `COMPLETE`.**
- **Frozen one-shot verdict: `CLIM-B-FAIL`.**
- **Failure reason: resolution robustness.**

Climate-B is the frozen equivalent-barotropic Bickley jet with perturbation kinetic energy versus signed cumulative eddy forcing of the infinitesimal poleward jet-translation tangent `g=-U'`.

The execution used all six frozen horizons

\[
T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}
\]

and the mandatory primary `(16,32)`, confirmation `(20,40)`, and high-audit `(24,48)` resolutions without retuning.

All algebraic and direct numerical gates passed: finite-time Hermiticity, `K_M` PSD, eigenpair/normalization/Rayleigh residuals, Lyapunov-tail versus Van-Loan cumulative operator, and direct terminal-energy / reconstructed Reynolds-stress cumulative-shift reproduction.

At each individual frozen resolution, Energy-vs-Shift separation is large and

\[
\Delta_{\rm shift}\simeq1,
\]

because the energy optimum remains in one meridional-parity sector whereas the signed shift channel couples opposite parity sectors.

However, the effect is not resolution robust. At no frozen horizon do the required objective-value and common-space optimizer/subspace refinement gates pass from primary through high audit. In particular, captured common-space mass remains below the frozen `0.95` threshold and the signed objective remains outside the frozen 2% value-convergence criterion.

Therefore the preregistered one-shot outcome is

\[
\boxed{\text{CLIM-B-FAIL — resolution robustness failure}}.
\]

No extra resolution, parameter retuning, scale-selective damping, alternative channel, or third Climate candidate was introduced.

## Canonical Climate-B execution artifacts

- `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_results.md`
- `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv`
- `tests/test_climate_intra_domain_contrast_pilot_0_1.py`

Local execution regression test before commit: `3 passed`.

## Active instruction

**Status:** `CLIMATE-B EXECUTION COMPLETE — RETURN TO MASTER FOR RESULT INTEGRATION/FREEZE`

**Next instruction:**

`RETURN TO MASTER`

This Climate chat must not self-authorize manuscript changes, a third Climate case, parameter retuning, additional horizons/resolutions, or any further Climate execution on a bare `GO`.

## Manuscript dependency

`Manuscript Structure Freeze 0.2` remains on HOLD until MASTER integrates/freezes the Climate-B result. It remains the mandatory return point afterward.

Climate-B has consumed the single additional Climate attempt authorized before the first manuscript.

\[
\boxed{\text{CLIMATE-B EXECUTION COMPLETE — RETURN TO MASTER}}
\]

**STOP.**
