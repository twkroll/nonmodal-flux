# Manuscript Draft Review Gate 0.1

**Status:** PASS WITH MAJOR EDITORIAL/REPRODUCIBILITY REVISION — SCIENCE UNCHANGED  
**Date:** 2026-09-03  
**Authority:** `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`  
**Reviewed package:** `research/manuscript/manuscript_draft_0_1.md`, `research/manuscript/evidence_citation_map_0_1.md`, `research/manuscript/figure_source_map_0_1.md`.  
**Scope:** draft review only. No new theory, no new simulation, no parameter search, no retuning, no new novelty claim.

## 0. Executive verdict

Draft 0.1 is scientifically coherent, consistent with the frozen evidence hierarchy, and publication-positionable under the frozen claim boundaries. It correctly preserves

\[
\boxed{\text{Plasma}=P2\text{-}A},\qquad
\boxed{\text{Neuro}=\text{NEURO-STRONG}},\qquad
\boxed{\text{Climate}=\text{CLIM-WEAK}},
\]

and it does not convert the project into a mathematical-novelty claim.

However, the draft is **not yet submission-ready** because it is too dependent on internal project names and result files to function as a standalone scientific article. The main required work is editorial and reproducibility-oriented: expose enough of each physical model, channel definition, admissible geometry, normalization and preregistration logic in the manuscript itself; tighten notation; clarify the status of “preregistration”; and normalize/verify the bibliography.

No new scientific calculation is required.

Therefore

\[
\boxed{\text{Manuscript Draft Review Gate 0.1 = PASS WITH MAJOR WRITING REVISION}.}
\]

The next authorized action is `Manuscript Structural Revision Package 0.2`.

---

## 1. What is already strong and should be preserved

### 1.1 Scientific spine

The manuscript has a clear common question: whether a conventional positive storage/state objective is redundant with an independently defined physical channel on the same admissible perturbation space. This is a stronger and safer organizing principle than presenting three unrelated application examples.

### 1.2 Nonuniform evidence hierarchy

The ordering Plasma -> Neuro -> Climate works well:

1. Plasma gives the strong signed-transport anchor with both positive and negative cumulative transport branches;
2. Neuro shows that the workflow survives a physically restricted low-dimensional preparation geometry and yields a large practical gap;
3. Climate gives the essential weak contrast in which a 90-degree subspace separation coexists with only about a 4.12% performance loss.

The weak Climate result should remain in the main paper rather than being hidden in supplementary material because it is central to the anti-effect-maximization message.

### 1.3 Claim discipline

Draft 0.1 correctly avoids broad novelty claims for transient growth, singular vectors, optimal stimulation, quadratic-output optimization, or generic objective dependence. The Neuro `M` semantics and the Climate angle-versus-gap restriction are preserved correctly.

### 1.4 Evidence discipline

The evidence/citation map and figure-source map are strong internal controls. Quantitative claims are traceable to frozen result files and the planned figures are explicitly prohibited from introducing new simulations or horizons.

---

## 2. Major revision required: the paper is not yet standalone

The largest weakness is that the Results sections name frozen branches and quote results without giving enough model-level information for an external reader to reconstruct what is being optimized.

### 2.1 Plasma model definition is too compressed

The current text gives `U(x)=cos x`, `C=kappa=1`, `N=0`, `nu_perp=0.020`, but it does not define the D10-ZF state equations, state ordering, the free-energy metric `M`, or the physical particle-transport matrix/channel in manuscript form.

**Required revision:** add a compact Plasma model subsection in Methods or an application-methods subsection containing the frozen linear equations/operator definition, state variables, energy/free-energy normalization, signed radial particle-transport observable, `B=I`, `R_in=M`, time normalization, resolution definition, and the role of `nu_perp=0.020`. Full matrix entries may go to Supplement, but the main text must be scientifically intelligible without knowing what “D10-ZF branch” means.

### 2.2 Neuro model definition is too compressed

The draft identifies V1/V4, V1-SP -> V4-SS and the rank-two preparation, but does not expose the CMC state layout, second-order synaptic-filter structure underlying `M`, the decomposition `A=A_rest+A_{j->i}`, or how the two fixed pulses generate the preparation map `B`.

**Required revision:** provide a compact frozen CMC definition with the population/state ordering needed to interpret the pathway, the filter-storage expression, the pathway contribution

\[
Q_{j\to i}=\frac12(A_{j\to i}^\dagger M+MA_{j\to i}),
\]

and the explicit conceptual construction of the rank-two pulse-preparation map. State clearly that positive/negative `q_{j->i}` means increasing/decreasing the chosen storage rate via that pathway, not excitatory/inhibitory sign.

### 2.3 Climate model definition is too compressed

The draft calls the system a damped two-layer Phillips-QG model but omits the actual QG PV equations, boundary conditions, the barotropic/baroclinic energy expression and the signed heat-transport definition.

**Required revision:** include the frozen two-layer QG equations, `kx != 0` eddy-state restriction, wall/periodic boundary conditions, QG perturbation energy and

\[
J_{\rm heat}(T)=\int_0^T x^\dagger Q_{\rm heat}x\,dt,
\]

with the poleward-positive sign convention. The full Fourier/Galerkin matrix construction may remain in Supplement/Methods appendix, but the physical observable must be explicit in the paper.

### 2.4 Main-text/Supplement division

Recommended division:

- **Main text:** physical equations sufficient to define `A`, `M`, `Q`, `B`, `R_in`, time normalization, horizons and verdict logic for each domain;
- **Supplement:** full parameter tables, matrix/state ordering, discretization details, numerical tolerances, complete horizon tables, preregistration chronology and regression-test details.

This is an editorial restructuring only and requires no new calculation.

---

## 3. Major revision required: preregistration terminology

The draft repeatedly uses “preregistered”. The project has strong internal anti-bias evidence through committed specifications/freezes before objective inspection. Nevertheless, in conventional publication language, “preregistered” may be interpreted as registration in a recognized external registry or a publicly declared protocol before analysis.

### Decision

Until the manuscript can document an externally/publicly verifiable preregistration mechanism in the Methods/Data Availability section, the safer default wording is:

> **pre-specified and frozen before objective-separation evaluation**

or

> **prospectively frozen in the version-controlled analysis record before effect inspection**.

The word “preregistered” may be retained only if the final manuscript explicitly documents the repository/commit chronology and the authors are comfortable defending that terminology.

This wording change does not weaken the scientific anti-retuning claim.

---

## 4. Major revision required: verdict and threshold logic must be visible

Draft 0.1 refers to the `NEURO-STRONG` rule and the weak Climate verdict but does not clearly define the common operational comparison rule in the Methods.

**Required revision:** add a concise subsection/table that distinguishes:

- geometry diagnostic `theta` or subspace angle;
- performance diagnostic `Delta_Q`;
- the pre-specified operational strong criterion used in the pilots (`theta >= 20 deg` and `Delta_Q >= 0.25` on at least two neighboring horizons);
- domain-specific numerical/robustness gates;
- the fact that these thresholds are operational preregistration rules for this study, **not universal physical constants**.

Climate must remain classified under its already frozen rule, and no threshold may be changed during revision.

---

## 5. Notation and normalization review

### 5.1 Factor-of-two convention

The manuscript defines

\[
S(x)=\tfrac12 x^\dagger Mx
\]

but then uses `K_M` without an explicit `1/2`. This is harmless for optimizer directions and normalized ratios but may confuse readers comparing reported objective values.

**Required revision:** state once that the overall `1/2` storage convention is omitted from finite-time operator eigenvalues because it does not affect optimizers or normalized gaps, or use one convention consistently throughout.

### 5.2 Energy versus storage language

Keep domain-specific labels in equations, axes and captions:

- Plasma: free energy;
- Neuro: synaptic-filter storage per input cost;
- Climate: QG perturbation energy.

Do not use a universal symbol `G_E` for Neuro in the final presentation unless explicitly relabeled as a generic positive-objective value.

### 5.3 Signed-channel semantics in Neuro

The framework may call `Q` signed, but the Neuro Results must continue to say that the frozen admissible preparation space reaches only positive cumulative values over the tested ladder. This restriction is already correct and should remain prominent.

---

## 6. Introduction and discussion review

### 6.1 Introduction

The Introduction is logically good but can be shortened. It currently repeats the nonredundancy thesis in several consecutive paragraphs. Revision 0.2 should reduce repetition and move some project-governance language into Methods.

Recommended narrative:

1. proxy-objective problem;
2. established prior art and what is not new;
3. missing integrated diagnostic question;
4. study design and three deliberately nonuniform cases;
5. one-sentence contribution statement.

### 6.2 Discussion

The Discussion is strong conceptually. It should add one explicit paragraph on the difference between **geometric identifiability/nonidentity** and **decision relevance**. The Climate case shows that structurally different optimizers can be practically substitutable for a given channel, while Plasma/Neuro show cases where they are not.

The phrase “physical channel” should be defined broadly enough to encompass both transport fluxes and the Neuro pathway contribution without implying that all three are the same class of conserved flux.

---

## 7. Abstract review

The Abstract is scientifically accurate but too technical for many target journals and likely longer than necessary.

Recommended revision:

- remove most operator notation from the Abstract;
- retain one sentence describing the tuple/workflow conceptually;
- keep one quantitative witness per domain;
- preserve the Climate 90-degree / 4.12% contrast;
- replace “preregistered” by the safer pre-specified/frozen wording unless registration status is documented.

A structured abstract can remain for now; journal-specific conversion should occur only after journal targeting.

---

## 8. Figure-plan review

The five-figure architecture is viable, but Figure 5 is the most important synthesis figure and should not look like a universal phase diagram.

### Required guardrails

- use domain-specific markers and clearly separate the three horizon ladders;
- do not fit a trend line across domains;
- do not imply that equal `theta`/`Delta` values have identical physical meaning beyond being common diagnostics;
- distinguish vector angle from degenerate-subspace angle in legend/caption;
- show Climate's longest-horizon point explicitly as the counterexample to angle-only interpretation.

### Figure 2 panel (d)

If full Plasma direct-trajectory samples are not stored, do not reconstruct them. Use the frozen endpoint summary or omit the panel.

### Figure 3

The two-pulse coordinate plot is especially strong because it makes the Neuro result experimentally interpretable. Preserve pulse sign and equal aspect ratio.

---

## 9. Bibliography and citation audit required before submission

The current bibliography is a placeholder and is sufficient for Draft 0.1 but not for submission.

A later writing-only pass must verify:

- full bibliographic metadata and DOI for every mandatory anchor;
- final status/citation form of the 2026 Ogino et al. item;
- consistent accents and author names (e.g. Sévellec);
- whether a small number of generic optimal-perturbation/Gramian references should be added for methodological context.

This is citation normalization, not a new novelty search. Any new novelty-sensitive claim would still require a new literature gate.

---

## 10. Claims checked against the Evidence Map

### PASS

The following central quantitative statements are consistent with the frozen evidence map:

- Plasma `T=1`: `Delta_Gamma ~= 0.504337`, `theta ~= 53.396 deg`, signed positive and negative cumulative extrema;
- Neuro 112/224 ms: `theta ~= 46.824/65.058 deg`, `Delta_Q ~= 0.529/0.818`, direct two-pulse optimizer interpretation;
- Climate `T/tau_ref=8`: energy `(3,2)` versus heat `(4,2)`, subspace angle `90 deg`, `Delta_heat ~= 0.0411846`, retained heat performance about 95.88%;
- no new scientific calculation is needed for the planned figures.

### RESTRICT

The phrases “preregistered workflow” and “physical channel” require the terminology clarifications above before external submission.

### FAIL

No scientific claim in Draft 0.1 is judged to require retraction or a new numerical calculation.

---

## 11. User decisions actually required

No scientific model/result decision is required now. The following editorial decisions can be deferred until after Revision 0.2:

1. **Journal family / audience:** physics-methods, nonlinear-dynamics, cross-disciplinary methods, or domain-oriented venue;
2. **Main-text versus Supplement depth:** the review recommends concise defining equations in the main text and full reproducibility detail in Supplement;
3. **Final title:** current title is acceptable, but a shorter title may be preferable after journal targeting;
4. **Use of the word “preregistered”:** default recommendation is to use “pre-specified and frozen before effect inspection” unless the final paper documents a defensible registration chronology.

The integrated three-domain paper itself remains the preferred frozen architecture; no decision to split the paper is required at this gate.

---

## 12. Protected boundaries

Still forbidden during the next revision:

- rerunning Plasma/Neuro/Climate;
- new horizons or parameters;
- new channels/pathways;
- changing `B` or `R_in`;
- Climate retuning;
- delayed Neuro extension;
- MODES/CONT/CASCADE calculations;
- Power-Grid, Photonics or realistic-Fusion execution;
- journal targeting or submission before the structural revision is reviewed.

---

## 13. Decision log additions

- **DEC-355:** Manuscript Draft Review Gate 0.1 = PASS WITH MAJOR EDITORIAL/REPRODUCIBILITY REVISION — STABLE.
- **DEC-356:** Draft 0.1 scientific claims remain compatible with frozen evidence; no new calculation is required — STABLE.
- **DEC-357:** Revision 0.2 must make each domain model/metric/channel/admissible geometry sufficiently self-contained for external readers — ACTIVE.
- **DEC-358:** Main text should contain compact defining physics; full matrices, parameter tables, tolerances and preregistration chronology should move to Supplement — ACTIVE EDITORIAL RULE.
- **DEC-359:** Default manuscript wording should be “pre-specified/frozen before effect inspection” rather than “preregistered” unless registration chronology is explicitly documented — ACTIVE CLAIM GUARDRAIL.
- **DEC-360:** Operational strong thresholds must be stated as study-specific rules, not universal constants — ACTIVE.
- **DEC-361:** Factor-of-two storage normalization must be made explicit/consistent — ACTIVE.
- **DEC-362:** Climate remains in the main manuscript as the canonical weak contrast; the integrated three-domain architecture is retained — FROZEN.
- **DEC-363:** Next MASTER task is `Manuscript Structural Revision Package 0.2`; no scientific branch is opened — ACTIVE.

---

## 14. Exact next action

Execute:

`Manuscript Structural Revision Package 0.2`

using only frozen model/specification/result/literature files. The revision may rewrite, reorganize, expose existing frozen equations, and normalize citations, but it may not create new scientific results.

**STOP.**