# MASTER Prompt — Climate Intra-Domain Contrast Pilot Execution 0.1

**Status:** ACTIVE EXECUTION INSTRUCTION  
**Authority:** `research/master/climate_intra_domain_contrast_pilot_freeze_0_1.md`  
**Target chat/branch:** existing Climate chat / `research/climate/`  
**Purpose:** execute exactly once the frozen Climate-B finite-time pilot and return the complete result to MASTER.

## Mandatory pre-read

Before doing anything else, read and obey:

1. `research/climate/STATUS.md`;
2. `research/master/climate_intra_domain_contrast_pilot_freeze_0_1.md`;
3. `research/climate/climate_intra_domain_contrast_pilot_specification_0_1.md`;
4. `research/climate/climate_intra_domain_contrast_candidate_freeze_0_1.md`;
5. `research/climate/climate_intra_domain_contrast_numerical_qualification_0_1.md`.

If these disagree on a frozen choice, STOP and return to MASTER. Do not resolve a conflict by choosing the more favorable effect.

## Scope

Execute the one-shot Climate-B finite-time pilot exactly as frozen. Compute and report the finite-time energy and signed jet-translation-forcing objectives, all numerical/robustness diagnostics, physical optimizer diagnostics, and exactly one frozen outcome class.

No new theory development, parameter search, horizon search, objective change, channel change, basis change, resolution change, retuning, alternative Climate candidate, manuscript rewrite, or literature novelty search is authorized.

## Immutable setup

Use exactly the frozen Bickley-jet model, dimensional parameters, nondimensionalization, `A_K`, `M_K`, `Q_shift,K`, `B=I`, `R_in=M_K`, quadrature, basis, state ordering, resolution ladder, and time normalization.

Execute exactly

\[
T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}.
\]

Report every horizon. Do not stop early after seeing a favorable or unfavorable result.

## Required finite-time quantities

For each required resolution and every frozen horizon compute according to the Pilot Specification:

\[
K_M(T),\quad G_M(T),\quad
K_{\rm shift}(T),\quad
J_{\rm shift}^{+}(T),\quad J_{\rm shift}^{-}(T).
\]

Compute the frozen degeneracy-aware energy-versus-positive-shift optimizer/subspace angle and the frozen `Delta_shift` performance gap when its denominator is safely interpretable. Report undefined/uninterpretable explicitly when the denominator rule fails; do not regularize it.

## Mandatory numerical gates

Execute all frozen checks, including:

- Lyapunov-tail versus independent block-exponential cumulative operator;
- Hermiticity before any roundoff symmetrization;
- `K_M` PSD;
- eigenpair, normalization, and Rayleigh residuals;
- direct physical terminal-energy reproduction;
- direct physical Reynolds-stress / jet-translation cumulative-channel reproduction;
- primary/confirmation/high-audit objective-value convergence;
- common-space optimizer/subspace captured-mass and principal-angle checks;
- minimum neighboring-horizon robustness requirement.

If a mandatory gate fails, retain the failure and apply the frozen `CLIM-B-FAIL` logic. Do not repair the model or add a resolution/horizon.

## Mandatory physical diagnostics

For verdict-relevant horizons report the frozen physical diagnostics for the energy and positive-shift optima/subspaces:

- zonal wavenumber content and dominant physical wavelength;
- meridional modal content;
- parity fractions;
- representative streamfunction and velocity structure when nondegenerate;
- zonal-mean Reynolds stress;
- momentum-flux convergence;
- projection onto `g=-U'`;
- dominant signed modal/parity-pair contributions;
- representative signed `q_shift(t)` histories.

Use subspace/projector-invariant reporting when an optimum is degenerate.

## Frozen verdict

Assign exactly one, using the Pilot Specification precedence and thresholds:

- `CLIM-B-FAIL`;
- `CLIM-B-NULL`;
- `CLIM-B-STRONG`;
- `CLIM-B-WEAK`.

A `CLIM-B-STRONG` result requires both

\[
\vartheta\ge20^\circ,\qquad \Delta_{\rm shift}\ge0.25
\]

at the same at least two neighboring fixed horizons, robustly from primary through high-resolution audit, plus reproducible physical/modal interpretation.

A weak/null/fail result is equally valid and must be retained. No third Climate candidate is permitted.

## Required artifacts

Commit at minimum:

1. `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_results.md` — complete human-readable result;
2. `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv` — machine-readable horizon/resolution metrics;
3. a regression/reproduction test under `tests/` that checks the frozen execution invariants and key canonical values;
4. updated `research/climate/STATUS.md`.

If additional machine-readable diagnostic files are necessary, they are allowed only to record the frozen execution, not to expand the scope.

The results document must explicitly contain: scope/forbidden actions, frozen assumptions, formulas/definitions, numerical gates, results at all horizons, resolution robustness, physical diagnostics, PASS/FAIL status of each required gate, final one-shot verdict, allowed/forbidden interpretations, open issues, and final STOP.

## Result handoff

After committing all execution artifacts:

- report canonical repo paths;
- report the full commit hash;
- report CI status if available;
- set `research/climate/STATUS.md` to `CLIMATE-B EXECUTION COMPLETE — RETURN TO MASTER FOR RESULT INTEGRATION/FREEZE`;
- set `Next instruction` to `RETURN TO MASTER`;
- STOP.

Do not self-authorize manuscript changes, a third Climate case, parameter retuning, new horizons, or further Climate execution.
