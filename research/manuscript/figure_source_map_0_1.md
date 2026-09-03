# Figure Source Map 0.1

**Status:** CANONICAL DRAFT SUPPORT  
**Authority:** `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`  
**Rule:** every panel must be generated only from already frozen data or frozen analytical definitions. No new simulation, horizon, parameter point, pathway, objective, admissible geometry, or resolution is allowed.

## Figure 1 — Common workflow and semantic separation

### Purpose
Introduce the transferable analysis pipeline without implying that the three domains share the same physical meaning.

### Panels
- **(a)** schematic tuple `C=(A,M,Q,B,R_in)` and flow `x(0)=BR_in^{-1/2}w -> e^{At}x(0)`.
- **(b)** two finite-time operators `K_M(T)` and `K_Q(T)` with positive-objective optimizer and signed-channel optimizer.
- **(c)** diagnostic pair: optimizer/subspace angle `theta` and performance gap `Delta_Q`.
- **(d)** domain-semantics table: Plasma free energy / particle transport; Neuro synaptic-filter storage / V1-SP -> V4-SS pathway contribution; Climate QG energy / eddy heat transport.

### Sources
- `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`
- `research/master/cross_domain_result_integration_freeze_0_1.md`

### Transformation
Purely diagrammatic typesetting of already frozen definitions. No numerical transformation.

### Caption guardrail
State that the commonality is methodological, not physical. Explicitly avoid “brain energy” for Neuro.

---

## Figure 2 — Plasma strong anchor

### Purpose
Show modal stability, finite-time free-energy growth, signed particle-transport extrema, and robust energy-vs-transport nonredundancy.

### Frozen sources
- `research/d10_zf_pilot_0_2_execution_data.csv`
- `research/d10_zf_pilot_0_2_execution_results.md`

### Panels
- **(a)** horizon curves `G_E(T)`, `G_Gamma,+`, and `G_Gamma,-` at primary display resolution (use one frozen resolution because scalar values are resolution-converged; note all three in caption).
- **(b)** `theta(T)` and `Delta_Gamma(T)` over the six frozen horizons, preferably dual aligned axes or two stacked presentation panels if journal style requires; do not invent interpolation.
- **(c)** dominant Fourier-mode weight distributions for energy- and transport-optimal directions at frozen `T=1`.
- **(d)** representative direct trajectories at `T=1` or the complete frozen horizon endpoint summary: modal vs energy-optimal vs transport-optimal, using already stored direct-trajectory data if present. If the CSV does not contain full time series, use only endpoint/table values already in the result report; do not rerun trajectories.

### Presentational transformations
- logarithmic or linear plotting may be chosen solely for legibility;
- normalization may use the already frozen energy-whitened convention;
- no smoothing, fitted curves, or interpolation beyond connecting frozen discrete points for visual guidance.

### Caption-level quantitative witness
At `T=1`: `G_E=1.8783`, `J_Gamma+=0.3535`, `J_Gamma-=-0.1462`, `theta=53.40°`, `Delta_Gamma=0.5043`.

### Guardrails
- call this a stable controlled D10-ZF benchmark;
- do not claim first plasma transient growth;
- do not imply nonlinear turbulence or experiment;
- report signed negative branch explicitly.

---

## Figure 3 — Neuro strong constrained-preparation result

### Purpose
Show that two objectives select experimentally interpretable different two-pulse preparations within the same frozen rank-two admissible geometry.

### Frozen sources
- `research/neuro/neuro_pilot_0_1_execution_data.csv`
- `research/neuro/neuro_pilot_0_1_execution_results.md`
- `research/neuro/neuro_pilot_specification_0_1.md` for pulse timing / coordinate definitions only.

### Panels
- **(a)** schematic of V1 -> V4 CMC source pair with highlighted V1-SP -> V4-SS pathway and two V1-SS afferent preparation pulses ending 2 ms and 16 ms before observation.
- **(b)** `theta(T)` and `Delta_Q(T)` at the six frozen horizons 7, 14, 28, 56, 112, 224 ms.
- **(c)** two-dimensional pulse-coordinate vectors `w_M` and `w_Q` at 112 ms and 224 ms, shown as arrows in the `(h1,h2)` plane.
- **(d)** optionally terminal storage `G_M` and `J_Q+` across the frozen horizon ladder if needed for scale context; if space is limited, replace with a compact table inset giving 112/224-ms numerical witnesses.

### Presentational transformations
- arrow normalization is already unit input cost; preserve sign.
- pulse-coordinate plane may be drawn with equal aspect ratio.
- no synthetic pulse waveforms beyond the frozen 1-ms schematic timing.

### Caption-level quantitative witnesses
- 112 ms: `theta=46.824°`, `Delta_Q=0.529017`, `w_M=(+0.768725,+0.639580)`, `w_Q=(+0.992410,-0.122974)`.
- 224 ms: `theta=65.058°`, `Delta_Q=0.817841`, `w_M=(+0.530000,+0.847998)`, `w_Q=(+0.992410,-0.122972)`.

### Guardrails
- metric label must be “synaptic-filter storage”, not “brain/metabolic energy”;
- do not show or imply a reachable negative cumulative pathway branch: the frozen admissible `K_Q` minimum is positive over the horizon ladder;
- do not call the pulse coordinates an optimized time-dependent control waveform; they are fixed preparation-pulse amplitudes followed by autonomous dynamics.

---

## Figure 4 — Climate weak contrast

### Purpose
Demonstrate that large optimizer/subspace separation can coexist with small target-performance loss.

### Frozen sources
- `research/climate/climate_ocean_pilot_0_1_execution_data.csv`
- `research/climate/climate_ocean_pilot_0_1_execution_results.md`

### Panels
- **(a)** horizon curves of `G_E`, `J_heat+`, and `J_heat-` for the primary `(12,12)` resolution.
- **(b)** conservative optimal-subspace angle and `Delta_heat` over the six frozen horizons.
- **(c)** modal-support diagram at `T/tau_ref=8`: energy `(3,2)` versus heat `(4,2)`, with barotropic/baroclinic fractions from the frozen diagnostics.
- **(d)** target-performance comparison at the longest horizon: `J_heat+` versus best heat transport attainable within the energy-optimal subspace; annotate retained fraction 95.88%.

### Optional presentational inset
Use the already frozen signed heat-flux history information at `T/tau_ref=8` only if the stored result file contains sufficient sampled data. If only summary values are stored, report the one late sign change and integrated positive/negative contributions textually; do not recompute a time series.

### Caption-level witnesses
At `T/tau_ref=8`: energy support `(3,2)`, heat support `(4,2)`, `theta_sub=90°`, `Delta_heat=0.0411846`, energy optimum retains ~95.88% of maximum cumulative poleward heat transport.

### Guardrails
- label result `CLIM-WEAK` / weak contrast;
- never imply that energy-optimal perturbations generally fail to transport heat;
- no Primitive-Equation, AMOC, blocking, or forecast-skill inference;
- angle must be shown with performance gap in the same figure/caption.

---

## Figure 5 — Cross-domain synthesis: geometry versus performance

### Purpose
Make the paper's central physical/methodological insight visible without pretending the domain metrics are dimensionally comparable.

### Frozen sources
- Plasma CSV/result report
- Neuro CSV/result report
- Climate CSV/result report
- claim freeze for roles and semantics

### Recommended panel logic
- **(a)** scatter plot in dimensionless diagnostic space `(theta, Delta_Q)` using only frozen horizon points. Use distinct marker shapes by domain; do not connect domains as if they were one physical trajectory.
- **(b)** role summary showing frozen verdicts: Plasma `P2-A`, Neuro `NEURO-STRONG`, Climate `CLIM-WEAK`.
- **(c)** one representative witness per domain, selected by preregistered/frozen logic rather than effect maximization: Plasma `T=1`, Neuro 112 and 224 ms adjacent supporting pair, Climate `T/tau_ref=8` contrast point.

### Presentational transformation
`theta` and `Delta` are already dimensionless/common diagnostics. No rescaling of physical objective values across domains is permitted.

### Caption guardrail
The plot compares diagnostic geometry/performance only. It does **not** place free energy, synaptic-filter storage, and QG energy on a common physical scale. Highlight the Climate point as the counterexample to “large angle implies large performance loss.”

---

## Table 1 — Frozen model/objective summary

### Sources
- manuscript claim freeze
- each pilot specification/result report

### Columns
Domain; model; spectral-stability statement; positive metric; signed channel; admissible geometry; input cost; horizon ladder; frozen verdict; role.

### Guardrail
Use domain-specific semantics verbatim.

---

## Table 2 — Representative quantitative witnesses

### Sources
All three frozen execution result reports.

### Suggested rows
- Plasma `T=1`.
- Neuro 112 ms.
- Neuro 224 ms.
- Climate `T/tau_ref=8`.

### Columns
Domain/horizon; optimizer angle/subspace angle; positive-channel optimum; channel value at positive-objective optimum; performance gap; signed negative extremum where reachable/applicable; interpretation.

### Guardrail
For Neuro, note that cumulative negative extremum is not reachable on the frozen preparation space; do not force a signed-negative entry for symmetry.

---

## Reproducibility rule for all plots

Plotting scripts, when created later, may only read the listed frozen `.csv` / result files and apply presentational transformations. They must not instantiate model generators, call matrix exponentials to create new horizon values, solve new eigenproblems, or rerun trajectories. If a requested panel is not supported by stored frozen data, the panel must be simplified rather than recalculated.

**STOP — figure plan introduces no new scientific calculation.**
