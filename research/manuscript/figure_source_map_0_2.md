# Figure Source Map 0.2

**Status:** CANONICAL SUPPORT FOR MANUSCRIPT REVISION 0.3  
**Authority:** `research/master/manuscript_structure_freeze_0_2.md`  
**Primary draft:** `research/manuscript/manuscript_draft_0_3.md`  
**Rule:** every panel and table must use only frozen data or frozen analytical definitions. No new simulation, eigensolve, matrix-exponential evaluation, trajectory, horizon, parameter point, pathway, objective, admissible geometry, interpolation, smoothing, fit, or model calculation is allowed.

## Main Figure 1 — Common workflow and domain semantics

**Purpose:** introduce the shared diagnostic layer without implying common physical semantics.

**Panels / content:**
- (a) frozen tuple `(A,M,Q,B,R_in)` and admissible preparation `x(0)=B R_in^{-1/2} w`;
- (b) terminal positive-objective operator and cumulative signed-channel operator;
- (c) geometry diagnostic `theta` / subspace angle versus target-performance diagnostic `Delta_Q`, with robustness shown as a separate gate;
- (d) domain-semantics summary for the three robust main-text domains: Plasma free energy / particle transport; Neuro synaptic-filter storage / V1-SP -> V4-SS pathway contribution; Climate-A QG energy / eddy heat transport.

**Frozen sources:**
- `research/manuscript/manuscript_draft_0_3.md`, Sec. 2;
- `research/master/manuscript_structure_freeze_0_2.md`;
- `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`.

**Guardrails:**
- commonality is methodological, not physical;
- define “physical channel” broadly as signed transport/exchange/pathway contribution;
- Neuro must be labeled “synaptic-filter storage”, never “brain energy”;
- do not include Climate-B as a fourth robust application domain in the principal semantics panel.

## Main Figure 2 — Plasma strong anchor

**Frozen sources:**
- `research/d10_zf_pilot_0_2_execution_data.csv`;
- `research/d10_zf_pilot_0_2_execution_results.md`;
- `research/d10_zf_pilot_0_1_specification.md` for model/basis definitions only.

**Permitted panels:**
- (a) frozen horizon values `G_E`, `J_Gamma+`, `J_Gamma-` at one stored display resolution, with resolution convergence stated in the caption;
- (b) `theta(T)` and `Delta_Gamma(T)` over the six frozen horizons;
- (c) frozen Fourier-mode weight distributions at `T=1` if supported directly by stored frozen result data;
- (d) direct-trajectory endpoint summary at `T=1` unless a full stored frozen time series exists. Do not reconstruct a scientific time series.

**Representative witness:**
`T=1`: `G_E=1.8783`, `J_Gamma+=0.3535`, `J_Gamma-=-0.1462`, `theta=53.40 deg`, `Delta_Gamma=0.5043`.

**Caption guardrails:**
- stable controlled D10-ZF benchmark;
- negative signed branch shown explicitly where displayed;
- no first-transient-growth, nonlinear-turbulence, experimental, or universality claim;
- resolution statement limited to frozen `K=32,64,96` and common resolved subspace.

## Main Figure 3 — Neuro constrained two-pulse result

**Frozen sources:**
- `research/neuro/neuro_pilot_0_1_execution_data.csv`;
- `research/neuro/neuro_pilot_0_1_execution_results.md`;
- `research/neuro/neuro_pilot_specification_0_1.md` for pathway and pulse geometry only.

**Permitted panels:**
- (a) V1/V4 CMC schematic with highlighted V1-SP -> V4-SS pathway and the two fixed V1-SS afferent preparation pulses;
- (b) `theta(T)` and `Delta_Q(T)` over 7, 14, 28, 56, 112, 224 ms;
- (c) unit-cost pulse-coordinate arrows `w_M` and `w_Q` at 112 and 224 ms with equal aspect ratio;
- (d) compact frozen-value inset/table for the 112/224-ms witnesses if needed.

**Witnesses:**
- 112 ms: `theta=46.824 deg`, `Delta_Q=0.529017`, `w_M=(+0.768725,+0.639580)`, `w_Q=(+0.992410,-0.122974)`;
- 224 ms: `theta=65.058 deg`, `Delta_Q=0.817841`, `w_M=(+0.530000,+0.847998)`, `w_Q=(+0.992410,-0.122972)`.

**Guardrails:**
- pulse amplitudes are fixed preparation coordinates, not an optimized time-dependent waveform;
- preserve pulse sign;
- do not depict an experimentally reachable negative cumulative pathway branch: the frozen admissible minimum is positive;
- neural storage is model-internal synaptic-filter storage only.

## Main Figure 4 — Climate-A robust weak contrast

**Frozen sources:**
- `research/climate/climate_ocean_pilot_0_1_execution_data.csv`;
- `research/climate/climate_ocean_pilot_0_1_execution_results.md`;
- `research/climate/climate_ocean_numerical_qualification_0_1.md` and `research/climate/climate_ocean_pilot_specification_0_1.md` for definitions only.

**Permitted panels:**
- (a) frozen `G_E`, `J_heat+`, `J_heat-` horizon values for primary `(12,12)`;
- (b) conservative optimal-subspace angle and `Delta_heat` over the six frozen horizons;
- (c) longest-horizon modal supports: Energy `(3,2)` versus Heat `(4,2)`, with stored BT/BC diagnostics;
- (d) `J_heat+` versus best heat transport inside the energy-optimal subspace, annotated with retained fraction 95.88%.

**Witness:**
`T/tau_ref=8`: `theta_sub=90 deg`, `Delta_heat=0.0411846`; energy-optimal subspace retains about 95.88% of maximum cumulative poleward heat transport.

**Guardrails:**
- label as `CLIM-WEAK` / robust weak contrast;
- geometry and target-performance gap must appear together;
- state that all six frozen horizons pass the prescribed refinement protocol if robustness is discussed;
- no claim that energy-optimal perturbations generally fail to transport heat;
- no Primitive-Equation, AMOC, blocking, climate-change, or forecast-skill inference.

## Main Figure 5 — Cross-domain robust geometry/performance summary

**Purpose:** summarize the three robust domains without constructing a phase diagram or implying a universal cross-domain law.

**Frozen sources:**
- Plasma: `research/d10_zf_pilot_0_2_execution_data.csv` and execution result;
- Neuro: `research/neuro/neuro_pilot_0_1_execution_data.csv` and execution result;
- Climate-A: `research/climate/climate_ocean_pilot_0_1_execution_data.csv` and execution result;
- wording/roles: `research/master/manuscript_structure_freeze_0_2.md` and Draft 0.3 Sec. 5.1.

**Frozen presentation:**
Use a **non-inferential paired summary** of geometry and performance. Acceptable implementations include:
- paired horizontal or vertical diagnostic strips, one for optimizer/subspace angle and one for target-performance gap;
- aligned domain rows with representative frozen witnesses and, where readable, the six stored horizon points;
- side-by-side small multiples showing geometry and performance separately for each domain.

The summary must preserve the distinction between vector angles and degenerate-subspace angles. Representative witnesses are Plasma `T=1`, Neuro 112/224 ms, and Climate-A `T/tau_ref=8`.

**Required visual rules:**
- no phase-diagram framing, decision regions, trend lines, fits, regression, correlation claims, universal boundary, or cross-domain law;
- no physical objective magnitudes on a common cross-domain scale;
- Climate-A longest-horizon witness must make the angle-versus-performance contrast visually clear;
- Climate-B fixed-resolution points are **excluded** from this robust-domain summary;
- caption may direct the reader to Supplement S5 for the rejected Climate-B robustness audit.

## Main Table 1 — Model/objective/admissible-geometry definitions

**Frozen sources:**
- `research/d10_zf_pilot_0_1_specification.md`;
- `research/neuro/neuro_pilot_specification_0_1.md`;
- `research/climate/climate_ocean_numerical_qualification_0_1.md`;
- `research/climate/climate_ocean_pilot_specification_0_1.md`;
- Draft 0.3 Sec. 2.6.

**Rows:** Plasma, Neuro, Climate-A only.

**Columns:** domain; defining model; positive metric; signed channel; admissible geometry/input cost; time normalization as space permits; frozen role.

**Guardrails:** preserve distinct physical semantics. Climate-B is not a fourth row in the main robust-domain definition table.

## Supplement Table S1 / former Main Table 2 — Operational study rules and representative outcomes

**Frozen sources:**
- Draft 0.3 Sec. 2.5 and Supplement S6;
- frozen pilot specifications and results;
- `research/master/manuscript_structure_freeze_0_2.md`.

**Include:**
- study-specific `theta>=20 deg` and `Delta_Q>=0.25` neighboring-horizon rule;
- explicit note that thresholds are operational, not universal constants;
- Plasma `T=1`, Neuro 112/224 ms, Climate-A `T/tau_ref=8` representative outcomes;
- Climate-B row only if labeled unambiguously `CLIM-B-FAIL — resolution robustness`.

## Supplement S5 Figure/Table — Climate-B one-shot robustness rejection

**Purpose:** document why a striking fixed-resolution effect was rejected by the pre-specified refinement protocol.

**Frozen sources only:**
- `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv`;
- `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_results.md`;
- `research/climate/climate_intra_domain_contrast_pilot_specification_0_1.md` for thresholds/roles;
- `research/climate/climate_intra_domain_contrast_numerical_qualification_0_1.md` for passed pre-effect gates;
- `research/master/climate_intra_domain_contrast_result_integration_freeze_0_1.md` for the frozen verdict.

**Preferred compact content, only if supported directly by stored frozen data:**
- objective-value convergence across primary `(16,32)`, confirmation `(20,40)`, high `(24,48)` for all six horizons;
- captured common-space mass and/or cross-resolution principal-angle failure for Energy and Shift optima;
- horizon-by-horizon robust `FAIL` status, explicitly `0/6` robust;
- optional same-resolution `Delta_shift=1` / large-angle / parity observation **only if the same panel or caption labels it `CLIM-B-FAIL — resolution robustness failure` and states that refinement failed**.

**Required guardrails:**
- visually separate “local algebraic/direct gates passed” from “cross-resolution gates failed”;
- no plot may imply a robust strong Climate-B effect;
- no isolated `90 deg` or `Delta_shift=1` annotation without same-context failure qualification;
- no interpolation, smoothing, extra resolution, new horizon, re-evaluation, or reconstructed scientific trajectory;
- no repair scenario, hyperdiffusion comparison, scale-selective-damping comparison, alternative channel, mask, EOF, or third Climate candidate.

## Supplement sections and source placement

- **S1 — Analysis freeze chronology and reproducibility protocol:** committed freeze/specification files only; no reconstructed chronology beyond version-controlled record.
- **S2 — Plasma details:** frozen Plasma specification/result/data.
- **S3 — Neuro details:** frozen Neuro specification/result/data.
- **S4 — Climate-A details:** frozen Climate-A qualification/specification/result/data.
- **S5 — Climate-B robustness rejection:** frozen Climate-B candidate/qualification/specification/result/data plus integration freeze.
- **S6 — Additional frozen-data tables / citation metadata:** frozen data and approved bibliography only.

## Reproducibility rule

Future plotting scripts may read the listed frozen CSV/result files and perform presentational transformations only. They must not instantiate model generators, solve new matrix exponentials or eigenproblems, create new horizons, rerun trajectories, smooth/interpolate scientific results, or fit cross-domain relationships. If a desired panel is not directly supported by frozen stored data, simplify or omit it.

**STOP — Figure Source Map 0.2 introduces no new scientific calculation or figure production.**
