# Neuro Research Status

**Last updated:** 2026-09-02  
**Branch:** `main`

## Current candidate

The only nominated first Neuro demonstrator is

\[
\boxed{\text{multi-region CMC/DCM}}.
\]

The primary physiological signed channel is frozen as

\[
\boxed{\mathrm{SP}_j\rightarrow\mathrm{SS}_i}
\]

with

\[
Q_{j\to i}^{\rm CORE}
=
\frac12(A_{j\to i}^{\dagger}M+MA_{j\to i}).
\]

The positive state/storage metric remains the pre-CORE synaptic-filter storage fixed by the CMC second-order postsynaptic filtering structure.

## Gate ledger

| Gate | Result | Consequence |
|---|---|---|
| Neuro Feasibility Gate 0.1 | `N-B` | CMC/DCM and coupled Jansen-Rit survived; `M` required dedicated clarification. |
| Neuro M-Gate 0.1 | `NM-A` | A pre-CORE positive synaptic-filter storage is strong enough in principle. |
| Neuro Pilot Candidate Gate 0.1 | `NOMINATED: multi-region CMC/DCM` | Primary channel fixed as `SP_j -> SS_i`; no CORE evaluation yet. |
| Neuro Admissible Input Geometry Gate 0.1 | `NB-A` | A natural admissible initial-state map with rank at least two exists without `B=I` or arbitrary hidden-state perturbations. |
| Cross-Domain Integration Gate 0.1 | `PASSED` | Neuro released to Pilot Specification 0.1 only; no CORE execution yet. |

## Canonical admissible input geometry after NB-A

The first-pilot input geometry is now defined at the **class level** as a two-component fixed preparation protocol through the already accepted afferent input to `SS_j`.

Let `b_aff,j` be the physiological CMC injection vector for the afferent drive to `SS_j`. Two fixed brief stimulus components with distinct pre-registered preparation delays generate

\[
\boxed{
B_{\rm prep}^{(2)}
=
\begin{bmatrix}
 b_1^{\rm eff}&b_2^{\rm eff}
\end{bmatrix},
}
\]

or, in the ideal impulse representation,

\[
\boxed{
B_{\rm prep}^{(2)}
=
\begin{bmatrix}
 e^{A\tau_1}b_{\rm aff,j}
&
 e^{A\tau_2}b_{\rm aff,j}
\end{bmatrix},
\qquad \tau_1\ne\tau_2.
}
\]

The second-order synaptic-filter block gives structural rank two for distinct delays; no additional hidden-state actuator is introduced.

The input metric is the pre-registered physical/experimental pulse-dose Gram matrix

\[
(R_{\rm in})_{k\ell}
=
E_{\rm ref}^{-1}\int h_k(t)h_\ell(t)\,dt.
\]

For equal, non-overlapping, equally calibrated same-modality pulses this reduces to

\[
R_{\rm in}=I_2
\]

**in input-coordinate space only**.

## Hard restrictions

The following remain prohibited for the first Neuro pilot:

- `B=I` without a physiological actuator model;
- arbitrary independent perturbations of latent CMC hidden states;
- choosing pulse timing, waveform, source, or input columns after inspecting a CORE effect;
- treating DCM modulatory inputs as additive initial-condition directions;
- optimizing a time-dependent control waveform;
- computing CORE optimizers or objective-separation effects before a full pilot preregistration freezes model, operating point, pulse protocol, and calibration.

## Next admissible step

Neuro is now released to **Pilot Specification 0.1** only.

**Next instruction:** `research/master/prompts/neuro_pilot_specification_0_1.md`

When the user writes `GO` in the Neuro branch, read this `STATUS.md` and then execute only the committed `Next instruction` according to `research/master/prompt_handoff_protocol_0_1.md`.

The specification must freeze, without parameter/effect search:

1. exact multi-region CMC architecture and stable operating point;
2. anatomical/source identities of `j` and `i`;
3. model parameters and state ordering;
4. exact `M` and `A_{j->i}` matrices;
5. fixed pulse shapes and preparation delays defining `B_prep^(2)`;
6. stimulus-to-model calibration and `R_in`;
7. rank/conditioning qualification of the frozen full-system `B`;
8. pre-CORE time normalization, fixed horizon ladder, later numerical checks and verdict rules.

Until that specification is complete and returned to MASTER:

\[
\boxed{\text{NO CORE-NEURO OPTIMIZATION.}}
\]

## Canonical documents

- `research/neuro/neuro_admissible_input_geometry_gate_0_1.md`
- `research/master/cross_domain_integration_gate_0_1.md`
- `research/master/prompts/neuro_pilot_specification_0_1.md`
