# Neuro Research Status

**Last updated:** 2026-09-02  
**Branch:** `main`

## Current state

The first frozen Neuro execution is complete.

\[
\boxed{\text{two-source multi-region CMC/DCM: V1 -> V4}}
\]

Primary signed pathway:

\[
\boxed{\mathrm{V1\,SP}\rightarrow\mathrm{V4\,SS}}
\]

with

\[
Q_{j\to i}^{\rm CORE}
=
\frac12(A_{j\to i}^\dagger M+MA_{j\to i}).
\]

The positive metric remains **synaptic-filter storage**, not metabolic or thermodynamic brain energy.

## Gate / execution ledger

| Gate / freeze | Result | Consequence |
|---|---|---|
| Neuro Feasibility Gate 0.1 | `N-B` | CMC/DCM and Jansen-Rit survived; metric clarification required. |
| Neuro M-Gate 0.1 | `NM-A` | Pre-CORE positive synaptic-filter storage accepted. |
| Neuro Pilot Candidate Gate 0.1 | `NOMINATED: multi-region CMC/DCM` | Primary channel fixed. |
| Neuro Admissible Input Geometry Gate 0.1 | `NB-A` | Natural rank-2 preparation geometry accepted. |
| Cross-Domain Integration Gate 0.1 | `PASSED` | Released to Pilot Specification. |
| Neuro Pilot Specification 0.1 | `COMPLETE` | Exact V1/V4 pilot frozen without CORE-effect inspection. |
| Cross-Domain Pilot Freeze 0.1 | `STABLE` | Pilot Execution 0.1 authorized. |
| Neuro Pilot Execution 0.1 | `NEURO-STRONG` | Execution complete; return to MASTER for result integration. |

## Frozen Pilot 0.1 tuple

```text
model                  = 2-source multi-region CMC/DCM
source j               = macaque V1
source i               = macaque V4
primary channel        = V1 SP -> V4 SS
state dimension        = 16
operating point        = x* = 0
propagation delays     = disabled
M                      = frozen synaptic-filter storage
Q                      = frozen V1-SP -> V4-SS pathway storage-rate contribution
pulse width            = 1 ms
pre-observation delays = (2 ms, 16 ms)
R_in                    = I_2 in pulse-amplitude input coordinates
rank(B)                 = 2
kappa_2(M^1/2 B)        = 34.2939603
tau_ref                 = 28 ms
horizon ladder          = (7,14,28,56,112,224) ms
alpha(A)                = -33.0964092356 s^-1
```

## Execution result

All frozen structural and numerical gates passed.

The preregistered simultaneous demonstration thresholds

\[
\vartheta\ge20^\circ,
\qquad
\Delta_Q\ge0.25
\]

are met at the neighboring horizons `112 ms` and `224 ms`.

Key values:

```text
112 ms:
theta   = 46.824271 deg
Delta_Q = 0.529017

224 ms:
theta   = 65.058256 deg
Delta_Q = 0.817841
```

The pathway-optimal preparation uses approximately

```text
w_Q = (+0.99241, -0.12297)
```

at both long horizons, while the terminal-storage optimum uses same-sign pulse mixtures and shifts toward the older pulse:

```text
112 ms: w_M = (+0.76872, +0.63958)
224 ms: w_M = (+0.53000, +0.84800)
```

The unique frozen verdict is

\[
\boxed{\text{NEURO-STRONG}}.
\]

## Canonical execution outputs

- `research/neuro/neuro_pilot_0_1_execution_results.md`
- `research/neuro/neuro_pilot_0_1_execution_data.csv`
- `tests/test_neuro_pilot_0_1.py`
- `research/neuro/neuro_pilot_specification_0_1.md`

## Active instruction

**Status:** `EXECUTION COMPLETE — RETURN TO MASTER FOR RESULT INTEGRATION`

**Next instruction:** `RETURN TO MASTER FOR RESULT INTEGRATION`

Under `research/master/prompt_handoff_protocol_0_1.md`, another bare `GO` in this Neuro branch must not open a new analysis, parameter study, model extension, pathway extension, delay extension, MODES/CONT/CASCADE task, or additional CORE execution.

MASTER must perform the next result-level cross-domain integration/freeze.

**STOP.**
