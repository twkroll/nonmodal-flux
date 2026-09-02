# Research roadmap

**Updated:** 2026-09-02

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
- [x] D10-ZF continuous balance exposes a second signed physical channel, mean-flow exchange `Q_U`, making T3 directly relevant to the coupled plasma pilot.
- [ ] Test whether the two-mode separation persists when the modal direct-sum simplification is removed by the D10-ZF coupled operator.
- [ ] Formalize terminal signed gain and cumulative signed gain as a common theorem package.
- [ ] After the autonomous coupled-pilot gate, consider a nonautonomous extension of the transport-generation hierarchy for shearing-wave dynamics.

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

**Status: D10.1 Fourier-Galerkin discretization selected and structurally validated; production coupled-model assembly is next**

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
- [x] Audit physically justified mechanisms that remove the direct-sum simplification without inserting an ad-hoc matrix coupling; see `research/hw_coupled_mode_audit.md`.
- [x] Accept D10-ZF: prescribed nonuniform zonal-flow linearization, initially `N(x)=0`, no ad-hoc mode coupling.
- [x] Derive the continuous coupled equations and exact perturbation-energy balance in `research/hw_zonal_flow_linearization.md`.
- [x] Identify the signed mean-flow energy-exchange channel `P_U` separately from the target radial particle flux `Gamma`.
- [x] Select a periodic coefficient-space Fourier-Galerkin representation at fixed `k_y`; see `research/hw_zonal_flow_discretization.md`.
- [x] Derive discrete `M`, `Q_Gamma`, `Q_U`, `D_C`, and `A_U` directly from the continuous forms.
- [x] Verify exact projected product-rule commutators, the multichannel balance, the `U=0` D2-A limit, the constant-flow Doppler limit, and sinusoidal sideband structure in test-only assembly.
- [ ] Promote the validated D10.1 formulas to a production zonal-flow model constructor without choosing a zonal-flow amplitude.
- [ ] Select one stable/subcritical prescribed zonal profile only after production structural tests pass.
- [ ] Check radial-resolution/sideband convergence of the selected coupled pilot before interpreting optimizer results.
- [ ] Repeat targeted prior-art chasing against the exact frozen convention and coupled mechanism.
- [ ] Only after that gate, consider any parameter map.

### Results of the parallel branch calculation

**Branch S — single mode.** The neutral pure-potential line has zero initial flux, normalized first transport-generation coefficient `0.8`, accumulated flux `0.13193948` at `T=1`, terminal flux `0.14460273`, and terminal energy ratio `0.56555978`. On the unrestricted two-state space, the top terminal-energy and accumulated-transport directions differ by about `27.66 deg`.

**Branch M — two uncoupled modes.** Use `kx=0.5` and `kx=1.5` with common `ky=1`, `C=1`, `kappa=1`, `nu_k=0.15`, and pure-potential input in each mode. The two-dimensional input space is exactly transport-neutral. At short time the energy criterion selects the `kx=1.5` mode while the transport criterion selects `kx=0.5`; at `T=1` the whitened terminal-energy values are approximately `(0.56555978, 0.65428728)` while accumulated transport values are `(0.13193948, 0.07319417)`, giving orthogonal optimal neutral directions.

The Branch-M result is structurally stronger for the Gate-0 wording, but its exact `90 deg` separation currently comes from competition between uncoupled modal blocks. D10-ZF is designed to remove exactly that simplification.

### D10-ZF continuous result

For a prescribed zonal potential `Phi(x)` with `U=Phi'`, fixed `k_y != 0`, and initially `N(x)=0`, the perturbation equations are

```math
\partial_t\nabla^2\varphi
+U\partial_y\nabla^2\varphi
-U''\partial_y\varphi
=C(\varphi-\eta),
```

```math
\partial_t\eta+U\partial_y\eta
=C(\varphi-\eta)-\kappa\partial_y\varphi.
```

The physical perturbation-energy balance is

```math
\frac{dE_{\rm pert}}{dt}
=\kappa\Gamma+\mathcal P_U
-C\int|\varphi-\eta|^2dx,
```

where `Gamma` remains the outward radial particle flux and `P_U` is the signed Reynolds-stress exchange with the prescribed mean flow. After discretization the required identity is

```math
A_U^\dagger M+M A_U
=2\kappa Q_\Gamma+2Q_U-D_C.
```

Thus the first coupled pilot remains autonomous and compatible with T1--T4, while simultaneously giving T3 a direct physical multichannel role.

### D10.1 structure-preserving discretization result

Use the orthonormal periodic radial Fourier basis `e_m=L_x^{-1/2} exp(i k_m x)` with a symmetric retained set `m=-K,...,K`. In coefficient space,

```math
D_x=\operatorname{diag}(i k_m),
\qquad
\Delta=D_x^2-k_y^2I,
```

and projected multiplication by a real prescribed `U(x)` is a Hermitian Toeplitz/Galerkin matrix `Umat`. Derivative-profile matrices are built from the same Fourier coefficients, so the finite-dimensional commutators

```math
[D_x,Umat]=U_x,
\qquad
[D_x,U_x]=U_{xx}
```

hold algebraically. This makes the continuous integration-by-parts balance exact after projection rather than defining `Q_U` from a residual.

The physics-derived discrete operators are

```math
M=\operatorname{diag}(-\Delta,I),
```

```math
Q_\Gamma=\frac{k_y}{2}
\begin{pmatrix}0&iI\\-iI&0\end{pmatrix},
```

```math
Q_U=\operatorname{diag}\left[
\frac{k_y}{2i}\left(U_xD_x-(U_xD_x)^\dagger\right),0
\right],
```

and

```math
D_C=2C
\begin{pmatrix}I&-I\\-I&I\end{pmatrix}.
```

The test-only assembly reproduces

```math
A_U^\dagger M+MA_U=2\kappa Q_\Gamma+2Q_U-D_C
```

to floating-point roundoff for a resolved sinusoidal profile. No `L_x`, radial resolution, profile harmonic, profile amplitude, or new damping law is frozen at this stage.

## Package E — Living theory note

**Status: active**

Maintain:

- `docs/theory_progress.tex` — source of truth for compact theory/progress notes;
- `docs/theory_progress.pdf` — compiled version with genuinely typeset equations.

Update this note after each material theorem, modeling decision, or gate decision. Equations in the PDF must be generated from LaTeX source, never inserted as formula images.

## Immediate next order

1. Promote the structurally validated D10.1 Fourier-Galerkin assembly to a production model module, still without selecting a zonal-flow amplitude.
2. Add production-level tests against the test-only reference assembly and the exact multichannel balance.
3. Then make the next physical pilot decision: choose one periodic zonal profile, radial domain/resolution pair, and stable/subcritical amplitude for a single falsification point.
4. Check resolution/sideband convergence, transport neutrality, spectral stability, and energy-versus-transport optimizer separation for that one coupled pilot.
5. After the autonomous coupled pilot, open the homogeneous-shear/nonautonomous branch as the candidate T5 theory extension.
6. Only after these physical-nontriviality gates pass, consider a controlled parameter map.
