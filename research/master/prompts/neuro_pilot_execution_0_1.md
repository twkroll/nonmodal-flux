# Neuro Pilot Execution 0.1 — MASTER Handoff

**Authority:** Cross-Domain Pilot Freeze 0.1  
**Scope:** execute only the frozen Neuro Pilot Specification 0.1.  
**No parameter search, no retuning, no model change, no new theory.**

## 1. Read first

Before calculation, read and obey:

1. `research/master/cross_domain_pilot_freeze_0_1.md`;
2. `research/neuro/neuro_pilot_specification_0_1.md`;
3. `research/neuro/STATUS.md`;
4. `research/master/cross_domain_integration_gate_0_1.md`.

If any frozen object conflicts, STOP and report the conflict rather than choosing a convenient interpretation.

## 2. Frozen pilot

Execute exactly the frozen two-source macaque V1/V4 autonomous CMC/DCM pilot:

- `n_x=16`;
- stable frozen generator `A` from the specification;
- synaptic-filter storage matrix `M`;
- primary signed pathway `V1 SP -> V4 SS` with frozen `Q_CORE`;
- frozen two-pulse V1-SS preparation map `B`;
- `R_in=I_2`;
- `tau_ref=28 ms`;
- horizons `T=(7,14,28,56,112,224) ms`.

Do not enable propagation delays. Do not alter V1/V4, the pathway, the operating point, any CMC parameter, pulse width, pulse timing, calibration, or horizon.

## 3. Structural gates before interpretation

Reproduce and record before interpreting any objective comparison:

- `alpha(A)<0`;
- `M=M^dagger>0`;
- `Q=Q^dagger` within the frozen tolerance;
- `R_in=R_in^dagger>0`;
- `rank(B)=2`;
- frozen storage/input-whitened conditioning gate `kappa_2(M^(1/2) B R_in^(-1/2))<=100`;
- semigroup check for the propagator;
- cumulative-channel primary evaluation versus independent adaptive quadrature, relative disagreement `<1e-8`;
- Hermiticity of later `K_M(T)` and `K_Q(T)` under the frozen tolerances.

Any failed structural/numerical gate yields `NEURO-NUMERICAL-FAIL` and STOP. Do not retune.

## 4. Required finite-time calculations

Use whitened input coordinates

\[
x(0)=BR_{\rm in}^{-1/2}w,
\qquad \|w\|_2=1.
\]

For each frozen horizon compute

\[
K_M(T)=R_{\rm in}^{-1/2}B^\dagger e^{A^\dagger T}Me^{AT}BR_{\rm in}^{-1/2},
\]

\[
G_M(T)=\lambda_{\max}(K_M(T)),
\]

interpreted only as **final synaptic-filter storage per fixed preparation-input cost**.

Compute

\[
P_Q(T)=\int_0^T e^{A^\dagger t}Qe^{At}\,dt,
\]

\[
K_Q(T)=R_{\rm in}^{-1/2}B^\dagger P_Q(T)BR_{\rm in}^{-1/2},
\]

and mandatory signed extrema

\[
J_Q^+(T)=\lambda_{\max}(K_Q(T)),
\qquad
J_Q^-(T)=\lambda_{\min}(K_Q(T)).
\]

The positive branch is primary. Never replace the signed channel by an absolute value or squared output.

## 5. Objective comparison

At each horizon obtain normalized positive-objective and positive-channel optimizers `w_M^*` and `w_Q^*` in the fixed two-dimensional whitened preparation space.

Report

\[
\vartheta(T)=\arccos\left|{w_M^*}^\dagger w_Q^*\right|.
\]

If either extremum is degenerate, use eigenspaces/projectors and principal angles rather than an arbitrary eigenvector.

When `J_Q^+(T)` is safely nonzero, report

\[
\Delta_Q(T)=
\frac{J_Q^+(T)-{w_M^*}^\dagger K_Q(T)w_M^*}{J_Q^+(T)}.
\]

If the denominator is near zero, mark `Delta_Q` uninterpretable; do not regularize it.

The frozen operational demonstration thresholds are

\[
\vartheta\ge20^\circ,
\qquad
\Delta_Q\ge0.25,
\]

and a threshold claim requires at least two neighboring fixed horizons.

## 6. Required physical diagnostics

For every horizon, and especially any horizon supporting the verdict, report enough information to determine whether the two optimizers are physically distinct beyond a vector angle:

- coefficients/amplitude mixture in the fixed `(h1,h2)` preparation basis;
- corresponding initial-state composition `x0=Bw` in V1/V4 and SS/SP/II/DP components;
- terminal storage composition by region/population;
- sign and time distribution of the fixed V1-SP -> V4-SS pathway contribution;
- direct trajectory values needed to validate the quadratic forms.

Do not call `M` brain energy or metabolic energy. Do not call the pathway observable generic information flow.

## 7. Frozen verdict classes

Classify exactly one:

- `NEURO-STRONG`;
- `NEURO-WEAK`;
- `NEURO-NULL`;
- `NEURO-TRANSPORT-NULL`;
- `NEURO-NUMERICAL-FAIL`.

Use the definitions in `research/master/cross_domain_pilot_freeze_0_1.md`. Do not invent a new class after seeing results.

## 8. Anti-bias rules

After the first CORE-effect quantity is computed, do not change anything frozen by the specification/freeze. In particular, no changes to regions, pathway, CMC parameters, operating point, propagation-delay scope, pulse timing, pulse shape, pulse calibration, input map, input metric, time normalization, or horizons.

A weak/null result is retained.

## 9. Required repository outputs

Create and commit:

- `research/neuro/neuro_pilot_0_1_execution_results.md` — complete scientific report, checks, tables, verdict, allowed/forbidden interpretation, STOP;
- `research/neuro/neuro_pilot_0_1_execution_data.csv` — machine-readable per-horizon numerical results and key diagnostics;
- numerical tests under `tests/` sufficient to reproduce the frozen structural and operator checks;
- update `research/neuro/STATUS.md` to `EXECUTION COMPLETE — RETURN TO MASTER FOR RESULT INTEGRATION` and point to the canonical result file.

Record exact commit hash and CI status. If CI fails, state this explicitly; do not silently change the frozen science to make CI pass.

## 10. STOP

After committing the outputs and updating `STATUS.md`, STOP. Do not open MODES, CONT, CASCADE, delay extensions, additional neural models, extra pathways, or any follow-on parameter study.
