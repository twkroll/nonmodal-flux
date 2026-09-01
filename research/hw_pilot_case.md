# First spectrally stable Hasegawa-Wakatani pilot case

**Date:** 2026-09-01  
**Status:** selected for the first single-case pilot; no parameter sweep

## Frozen D2-A convention

This pilot uses the accepted D2-A non-zonal linear Hasegawa-Wakatani convention. The state is

```math
z_k=(\phi_k,n_k)^T,
```

with `x` radial, `y` poloidal, `v_E=e_z x grad(phi)`, Fourier convention `exp(i k dot x)`, physical energy metric

```math
M_k=\operatorname{diag}(k^2,1),
```

and signed outward radial particle-flux form

```math
Q_{\Gamma,k}=\frac{k_y}{2}
\begin{pmatrix}
0&i\\
-i&0
\end{pmatrix}.
```

No observable or metric is fitted to the pilot.

## Selected parameters

Use exactly one mode and one damping rate:

```text
kx       = 0.5
ky       = 1.0
C        = 1.0
kappa    = 1.0
nu_k     = 0.15
```

Thus `k^2=1.25` and

```math
A=
\begin{pmatrix}
-0.95&0.8\\
1-i&-1.15
\end{pmatrix},
\qquad
M=
\begin{pmatrix}
1.25&0\\
0&1
\end{pmatrix},
```

```math
Q_\Gamma=\frac12
\begin{pmatrix}
0&i\\
-i&0
\end{pmatrix}.
```

The explicit sink is

```math
D=2C
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}
+2\nu_kM
=
\begin{pmatrix}
2.375&-2\\
-2&2.3
\end{pmatrix}.
```

The damping is an explicit single-mode perpendicular damping rate. It is not inserted automatically by the model constructor and is not calibrated here as a realistic edge-plasma transport coefficient. Its role in this first falsification pilot is to place the already frozen drift-wave mode safely in the spectrally stable and energy-contractive regime while keeping the D2-A balance exact. A later physical application may replace this single-mode rate by a documented Laplacian or hyper-diffusive law before any parameter study.

## Spectral stability

The eigenvalues are approximately

```math
\lambda_1=-0.0629681-0.405255i,
\qquad
\lambda_2=-2.037032+0.405255i.
```

Hence the spectral abscissa is approximately `-0.06297 < 0`.

The generator remains nonnormal. In physical-energy coordinates

```math
A_M=M^{1/2}AM^{-1/2},
```

the Frobenius norm of the normality commutator is approximately

```math
\|A_M^\dagger A_M-A_MA_M^\dagger\|_F\approx1.1593,
```

so stability is not obtained by making the dynamics normal.

## Exact energy/flux balance and strict energy contraction

The frozen balance is

```math
A^\dagger M+MA=2\kappa Q_\Gamma-D.
```

For this pilot, the ordinary eigenvalues of the Hermitian balance matrix are approximately

```math
-4.57388,\qquad -0.101118,
```

so

```math
A^\dagger M+MA\prec0.
```

Equivalently, the generalized instantaneous energy-rate eigenvalues relative to `M` are approximately

```math
-4.10998,\qquad -0.0900249.
```

Therefore every nonzero trajectory has strictly decreasing physical energy. This makes the case a strong physical instantiation of the abstract T4 corollary: any positive signed particle transport cannot be attributed to transient growth of the chosen physical energy.

## Transport-neutral diagnostic input

For the first transport-neutral diagnostic use a pure-potential initial perturbation,

```math
B_\phi=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
R_{\rm in}=B_\phi^\dagger M B_\phi=1.25.
```

Then

```math
B_\phi^\dagger Q_\Gamma B_\phi=0,
```

so the initial particle flux vanishes exactly. Nevertheless,

```math
\frac{B_\phi^\dagger(A^\dagger Q_\Gamma+Q_\Gamma A)B_\phi}
{B_\phi^\dagger M B_\phi}=0.8>0.
```

Thus T1 predicts positive dynamically generated outward transport with cumulative onset `O(T^2)`. At `T=1`, the direct numerical diagnostic gives a normalized accumulated particle transport of approximately `0.13194`, while the terminal physical-energy ratio of the same input is approximately `0.56556 < 1`.

## Structural limitation of a single two-field Fourier mode

This point is important before the optimizer comparison is interpreted. For `k_y != 0`, `Q_Gamma` is nonsingular with signature `(1,1)`. Over complex input coordinates, a totally `Q_Gamma`-isotropic subspace can therefore have dimension at most one. Consequently a complex-linear transport-neutral map satisfying

```math
B^\dagger Q_\Gamma B=0
```

cannot have two independent columns for this single `2 x 2` Fourier mode.

The pure-potential neutral input above is therefore a genuine nontrivial **transport-generation diagnostic**, but its one-dimensional input space does not permit a directional competition between an energy-optimal and a transport-optimal initial condition inside the neutral subspace: there is only one admissible direction up to complex scaling.

This is not a numerical defect. It is a structural limitation of the single-mode two-field pilot. The full two-dimensional state can still be used to compare energy- and transport-optimal directions, while the neutral line can test dynamic generation of flux from zero initial transport. If the headline claim is required to combine both properties in the *same nontrivial neutral optimization space*, the next model must enlarge the state/input dimension, for example by using multiple Fourier modes or a richer physical model.

## Gate role

This case is deliberately chosen as a single falsification point, not as evidence from a parameter map. Before any sweep, the next calculation should decide how to handle the structural neutral-subspace limitation above and then compare finite-horizon energy and signed-particle-flux objectives consistently.