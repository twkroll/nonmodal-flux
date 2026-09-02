# Cross-Domain Pilot Freeze 0.1

**Status:** STABLE — EXECUTION RELEASED  
**Date:** 2026-09-02  
**Scope:** final preregistration/freeze before the first CORE-effect calculations in the Neuro and Climate/Ocean application branches.

## 1. Preconditions

This freeze accepts only already committed, pre-effect specifications:

- `research/master/cross_domain_integration_gate_0_1.md` — PASSED;
- `research/neuro/neuro_pilot_specification_0_1.md` — COMPLETE;
- `research/climate/climate_ocean_pilot_specification_0_1.md` — COMPLETE;
- Neuro `STATUS.md` and Climate `STATUS.md`, both previously at `RETURN TO MASTER FOR PILOT FREEZE`.

No `K_M(T)`, `K_Q(T)`, optimizer, optimizer angle, gap, or objective-separation result was used to make this freeze decision.

The Plasma/D10-ZF Pilot 0.2 P2-A Result Freeze remains the global scientific savepoint and is not modified.

## 2. Freeze decision

Both application pilots are sufficiently specified to execute without further model choice, parameter choice, horizon choice, objective choice, or effect-guided tuning.

Therefore

\[
\boxed{\text{Cross-Domain Pilot Freeze 0.1 = STABLE}}
\]

and, independently,

\[
\boxed{\text{Neuro Pilot 0.1 = FROZEN FOR EXECUTION}},
\]

\[
\boxed{\text{Climate/Ocean Pilot 0.1 = FROZEN FOR EXECUTION}}.
\]

Both may execute in parallel. Neither outcome may be used to alter the frozen setup of the other.

## 3. Shared finite-time reporting layer

For each frozen application tuple

\[
\mathfrak C=(A,M,Q,B,R_{\rm in}),
\qquad M\succ0,
\qquad Q=Q^\dagger,
\]

use whitened input coordinates

\[
x(0)=BR_{\rm in}^{-1/2}w,
\qquad \|w\|_2=1.
\]

The positive terminal storage/state objective is

\[
K_M(T)=R_{\rm in}^{-1/2}B^\dagger e^{A^\dagger T}Me^{AT}BR_{\rm in}^{-1/2},
\]

\[
G_M(T)=\lambda_{\max}(K_M(T)).
\]

The signed cumulative channel is

\[
P_Q(T)=\int_0^T e^{A^\dagger t}Qe^{At}\,dt,
\]

\[
K_Q(T)=R_{\rm in}^{-1/2}B^\dagger P_Q(T)BR_{\rm in}^{-1/2}.
\]

Mandatory signed extrema are

\[
J_Q^+(T)=\lambda_{\max}(K_Q(T)),
\qquad
J_Q^-(T)=\lambda_{\min}(K_Q(T)).
\]

The positive branch is primary, while the negative branch remains mandatory reporting.

For normalized positive-objective and positive-channel optimizers `w_M^*`, `w_Q^*`, report

\[
\vartheta(T)=\arccos\left|{w_M^*}^\dagger w_Q^*\right|,
\]

with eigenspace/projector comparison at degeneracy, and

\[
\Delta_Q(T)=
\frac{J_Q^+(T)-{w_M^*}^\dagger K_Q(T)w_M^*}{J_Q^+(T)}
\]

only if the denominator is safely nonzero. No post-hoc regularization is allowed.

The inherited operational demonstration thresholds remain

\[
\boxed{\vartheta\ge20^\circ},
\qquad
\boxed{\Delta_Q\ge0.25}
\]

at at least two neighboring horizons. These are project-level preregistered thresholds, not universal physical constants.

## 4. Neuro Pilot 0.1 freeze

The Neuro pilot is frozen exactly as specified in `research/neuro/neuro_pilot_specification_0_1.md`:

- model: two-source autonomous CMC/DCM;
- sources: macaque V1 and V4;
- primary signed pathway: V1 SP -> V4 SS;
- state dimension: 16;
- operating point: `x*=0`;
- propagation-delay module: disabled for this autonomous ODE pilot;
- exact generator `A`: specification Section 5;
- positive metric `M`: synaptic-filter storage, specification Section 6;
- signed channel
  \[
  Q_{V1\,SP\to V4\,SS}^{\rm CORE}
  =\frac12(A_{j\to i}^\dagger M+MA_{j\to i});
  \]
- admissible input map: two fixed 1-ms V1-SS afferent preparation pulses ending 2 ms and 16 ms before observation;
- `R_in=I_2` in the two-dimensional pulse-amplitude input coordinates;
- `rank(B)=2`;
- `kappa_2(M^{1/2}B)=34.2940<100`;
- `tau_ref=28 ms`;
- horizons: `T=(7,14,28,56,112,224) ms`;
- frozen spectral qualification: `alpha(A)=-33.0964092356 s^-1 < 0`.

The word **energy** must not be used for this Neuro `M`. The allowed interpretation is **synaptic-filter storage** or positive model-internal state storage. The signed `Q` is the contribution of the pre-defined V1-SP -> V4-SS pathway to the storage rate, not generic information flow.

### Neuro verdict classes frozen before execution

- **NEURO-STRONG:** all structural/numerical checks pass; `J_Q^+` is interpretable; both `vartheta>=20 deg` and `Delta_Q>=0.25` hold at at least two neighboring fixed horizons; the separation has a reproducible physiological/input-composition interpretation.
- **NEURO-WEAK:** all structural/numerical checks pass and nonzero objective separation exists, but one operational threshold or the physical-structure requirement is not met strongly enough for `NEURO-STRONG`.
- **NEURO-NULL:** structural/numerical checks pass but storage-optimal and pathway-transfer-optimal preparation mixtures are practically redundant on the frozen horizon ladder.
- **NEURO-TRANSPORT-NULL:** the positive signed pathway extremum is zero or too close to zero for a meaningful positive-branch gap over the relevant fixed horizons.
- **NEURO-NUMERICAL-FAIL:** a preregistered structural, integral, Hermiticity, rank/conditioning, or reproducibility check fails.

No class may be redefined after execution.

## 5. Climate/Ocean Pilot 0.1 freeze

The Climate/Ocean pilot is frozen exactly as specified in `research/climate/climate_ocean_pilot_specification_0_1.md`:

- model: damped two-layer Phillips-QG channel;
- physical parameters unchanged from Numerical Qualification 0.1;
- `B=I` on the physically restricted balanced QG eddy state space;
- `R_in=M_K`;
- positive objective: QG perturbation energy;
- signed channel: cumulative northward/poleward eddy heat transport;
- `tau_ref=0.7233796296 d`;
- fixed horizons: `T/tau_ref=(0.25,0.5,1,2,4,8)`;
- fixed resolution ladder: `(4,4),(8,8),(12,12),(16,16),(24,24)`;
- primary: `(12,12)`;
- confirmation: `(16,16)`;
- high-resolution audit: `(24,24)`;
- fixed spectral qualification at every rung: `alpha(A_K)=-0.1 d^-1<0`;
- exact modal assembly and all preregistered numerical/robustness checks remain unchanged.

The already frozen Climate verdict classes remain binding:

`CLIM-STRONG`, `CLIM-WEAK`, `CLIM-NULL`, `CLIM-TRANSPORT-NULL`, `CLIM-RESOLUTION-FAIL`, `CLIM-NUMERICAL-FAIL`.

No class or resolution role may be changed after execution starts.

## 6. Anti-bias rules after this freeze

From this commit onward, neither branch may change after seeing any CORE-effect result:

- model or operating point;
- physical parameters;
- `M`, `Q`, `B`, or `R_in`;
- Neuro region/pathway identity, pulse widths, pulse delays, calibration, or delay-module scope;
- Climate physical parameters, basis, resolution ladder, or resolution roles;
- horizon ladder;
- positive/negative channel orientation;
- operational thresholds;
- numerical tolerance gates;
- verdict classes.

A weak, null, transport-null, resolution-failed, or numerical-failed result is a valid frozen outcome and must not trigger retuning.

## 7. Parallel execution and integration boundary

Execution is now released in parallel:

\[
\boxed{\text{Neuro Pilot Execution 0.1}}
\quad\parallel\quad
\boxed{\text{Climate/Ocean Pilot Execution 0.1}}.
\]

Each branch must execute only its committed MASTER prompt, write a canonical result Markdown file, write machine-readable data where requested, update its own `STATUS.md`, commit the output, and STOP.

After both return, no further application tuning or new branch is opened automatically. The next MASTER step is a result-level cross-domain integration/freeze.

Power Grids, Photonics/Waves, and realistic Fusion remain protected. MODES, CONT, and CASCADE remain waiting modules.

## 8. Decision log

- **DEC-302:** Cross-Domain Pilot Freeze 0.1 declared STABLE — STABLE.
- **DEC-303:** Neuro Pilot 0.1 frozen for execution — STABLE.
- **DEC-304:** Climate/Ocean Pilot 0.1 frozen for execution — STABLE.
- **DEC-305:** Neuro and Climate may execute in parallel without conditioning one another — STABLE.
- **DEC-306:** No CORE-effect quantity was used to choose either frozen pilot setup — STABLE.
- **DEC-307:** Neuro verdict classes frozen before execution — STABLE.
- **DEC-308:** Climate pre-existing verdict classes retained unchanged — STABLE.
- **DEC-309:** No retuning after first CORE-effect inspection in either branch — STABLE.
- **DEC-310:** Weak/null outcomes are retained as scientific results — STABLE.
- **DEC-311:** Next integration occurs only after both frozen executions return — ACTIVE.

## 9. Handoff

Canonical execution prompts:

- `research/master/prompts/neuro_pilot_execution_0_1.md`
- `research/master/prompts/climate_ocean_pilot_execution_0_1.md`

Under Shared Prompt Handoff Protocol 0.1, a bare `GO` in the corresponding branch executes the active committed prompt and nothing else.
