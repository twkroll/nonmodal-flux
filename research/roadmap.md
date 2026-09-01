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
- the living TeX/PDF theory note is maintained in `docs/`.

The canonical theorem directory is `research/theorems/`. New theorem statements should be added there rather than creating a parallel theory tree.

## Package A — Scope and novelty discipline

**Status: complete for first pass**

- [x] Separate positive physical metric `M` from signed transport form `Q`.
- [x] Require Luelff-style physics-derived transport forms; no ad-hoc sums of amplitudes.
- [x] Keep AI applications as an idea only (`D7`).
- [x] First claim/literature audit.
- [x] Targeted prior-art audits for T1, T3, and T4.
- [x] Consolidate theorem-note layout and remove duplicate T1 drafts.
- [ ] Repeat citation chasing after the frozen plasma convention is instantiated numerically.

## Package B — Finite-dimensional theory

**Status: abstract core validated; physical instantiation next**

- [x] T1: short-time transport generation from a transport-neutral input space, including transport-generation order and coordinate invariance.
- [x] T2: exact balance identity and elementary signed bounds.
- [x] T3: multichannel non-identifiability and channel-resolved bounds, with global and reachable-subspace versions separated.
- [x] T4: short-time separation of energy-optimal and transport-optimal disturbances.
- [x] Synthetic proof-of-principle that reachable-subspace leakage constants can be substantially sharper than global constants.
- [ ] Test whether that sharpening survives in the physical plasma pilot.
- [ ] Formalize terminal signed gain and cumulative signed gain as a common theorem package.

## Package C — Model-independent JAX core

**Status: validated for the current finite-dimensional scope**

Implemented and tested before any plasma sweep:

1. validated data container for `(A,M,Q,B,R_in)`;
2. constant propagator via matrix exponential;
3. terminal signed gain and extremal inputs;
4. cumulative transport Gramian and extremal inputs;
5. Cholesky-whitened Hermitian generalized eigenproblems;
6. coordinate/scaling invariance tests;
7. T1/T2/T3/T4 synthetic theorem witnesses;
8. signed positive/negative branches and short-time asymptotics.

## Package D — Plasma convention and pilot

**Status: active; first stable single-case pilot selected, structural input-space gate reached**

- [x] Compare candidate Hasegawa-Wakatani conventions for the first non-zonal linear pilot.
- [x] Freeze D2-A: `x` radial, `y` poloidal, `v_E=e_z x grad(phi)`, Fourier `exp(i k dot x)`, state `(phi_k,n_k)`.
- [x] Derive PDE -> Fourier operator `L_k` by hand for `k_y != 0`.
- [x] Derive physical energy metric `M_k = diag(k^2,1)` from the continuous energy.
- [x] Derive particle-flux form `Q_{Gamma,k}` directly from `Gamma=<n v_x>`.
- [x] Verify the exact linear energy/particle-flux balance algebraically in the convention audit.
- [x] Add convention-lock tests for `L_k`, `M_k`, `Q_{Gamma,k}`, the cross-phase identity, and the exact balance, including uniform perpendicular damping.
- [x] Implement the minimal Hasegawa-Wakatani model constructor without adding ad-hoc observables; model-level tests reproduce the frozen matrices and balance.
- [x] Select and document one spectrally stable pilot case: `(kx,ky,C,kappa,nu_k)=(0.5,1.0,1.0,1.0,0.15)`.
- [x] Verify spectral stability, metric nonnormality, exact balance, strict energy contraction, and positive flux generation from a pure-potential transport-neutral input.
- [ ] Decide whether the single-mode transport-neutral line is sufficient as a generation diagnostic while optimizer separation is tested on the full state, or whether the headline pilot must be enlarged to a multidimensional transport-neutral input space.
- [ ] Run the corresponding single-case finite-horizon optimizer comparison after that gate decision.
- [ ] Only after the single-case pilot passes, consider parameter maps.

### Structural gate discovered in D2.3

For one complex two-field Fourier mode, `Q_Gamma` has signature `(1,1)`. Therefore a complex-linear totally transport-neutral subspace satisfying `B^† Q_Gamma B=0` can have dimension at most one. The selected pure-potential line is a valid T1 transport-generation diagnostic, but it cannot contain distinct energy-optimal and transport-optimal directions.

This creates a genuine branch point rather than a numerical implementation issue.

## Package E — Living theory note

**Status: active**

Maintain:

- `docs/theory_progress.tex` — source of truth for compact theory/progress notes;
- `docs/theory_progress.pdf` — compiled version with genuinely typeset equations.

Update this note after each material theorem, modeling decision, or gate decision. Equations in the PDF must be generated from LaTeX source, never inserted as formula images.

## Immediate next order

1. Resolve the structural input-space gate: single-mode neutral-line diagnostic plus full-state optimizer comparison, versus enlargement to a multidimensional transport-neutral pilot.
2. After that decision, run exactly one finite-horizon optimizer comparison; do not start a broad sweep.
3. Use the result as the next Gate-0 falsification point and repeat targeted citation chasing around the exact frozen convention.
4. Only after the single-case pilot passes, consider parameter maps.
