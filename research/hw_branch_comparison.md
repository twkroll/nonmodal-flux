# Hasegawa-Wakatani pilot branch comparison

**Date:** 2026-09-01  
**Status:** both diagnostic branches evaluated; no final branch freeze yet

## Purpose

The single complex two-field D2-A mode has a one-dimensional maximal totally
`Q_Gamma`-isotropic subspace.  Rather than choosing prematurely between a
minimal single-mode demonstration and a multidimensional neutral optimization,
we evaluate both constructions and compare what each actually establishes.

This note is a controlled falsification comparison, not a parameter sweep.

## Branch S — single frozen D8 mode

Use the accepted D8 case

```text
kx = 0.5
ky = 1.0
C = 1.0
kappa = 1.0
nu_k = 0.15
```

with the transport-neutral pure-potential input

```math
B_\phi=(1,0)^T,
\qquad
R_{\rm in}=1.25.
```

The entire physical state dynamics is strictly energy-contracting,

```math
A^\dagger M+MA\prec0,
```

and the neutral line has

```math
B_\phi^\dagger Q_\Gamma B_\phi=0.
```

Nevertheless the normalized first transport-generation coefficient is

```math
H_1=0.8>0.
```

At `T=1`, for that same neutral input direction,

```math
G^{\rm acc}_\Gamma(1)\approx0.13193948,
```

```math
G^{\rm term}_\Gamma(1)\approx0.14460273,
```

while the terminal physical-energy ratio is

```math
G_E(1)\approx0.56555978<1.
```

Thus the single-mode neutral branch gives a direct physical realization of
**dynamically generated outward signed particle transport from exactly zero
initial flux despite monotonically decreasing physical energy**.

The neutral line itself cannot compare two competing admissible directions.
On the unrestricted two-dimensional state space, however, the `T=1` terminal
energy eigenvalues are approximately

```math
0.01656892,\qquad0.90504223,
```

and the accumulated signed-flux extrema are approximately

```math
-0.12889160,\qquad0.27250824.
```

The top energy and top accumulated-transport directions have phase-invariant
angle

```math
\vartheta\approx0.48282038\ {\rm rad}\approx27.66^\circ.
```

This separation is real, but it is not a separation *inside the neutral line*.

## Branch M — two uncoupled D2-A modes

To remove only the neutral-subspace dimension obstruction, take two uncoupled
copies of the same frozen D2-A physics with the same `ky`, `C`, `kappa`, and
`nu_k`, differing only in radial wavenumber:

```text
mode 1: kx = 0.5, ky = 1.0
mode 2: kx = 1.5, ky = 1.0
C = 1.0, kappa = 1.0, nu_k = 0.15 for both
```

The state is the direct sum of the two `(phi,n)` modes.  Use the two-dimensional
input map

```math
B=
\begin{pmatrix}
1&0\\
0&0\\
0&1\\
0&0
\end{pmatrix},
```

so each column is initially pure potential in one Fourier mode.  The natural
input metric is

```math
R_{\rm in}=\operatorname{diag}(1.25,3.25),
```

and the whole two-dimensional admissible input space satisfies exactly

```math
B^\dagger Q B=0.
```

Both blocks are spectrally stable and the total four-dimensional physical
energy is strictly contractive.

### Short-time competition inside the same neutral space

After whitening by the natural input metric, the leading terminal-energy rate
operator is

```math
E_1=\operatorname{diag}(-1.9,-0.9153846154),
```

whereas the leading accumulated-transport generation operator is

```math
H_1=\operatorname{diag}(0.8,0.3076923077).
```

Hence the energy criterion selects mode 2 (least initial energy loss), while the
transport criterion selects mode 1 (strongest outward flux generation).  Their
optimal neutral input directions are exactly orthogonal in the whitened input
coordinates.

### Finite horizon `T=1`

The whitened terminal-energy operator is approximately

```math
K_E(1)=\operatorname{diag}(0.56555978,0.65428728),
```

while the whitened accumulated particle-transport operator is approximately

```math
K_\Gamma^{\rm acc}(1)
=\operatorname{diag}(0.13193948,0.07319417).
```

Thus at finite horizon the ranking remains reversed:

- energy-optimal neutral input: pure potential in mode 2;
- transport-optimal neutral input: pure potential in mode 1;
- phase-invariant angle: `pi/2`.

This is the first physical D2-A example in the repository where energy- and
transport-optimal disturbances differ **within the same multidimensional,
exactly transport-neutral admissible space** while total physical energy is
strictly decreasing.

## Interpretation and limitation

The two-mode result is stronger with respect to the abstract T4/Gate-0 wording,
because it combines transport neutrality and directional optimization in the
same admissible space.  However, its present `90 degree` separation is produced
by competition between two **uncoupled** Fourier blocks.  The construction does
not yet show a nontrivial mixed-mode optimizer or inter-mode dynamical coupling.
It should therefore be treated as the minimal dimensional proof-of-principle,
not yet as the strongest possible plasma result.

The single-mode result remains useful because it is maximally minimal and makes
the cross-phase/flux-generation mechanism transparent.  The two branches are
therefore complementary rather than mutually exclusive:

- Branch S isolates dynamic transport generation in one physical drift-wave
  mode;
- Branch M demonstrates a genuine multidimensional neutral optimization and
  energy/transport ranking reversal.

## Next falsification question

Before declaring Branch M the headline plasma result, test whether the
energy/transport separation persists in a less decomposable setting, for
example a physically justified coupled-mode/shearing construction or a richer
reduced model.  The current two-mode direct sum is already sufficient to show
that the single-mode neutral-dimension obstruction is not a fundamental
obstruction to the project formulation.