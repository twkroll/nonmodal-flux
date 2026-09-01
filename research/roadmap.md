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
- [ ] Repeat citation chasing around the exact frozen HW convention and the now-computed pilot observables.

## Package B — Finite-dimensional theory

**Status: abstract core validated; first physical instantiations now available**

- [x] T1: short-time transport generation from a transport-neutral input space, including transport-generation order and coordinate invariance.
- [x] T2: exact balance identity and elementary signed bounds.
- [x] T3: multichannel non-identifiability and channel-resolved bounds, with global and reachable-subspace versions separated.
- [x] T4: short-time separation of energy-optimal and transport-optimal disturbances.
- [x] Synthetic proof-of-principle that reachable-subspace leakage constants can be substantially sharper than global constants.
- [x] Physical HW realization of T1/T4 transport generation during strict physical-energy contraction.
- [x] Physical two-mode D2-A realization of energy/transport optimizer separation inside the same multidimensional transport-neutral input space.
- [ ] Test whether the two-mode separation persists when the modal direct-sum simplification is removed.
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

**Status: both initial diagnostic branches computed; next gate is physical nontriviality beyond an uncoupled modal direct sum**

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
- [x] Branch S: compute the single-mode neutral-line transport generation and full-state finite-horizon energy/transport optimizer separation.
- [x] Branch M: compute a two-mode direct-sum pilot with a two-dimensional exactly transport-neutral pure-potential input space.
- [x] Document the branch comparison in `research/hw_branch_comparison.md` and record the parallel strategy as D9.
- [ ] Decide what physically justified coupling/enrichment should replace the direct-sum simplification for the next falsification test.
- [ ] Repeat targeted prior-art chasing against the exact frozen convention and branch results.
- [ ] Only after that gate, consider any parameter map.

### Results of the parallel branch calculation

**Branch S — single mode.** The neutral pure-potential line has zero initial flux, normalized first transport-generation coefficient `0.8`, accumulated flux `0.13193948` at `T=1`, terminal flux `0.14460273`, and terminal energy ratio `0.56555978`. On the unrestricted two-state space, the top terminal-energy and accumulated-transport directions differ by about `27.66 deg`.

**Branch M — two uncoupled modes.** Use `kx=0.5` and `kx=1.5` with common `ky=1`, `C=1`, `kappa=1`, `nu_k=0.15`, and pure-potential input in each mode. The two-dimensional input space is exactly transport-neutral. At short time the energy criterion selects the `kx=1.5` mode while the transport criterion selects `kx=0.5`; at `T=1` the whitened terminal-energy values are approximately `(0.56555978, 0.65428728)` while accumulated transport values are `(0.13193948, 0.07319417)`, giving orthogonal optimal neutral directions.

The Branch-M result is structurally stronger for the Gate-0 wording, but its exact `90 deg` separation currently comes from competition between uncoupled modal blocks. That simplicity is now the next falsification target rather than something to hide.

## Package E — Living theory note

**Status: active**

Maintain:

- `docs/theory_progress.tex` — source of truth for compact theory/progress notes;
- `docs/theory_progress.pdf` — compiled version with genuinely typeset equations.

Update this note after each material theorem, modeling decision, or gate decision. Equations in the PDF must be generated from LaTeX source, never inserted as formula images.

## Immediate next order

1. Choose a physically justified way to remove the uncoupled two-mode direct-sum simplification without changing D2-A silently; likely candidates are a documented shearing/coupled-mode construction or a richer reduced drift-fluid model.
2. Re-test transport neutrality, energy contraction, and energy/transport optimizer separation in that less decomposable setting.
3. Repeat targeted citation chasing against the exact frozen convention and the specific mechanism found.
4. Only after this physical-nontriviality gate passes, consider a controlled parameter map.