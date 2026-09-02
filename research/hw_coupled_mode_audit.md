# Audit of physically justified mode coupling for the Hasegawa-Wakatani pilot

**Date:** 2026-09-02  
**Status:** coupling mechanisms assessed; no new coupling convention frozen yet

## Purpose

The uncoupled two-mode D2-A pilot gives a clean two-dimensional transport-neutral input space and a finite-horizon separation between energy-optimal and particle-flux-optimal initial disturbances. Its exact modal direct-sum structure is, however, the next falsification target. This note asks how to remove that direct-sum simplification without inserting an ad-hoc off-diagonal matrix.

The project rule D5 remains binding: any coupling must come from a continuous physical model before discretization. We therefore reject a generic constant block coupling

```math
A=\begin{pmatrix}A_1&C_{12}\\C_{21}&A_2\end{pmatrix}
```

unless `C_12` and `C_21` are derived from a stated physical mechanism.

## Baseline PDE and frozen D2-A objects

In the sign/orientation convention already frozen as D2-A, the non-zonal HW equations can be written schematically as

```math
\partial_t\zeta+\{\phi,\zeta\}=C(\phi-n)+\mathcal D_\zeta,
\qquad \zeta=\nabla^2\phi,
```

```math
\partial_t n+\{\phi,n\}=C(\phi-n)-\kappa\,\partial_y\phi+\mathcal D_n.
```

For a homogeneous zero-flow background, each Fourier mode is independent and reduces to the already tested D2-A `2 x 2` matrix. The physical perturbation energy and radial particle flux remain

```math
E=\frac12\int\left(|\nabla\phi|^2+|n|^2\right)\,d^2x,
```

```math
\Gamma=\int n v_x\,d^2x,
\qquad v_x=-\partial_y\phi.
```

Any coupled discretization must be derived from these continuous expressions rather than reweighted after assembly.

## Candidate A — prescribed zonal-flow background: recommended autonomous robustness test

Let the background contain a stationary zonal potential `Phi(x)` and, optionally, a stationary zonal density `N(x)`. Write

```math
\phi=\Phi(x)+\varphi,
\qquad n=N(x)+\eta,
```

and linearize in `(varphi,eta)`. With

```math
U(x)=\Phi'(x),
```

the linearized advection contains the terms

```math
U(x)\,\partial_y\nabla^2\varphi
```

and

```math
-U''(x)\,\partial_y\varphi
```

in the vorticity equation, together with

```math
U(x)\,\partial_y\eta
```

and, if `N` is retained, an additional term proportional to `N'(x)\partial_y\varphi` in the density equation. Thus a nonuniform zonal profile couples radial Fourier sidebands at fixed `k_y`.

This is not an invented coupling. Linearization of modified HW-type models about prescribed zonal states is a standard route in the drift-wave/zonal-flow literature. Zhu, Zhou and Dodin (Phys. Rev. Lett. 124, 055002, 2020; arXiv:1910.05227) explicitly study a prescribed zonal velocity `U(x)` and zonal density `N(x)` and obtain a linear drift-wave operator whose spectrum depends on `U`, `U''`, and the effective density gradient. Numata, Ball and Dewar (Phys. Plasmas 14, 102312, 2007) provide the modified-HW zonal-flow context. Recent reduced-mode studies of HW turbulence also retain zonal modes and their sidebands rather than representing their effect by arbitrary matrix couplings.

### Why this is attractive for the present project

For fixed `U(x)` and `N(x)` the perturbation problem remains autonomous:

```math
\partial_t x=\mathcal A_{U,N}x.
```

After a documented radial discretization at one nonzero `k_y`, this becomes a constant finite-dimensional matrix `A_{U,N}`. Therefore the current finite-horizon machinery for terminal output, accumulated transport, Cholesky whitening, and T1--T4 applies without changing its mathematical definitions.

The physical metric and target transport observable are still obtained from

```math
E=\frac12\int\left(|\partial_x\varphi|^2+k_y^2|\varphi|^2+|\eta|^2\right)dx
```

and

```math
\Gamma=k_y\int\operatorname{Im}(\eta^*\varphi)\,dx.
```

A spectral/Galerkin or structure-preserving real-space discretization then produces `M` and `Q_Gamma` including the radial quadrature/mass matrix. This is precisely the D5-compatible construction.

### Important balance change

A prescribed zonal flow is an external/background energy reservoir for the perturbations. Consequently, the perturbation energy balance generally acquires a mean-flow exchange term in addition to density-gradient drive and dissipation. One should therefore not assume in advance that the old single-mode identity

```math
A^\dagger M+MA=2\kappa Q_\Gamma-D
```

survives unchanged. The coupled operator must be derived first, and its symmetric `M`-part must be decomposed into physically interpretable density-gradient, mean-flow-exchange, and dissipative terms.

This is scientifically useful rather than a defect: it tests whether transport-optimality remains distinct from energy-optimality when physically meaningful mode exchange is present.

### Discretization warning

A sinusoidal zonal flow such as

```math
U(x)=u\cos(q_Zx)
```

couples a radial Fourier mode to neighboring sidebands. A two-sideband truncation is not exactly closed; the full Fourier chain is infinite. Therefore the next test should not hide this by declaring an arbitrary `4 x 4` closed model. Two defensible choices are:

1. a small but explicitly stated Galerkin truncation with convergence checked by adding sidebands, or
2. a modest periodic radial grid/spectral discretization at fixed `k_y`.

The second route is cleaner for the first robustness test because it avoids making the truncation itself the main modeling assumption.

## Candidate B — homogeneous shear: recommended subsequent theory-extension test

For a homogeneous shear flow `U(x)=Sx`, the canonical shearing-wave representation uses a time-dependent radial wave number,

```math
k_x(t)=k_{x0}-S k_y t
```

(up to sign convention). The corresponding HW operator is nonautonomous,

```math
\dot z=A(t)z,
```

rather than a constant matrix. Linear drift waves in collisional plasma with homogeneous shear have explicitly been treated by a nonmodal HW approach in the literature (e.g. Mikhailenko, Mikhailenko and Stepanov, Phys. Plasmas 7, 94, 2000).

This is physically very natural and strongly aligned with the nonmodal theme, but it is not merely an application change. It promotes the project from

```math
\Phi(T)=e^{AT}
```

to a time-ordered propagator `Phi(t,t0)` and makes the higher-order short-time transport-generation hierarchy depend on time derivatives of the generator. It is therefore the natural candidate for a later nonautonomous theorem package rather than the first coupled robustness check.

## Candidate C — radially varying density-gradient background

Allowing `kappa=kappa(x)` also destroys radial Fourier independence. In the density equation, multiplication by `kappa(x)` couples radial Fourier components of `phi`.

This mechanism is physically legitimate, but it complicates the interpretation of the energy balance: the background drive couples to a spatially weighted local particle flux rather than simply `kappa` times the domain-integrated `Gamma`. The target observable `Q_Gamma` remains the unweighted physical radial particle flux, while the drive term becomes a distinct weighted quadratic form. That is potentially interesting for T3/multichannel ideas, but it is a less clean first test of whether the present optimizer separation survives mode coupling.

## Candidate D — evolving zonal mode / nonlinear triad

Retaining the zonal mode dynamically together with drift-wave sidebands gives the familiar nonlinear drift-wave/zonal-flow interaction. Reduced HW models built from zonal modes and sidebands are well established, and recent work emphasizes that several retained modes can be required to reproduce transport-regime transitions.

However, once the zonal amplitude evolves through quadratic mode coupling, the perturbation dynamics are no longer the constant linear initial-value problem addressed by the current T1--T4 package. This should remain a later branch rather than the immediate Gate-0 robustness test.

## Ranking

For the current research question the candidates rank as follows:

1. **Prescribed zonal-flow linearization with radial discretization** — best immediate application/robustness test; physically derived coupling; autonomous; current finite-horizon theory still applies.
2. **Homogeneous shear / shearing waves** — best next theory-extension target; physically canonical and intrinsically nonautonomous.
3. **Radially varying density gradient** — useful later for separating target flux from spatially weighted drive and for multichannel/balance questions.
4. **Fully evolving zonal-flow triads** — important nonlinear application, but premature for the present linear Gate-0 sequence.

## Proposed next gate

No coupling parameters are frozen in this audit. The next modeling decision should choose whether to adopt the prescribed-zonal-flow route as the immediate coupled pilot.

If accepted, the implementation sequence should be:

1. derive the linearized continuous equations around prescribed `U(x)` (and initially set `N(x)=0` unless a source-level reason requires otherwise);
2. derive the continuous perturbation-energy balance and identify the mean-flow exchange term explicitly;
3. derive `M` and the unweighted physical `Q_Gamma` before discretization;
4. choose a small periodic radial domain/discretization and verify convergence against a finer radial resolution;
5. only then choose one subcritical/stable zonal-flow profile and run the finite-horizon energy-versus-transport comparison.

This keeps the immediate step primarily a **physical robustness test of T1--T4**. The homogeneous-shear case should follow as a separate branch because it is the point where the **underlying theory itself becomes nonautonomous**.

## Literature anchors used in this audit

- H. Zhu, Y. Zhou, I. Y. Dodin, *Theory of the Tertiary Instability and the Dimits Shift from Reduced Drift-Wave Models*, Phys. Rev. Lett. **124**, 055002 (2020), DOI 10.1103/PhysRevLett.124.055002; arXiv:1910.05227.
- R. Numata, R. Ball, R. L. Dewar, *Bifurcation in electrostatic resistive drift wave turbulence*, Phys. Plasmas **14**, 102312 (2007), DOI 10.1063/1.2796106.
- P. L. Guillon, R. Angles, Y. Sarazin, D. Gürcan, *Anisotropic truncation for turbulent transport and zonal flows in the Hasegawa-Wakatani system*, Plasma Phys. Control. Fusion **68**, 085022 (2026).
- V. S. Mikhailenko, V. V. Mikhailenko, K. N. Stepanov, *Temporal evolution of linear drift waves in a collisional plasma with homogeneous shear flow*, Phys. Plasmas **7**, 94 (2000), DOI 10.1063/1.873785.
- M. A. Beer/Camargo-era nonmodal HW context remains represented by Camargo, Tippett and Caldas, Phys. Rev. E **58**, 3693 (1998), DOI 10.1103/PhysRevE.58.3693.
