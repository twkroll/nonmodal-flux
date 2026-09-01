# T4 — Short-time separation of energy-optimal and transport-optimal disturbances

**Date:** 2026-09-01  
**Status:** proved in finite dimension; supporting structural theorem; plasma relevance still to be tested

## Setup

Let

```math
\dot x = A x,\qquad x(0)=Bu,
```

with physical energy/free-energy metric

```math
M=M^\dagger\succ0,
```

physics-derived signed transport form

```math
Q=Q^\dagger,
```

and choose the natural input normalization

```math
R_{\rm in}=B^\dagger M B\succ0.
```

Define the terminal physical-energy operator in whitened input coordinates,

```math
K_E(T)=R_{\rm in}^{-1/2}B^\dagger e^{A^\dagger T}M e^{AT}B R_{\rm in}^{-1/2},
```

and the cumulative signed-transport operator

```math
K_Q(T)=R_{\rm in}^{-1/2}B^\dagger P_Q(T)B R_{\rm in}^{-1/2},
\qquad
P_Q(T)=\int_0^T e^{A^\dagger t}Qe^{At}\,dt.
```

Because of the natural normalization,

```math
K_E(0)=I.
```

Introduce the first energy-production matrix

```math
E_1=R_{\rm in}^{-1/2}B^\dagger(A^\dagger M+MA)B R_{\rm in}^{-1/2},
```

and, for a transport-neutral admissible space `B^\dagger QB=0`, the first transport-production matrix

```math
H_1=R_{\rm in}^{-1/2}B^\dagger(A^\dagger Q+QA)B R_{\rm in}^{-1/2}.
```

Then

```math
K_E(T)=I+TE_1+O(T^2),
```

while T1 gives

```math
K_Q(T)=\frac{T^2}{2}H_1+O(T^3).
```

## Proposition T4.1 — Limiting optimal subspaces

Assume the largest eigenvalue of `E_1` is simple, with normalized eigenvector `v_E`, and the largest eigenvalue of `H_1` is simple, with normalized eigenvector `v_Q`.

Let `u_E(T)` be a normalized maximizer of terminal physical energy and `u_Q(T)` a normalized maximizer of cumulative positive signed transport, both expressed in whitened input coordinates. Then, after a phase choice,

```math
u_E(T)\to v_E,
\qquad
u_Q(T)\to v_Q
\qquad(T\downarrow0),
```

and the energy-transport angle satisfies

```math
\vartheta(T)
=\arccos\!\left(|u_E(T)^\dagger u_Q(T)|\right)
\longrightarrow
\vartheta_0
=\arccos\!\left(|v_E^\dagger v_Q|\right).
```

If `v_E` and `v_Q` are not collinear, then there exists `T_0>0` such that the energy-optimal and transport-optimal disturbances are distinct for all `0<T<T_0`.

### Proof

Subtracting the identity and dividing by `T` gives

```math
\frac{K_E(T)-I}{T}=E_1+O(T).
```

The eigenvectors of `K_E(T)` are the same as those of `(K_E(T)-I)/T`. Standard perturbation theory for Hermitian matrices with a simple isolated largest eigenvalue therefore implies convergence of its dominant normalized eigenvector to `v_E`.

Likewise,

```math
\frac{2K_Q(T)}{T^2}=H_1+O(T),
```

so the dominant transport eigenvector converges to `v_Q`. Continuity of the absolute inner product gives the angle limit. If the limiting angle is positive, continuity gives a positive separation for sufficiently small horizons. `\square`

## Proposition T4.2 — Balance interpretation under transport-neutral initialization

Suppose a one-channel physical balance holds,

```math
A^\dagger M+MA=gQ-D,
\qquad D=D^\dagger\succeq0,
```

and the admissible space is transport-neutral,

```math
B^\dagger QB=0.
```

Then

```math
E_1
=-R_{\rm in}^{-1/2}B^\dagger D B R_{\rm in}^{-1/2}
\preceq0.
```

Thus the short-time energy-optimal disturbance is the **least initially dissipative** admissible direction, while the short-time transport-optimal disturbance is controlled by the independent matrix

```math
H_1
=R_{\rm in}^{-1/2}B^\dagger(A^\dagger Q+QA)B R_{\rm in}^{-1/2}.
```

The two short-time optimals coincide only if their relevant extremal eigenspaces intersect appropriately. In the simple-eigenvalue case, coincidence requires the least-dissipative eigenvector of the projected dissipation matrix to equal the maximal transport-production eigenvector.

### Interpretation

This is stronger than the generic statement that two arbitrary observables have different optimizers. Under the physical balance and initial transport-neutrality, the two optimization problems acquire different physical meanings:

- energy optimal: lose the least free energy initially;
- transport optimal: generate the target signed flux most rapidly.

## Corollary T4.3 — Positive signed transport despite monotone physical energy

Assume

```math
A^\dagger M+MA\preceq0,
```

so that the physical energy is monotonically nonincreasing for every trajectory. Also assume

```math
B^\dagger QB=0
```

and

```math
\lambda_{\max}(H_1)>0.
```

Then for all sufficiently small `T>0`,

```math
\mathcal G_{Q,+}(T)>0,
```

although

```math
E_M(x(T))\le E_M(x(0))
```

for every initial condition.

This gives a precise local-in-time version of the project claim that monotone global physical energy does not suppress directed transport channels.

## Multi-channel balance

If

```math
A^\dagger M+MA
=\sum_{\alpha=1}^r g_\alpha Q_\alpha-D
```

and the target channel `a` is initially neutral,

```math
B^\dagger Q_aB=0,
```

then

```math
E_1
=R_{\rm in}^{-1/2}B^\dagger
\left(\sum_{\beta\ne a}g_\beta Q_\beta-D\right)
B R_{\rm in}^{-1/2}.
```

Hence the short-time energy optimal is controlled by competing physical channels plus dissipation, whereas the target-flux optimal is controlled by the first dynamical derivative of `Q_a`. This is the version most relevant to a later particle-versus-heat-flux model.

## Degeneracy warning

Because `K_E(0)=I`, the zeroth-order energy problem is fully degenerate. The first nonzero coefficient in the expansion of `K_E(T)-I` selects the short-time energy optimal. If `E_1` is proportional to the identity or has a degenerate largest eigenvalue, higher-order terms must be used. The same applies to `H_1` when its relevant eigenvalue is degenerate or zero.

## Coordinate invariance

Under `x'=Sx` with

```math
A'=SAS^{-1},\quad
M'=S^{-\dagger}MS^{-1},\quad
Q'=S^{-\dagger}QS^{-1},\quad
B'=SB,
```

both projected matrices `E_1` and `H_1` are unchanged. Therefore the limiting angle `\vartheta_0` is a physical coordinate invariant.

## Current assessment

T4 is useful because it upgrades the vague claim `u_E\ne u_Q` to a falsifiable short-time statement with a physical interpretation. The underlying perturbation theory is standard, so T4 alone is unlikely to carry P1. Its value is highest when combined with:

1. a physics-derived Luelff-style flux operator;
2. a physically justified transport-neutral input space;
3. a robust finite-horizon mismatch in the plasma pilot;
4. T2/T3 balance bounds explaining the finite-horizon magnitude.

## Immediate tests for the future JAX core

1. Verify the `K_E(T)=I+TE_1+O(T^2)` scaling.
2. Verify the `K_Q(T)=T^2H_1/2+O(T^3)` scaling under `B^\dagger QB=0`.
3. Verify convergence of the numerical energy/transport angle to `\vartheta_0` in a nondegenerate analytic example.
4. Add a contractive example with `A^\dagger M+MA\preceq0` and `\lambda_{\max}(H_1)>0`.
5. Verify coordinate invariance of `E_1`, `H_1`, and `\vartheta_0`.