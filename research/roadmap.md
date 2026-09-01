# Research roadmap

**Updated:** 2026-09-01

This file is the short operational view of the research program. Detailed theorem notes and literature audits live elsewhere.

## Repository consolidation checkpoint

**Status: complete**

The first repository-cleanup package is finished:

- the T1 material has been consolidated into one canonical theorem note;
- superseded/duplicate T1 drafts have been removed;
- T2, T3, and T4 remain separate theorem notes because they address distinct statements;
- targeted prior-art notes are kept separately from theorem derivations;
- AI applications are explicitly parked as an exploratory idea only under decision D7;
- the living TeX/PDF theory note is the next documentation task.

The canonical theorem directory is `research/theorems/`. New theorem statements should be added there rather than creating a parallel theory tree.

## Package A — Scope and novelty discipline

**Status: complete for first pass**

- [x] Separate positive physical metric `M` from signed transport form `Q`.
- [x] Require Luelff-style physics-derived transport forms; no ad-hoc sums of amplitudes.
- [x] Keep AI applications as an idea only (`D7`).
- [x] First claim/literature audit.
- [x] Targeted prior-art audits for T1, T3, and T4.
- [x] Consolidate theorem-note layout and remove duplicate T1 drafts.
- [ ] Repeat citation chasing after a specific plasma convention is chosen.

The unchecked citation-chasing item is deliberately deferred and does not block the next package.

## Package B — Finite-dimensional theory

**Status: active**

- [x] T1: short-time transport generation from a transport-neutral input space, including transport-generation order and coordinate invariance.
- [x] T2: exact balance identity and elementary signed bounds.
- [x] T3: multichannel non-identifiability and first channel-resolved bound.
- [x] T4: short-time separation of energy-optimal and transport-optimal disturbances.
- [ ] Strengthen T3 by finding computable, non-circular bounds for reachable-subspace leakage constants.
- [ ] Formalize terminal signed gain and cumulative signed gain as a common theorem package.
- [ ] Formalize full coordinate invariance for `A,M,Q,B,R_in` and finite-horizon optimals.

## Package C — Model-independent JAX core

**Status: queued after the living theory note**

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

**Status: next**

Maintain:

- `docs/theory_progress.tex` — source of truth for compact theory/progress notes;
- `docs/theory_progress.pdf` — compiled version with genuinely typeset equations.

Update this note after each material theorem, modeling decision, or gate decision. Equations in the PDF must be generated from LaTeX source, never inserted as formula images.

## Immediate next order

1. Create the living `docs/theory_progress.tex` and compiled PDF from the current canonical theorem notes.
2. Implement C1: validated mathematical data types and metric/observable checks.
3. Implement C2/C3: propagator and terminal signed gain with analytic tests.
4. Implement cumulative Gramian and T1/T4 asymptotic tests.
5. Then return to D2 and perform the model-specific Hasegawa-Wakatani convention audit.
