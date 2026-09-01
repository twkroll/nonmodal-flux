# Research roadmap

**Updated:** 2026-09-01

This file is the short operational view of the research program. Detailed theorem notes and literature audits live elsewhere.

## Package A — Scope and novelty discipline

**Status: active / mostly complete for first pass**

- [x] Separate positive physical metric `M` from signed transport form `Q`.
- [x] Require Luelff-style physics-derived transport forms; no ad-hoc sums of amplitudes.
- [x] Keep AI applications as an idea only (`D7`).
- [x] First claim/literature audit.
- [x] T1/T3 targeted prior-art audits.
- [ ] Repeat citation chasing after a specific plasma convention is chosen.

## Package B — Finite-dimensional theory

**Status: active**

- [x] T1: short-time transport generation from a transport-neutral input space.
- [x] Higher-order transport-generation hierarchy / coordinate invariance recorded in `research/theory/T1_short_time_transport_generation.md`.
- [x] T2: exact balance identity and elementary signed bounds.
- [x] T3: multichannel non-identifiability and first channel-resolved bound.
- [x] T4: short-time separation of energy-optimal and transport-optimal disturbances.
- [ ] Strengthen T3 by finding computable, non-circular bounds for reachable-subspace leakage constants.
- [ ] Formalize terminal signed gain and cumulative signed gain as a common theorem package.
- [ ] Formalize full coordinate invariance for `A,M,Q,B,R_in` and optimals.

## Package C — Model-independent JAX core

**Status: next implementation package**

Implement before any plasma sweep:

1. validated data container for `(A,M,Q,B,R_in)`;
2. constant propagator via matrix exponential;
3. terminal signed gain;
4. cumulative transport Gramian by quadrature and a reference Lyapunov route;
5. Cholesky-whitened Hermitian generalized eigenproblem;
6. energy/transport angle;
7. coordinate-transformation helpers;
8. analytic and invariance tests, including the stable 2x2 transport-generation witness.

## Package D — Plasma convention and pilot

**Status: blocked by D2 until convention audit is complete**

- [ ] Compare candidate Hasegawa-Wakatani conventions.
- [ ] Derive PDE -> Fourier operator `L_k` by hand.
- [ ] Derive free-energy metric `M_k` from the model balance.
- [ ] Derive particle-flux form `Q_{Gamma,k}` directly from the physical flux.
- [ ] Verify cross-phase identity and balance symbolically/numerically.
- [ ] Only then run the single-case pilot and later parameter maps.

## Package E — Living theory note

**Status: required continuously**

Maintain:

- `docs/theory_progress.tex` — source of truth for compact theory/progress notes;
- `docs/theory_progress.pdf` — compiled version with genuinely typeset equations.

Update this note after each material theorem, modeling decision, or gate decision. Equations in the PDF must be generated from LaTeX source, never inserted as formula images.

## Immediate next order

1. Create/update the living TeX/PDF note.
2. Implement C1: validated mathematical data types and metric/observable checks.
3. Implement C2/C3: propagator and terminal signed gain with analytic tests.
4. Implement cumulative Gramian and T1/T4 asymptotic tests.
5. Then return to D2 and perform the model-specific HW convention audit.