# Neuro Pilot Specification 0.1 — MASTER Handoff

Execute this instruction in the Neuro branch. This is a **specification/freeze-preparation task only**.

## Scope

No CORE optimization, no parameter search for large effects, no calculation or inspection of

\[
K_M(T),\quad K_Q(T),\quad w_M^\star,\quad w_Q^\star,\quad \vartheta(T),\quad \Delta_Q(T).
\]

Use only the already accepted chain:

\[
\text{multi-region CMC/DCM},
\qquad
\mathrm{SP}_j\to\mathrm{SS}_i,
\]

\[
Q_{j\to i}^{\rm CORE}
=
\frac12(A_{j\to i}^\dagger M+MA_{j\to i}),
\]

and the `NB-A` admissible preparation geometry.

## Required freeze objects

Freeze one concrete first-pilot CMC/DCM instantiation using only pre-CORE physiological, experimental and stability criteria:

1. exact number of regions and anatomical/source identities of `j` and `i`;
2. exact CMC architecture, state ordering and all model parameters;
3. exact stable operating point and the resulting autonomous linear generator `A`;
4. exact synaptic-filter storage matrix `M=M^dagger>0` and its units/scaling;
5. exact pathway block `A_{j->i}` and the resulting Hermitian signed channel `Q_{j->i}^{CORE}`;
6. exact afferent injection vector `b_aff,j`;
7. two fixed finite preparation pulse shapes `h_1,h_2`, fixed pre-observation delays `tau_1 != tau_2`, and the resulting full-system
   \[
   B=B_{prep}^{(2)}=[b_1^{eff},b_2^{eff}];
   \]
8. stimulus-to-model calibration and
   \[
   (R_{in})_{kl}=E_{ref}^{-1}\int h_k(t)h_l(t)\,dt;
   \]
9. numerical rank and conditioning of the frozen `B`; if effective rank collapses or conditioning is scientifically unacceptable, STOP rather than retune pulse timing after inspection;
10. a pre-CORE Neuro time normalization `tau_ref` with explicit physiological/model meaning;
11. the inherited dimensionless horizon ladder
   \[
   T/tau_{ref}\in\{0.25,0.5,1,2,4,8\};
   \]
12. numerical integration tolerances/checks and all later execution sanity checks.

## Shared cross-domain reporting protocol to preregister

The later positive objective will be

\[
K_M(T)=R_{in}^{-1/2}B^\dagger e^{A^\dagger T}Me^{AT}BR_{in}^{-1/2},
\]

interpreted only as **final synaptic-filter storage per fixed experimental input cost**.

The later signed cumulative pathway operator will be

\[
K_Q(T)=R_{in}^{-1/2}B^\dagger
\left[\int_0^T e^{A^\dagger t}Q_{j\to i}^{CORE}e^{At}\,dt\right]
BR_{in}^{-1/2}.
\]

The positive signed branch is primary, but the negative extremum must also be reported.

Preregister the inherited operational demonstration thresholds

\[
\vartheta(T)\ge20^\circ,
\qquad
\Delta_Q(T)\ge0.25
\]

for at least two neighboring fixed horizons. State explicitly that these are project-level operational thresholds, not universal neurophysiological constants.

Require domain-specific physical interpretation beyond vector angle, such as region/population composition, phase/state composition, or preparation-pulse mixture, whichever is physically meaningful after the model is frozen.

## Anti-bias rules

- Do not select regions, operating point, pulse timings, pulse shapes, calibration or horizons by inspecting a CORE effect.
- Do not replace the accepted afferent preparation geometry with `B=I`.
- Do not add arbitrary hidden-state kicks.
- Do not turn the problem into time-dependent optimal control.
- Do not call the storage `brain energy` or `metabolic energy`.
- If a required physical/model choice cannot be justified independently of CORE, classify the pilot as not yet ready and STOP.

## Output

Create and commit

`research/neuro/neuro_pilot_specification_0_1.md`

and update

`research/neuro/STATUS.md`.

The status file must contain a `Next instruction` field. If the specification is complete, set it to `RETURN TO MASTER FOR PILOT FREEZE`; do not self-authorize execution.

Report exact repository paths, commit hash and CI/test status if relevant.

**STOP after specification.**
