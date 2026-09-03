# Frozen-Data Figure Captions 0.1

**Authority:** `research/manuscript/figure_source_map_0_2.md`  
**Target packaging:** Physical Review E Regular Article  
**Rule:** frozen evidence only; no interpolated or recomputed scientific values.

## Main Figure 1 — Common workflow and domain semantics

**Figure 1. Common frozen-data workflow.** The shared methodological layer freezes the linear generator `A`, positive metric `M`, signed channel `Q`, admissible preparation map `B`, and input-cost metric `R_in` before objective-separation evaluation. Terminal positive-objective and cumulative signed-channel optima are compared using optimizer/subspace geometry and target-performance loss, after which numerical/direct and prescribed robustness gates are applied. The three principal domains retain distinct physical semantics: Plasma free energy versus radial particle transport; Neuro model-internal synaptic-filter storage versus the V1-SP -> V4-SS pathway contribution to storage rate; and Climate-A QG perturbation energy versus poleward eddy heat transport. Climate-B is not a fourth robust application; it is the Supplement S5 robustness-rejection case.

## Main Figure 2 — Plasma strong anchor

**Figure 2. Plasma strong anchor (`P2-A`).** Frozen six-horizon D10-ZF values are shown using the stored `K=32` display rows; the tested `K=32,64,96` ladder agrees on the common resolved subspace for the reported objective-separation quantities. The left panel separates optimizer geometry (`theta/90`) from the particle-transport performance gap `Delta_Gamma`; the right panel retains both positive and negative extrema of the signed cumulative particle-transport objective. The frozen `T=1` witness has `G_E=1.8783`, `theta=53.40 deg`, and `Delta_Gamma=0.5043`, so the free-energy optimum misses about 50.4% of the maximum positive cumulative particle transport. This is a stable controlled benchmark, not a claim of first plasma transient growth, nonlinear turbulence, experiment, or universality.

## Main Figure 3 — Neuro constrained two-pulse result

**Figure 3. Neuro constrained two-pulse result (`NEURO-STRONG`).** The left panel shows the stored six-horizon optimizer angle and pathway-performance gap for the frozen rank-two preparation geometry. The right panels compare unit-cost pulse-coordinate directions at 112 and 224 ms. The pathway-optimal direction retains the stored negative second pulse coordinate, while the storage-optimal directions are different. Pulse amplitudes are coordinates of two fixed 1-ms afferent V1-SS preparations ending 2 and 16 ms before observation; they are not a time-dependent optimal-control waveform. The signed channel is the V1-SP -> V4-SS contribution to the selected synaptic-filter storage-rate balance. No experimentally reachable negative cumulative pathway branch is depicted because the frozen admissible minimum is positive. Witnesses: 112 ms, `theta=46.824 deg`, `Delta_Q=0.529017`; 224 ms, `theta=65.058 deg`, `Delta_Q=0.817841`.

## Main Figure 4 — Climate-A robust weak contrast

**Figure 4. Climate-A robust weak geometry-versus-performance contrast (`CLIM-WEAK`).** All six frozen horizons pass the prescribed primary/confirmation/high-resolution refinement protocol. The left panel displays conservative optimal-subspace angle and heat-performance gap separately. At the longest frozen horizon, `T/tau_ref=8`, the energy optimum occupies `(|m|,n)=(3,2)` while the poleward-heat optimum occupies `(4,2)`; the conservative subspace angle is `90 deg`. Despite that sharp geometric difference, `Delta_heat=0.0411846`, and the energy-optimal subspace retains about 95.88% of the maximum cumulative poleward heat transport (`J_heat+=1.54449`, best heat performance within the energy-optimal subspace `=1.48088`). The result is an idealized QG contrast only; no Primitive-Equation, AMOC, blocking, climate-change, forecast-skill, or generic energy-optimization-failure inference is made.

## Main Figure 5 — Cross-domain robust summary

**Figure 5. Non-inferential cross-domain geometry/performance summary.** Representative frozen robust-domain witnesses are aligned on separate geometry and target-performance axes: Plasma `T=1`; Neuro 112 and 224 ms; and Climate-A `T/tau_ref=8`. The two diagnostics are deliberately separated; no trend line, fit, regression, threshold region, phase diagram, universal boundary, correlation claim, or common physical-objective scale is implied. Climate-B fixed-resolution points are excluded because that one-shot case failed the frozen refinement protocol; see Supplement Fig. S5.

## Supplement Figure S5 — Climate-B robustness rejection

**Supplement Fig. S5. Climate-B one-shot robustness rejection.** The frozen Bickley-jet execution passed the local algebraic, eigensolver/PSD, finite-time-integral cross-check, and direct physical-reproduction gates, but failed the independently frozen cross-resolution physical-claim criteria. The signed-objective refinement discrepancy exceeds the `0.02` limit and captured common-space optimizer mass remains below the `0.95` minimum at all verdict-relevant refinements; zero of six frozen horizons is resolution robust. Attractive fixed-truncation observations, including `Delta_shift=1` and large optimizer angles, are therefore rejected as robust Climate-B evidence. Frozen verdict: **`CLIM-B-FAIL — resolution robustness failure`**. No repair, extra resolution, retuning, alternative channel/admissible geometry, scale-selective damping comparison, or third Climate candidate is part of this package.
