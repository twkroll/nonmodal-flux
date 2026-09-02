# Climate/Ocean Pilot Execution 0.1 — MASTER Handoff

**Authority:** Cross-Domain Pilot Freeze 0.1  
**Scope:** execute only the frozen Climate/Ocean Pilot Specification 0.1.  
**No parameter search, no retuning, no model change, no new theory.**

## 1. Read first

Before calculation, read and obey:

1. `research/master/cross_domain_pilot_freeze_0_1.md`;
2. `research/climate/climate_ocean_pilot_specification_0_1.md`;
3. `research/climate/climate_ocean_numerical_qualification_0_1.md`;
4. `research/climate/STATUS.md`;
5. `research/master/cross_domain_integration_gate_0_1.md`.

If any frozen object conflicts, STOP and report the conflict rather than selecting a convenient interpretation.

## 2. Frozen pilot

Execute exactly the qualified damped two-layer Phillips-QG pilot with

\[
(A_K,M_K,Q_{{\rm heat},K},B=I,R_{\rm in}=M_K)
\]

and the unchanged physical parameters, basis, nondimensionalization and signed convention from the specification.

Positive transport remains northward/poleward eddy heat transport.

Frozen time normalization and horizon ladder:

\[
\tau_{\rm ref}=0.7233796296\,\mathrm d,
\qquad
T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}.
\]

Frozen resolution roles:

- `(4,4)` qualification-only smoke;
- `(8,8)` coarse audit;
- `(12,12)` **primary**;
- `(16,16)` **confirmation**;
- `(24,24)` **high-resolution audit**.

No rung may be added, removed, or reassigned.

## 3. Structural and numerical gates

Execute all checks exactly as preregistered in the Pilot Specification before interpreting any objective separation, including:

- `M_K=M_K^dagger>0`;
- `Q_heat,K=Q_heat,K^dagger` and signed/indefinite;
- spectral stability at every frozen resolution;
- frozen Hermiticity tolerances for `K_E` and `K_heat`;
- eigenresidual, normalization and Rayleigh-quotient tolerances;
- energy-operator positive-semidefiniteness within roundoff;
- primary augmented-exponential cumulative-heat integral;
- independent stable Lyapunov-tail identity;
- direct trajectory/adaptive quadrature check at the frozen tolerance;
- no silent symmetrization before the Hermiticity gate passes.

Any failed numerical gate is classified under the already frozen Climate verdict scheme. Do not retune.

## 4. Required finite-time calculations

For each frozen resolution role and horizon, compute the preregistered energy operator

\[
K_E(T)=M_K^{-1/2}e^{A_K^\dagger T}M_Ke^{A_KT}M_K^{-1/2},
\]

\[
G_E(T)=\lambda_{\max}(K_E(T)).
\]

Compute

\[
H_K(T)=\int_0^T e^{A_K^\dagger t}Q_{{\rm heat},K}e^{A_Kt}\,dt,
\]

\[
K_{\rm heat}(T)=M_K^{-1/2}H_K(T)M_K^{-1/2},
\]

with signed extrema

\[
J_{\rm heat}^{+}(T)=\lambda_{\max}(K_{\rm heat}(T)),
\qquad
J_{\rm heat}^{-}(T)=\lambda_{\min}(K_{\rm heat}(T)).
\]

The positive/poleward branch is primary and the negative/equatorward extremum is mandatory reporting.

## 5. Objective comparison

At each fixed horizon compare the positive energy-optimal and positive heat-transport-optimal directions/eigenspaces.

Report

\[
\vartheta(T)=\arccos\left|{w_E^*}^\dagger w_{\rm heat}^*\right|,
\]

only for nondegenerate one-dimensional optima. For the exact `+/-m` representation degeneracies and any other degeneracy, obey the frozen eigenspace/projector and principal-angle protocol instead of selecting an arbitrary eigenvector.

When `J_heat^+(T)` is safely nonzero, report

\[
\Delta_{\rm heat}(T)=
\frac{J_{\rm heat}^+(T)-{w_E^*}^\dagger K_{\rm heat}(T)w_E^*}{J_{\rm heat}^+(T)}.
\]

Do not regularize a near-zero denominator.

The frozen project-level thresholds are

\[
\vartheta\ge20^\circ,
\qquad
\Delta_{\rm heat}\ge0.25
\]

at at least two neighboring fixed horizons.

## 6. Resolution robustness

Apply the preregistered resolution-robustness protocol exactly.

For `Y in {G_E, J_heat^+, |J_heat^-|}`, require the frozen adjacent refinement discrepancy criterion for primary/confirmation and confirmation/high-resolution audit before a horizon supports a resolution-robust claim.

Cross-resolution optimizer comparison must use projection to the common modal subspace, common-space mass/overlap/projector metrics and the specification's degeneracy rules. Never compare unequal-dimensional raw vectors by zero padding and a naive angle.

If the frozen robustness gate fails, use the pre-existing `CLIM-RESOLUTION-FAIL` verdict rather than retuning or adding resolution.

## 7. Required physical diagnostics

For the primary result and all horizons relevant to the verdict, report the preregistered domain-specific structure, including:

- barotropic versus baroclinic energy fraction;
- modal `(m,n)` weights/support;
- layer-space structure reconstructed from `(psi,tau)`;
- relevant relative phases responsible for signed heat transport;
- poleward/equatorward sign history along direct trajectories;
- enough common-modal-space information to establish whether optimizer differences survive refinement.

A vector/subspace separation without physical structure is insufficient for a strong verdict.

## 8. Frozen verdict classes

Classify exactly one of the already preregistered classes:

- `CLIM-STRONG`;
- `CLIM-WEAK`;
- `CLIM-NULL`;
- `CLIM-TRANSPORT-NULL`;
- `CLIM-RESOLUTION-FAIL`;
- `CLIM-NUMERICAL-FAIL`.

Do not add or redefine classes after seeing results.

## 9. Anti-bias rules

After the first CORE-effect quantity is evaluated, change none of the frozen physical parameters, damping, basis, state ordering, sign convention, resolutions, resolution roles, horizons, numerical tolerances, thresholds, or verdict rules.

A weak/null/failure outcome is retained.

## 10. Required repository outputs

Create and commit:

- `research/climate/climate_ocean_pilot_0_1_execution_results.md` — complete scientific report, numerical checks, resolution audit, physical diagnostics, verdict, allowed/forbidden interpretation, STOP;
- `research/climate/climate_ocean_pilot_0_1_execution_data.csv` — machine-readable results by resolution and horizon;
- numerical tests under `tests/` sufficient to reproduce the frozen structural, integral and robustness checks;
- update `research/climate/STATUS.md` to `EXECUTION COMPLETE — RETURN TO MASTER FOR RESULT INTEGRATION` and point to the canonical result file.

Record exact commit hash and CI status. If CI fails, report it explicitly; do not change the frozen science to obtain a passing result.

## 11. STOP

After committing the outputs and updating `STATUS.md`, STOP. Do not open a new Climate model, Primitive-Equation extension, MODES/CONT/CASCADE analysis, parameter study, or application retuning.
