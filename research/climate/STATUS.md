# Climate/Ocean Branch Status

## Current state

### Climate-A — existing frozen pilot

- Feasibility Gate 0.1: `PASSED`.
- Pilot Candidate Freeze 0.1: `STABLE`.
- Numerical Qualification 0.1: `QUALIFIED`.
- Cross-Domain Integration Gate 0.1: `PASSED`.
- Pilot Specification 0.1: `COMPLETE`.
- Cross-Domain Pilot Freeze 0.1: `STABLE`.
- Pilot Execution 0.1: `COMPLETE`.
- Cross-Domain Result Integration & Freeze 0.1: `STABLE`.
- Frozen verdict: `CLIM-WEAK`.

Climate-A remains the damped two-layer Phillips-QG heat-transport pilot and is permanently frozen against retuning.

At `T/tau_ref=8`,

\[
(|m|,n)_E=(3,2),\qquad (|m|,n)_{heat}=(4,2),
\]

\[
\vartheta_{sub}=90^\circ,\qquad \Delta_{heat}=0.04118455338,
\]

so the energy-optimal subspace retains approximately 95.88% of maximum cumulative poleward heat transport.

### Climate-B — one-shot intra-domain contrast branch

`Climate Intra-Domain Contrast Feasibility Gate 0.1` has passed.

Nominated candidate only:

\[
\boxed{\text{equivalent-barotropic midlatitude Bickley jet}}
\]

with

- positive objective: barotropic perturbation kinetic energy;
- signed physical channel: eddy-induced forcing of the infinitesimal poleward jet-translation coordinate, obtained by projecting eddy momentum-flux convergence onto `g(y)=-U'(y)`;
- provisional admissible eddy geometry: `B=I`, `R_in=M`;
- exactly one nominated dimensional point from the feasibility gate;
- no CORE-effect quantity inspected yet.

Hard rule: Climate-B is one additional attempt only. If it fails qualification or later returns weak/null, no third Climate candidate is authorized before the first manuscript.

## Active instruction

**Status:** `CLIMATE-B CANDIDATE FREEZE AUTHORIZED — AWAIT GO`

**Next instruction:**

`research/master/prompts/climate_intra_domain_contrast_candidate_freeze_0_1.md`

A bare `GO` in the Climate chat must read and execute that committed instruction exactly.

The Candidate Freeze may define/freeze the physical and numerical representation but must not compute `K_M`, `K_shift`, optimizer directions/subspaces, angles, gaps or any objective-separation quantity.

## Manuscript dependency

`Manuscript Structure Freeze 0.2` is on HOLD pending resolution of this one-shot Climate-B branch. It is not canceled and remains the mandatory return point.

## Canonical documents

Climate-A:

- `research/climate/climate_ocean_numerical_qualification_0_1.md`
- `research/climate/climate_ocean_pilot_specification_0_1.md`
- `research/climate/climate_ocean_pilot_0_1_execution_results.md`
- `research/climate/climate_ocean_pilot_0_1_execution_data.csv`

Climate-B governance:

- `research/master/climate_intra_domain_contrast_feasibility_gate_0_1.md`
- `research/master/prompts/climate_intra_domain_contrast_candidate_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / AWAIT GO.**