# Neuro Research Status

**Last updated:** 2026-09-02  
**Branch:** `main`

## Current candidate

The only nominated first Neuro demonstrator remains

\[
\boxed{\text{multi-region CMC/DCM}}.
\]

The concrete Pilot-Specification instantiation is now frozen as a two-source macaque visual hierarchy

\[
\boxed{j=\mathrm{V1},\qquad i=\mathrm{V4}}.
\]

The primary physiological signed channel remains

\[
\boxed{\mathrm{V1\,SP}\rightarrow\mathrm{V4\,SS}}
\]

with

\[
Q_{j\to i}^{\rm CORE}
=
\frac12(A_{j\to i}^{\dagger}M+MA_{j\to i}).
\]

The positive state/storage metric is the pre-CORE synaptic-filter storage fixed by the CMC second-order postsynaptic filtering structure.

## Gate ledger

| Gate / freeze | Result | Consequence |
|---|---|---|
| Neuro Feasibility Gate 0.1 | `N-B` | CMC/DCM and coupled Jansen-Rit survived; `M` required dedicated clarification. |
| Neuro M-Gate 0.1 | `NM-A` | A pre-CORE positive synaptic-filter storage is strong enough in principle. |
| Neuro Pilot Candidate Gate 0.1 | `NOMINATED: multi-region CMC/DCM` | Primary channel fixed as `SP_j -> SS_i`; no CORE evaluation. |
| Neuro Admissible Input Geometry Gate 0.1 | `NB-A` | A natural admissible preparation map with rank at least two exists without `B=I` or arbitrary hidden-state perturbations. |
| Cross-Domain Integration Gate 0.1 | `PASSED` | Neuro released to Pilot Specification 0.1 only. |
| Neuro Pilot Specification 0.1 | `COMPLETE` | Concrete V1/V4 model, `A`, `M`, channel block, two-pulse `B`, input metric, time normalization and execution checks frozen. Execution is **not** self-authorized. |

## Frozen Pilot Specification 0.1

Canonical file:

`research/neuro/neuro_pilot_specification_0_1.md`

Key frozen objects:

```text
model                  = 2-source multi-region CMC/DCM
reference dynamics     = SPM12 spm_fx_cmc.m, blob 66606f2e8c45b896ba239d26d98a45cd1b94b33d
source j               = macaque V1
source i               = macaque V4
primary channel        = V1 SP -> V4 SS
state dimension        = 16
operating point        = x* = 0
propagation delays     = disabled for this autonomous ODE pilot
T (ms)                 = (2, 2, 16, 28)
G (1/s)                = (800,800,1600,800,800,400,800,800,400,200)
E (1/s)                = (200,100,200,100)
sigmoid R              = 2/3
sigmoid derivative     = 1/6 at baseline
exogenous input        = V1 SS only, standard SPM factor 32
b_aff,V1               = 16000 * e_2
A_j->i                 = only entry (10,3)=16666.6666666667
Q_j->i^CORE            = only symmetric entries (10,3),(3,10)=8333.33333333333
pulse width            = 1 ms
pre-observation delays = (2 ms, 16 ms)
R_in                    = I_2
rank(B)                 = 2
kappa_2(M^1/2 B)        = 34.2940
tau_ref                 = 28 ms
horizon ladder          = (7,14,28,56,112,224) ms
```

The exact `16 x 16` generator `A`, storage matrix `M`, finite-pulse `B` columns and numerical qualification are recorded in the canonical specification file.

## Qualification status

Pre-CORE checks completed during specification only:

- exact baseline fixed point `x*=0`;
- asymptotic stability of the frozen generator:
  \[
  \alpha(A)=-33.0964092356\;\mathrm{s}^{-1}<0;
  \]
- `M=M^dagger>0` by construction;
- `Q_{j->i}^{CORE}=Q_{j->i}^{CORE\,dagger}` by construction;
- finite two-pulse preparation map has numerical rank `2`;
- storage/input-whitened conditioning is `34.2940`, below the frozen qualification ceiling `100`;
- no timing, parameter, region or pathway was retuned after qualification.

No `K_M`, `K_Q`, optimizer, angle or objective-separation quantity has been evaluated.

## Hard restrictions

The following remain prohibited unless MASTER explicitly opens a new task:

- any CORE-Neuro optimization or objective-separation calculation;
- changing V1/V4, the operating point or any frozen CMC parameter after inspecting a CORE effect;
- `B=I` or arbitrary independent perturbations of latent CMC hidden states;
- changing the two pulse shapes, widths, delays or input calibration after the specification freeze;
- optimizing a time-dependent stimulus waveform;
- enabling propagation delays without a new MASTER-approved model freeze;
- adding horizons outside the frozen ladder to rescue a result;
- calling the storage brain energy or metabolic energy.

## Next instruction

**Next instruction:** `RETURN TO MASTER FOR PILOT FREEZE`

Under `research/master/prompt_handoff_protocol_0_1.md`, a bare `GO` in this branch must **not** silently start pilot execution while this field says `RETURN TO MASTER`.

\[
\boxed{\text{NO CORE-NEURO EXECUTION AUTHORIZED.}}
\]

## Canonical documents

- `research/neuro/neuro_admissible_input_geometry_gate_0_1.md`
- `research/neuro/neuro_pilot_specification_0_1.md`
- `research/master/cross_domain_integration_gate_0_1.md`
- `research/master/prompts/neuro_pilot_specification_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`
