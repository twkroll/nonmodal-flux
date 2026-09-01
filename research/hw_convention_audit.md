# Hasegawa–Wakatani convention audit for the first plasma pilot

**Date:** 2026-09-01  
**Status:** convention comparison complete; D2 not yet frozen

## Purpose

Before implementing a Hasegawa–Wakatani model, fix the sign, Fourier, energy, and particle-flux conventions from a physical PDE statement. The first pilot is intended to test finite-horizon signed particle transport, not merely energy amplification, so the flux form must be derived from the physical radial `E x B` particle flux.

## Candidate model families

### 1. Original / standard 2-D Hasegawa–Wakatani form

A common normalized form uses vorticity `Omega = nabla_perp^2 phi` and density perturbation `n`,

```math
\partial_t\Omega+[\phi,\Omega]=C(\phi-n)+\text{dissipation},
```

```math
\partial_t n+[\phi,n]+\kappa\,\partial_y\phi=C(\phi-n)+\text{dissipation}.
```

The background density gradient is `kappa>0` for density decreasing in the positive radial `x` direction.

### 2. Modified Hasegawa–Wakatani form

The modified model replaces the resistive coupling by its non-zonal part,

```math
C(\phi-n)\longrightarrow C(\widetilde\phi-\widetilde n).
```

For the first single-mode pilot we require `k_y != 0`. Such a Fourier mode is non-zonal, so `tilde phi = phi` and `tilde n = n`. Therefore the original and modified HW models have the same linear `k_y != 0` subsystem relevant to this pilot. The original-vs-modified choice does not need to block the first linear transport calculation.

### 3. Flux-balanced Hasegawa–Wakatani form

The flux-balanced HW model changes the nonlinear/zonal structure and has better asymptotic behavior toward the modified Hasegawa–Mima limit. It is valuable for later nonlinear or zonal-flow studies. However, published comparisons state that the linear drift instability of the non-zonal sector is the same as in the modified HW model. It is therefore not necessary as the first finite-dimensional pilot unless the research question is specifically about zonal feedback.

## Recommended first-pilot convention

For the first linear non-zonal mode, use the standard/modified HW subsystem with the following explicit coordinate convention:

- `x` is radial and `y` is poloidal;
- `B = B e_z` and normalized `E x B` velocity is `v_E = e_z x grad phi`;
- hence the radial velocity is `v_x = -partial_y phi`;
- Fourier amplitudes use `exp(i k_x x + i k_y y)`;
- define `k^2 = k_x^2+k_y^2` and use the state `z_k=(phi_k,n_k)^T`.

With no added perpendicular dissipation, linearization of the non-zonal mode gives

```math
-k^2\dot\phi_k=C(\phi_k-n_k),
```

```math
\dot n_k+i\kappa k_y\phi_k=C(\phi_k-n_k),
```

or

```math
\dot z_k=L_k z_k,
```

with

```math
L_k=
\begin{pmatrix}
-C/k^2 & C/k^2\\
C-i\kappa k_y & -C
\end{pmatrix}.
```

This convention should be treated as provisional until D2 is explicitly frozen, but it has the advantage that the energy and radial particle-flux balance close exactly and transparently.

## Physical energy/free-energy metric

For the continuous HW energy

```math
E=\frac12\int\left(|\nabla\phi|^2+n^2\right)\,d^2x,
```

the corresponding single complex Fourier-mode contribution can be represented, up to the common Fourier-pair normalization, as

```math
E_k=\frac12\left(k^2|\phi_k|^2+|n_k|^2\right)
=\frac12 z_k^\dagger M_k z_k,
```

with

```math
M_k=\begin{pmatrix}k^2&0\\0&1\end{pmatrix}.
```

No ad-hoc weights are introduced.

## Physical radial particle-flux form

The radial turbulent particle flux is

```math
\Gamma=\langle n v_x\rangle
=-\langle n\,\partial_y\phi\rangle.
```

For the Fourier convention above, the modal signed flux is proportional to

```math
\Gamma_k=k_y\,\operatorname{Im}(n_k^*\phi_k).
```

Define `Q_{Gamma,k}` by `Gamma_k=z_k^dagger Q_{Gamma,k} z_k`. Then

```math
Q_{\Gamma,k}
=\frac{k_y}{2}
\begin{pmatrix}
0&i\\
-i&0
\end{pmatrix}.
```

This matrix is Hermitian and indefinite for `k_y != 0`. Its sign reverses if the radial direction, magnetic-field direction, or Fourier convention is reversed; those changes are convention changes, not changes in the physics. The outward-flux sign must therefore remain tied to the explicit coordinate convention above.

## Exact linear energy balance

For the proposed `L_k` and `M_k`, direct calculation gives

```math
L_k^\dagger M_k+M_kL_k
=2\kappa Q_{\Gamma,k}-2C S,
```

where

```math
S=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\succeq0.
```

Consequently

```math
\frac{dE_k}{dt}
=\kappa\Gamma_k-C|\phi_k-n_k|^2.
```

This identity is the main reason to prefer this convention for the first pilot: `M_k` and `Q_{Gamma,k}` are obtained independently from the continuous physical energy and flux, and the resulting matrices satisfy the expected physical balance without fitted weights.

In the abstract project notation,

```math
A^\dagger M+MA=gQ-D,
```

this corresponds to

```math
g=2\kappa,\qquad Q=Q_{\Gamma,k},\qquad D=2C S
```

before adding perpendicular dissipation.

## Added perpendicular dissipation

Many numerical HW formulations add Laplacian or hyper-diffusive terms. If the same Fourier damping rate `nu_k>=0` acts on both `phi_k` and `n_k`, then

```math
L_k\longrightarrow L_k-\nu_k I
```

and the balance gains the additional positive semidefinite sink

```math
D_{\perp,k}=2\nu_k M_k.
```

This is a clean way to obtain a spectrally stable pilot if the undamped resistive-drift mode is unstable at the chosen parameters. The precise dissipation model should be frozen together with the numerical pilot, rather than inserted merely to force stability.

## What is and is not decided by this audit

The audit removes one apparent ambiguity: for a single `k_y != 0` linear pilot, original HW and modified HW coincide in the sector being studied. It also fixes the algebraic consequences of one explicit spatial/Fourier orientation.

A genuine D2 decision remains before implementation: whether to freeze this convention as the repository standard, including the outward radial sign and the chosen perpendicular dissipation model. No `hasegawa_wakatani.py` implementation should be added before that freeze.

## Recommended D2 freeze

Recommended wording:

> **D2.** For the first plasma pilot use the non-zonal (`k_y != 0`) linear Hasegawa–Wakatani subsystem with `x` radial, `y` poloidal, `v_E=e_z x grad phi`, Fourier convention `exp(i k dot x)`, state `(phi_k,n_k)`, physical energy `E_k=(k^2|phi_k|^2+|n_k|^2)/2`, and outward particle flux `Gamma_k=k_y Im(n_k^* phi_k)`. The exact matrices are derived from these definitions before discretization. Original and modified HW are equivalent for this single non-zonal linear mode. Any perpendicular dissipation used to make the pilot spectrally stable must be stated explicitly and retained in the physical balance.

## References used in the convention audit

- S. J. Camargo, M. K. Tippett, I. L. Caldas, *Nonmodal energetics of resistive drift waves*, Phys. Rev. E 58, 3693–3704 (1998), DOI 10.1103/PhysRevE.58.3693. This is the main nonmodal HW reference for the project; the accessible abstract confirms the nonnormal/nonmodal and density–potential phase-shift focus, but the present sign derivation is not inferred from the abstract.
- A. Hasegawa and M. Wakatani, *Plasma edge turbulence*, Phys. Rev. Lett. 50, 682–686 (1983).
- R. Numata, R. Ball, R. L. Dewar, *Bifurcation in electrostatic resistive drift wave turbulence*, Phys. Plasmas 14, 102312 (2007), for the modified HW non-zonal coupling.
- A. J. Majda, D. Qi, A. J. Cerfon, *A flux-balanced fluid model for collisional plasma edge turbulence: model derivation and basic physical features*, Phys. Plasmas 25, 102307 (2018), DOI 10.1063/1.5049389, arXiv:1807.08054.
- R. Guillon and O. D. Gürcan, *Flux-driven turbulent transport using penalisation in the Hasegawa–Wakatani system*, J. Plasma Phys. 91, E145 (2025), DOI 10.1017/S0022377825100895. This provides an explicit modern fixed-gradient mHW convention and the radial particle-flux definition `Gamma_n=<n v_x>`, with `v_x=-partial_y phi`.
