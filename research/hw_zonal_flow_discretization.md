# Structure-preserving radial discretization for the D10-ZF pilot

**Date:** 2026-09-02  
**Status:** D10.1 discretization design selected; no zonal-flow amplitude or pilot profile frozen yet

## Purpose

D10-ZF fixes the continuous autonomous perturbation problem around a prescribed nonuniform zonal flow. The next task is to discretize the radial coordinate without destroying the independently derived physical energy, radial particle flux, mean-flow exchange, or the exact multichannel balance.

This note selects a **periodic Fourier-Galerkin representation in the radial coordinate at one fixed nonzero `k_y`** for the first coupled pilot. This is a structural discretization choice, not a choice of zonal-flow amplitude, spectral stability point, or parameter sweep.

The main reason for using a coefficient-space Galerkin formulation rather than an aliased collocation formula is that multiplication by a prescribed profile and radial differentiation satisfy exact finite-dimensional commutator identities when both are represented by projected Fourier operators. Those identities reproduce the continuous integration-by-parts energy balance algebraically.

## Continuous D10-ZF equations

At fixed `k_y != 0`, write

```math
\varphi(x,y,t)=\hat\varphi(x,t)e^{i k_y y},
\qquad
\eta(x,y,t)=\hat\eta(x,t)e^{i k_y y}.
```

Define

```math
\Delta_k=\partial_x^2-k_y^2.
```

For a prescribed real zonal velocity `U(x)` and zero zonal density background, the accepted equations are

```math
\partial_t\Delta_k\hat\varphi
+i k_y U\Delta_k\hat\varphi
-i k_y U''\hat\varphi
=C(\hat\varphi-\hat\eta),
```

```math
\partial_t\hat\eta+i k_y U\hat\eta
=C(\hat\varphi-\hat\eta)-i\kappa k_y\hat\varphi.
```

The continuous physical quantities are

```math
E=\frac12\int_0^{L_x}
\left(
|\partial_x\hat\varphi|^2+k_y^2|\hat\varphi|^2+|\hat\eta|^2
\right)dx,
```

```math
\Gamma=k_y\int_0^{L_x}\operatorname{Im}(\hat\eta^*\hat\varphi)\,dx,
```

```math
\mathcal P_U=k_y\int_0^{L_x}
U'(x)\operatorname{Im}(\hat\varphi^*\partial_x\hat\varphi)\,dx,
```

and

```math
\frac{dE}{dt}=\kappa\Gamma+\mathcal P_U
-C\int_0^{L_x}|\hat\varphi-\hat\eta|^2dx.
```

## Radial Fourier-Galerkin space

Use an orthonormal periodic basis

```math
e_m(x)=L_x^{-1/2}e^{i k_m x},
\qquad
k_m=\frac{2\pi m}{L_x},
```

with a symmetric retained index set

```math
\mathcal I_K=\{-K,\ldots,K\}.
```

The number of retained radial modes is `N_x=2K+1`. Expand

```math
\hat\varphi(x,t)=\sum_{m\in\mathcal I_K}\phi_m(t)e_m(x),
\qquad
\hat\eta(x,t)=\sum_{m\in\mathcal I_K}\eta_m(t)e_m(x).
```

The state ordering is

```math
z=(\phi,\eta)^T\in\mathbb C^{2N_x}.
```

Because the basis is orthonormal, the projected radial `L^2` mass matrix is the identity. No post-hoc quadrature weights are introduced.

## Derivative and Laplacian matrices

Let

```math
D_x=\operatorname{diag}(i k_m),
```

so

```math
D_x^\dagger=-D_x.
```

Define

```math
\Delta= D_x^2-k_y^2 I
=-\operatorname{diag}(k_m^2+k_y^2).
```

Since `k_y != 0`, `Delta` is strictly negative definite and invertible on the retained radial space. Define

```math
K_\phi=-\Delta
=\operatorname{diag}(k_m^2+k_y^2)>0.
```

## Projected multiplication by the prescribed zonal flow

Let

```math
U(x)=\sum_q U_q e^{i 2\pi q x/L_x}
```

be a real prescribed periodic profile, so `U_{-q}=U_q^*`. Its projected multiplication matrix is the Toeplitz/Galerkin matrix

```math
(\mathsf U)_{mn}=U_{m-n},
\qquad m,n\in\mathcal I_K.
```

Hence

```math
\mathsf U^\dagger=\mathsf U.
```

The derivative-profile matrices must be generated from the **same Fourier coefficients**, not by an unrelated numerical differentiation:

```math
(\mathsf U_x)_{mn}=i(k_m-k_n)U_{m-n},
```

```math
(\mathsf U_{xx})_{mn}=-(k_m-k_n)^2U_{m-n}.
```

Then the finite-dimensional commutator identities hold exactly:

```math
[D_x,\mathsf U]=\mathsf U_x,
```

```math
[D_x,\mathsf U_x]=\mathsf U_{xx}.
```

Equivalently,

```math
[D_x^2,\mathsf U]=D_x\mathsf U_x+\mathsf U_xD_x.
```

These are the discrete counterparts of the product rule needed by the perturbation-energy balance.

## Discrete physical energy metric

The Galerkin projection of the continuous energy gives

```math
E=\frac12 z^\dagger M z,
```

with

```math
M=
\begin{pmatrix}
K_\phi&0\\
0&I
\end{pmatrix}.
```

Thus `M=M^dagger>0` for every retained radial resolution because `k_y != 0`.

No additional modal weights are admissible unless they arise from a later change of physical normalization or geometry.

## Discrete outward particle-flux form

The unweighted physical radial particle flux becomes

```math
\Gamma=k_y\operatorname{Im}(\eta^\dagger\phi)
=z^\dagger Q_\Gamma z,
```

where

```math
Q_\Gamma=
\frac{k_y}{2}
\begin{pmatrix}
0&iI\\
-iI&0
\end{pmatrix}.
```

This is the direct radial Galerkin extension of the frozen D2-A single-mode flux operator. It remains Hermitian and indefinite.

## Discrete mean-flow exchange form

The projected continuous quantity

```math
\mathcal P_U
=k_y\operatorname{Im}(\phi^\dagger\mathsf U_xD_x\phi)
```

is represented by a Hermitian potential-space block

```math
H_U
=\frac{k_y}{2i}
\left[
\mathsf U_xD_x-(\mathsf U_xD_x)^\dagger
\right].
```

Since `D_x^dagger=-D_x` and `U_x^dagger=U_x`, this can also be written as

```math
H_U
=\frac{k_y}{2i}
\left(\mathsf U_xD_x+D_x\mathsf U_x\right).
```

The full signed mean-flow exchange operator is

```math
Q_U=
\begin{pmatrix}
H_U&0\\
0&0
\end{pmatrix},
```

so

```math
\mathcal P_U=z^\dagger Q_U z.
```

`Q_U` is a signed physical exchange form, not a norm and not part of the target particle-flux observable.

## Resistive sink

The continuous sink

```math
C\int|\hat\varphi-\hat\eta|^2dx
```

corresponds to

```math
D_C=2C
\begin{pmatrix}
I&-I\\
-I&I
\end{pmatrix}\succeq0.
```

The factor `2` is required because the energy is `E=(1/2)z^dagger M z`.

No perpendicular damping law is frozen in D10.1. The single-mode diagnostic damping used in D8 is not silently copied to an entire radial spectrum. Any later radial Laplacian/hyperdiffusive sink must be separately derived and added to the balance as its own positive-semidefinite contribution.

## Discrete coupled generator

Define

```math
F_\phi
=-i k_y\mathsf U\Delta
+i k_y\mathsf U_{xx}
+C I.
```

The Galerkin system is

```math
\dot z=A_U z,
```

with blocks

```math
A_{\phi\phi}=\Delta^{-1}F_\phi,
```

```math
A_{\phi\eta}=-C\Delta^{-1},
```

```math
A_{\eta\phi}=(C-i\kappa k_y)I,
```

```math
A_{\eta\eta}=-CI-i k_y\mathsf U.
```

The inverse here is only part of the analytic block expression. Production implementation should exploit the diagonal `Delta` through elementwise scaling or a linear solve rather than form a generic dense matrix inverse.

## Exact discrete multichannel balance

With the operators above, the commutator identity implies

```math
A_U^\dagger M+M A_U
=2\kappa Q_\Gamma+2Q_U-D_C.
```

The mean-flow part follows from

```math
i k_y\left(\mathsf U D_x^2-D_x^2\mathsf U\right)
=-i k_y\left(\mathsf U_xD_x+D_x\mathsf U_x\right)
=2H_U.
```

Therefore the finite-dimensional Galerkin system reproduces the continuous physical balance exactly up to floating-point roundoff, rather than defining `Q_U` afterward as a residual.

This is the key D5 requirement for the coupled pilot.

## Structural limits and sanity checks

### Zero zonal flow

For

```math
\mathsf U=\mathsf U_x=\mathsf U_{xx}=0,
```

`Q_U=0` and `A_U` decomposes into independent D2-A radial Fourier blocks with zero added perpendicular damping.

### Constant zonal flow

For a constant `U_0`,

```math
\mathsf U=U_0I,
\qquad
\mathsf U_x=\mathsf U_{xx}=0.
```

Hence `Q_U=0`. The flow contributes only the common fixed-`k_y` Doppler shift and does not couple radial modes or exchange perturbation energy.

### Nonuniform zonal flow

For a profile with nonzero Fourier coefficient at radial harmonic `q`, the multiplication matrix connects radial indices with

```math
m-n=q.
```

Thus a sinusoidal profile produces the expected nearest-sideband coupling in coefficient space without inserting an ad-hoc block matrix.

## Why not use raw Fourier collocation first

A pseudospectral collocation implementation is computationally natural, but naive pointwise multiplication plus differentiation can introduce aliasing and can spoil the exact finite-dimensional product-rule/commutator identity at a fixed resolution. The first structural implementation should therefore use coefficient-space projected multiplication matrices, for which the balance identity is algebraic.

A faster FFT/collocation realization may be added later only after it is shown to reproduce the same projected operators or after dealiasing is included and the balance residual is quantified.

## Resolution/convergence policy

D10.1 does **not** freeze `L_x`, `K`, a zonal harmonic, or a zonal-flow amplitude. Those enter the next physical pilot gate.

Before any optimizer result is interpreted, the following must be checked:

1. the exact matrix balance residual stays at floating-point roundoff for each resolution;
2. `M` remains positive definite and `Q_Gamma`, `Q_U` remain Hermitian;
3. the target profile is spectrally resolved by the retained Fourier coefficients;
4. spectral stability and the relevant finite-horizon gains/modes are stable under at least one radial-resolution increase;
5. boundary/truncation sensitivity of the optimizer is checked by adding radial sidebands before any parameter map is attempted.

## Implementation order

1. Add test-only Fourier-Galerkin assembly that verifies the commutator identities and exact multichannel balance for a simple resolved real profile.
2. Verify the `U=0` reduction to independent D2-A blocks and the constant-`U` Doppler-only limit.
3. Only after those tests pass, add a production zonal-flow model constructor using the same formulas.
4. Then select one prescribed profile and one amplitude for the first coupled falsification point, with a resolution check.

No coupled pilot parameter is selected in this note.