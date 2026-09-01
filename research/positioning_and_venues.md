# Literature positioning and venue strategy

**Date:** 2026-09-01

## Positioning in the current literature

The project sits at the intersection of four established bodies of work:

1. **Classical nonmodal stability / transient growth.** Optimizing finite-time state or energy amplification under a positive norm is established.
2. **Quadratic-output systems and indefinite quadratic control.** Quadratic outputs, Gramians, Lyapunov equations, and indefinite quadratic costs are established mathematical objects.
3. **Physics-derived transport objectives.** Lülff-style transport forms show that a physically meaningful transfer quantity may be represented by a Hermitian indefinite bilinear form whose signs correspond to opposite transport directions.
4. **Plasma free-energy / optimal-mode theory.** Free-energy growth bounds and optimal free-energy growth modes are established; particle and heat fluxes occur explicitly in free-energy balances.

The project is therefore not publishable merely as a combination of `nonmodal + quadratic output + Gramian`.

## Distinctive candidate contribution

The strongest current formulation is:

> Finite-horizon optimization of a **physics-derived signed transport observable** under an independent positive disturbance/free-energy metric, with a **physically admissible and transport-neutral initial subspace**, together with structural results showing how transport is dynamically generated and constrained by the physical balance.

The distinctive scientific content must come from at least two of the following simultaneously:

- a theorem beyond the elementary spectral characterization;
- transport-neutral admissible inputs (`B^†QB=0`) with higher-order generation structure;
- a channel-resolved balance theorem involving multiple physical flux operators;
- a robust plasma result in which flux-optimal and free-energy-optimal disturbances differ for a mechanistically understood reason;
- a nontrivial asymptotic regime;
- a local/global separation theorem for passive networks.

## Current paper sufficiency assessment

### Not enough yet

The present T1 short-time proposition and T2 exact balance identity are not enough for a strong standalone foundations paper. Both are mathematically useful but close to standard Taylor/Lyapunov manipulations.

### Minimum package that likely *is* enough

A credible P1 should contain:

1. a clean general formulation and coordinate-invariance result;
2. T1/T2 as supporting propositions;
3. **one genuinely nontrivial theorem**, preferably a channel-resolved or admissible-subspace bound;
4. a physically exact Lülff-style particle-flux operator derived from a fixed plasma model;
5. a stable plasma regime with a robust, nontrivial difference between free-energy and flux optimals under transport-neutral initialization;
6. at least one analytic/asymptotic explanation of that difference;
7. null controls (`Q=M`, normal replacement, zero drive, unrestricted vs neutral input).

If item 3 fails, the safer publication strategy is to make the theory the method section of a plasma paper rather than force a separate abstract foundations article.

## Possible publication venues

### Physics-first route

**Physical Review E** — strong fit if the paper emphasizes nonnormal dynamics, signed transport, general complex-system structure, and a compact plasma example. PRE explicitly covers nonlinear dynamics, plasma, computational physics, ML and AI. This is probably the most natural broad-physics target for a general P1 if the theorem package is solid but not a major control-theory breakthrough.

**Physical Review Research** — plausible if the result convincingly bridges dynamical-systems theory and multiple physical domains and has a broader conceptual message. Higher bar for breadth/significance than a domain-specific plasma article.

**SIAM Journal on Applied Dynamical Systems** — strong fit if the mathematical dynamical-systems content becomes the dominant contribution, especially with theorem-level results on signed observables, subspace geometry and transient dynamics.

### Plasma-first route

**Journal of Plasma Physics** — likely strong target for P1 merged with the plasma application, especially if the free-energy/flux construction and asymptotics are central.

**Physics of Plasmas** — natural venue for a detailed plasma theory/application paper with substantial analytical and computational validation.

### Control-first route

**IEEE Transactions on Automatic Control** or a similar control-theory venue would require a substantially stronger general theorem than T1/T2 and a contribution recognizable as new systems/control theory, not primarily a new physical interpretation of existing quadratic-output machinery.

### Fluid/transport route

**Journal of Fluid Mechanics** would be credible only if a fluid/plasma transport application becomes the main scientific result and yields significant mechanistic fluid-dynamical insight. A generic framework plus a small matrix example would not be enough.

## Current ranking

If the project succeeds roughly as presently envisioned:

1. **PRE** for a general foundations + reduced plasma paper.
2. **JPP** if the strongest novelty turns out to be plasma-specific.
3. **SIADS** if a genuinely new theorem package becomes the centerpiece.
4. **PRResearch** if the cross-domain result becomes unusually broad and compelling.
5. **Physics of Plasmas** for a more application-heavy plasma version.

This ranking should be revisited after Gate 1 and the first HW pilot.

## Relevant current literature anchors

- Lülff (2015): transport-oriented POD via an indefinite bilinear heat-transport form.
- Camargo, Tippett & Caldas (1998): nonmodal HW energetics and phase dynamics.
- Benner, Goyal & Pontes Duff (2022): quadratic-output Gramians and energy functionals.
- Plunk & Helander (2022): gyrokinetic energetic bounds and optimal free-energy growth.
- Hillebrecht (2026): current quadratic-output gain bounds, reinforcing that generic gain theory is not an open novelty claim.
- Maldonado et al. (2023): transient growth in power systems.
- Recent work in 2025–2026 continues to treat nonnormal amplification as an active cross-domain topic, so conceptual novelty is possible but must be sharply formulated.
