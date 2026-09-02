# Neuro Research Status

**Last updated:** 2026-09-02  
**Branch:** `main`

## Current state

The first Neuro demonstrator is frozen as

\[
\boxed{\text{two-source multi-region CMC/DCM: V1 -> V4}}
\]

with primary signed pathway

\[
\boxed{\mathrm{V1\,SP}\rightarrow\mathrm{V4\,SS}}
\]

and

\[
Q_{j\to i}^{\rm CORE}=\frac12(A_{j\to i}^\dagger M+MA_{j\to i}).
\]

The positive metric is **synaptic-filter storage**, not metabolic or thermodynamic brain energy.

## Gate ledger

| Gate / freeze | Result | Consequence |
|---|---|---|
| Neuro Feasibility Gate 0.1 | `N-B` | CMC/DCM and Jansen-Rit survived; metric clarification required. |
| Neuro M-Gate 0.1 | `NM-A` | Pre-CORE positive synaptic-filter storage accepted. |
| Neuro Pilot Candidate Gate 0.1 | `NOMINATED: multi-region CMC/DCM` | Primary channel fixed. |
| Neuro Admissible Input Geometry Gate 0.1 | `NB-A` | Natural rank-2 preparation geometry accepted. |
| Cross-Domain Integration Gate 0.1 | `PASSED` | Released to Pilot Specification only. |
| Neuro Pilot Specification 0.1 | `COMPLETE` | Exact V1/V4 pilot frozen, no CORE effect inspected. |
| Cross-Domain Pilot Freeze 0.1 | `STABLE` | **Pilot Execution 0.1 authorized under committed MASTER prompt.** |

## Frozen Pilot 0.1 tuple

```text
model                  = 2-source multi-region CMC/DCM
source j               = macaque V1
source i               = macaque V4
primary channel        = V1 SP -> V4 SS
state dimension        = 16
operating point        = x* = 0
propagation delays     = disabled for this autonomous ODE pilot
M                      = frozen synaptic-filter storage
Q                      = frozen V1-SP -> V4-SS pathway storage-rate contribution
pulse width            = 1 ms
pre-observation delays = (2 ms, 16 ms)
R_in                    = I_2 in pulse-amplitude input coordinates
rank(B)                 = 2
kappa_2(M^1/2 B)        = 34.2940
tau_ref                 = 28 ms
horizon ladder          = (7,14,28,56,112,224) ms
alpha(A)                = -33.0964092356 s^-1
```

All exact matrices, state ordering, pulse columns and numerical qualification are in:

`research/neuro/neuro_pilot_specification_0_1.md`

## Active instruction

**Status:** `EXECUTION AUTHORIZED — FROZEN`

**Next instruction:**

`research/master/prompts/neuro_pilot_execution_0_1.md`

Under `research/master/prompt_handoff_protocol_0_1.md`, a bare `GO` in the Neuro branch must read and execute that committed instruction exactly.

The execution may compute the frozen `K_M(T)`, `K_Q(T)`, signed extrema, optimizer comparison, physical diagnostics and verdict, but may not retune any frozen object after the first effect quantity is inspected.

## Required return state

After execution, write the canonical results and data, update this file to

`EXECUTION COMPLETE — RETURN TO MASTER FOR RESULT INTEGRATION`,

commit, and STOP.

## Canonical documents

- `research/neuro/neuro_admissible_input_geometry_gate_0_1.md`
- `research/neuro/neuro_pilot_specification_0_1.md`
- `research/master/cross_domain_integration_gate_0_1.md`
- `research/master/cross_domain_pilot_freeze_0_1.md`
- `research/master/prompts/neuro_pilot_execution_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`
