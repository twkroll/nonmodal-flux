# Post-Paper Scientific Roadmap Gate 0.1

**Date:** 2026-09-04  
**Authority:** MASTER  
**Scope:** roadmap/branch selection only; no new scientific execution in this gate.

## Overall decision

The first-paper scientific content remains frozen under

`research/master/first_paper_scientific_content_freeze_0_1.md`.

The submission track remains parked by user choice.

The recommended next scientific program is

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

starting from the already-developed four-moment gyrofluid R1 branch and proceeding only through pre-effect physical/structural gates.

The immediate selected task is **B5.5 — physical ion heat-flux observable derivation**. No finite-time optimization, effect inspection, parameter search, or new pilot is authorized by this roadmap gate.

No parallel scientific branch is activated now. `MODES` is retained as the preferred conditional companion only after a qualified higher-dimensional Fusion operator exists and representation/reduction robustness becomes a concrete bottleneck.

---

## 1. Post-paper baseline

Paper 1 has established and frozen:

- the branch-independent finite-time framework `(A,M,Q,B,R_in)`;
- Plasma `P2-A` as a strong anchor;
- Neuro `NEURO-STRONG` as a constrained-input strong demonstrator;
- Climate-A `CLIM-WEAK` as a robust geometry-versus-performance contrast;
- Climate-B `CLIM-B-FAIL` as a resolution-robustness rejection case;
- the methodological lesson that optimizer geometry, target-performance loss, and representation/numerical robustness are distinct evidentiary layers.

The next program should therefore ask a scientifically new question rather than merely add another Paper-1-style witness.

The Fusion branch is unusually mature for this purpose. Existing repository work has already identified a physically credible hierarchy from energy-conserving gyrofluid moments toward local gyrokinetics/GENE, selected the anisotropic four-moment ZLR model as the preferred reduced derivation target, derived closed slab and minimal-curvature generators, and established a common positive free-energy metric for the two branches. The latest energetic check shows that curvature is skew-adjoint in the same metric and that the profile-drive Hermitian part reduces to the ion-temperature-gradient injection channel. The physical normalization/sign and Hermitian matrix of the ion radial heat flux remain deliberately open. This makes the next scientific question concrete and pre-effect.

---

## 2. Candidate-program comparison

Novelty levels are prospective project classifications only; no new literature search was performed in this gate.

| Program family | Scientific question | Novelty potential | New theory vs application | Falsifiability | Cost | Main risk | Independent-paper potential | Roadmap decision |
|---|---|---|---|---|---|---|---|---|
| **CORE 0.2 / theory consolidation** | Is there a concrete structural theorem beyond the already frozen generation/balance/geometry machinery? | `N1–N2`; `N3` only if a genuinely new theorem emerges | theory-heavy | high | medium | prior-art/novelty risk; earlier candidate mathematics was largely demoted as known structure | moderate only with a precise new theorem | **PARK**; do not search for theory merely to extend CORE |
| **MODES** | Which reduced/modal/Krylov representations preserve signed-channel optima and generation structure? | `N2`, possible `N3` | methodological | high | medium | can become a reduction-diagnostics paper without a sufficiently demanding physical target | good if attached to a high-dimensional validated application | **CONDITIONAL SECONDARY** after Fusion dimensionality justifies it; not parallel now |
| **CONT** | How do finite-time signed objectives and optimal subspaces continue through parameter variation and optimizer switches? | `N2`, possible `N3` | methodology + computation | high | medium | known eigenvalue/subspace-continuation machinery; risk of overstating switches as bifurcations | moderate/good if a physical family shows robust switch structure | **PARK** until a new physical family provides a justified continuation parameter |
| **CASCADE** | Can physically defined scale-to-scale signed transfer be treated without forcing nonlinear triadic fluxes into a quadratic-output theory? | `N2–N3` | theory/application mix | high | high | many genuine cascade fluxes are nonlinear/triadic and outside current fixed-`Q` core | good but requires a distinct formulation | **PARK**; do not force nonlinear cascade observables into current CORE |
| **Neuro next step** | Do delay/pathway expansion and richer admissible preparations change channel-optimal perturbations? | `N1–N2`, possible `N3` | application/model extension | high | medium/high | may read as a fidelity extension of Paper 1 rather than a new question | moderate | **PARK**; preserve delayed/higher-fidelity Neuro for later |
| **Higher-fidelity Climate/Ocean** | Do objective diagnostics remain useful in a more realistic geophysical model? | `N1–N2`, possible `N3` | application | high | high | too easily interpreted as repairing Climate-A/B; large model/representation risk | good only as a clearly new program | **PARK**; no Climate-B repair or third-candidate lineage |
| **realistic Fusion** | In an energy-consistent ITG/gyrofluid→gyrokinetic hierarchy, how does finite-horizon signed ion heat transport differ from free-energy optimality, and does the distinction survive FLR/parallel/kinetic fidelity? | `N1 + N2 + N3`; `N4` not assumed | physical derivation + application, with possible later methodological support | **very high**; observable/metric/closure/robustness may fail before any effect | medium initially, high later | semantic correctness of heat flux, closure/fidelity, eventual operator size | **high** if reduced result is validated through FLR and preferably local GK/GENE-compatible layer | **SELECT PRIMARY** |
| **Power Grids** | Does transient-state/storage optimality differ from directed transfer/corridor-loading optimality? | `N1 + N2 + N3` | application | high | medium/high | domain/channel semantics and collaboration constraints | high | **PROTECTED / PARKED**; no execution without explicit user/collaborator authorization |
| **Photonics/Waves** | Does stored electromagnetic energy differ from directed Poynting-flux/channel optimality? | `N1 + N2 + N3` | application | high | medium/high | channel/boundary/port normalization and collaboration constraints | high | **PROTECTED / PARKED**; no execution without explicit user/collaborator authorization |

---

## 3. Why Fusion is selected

### 3.1 It asks a question not answered by Paper 1

The intended Fusion program is not merely “find another system with a large angle/gap.” Its scientific question is hierarchical:

\[
\boxed{
\text{free-energy optimality}
\quad\text{vs.}\quad
\text{finite-horizon signed ion heat-transport optimality}
}
\]

under controlled increases in fusion-model fidelity:

\[
\text{anisotropic ZLR gyrofluid}
\rightarrow
\text{FLR gyrofluid}
\rightarrow
\text{parallel/flux-tube or local gyrokinetic validation}.
\]

The program can therefore succeed scientifically even if an early reduced model gives weak/null objective separation: the first question is whether the physical channel, metric, admissible geometry and energetic balance survive the model hierarchy cleanly.

### 3.2 The branch already has a strong pre-effect derivational foundation

Existing Fusion work provides:

- an observable dictionary distinguishing free energy from particle/heat transport;
- a model audit ranking energy-conserving gyrofluid and gyrokinetic targets;
- a minimal-model audit selecting the Strintzi–Scott–Brizard four-moment family;
- a reduction audit selecting anisotropic ZLR `R1` as the first derivation target and FLR `R2` as the next validation deformation;
- source-convention extraction;
- slab and minimal-curvature linearizations/generators;
- a source-derived positive free-energy metric;
- a curvature free-energy consistency check.

The current open object is not an effect but the physically normalized signed ion heat-flux operator. That is exactly the kind of pre-effect gate the project governance is designed to handle.

### 3.3 Clean falsification is available

The selected Fusion line must stop or redirect if any of the following occurs before effect inspection:

- the heat-flux observable cannot be derived uniquely from the source convention;
- the resulting quadratic form does not reproduce the temperature-gradient work in the free-energy balance with consistent sign/prefactor;
- the candidate metric loses positivity after a later fidelity step;
- the intended reduced system is not closed;
- the physical heat channel collapses or becomes uninformative under the chosen admissible geometry;
- spectral/numerical qualification fails;
- later resolution/fidelity checks fail.

No retuning to obtain a large objective-separation effect is allowed.

---

## 4. Selected Fusion dependency chain

### Gate F1.1 / B5.5 — Ion heat-flux observable derivation

Derive, from the already fixed R1 source convention and physical radial `E×B` thermal-energy/heat-flux definition:

\[
q_{i,k}=z_k^\dagger Q_{q_i,k}z_k,
\qquad Q_{q_i,k}=Q_{q_i,k}^\dagger,
\]

including exact sign, dimensional/nondimensional prefactors, Fourier-pair convention and the pressure/temperature combination. Verify consistency with the B5.4 free-energy injection identity. Do not compute any finite-time objective.

**Stop if ambiguous or inconsistent.**

### Gate F1.2 — Admissible input geometry and input cost

Only after B5.5 passes, determine a physically defensible `B` and `R_in` for the reduced fusion state. Do not force transport neutrality; test whether a neutral subspace is physically meaningful and sufficiently dimensional. Full-state actuation is not assumed automatically.

### Gate F1.3 — Fusion candidate/convention freeze

Freeze one reduced candidate using physical/structural criteria only. The minimal-curvature R1 branch is the intended primary candidate if B5.5–F1.2 remain consistent; the slab branch is an analytic/limiting control, not an effect-selected competitor. Freeze state ordering, normalizations, equilibrium-gradient convention, `A,M,Q_q,B,R_in`, dissipation/closure, and a physical parameter point without inspecting finite-time objective separation.

### Gate F1.4 — Numerical/spectral qualification

Verify positivity/Hermiticity, exact/expected balance identities, stability or explicitly allowed spectral regime, conditioning, representation/resolution checks and direct physical channel reconstruction. No optimizer-angle or target-gap inspection.

### Literature checkpoint

After the physical candidate and channel are frozen, but before the first finite-time execution, run a **targeted Fusion positioning audit** restricted to the exact frozen question: finite-horizon signed ion heat-transport optimality versus free-energy optimality in the selected gyrofluid/gyrokinetic setting. This avoids choosing the model from a desired novelty/effect outcome. It may classify prior art but may not retune the candidate.

### Gate F1.5 — Pilot specification

Freeze horizon ladder, finite-time operators, degeneracy rules, signed extrema, performance-gap definitions, physical reconstruction checks, robustness/fidelity rules and one-shot verdict logic. Weak/null/fail results remain valid.

### MASTER Pilot Freeze → one-shot execution → Result Freeze

Only after the above gates pass may MASTER release a finite-time execution. No early stopping or parameter/horizon rescue is allowed.

### F2 / F3 fidelity progression

- `R2`: restore FLR consistently as a controlled physical deformation;
- later restore richer parallel/flux-tube structure or move to a local linear gyrokinetic/GENE-compatible operator;
- kinetic-electron/multichannel work is later still.

Progression decisions must be based on physical fidelity and structural validity, **not** on whether the preceding stage produced a large objective-separation effect.

---

## 5. Parallelism decision

\[
\boxed{\text{No immediate parallel scientific branch}}
\]

Reason: B5.5 is a narrow physical derivation gate and should establish the primitive Fusion channel before MODES/CONT/CASCADE machinery is attached.

`MODES` becomes the preferred conditional secondary branch if the Fusion operator later becomes high dimensional enough that structure-preserving reduction, dynamic jet/Krylov subspaces, or representation robustness is a real scientific issue. At that point a separate MASTER gate must decide whether MODES is support methodology or an independent paper.

`CONT` may later become natural once a physically frozen Fusion parameter family exists. It is not activated before a non-effect-selected parameterization is defined.

---

## 6. Parked/protected branches

- **CORE 0.2:** parked; no theory search without a concrete unresolved structural hypothesis.
- **MODES:** parked, conditional Fusion companion.
- **CONT:** parked until a justified physical parameter family exists.
- **CASCADE:** parked; nonlinear/triadic scale fluxes must not be forced into fixed quadratic `Q`.
- **Neuro:** first result remains frozen; delayed/pathway-expanded work protected for later.
- **Climate:** Climate-A/B remain frozen; no Climate-B repair and no third-candidate rescue lineage.
- **Power Grids:** protected collaboration branch; evaluation retained, execution not authorized.
- **Photonics/Waves:** protected collaboration branch; evaluation retained, execution not authorized.
- **Manuscript/submission:** Paper-1 content frozen; submission track parked.

---

## 7. Rollback boundary

The first-paper baseline remains immutable under

`research/master/first_paper_scientific_content_freeze_0_1.md`.

All Fusion work from this point is a **post-paper scientific lineage**. It may cite and reuse the frozen framework, but it may not silently rewrite Paper 1.

The new roadmap savepoint is this file. If B5.5 fails, return to MASTER without opening a parameter search or effect calculation. If later reduced-model gates fail, MASTER may promote the six-moment GEM or direct gyrokinetic route according to the pre-existing physical hierarchy, but only through a new explicit gate.

---

## 8. Exact next branch/chat and handoff

Selected branch:

\[
\boxed{\text{60 – FUSION – Gyrofluid/Gyrokinetic Transport}}
\]

Canonical branch status:

`research/fusion/STATUS.md`

Canonical next instruction:

`research/master/prompts/fusion_ion_heat_flux_observable_derivation_gate_0_1.md`

In the Fusion chat, a bare `GO` must first read `research/fusion/STATUS.md` and then execute only that committed instruction.

If the dedicated Fusion chat does not yet exist, create it as a new project chat whose role is to follow the repository `STATUS.md` / prompt-handoff protocol; then issue `GO`.

---

## Final roadmap verdict

\[
\boxed{\text{SELECT FUSION-F1; START WITH B5.5 PHYSICAL ION HEAT-FLUX DERIVATION}}
\]

No new science was executed in this roadmap gate.

**STOP — ROADMAP SELECTION COMPLETE; AWAIT FUSION `GO`.**