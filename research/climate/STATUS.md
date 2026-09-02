# Climate/Ocean Branch Status

## Current state

- Feasibility Gate 0.1: `PASSED`.
- Pilot Candidate Freeze 0.1: `STABLE`.
- Numerical Qualification 0.1: `QUALIFIED`.
- Cross-Domain Integration Gate 0.1: `PASSED`.
- Pilot Specification 0.1: `COMPLETE`.
- Cross-Domain Pilot Freeze 0.1: `STABLE`.
- **Pilot Execution 0.1: AUTHORIZED under committed MASTER prompt.**

## Frozen pilot

The Climate/Ocean pilot remains the damped two-layer Phillips-QG channel with

\[
(A_K,M_K,Q_{{\rm heat},K},B=I,R_{\rm in}=M_K)
\]

on the balanced QG eddy state space with zonal periodicity, meridional Dirichlet streamfunction conditions, and all `k_x=0` modes excluded.

The positive signed convention remains northward/poleward eddy heat transport and

\[
J_{\rm heat}(T)=\int_0^T x^\dagger Q_{{\rm heat},K}x\,dt.
\]

## Frozen numerical qualification

\[
\tau_{\rm ref}=0.7233796296\,\mathrm d,
\qquad
\alpha(A_K)=-0.1\,\mathrm d^{-1}<0
\]

at every qualified resolution.

The fixed ladder is

\[
(M_x,N_y)=(4,4),(8,8),(12,12),(16,16),(24,24).
\]

Resolution roles are frozen as:

- `(4,4)` qualification-only smoke;
- `(8,8)` coarse audit;
- `(12,12)` **primary**;
- `(16,16)` **confirmation**;
- `(24,24)` **high-resolution audit**.

The horizon ladder remains

\[
T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}.
\]

All matrix assembly, numerical methods, tolerance gates, resolution-robustness rules, degeneracy handling, physical diagnostics, operational thresholds and verdict classes are frozen in:

`research/climate/climate_ocean_pilot_specification_0_1.md`

No frozen physical parameter, basis, resolution role, horizon or verdict rule may be changed after the first CORE-effect quantity is inspected.

## Active instruction

**Status:** `EXECUTION AUTHORIZED — FROZEN`

**Next instruction:**

`research/master/prompts/climate_ocean_pilot_execution_0_1.md`

Under `research/master/prompt_handoff_protocol_0_1.md`, a bare `GO` in the Climate/Ocean branch must read and execute that committed instruction exactly.

The execution is now authorized to compute the frozen `K_E(T)`, `K_heat(T)`, signed extrema, optimizer/eigenspace comparison, resolution audit, physical diagnostics and exactly one preregistered Climate verdict.

## Required return state

After execution, write the canonical results and data, update this file to

`EXECUTION COMPLETE — RETURN TO MASTER FOR RESULT INTEGRATION`,

commit, and STOP.

## Canonical documents

- `research/climate/climate_ocean_numerical_qualification_0_1.md`
- `research/climate/climate_ocean_pilot_specification_0_1.md`
- `research/master/cross_domain_integration_gate_0_1.md`
- `research/master/cross_domain_pilot_freeze_0_1.md`
- `research/master/prompts/climate_ocean_pilot_execution_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`
