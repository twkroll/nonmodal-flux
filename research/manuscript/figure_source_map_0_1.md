# Figure Source Map 0.1

**Status:** CANONICAL SUPPORT FOR MANUSCRIPT REVISION 0.2  
**Authority:** `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md` and `research/master/manuscript_draft_review_gate_0_1.md`  
**Rule:** every panel must use only frozen data or frozen analytical definitions. No new simulation, horizon, parameter point, pathway, objective, eigensolve, or model calculation is allowed.

## Figure 1 — Common workflow and domain semantics

**Purpose:** introduce the shared diagnostic layer without implying common physical semantics.

Panels:
- (a) frozen tuple `(A,M,Q,B,R_in)` and admissible preparation `x(0)=B R_in^{-1/2} w`;
- (b) terminal positive-objective and cumulative signed-channel operators;
- (c) geometry diagnostic `theta`/subspace angle versus performance diagnostic `Delta_Q`;
- (d) domain-semantics table: Plasma free energy / particle transport; Neuro synaptic-filter storage / V1-SP -> V4-SS pathway contribution; Climate QG energy / eddy heat transport.

Sources:
- `research/manuscript/manuscript_draft_0_2.md`, Sec. 2;
- `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`.

Caption guardrails:
- commonality is methodological, not physical;
- define “physical channel” broadly as a signed transport/exchange/pathway-contribution observable;
- Neuro label must be “synaptic-filter storage”, never “brain energy”.

## Figure 2 — Plasma strong anchor

Frozen sources:
- `research/d10_zf_pilot_0_2_execution_data.csv`;
- `research/d10_zf_pilot_0_2_execution_results.md`.

Panels:
- (a) frozen horizon values `G_E`, `J_Gamma+`, `J_Gamma-` at one display resolution, with resolution convergence stated in caption;
- (b) `theta(T)` and `Delta_Gamma(T)` over the six frozen horizons;
- (c) frozen Fourier-mode weight distributions at `T=1`;
- (d) direct-trajectory endpoint summary at `T=1` unless full frozen time-series samples already exist. Do not reconstruct a time series.

Representative witness:
`T=1`: `G_E=1.8783`, `J_Gamma+=0.3535`, `J_Gamma-=-0.1462`, `theta=53.40 deg`, `Delta_Gamma=0.5043`.

Guardrails:
- stable controlled D10-ZF benchmark;
- negative signed branch shown explicitly;
- no first-transient-growth, nonlinear-turbulence, or experimental claim.

## Figure 3 — Neuro constrained two-pulse result

Frozen sources:
- `research/neuro/neuro_pilot_0_1_execution_data.csv`;
- `research/neuro/neuro_pilot_0_1_execution_results.md`;
- `research/neuro/neuro_pilot_specification_0_1.md` for pathway/pulse geometry only.

Panels:
- (a) V1/V4 CMC schematic with highlighted V1-SP -> V4-SS pathway and two fixed V1-SS afferent preparation pulses;
- (b) `theta(T)` and `Delta_Q(T)` over 7, 14, 28, 56, 112, 224 ms;
- (c) unit-cost pulse-coordinate arrows `w_M` and `w_Q` at 112 and 224 ms with equal aspect ratio;
- (d) compact inset/table for the 112/224-ms quantitative witnesses if needed.

Witnesses:
- 112 ms: `theta=46.824 deg`, `Delta_Q=0.529017`, `w_M=(+0.768725,+0.639580)`, `w_Q=(+0.992410,-0.122974)`;
- 224 ms: `theta=65.058 deg`, `Delta_Q=0.817841`, `w_M=(+0.530000,+0.847998)`, `w_Q=(+0.992410,-0.122972)`.

Guardrails:
- pulse amplitudes are fixed preparation coordinates, not an optimized time-dependent control waveform;
- preserve pulse sign;
- do not draw a reachable negative cumulative pathway branch because the frozen admissible minimum is positive.

## Figure 4 — Climate/Ocean weak contrast

Frozen sources:
- `research/climate/climate_ocean_pilot_0_1_execution_data.csv`;
- `research/climate/climate_ocean_pilot_0_1_execution_results.md`.

Panels:
- (a) frozen `G_E`, `J_heat+`, `J_heat-` horizon values for primary `(12,12)`;
- (b) conservative optimal-subspace angle and `Delta_heat` over six frozen horizons;
- (c) longest-horizon modal supports: energy `(3,2)` versus heat `(4,2)`, with frozen BT/BC diagnostics;
- (d) `J_heat+` versus best heat transport in the energy-optimal subspace, annotated with retained fraction 95.88%.

Witness:
`T/tau_ref=8`: `theta_sub=90 deg`, `Delta_heat=0.0411846`, energy-optimal subspace retains about 95.88% of maximum cumulative poleward heat transport.

Guardrails:
- label as `CLIM-WEAK` / weak contrast;
- angle and performance gap must appear together;
- no claim that energy-optimal perturbations generally fail to transport heat;
- no Primitive-Equation, AMOC, blocking, or forecast-skill inference.

## Figure 5 — Cross-domain synthesis: geometry versus performance

Frozen sources:
- all three frozen execution CSV/result files;
- `research/manuscript/manuscript_draft_0_2.md`, Sec. 5, for wording/roles only.

Panels:
- (a) scatter in dimensionless diagnostic space `(theta,Delta_Q)` using frozen horizon points only;
- (b) frozen role summary: Plasma `P2-A`, Neuro `NEURO-STRONG`, Climate `CLIM-WEAK`;
- (c) representative frozen witnesses: Plasma `T=1`, Neuro 112/224 ms, Climate `T/tau_ref=8`.

Required visual rules:
- distinct domain marker shapes;
- no cross-domain trend line, fit, or implied universal phase diagram;
- vector angles and degenerate-subspace angles must be distinguished in legend/caption;
- Climate longest-horizon point must be identified as the counterexample to angle-only interpretation;
- physical objective magnitudes are never put on a common cross-domain scale.

## Table 1 — Model/objective definition

Sources:
- `research/d10_zf_pilot_0_1_specification.md`;
- `research/neuro/neuro_pilot_specification_0_1.md`;
- `research/climate/climate_ocean_numerical_qualification_0_1.md`;
- `research/climate/climate_ocean_pilot_specification_0_1.md`.

Columns:
Domain; defining model; stability statement; positive metric; signed channel; admissible geometry; input cost; time normalization; horizon ladder; frozen verdict/role.

## Table 2 — Operational study rules and representative outcomes

Sources:
- `research/manuscript/manuscript_draft_0_2.md`, Sec. 2.5;
- frozen pilot specifications and results.

Include:
- study-specific `theta>=20 deg` and `Delta_Q>=0.25` neighboring-horizon rule;
- note that thresholds are operational, not universal constants;
- representative rows for Plasma `T=1`, Neuro 112/224 ms, Climate `T/tau_ref=8`;
- signed negative extremum only where reachable/applicable.

## Reproducibility rule

Future plotting scripts may read the listed frozen CSV/result files and perform presentational transformations only. They must not instantiate model generators, solve new matrix exponentials/eigenproblems, create new horizon values, rerun trajectories, smooth data, or interpolate scientific results. If a desired panel is unsupported by stored frozen data, simplify or omit the panel.

**STOP — figure plan introduces no new scientific calculation.**