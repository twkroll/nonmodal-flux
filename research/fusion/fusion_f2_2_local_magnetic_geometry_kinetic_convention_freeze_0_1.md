# Fusion F2.2 — Local Magnetic-Geometry Family / Kinetic Convention Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER / `research/master/prompts/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`  
**Status:** `F2.2 PASS — LOCAL MAGNETIC-GEOMETRY / KINETIC CONVENTIONS FROZEN — RETURN TO MASTER`

## Scope

This gate freezes only the continuous local toroidal geometry family and the kinetic coordinate/trapping/bounce conventions for the already-frozen reduced F2-R architecture

\[
\boxed{
\text{finite-ion-FLR electrostatic local-GK ions}
+\text{collisionless bounce-averaged trapped electrons}
}
\]

with passing electrons adiabatic at leading order.

No density/temperature-gradient amplitudes, physical geometry point, wavenumber point, phase-space discretization, kinetic input map `B`, input cost `R_in`, discrete `A/M/Q`, spectrum, propagator, Gramian, cumulative objective, optimizer, GENE run or effect size is constructed here.

The selection criterion is source fidelity, transparent trapped-particle geometry, tractability and later local-GK/GENE mapping only.

---

# 1. Geometry-family decision

The primary F2-R geometry family is frozen as

\[
\boxed{
\text{large-aspect-ratio circular local tokamak}
\; + \;
\hat s\text{-}\alpha_{\rm MHD}\text{ flux-tube geometry}
}
\]

in ballooning space.

This is a source-consistent specialization rather than a change of the F2-R model. The bounce-averaged-electron source equations are written for a general local toroidal flux tube through the functions

\[
B(l),\qquad k_\perp(l),\qquad \omega_{da}(l),
\]

and the exact orbit/bounce average. The selected circular `s-alpha` family supplies these functions analytically while retaining a genuine magnetic well and finite ion FLR. It is also a standard mapping target for local gyrokinetic codes.

The family is selected before any numerical value of aspect ratio, safety factor, magnetic shear, `alpha_MHD`, ballooning angle or perpendicular wavenumber is inspected.

A square-well magnetic field is not selected as primary because it is useful analytically but is less direct as a later local-GK/GENE geometry reference. A shaped Miller-equilibrium family is not selected at F2.2 because it adds geometric parameters before the reduced two-species lineage has been qualified; it remains a later fidelity upgrade, not a competing F2.2 branch.

---

# 2. Magnetic coordinates, orientation and Fourier convention

## 2.1 Clebsch coordinates

Use magnetic coordinates

\[
(\psi,\alpha,l),
\]

with the Clebsch convention already used in F2.1,

\[
\boxed{\mathbf B=\nabla\psi\times\nabla\alpha.}
\]

Freeze the orientations as follows.

- `psi` is a local radial flux coordinate increasing outward.
- `alpha` is the field-line/binormal label whose sign is fixed by the Clebsch relation above.
- `l` is physical arc length along the magnetic field and increases in the direction of `B`.
- The geometric poloidal angle `theta` is chosen so that `theta=0` is the outboard midplane, `theta=pi` is the inboard midplane, and `dl/dtheta>0` for positive `q`.

The symbol `alpha` for the Clebsch field-line label must not be confused with the `s-alpha` equilibrium parameter `alpha_MHD` introduced below.

## 2.2 Perpendicular Fourier convention

For one local perpendicular Fourier component,

\[
\boxed{
f(\psi,\alpha,l,t)
=\hat f(l,t)\exp\!\left[i(k_\psi\psi+k_\alpha\alpha)\right].
}
\]

Hence

\[
\mathbf k_\perp
=k_\psi\nabla\psi+k_\alpha\nabla\alpha.
\]

The nonzonal F2-R sector is

\[
\boxed{k_\alpha\neq0.}
\]

The sign of every drift frequency is defined relative to this `exp(+i k dot x)` convention. No separate sign flip may be introduced later in a code mapping.

For the circular `s-alpha` representation it is convenient to use local physical radial/binormal wavenumbers `(k_x,k_y)` obtained from `(k_psi,k_alpha)` by the reference-surface metric. `k_y` is signed: positive `k_y` is the positive-`alpha` phase direction under this mapping. Its numerical value and sign representative are not frozen in F2.2.

---

# 3. Analytic circular large-aspect-ratio magnetic family

Let the reference surface have major radius `R0`, minor radius `r0`, and inverse aspect ratio

\[
\epsilon\equiv\frac{r_0}{R_0},
\qquad 0<\epsilon<1.
\]

The circular surface is

\[
R(\theta)=R_0\left(1+\epsilon\cos\theta\right).
\]

At the retained large-aspect-ratio order, freeze the field-strength family as

\[
\boxed{
B(\theta)
=\frac{B_0}{1+\epsilon\cos\theta}.
}
\tag{F2.2-B}
\]

Here `B0` is the reference toroidal-field scale at `R=R0`. Thus

\[
B_{\min}=\frac{B_0}{1+\epsilon}
\quad\text{at}\quad\theta=2\pi w,
\]

\[
B_{\max}=\frac{B_0}{1-\epsilon}
\quad\text{at}\quad\theta=(2w+1)\pi,
\qquad w\in\mathbb Z.
\]

The leading circular field-line metric is

\[
\boxed{
\frac{dl}{d\theta}
\equiv J_l(\theta)
=qR(\theta)
=qR_0(1+\epsilon\cos\theta)>0.
}
\tag{F2.2-l}
\]

Equivalently,

\[
\mathbf b\cdot\nabla\theta
=\frac{1}{qR(\theta)}.
\]

The Clebsch spatial Jacobian is then

\[
\boxed{
d^3r
=\frac{d\psi\,d\alpha\,dl}{B}
=\frac{J_l(\theta)}{B(\theta)}
\,d\psi\,d\alpha\,d\theta.
}
\tag{F2.2-J}
\]

Terms beyond the selected large-aspect-ratio circular ordering, including shaped surfaces and higher-order corrections to `|B|` from the poloidal field, are not silently included. They belong to a later geometry-fidelity upgrade if authorized.

---

# 4. `s-alpha` perpendicular metric and magnetic shear

Let

\[
\hat s
\equiv\frac{r_0}{q}\frac{dq}{dr}
\]

be the local magnetic shear and let `alpha_MHD` denote the standard `s-alpha` pressure/Shafranov-shift geometry parameter. Both remain symbolic in F2.2.

Freeze a local radial wavenumber `k_x0` at `theta=0` and a signed binormal wavenumber `k_y`. Define

\[
\boxed{
\Lambda(\theta)
\equiv
\frac{k_{x0}}{k_y}
+\hat s\,\theta
-\alpha_{\rm MHD}\sin\theta.
}
\tag{F2.2-Lambda}
\]

The perpendicular wavenumber is

\[
\boxed{
k_\perp^2(\theta)
=k_y^2\left[1+\Lambda^2(\theta)\right].
}
\tag{F2.2-kperp}
\]

This is the frozen circular `s-alpha` metric convention for the reduced F2-R lineage.

When `shat != 0`, define the ballooning angle by

\[
\boxed{
\theta_0
\equiv-rac{k_{x0}}{\hat s k_y},
}
\]

so that

\[
\Lambda(\theta)
=\hat s(\theta-\theta_0)
-\alpha_{\rm MHD}\sin\theta.
\]

Thus the sign relation between radial wavenumber and ballooning angle is frozen. `theta0`, `kx0` and `ky` remain numerical parameters for a later gate.

Under one poloidal turn,

\[
\boxed{
\Lambda(\theta+2\pi)
=\Lambda(\theta)+2\pi\hat s.
}
\]

Equivalently, the local radial wavenumber shifts as

\[
\boxed{
k_x(\theta+2\pi)
=k_x(\theta)+2\pi\hat s\,k_y.}
\tag{F2.2-twist}
\]

This fixes the sign needed by any later twist-and-shift implementation.

The ion gyroaverage is therefore

\[
\boxed{
J_{0i}(\theta,E_i,\mu_i)
=J_0\!\left(
\frac{k_\perp(\theta)v_{\perp i}}{|\Omega_i(\theta)|}
\right),
}
\]

with finite ion FLR retained.

---

# 5. Magnetic-drift convention

## 5.1 General source-faithful definition

Use signed cyclotron frequency

\[
\Omega_a
=\frac{e_a B}{m_a c},
\]

where `e_a` includes the species charge sign.

Define curvature

\[
\boldsymbol\kappa
=\mathbf b\cdot\nabla\mathbf b.
\]

The guiding-centre magnetic drift is frozen as

\[
\boxed{
\mathbf v_{da}
=\frac{1}{\Omega_a}
\mathbf b\times
\left(
 v_\parallel^2\boldsymbol\kappa
+\frac{v_\perp^2}{2}\nabla\ln B
\right).
}
\tag{F2.2-vd}
\]

The magnetic-drift frequency is

\[
\boxed{
\omega_{da}
\equiv\mathbf k_\perp\cdot\mathbf v_{da}
=\omega_{\kappa a}+\omega_{\nabla B,a}.
}
\tag{F2.2-omega}
\]

With the Fourier convention of section 2, the linear gyrokinetic equation contains

\[
\boxed{+i\omega_{da}g_a.}
\]

This fixes the sign unambiguously. A later code interface must reproduce this definition from its own coordinates rather than insert an independent sign convention.

Because `Omega_e<0` and `Omega_i>0` for a hydrogenic plasma, the charge-sign reversal is automatically included between electron and ion magnetic drifts.

## 5.2 Circular `s-alpha` specialization

At leading large-aspect-ratio order, curvature and grad-`B` share the standard circular `s-alpha` geometric factor. Define

\[
\boxed{
\mathcal D(\theta)
\equiv
\cos\theta+\Lambda(\theta)\sin\theta.
}
\tag{F2.2-D}
\]

The positive binormal orientation is chosen consistently with the Clebsch convention so that

\[
\boxed{
\omega_{da}(\theta)
=\frac{k_y}{\Omega_a R_0}
\left(v_\parallel^2+\frac{v_\perp^2}{2}\right)
\mathcal D(\theta)
}
\tag{F2.2-drift-sa}
\]

in this large-aspect-ratio representation.

The two physical pieces remain identifiable as

\[
\omega_{\kappa a}
=\frac{k_yv_\parallel^2}{\Omega_aR_0}\mathcal D(\theta),
\]

\[
\omega_{\nabla B,a}
=\frac{k_yv_\perp^2}{2\Omega_aR_0}\mathcal D(\theta).
\]

No numerical drift amplitude is frozen here.

For bounce-averaged trapped electrons, the governing drift is the orbit average

\[
\boxed{
\overline{\omega}_{de}(E_e,\lambda,w)
=\overline{\omega_{de}(\theta,E_e,\lambda)}_w.
}
\]

---

# 6. Trapped/passing classification

For the trapped-electron variables use the F2.1 pitch coordinate

\[
\boxed{
\lambda
\equiv\frac{v_\perp^2}{v^2B}.
}
\]

Then

\[
v_\parallel
=\sigma v\sqrt{1-\lambda B(\theta)},
\qquad \sigma=\pm1.
\]

The physically accessible orbit requires

\[
1-\lambda B(\theta)\ge0.
\]

For the selected circular field, freeze

\[
\boxed{
0\le\lambda<\frac1{B_{\max}}
\quad\Longrightarrow\quad\text{passing},
}
\]

and

\[
\boxed{
\frac1{B_{\max}}<\lambda<\frac1{B_{\min}}
\quad\Longrightarrow\quad\text{trapped}.
}
\tag{F2.2-trap}
\]

The separatrix `lambda=1/Bmax` is a measure-zero boundary with divergent bounce time and is treated as a limiting surface, not as an interior quadrature point in any later discretization.

For a trapped orbit in well `w`, the two bounce points satisfy

\[
\lambda B(\theta_\pm)=1.
\]

Writing

\[
\theta_\pm=2\pi w\pm\theta_b,
\qquad 0<\theta_b<\pi,
\]

the circular family gives

\[
\boxed{
\cos\theta_b
=\frac{\lambda B_0-1}{\epsilon}.
}
\tag{F2.2-bouncepoint}
\]

Each connected interval

\[
[\theta_-(\lambda,w),\theta_+(\lambda,w)]
\]

is one trapping well. In the present circular family there is one equivalent magnetic well per `2pi` period, but magnetic shear makes the perpendicular wavevector generally well dependent in ballooning space, so the well label `w` is retained in the electron state.

For any later noncircular geometry with multiple distinct wells in one period, `w` must label each connected component of the allowed set `1-lambda B>=0`. Disconnected wells are not averaged together.

---

# 7. Exact trapped-electron bounce average

For a quantity `h_sigma(theta,E,lambda,w)` on a trapped orbit, freeze the bounce average as the full forward/backward orbit-time average

\[
\boxed{
\overline h_w
=
\frac{
\displaystyle
\sum_{\sigma=\pm1}
\int_{\theta_-}^{\theta_+}
\frac{J_l(\theta)\,
 h_\sigma(\theta,E,\lambda,w)}
{v\sqrt{1-\lambda B(\theta)}}\,d\theta
}{
\displaystyle
\sum_{\sigma=\pm1}
\int_{\theta_-}^{\theta_+}
\frac{J_l(\theta)}
{v\sqrt{1-\lambda B(\theta)}}\,d\theta
}.
}
\tag{F2.2-bounce}
\]

The corresponding bounce period is

\[
\boxed{
\tau_b(E,\lambda,w)
=
\sum_{\sigma=\pm1}
\int_{\theta_-}^{\theta_+}
\frac{J_l(\theta)}
{v\sqrt{1-\lambda B(\theta)}}\,d\theta.
}
\]

For the leading bounce-averaged electron state, which is independent of `sigma`, the common factors of `2/v` cancel and the average reduces to

\[
\overline h_w
=
\frac{
\displaystyle
\int_{\theta_-}^{\theta_+}
 h(\theta)
\frac{J_l(\theta)d\theta}{\sqrt{1-\lambda B(\theta)}}
}{
\displaystyle
\int_{\theta_-}^{\theta_+}
\frac{J_l(\theta)d\theta}{\sqrt{1-\lambda B(\theta)}}
}.
\]

This is exactly the source bounce-time measure expressed in the frozen `theta` coordinate. It must be used for

\[
\overline\phi_w,
\qquad
\overline\omega_{de,w},
\]

and every other trapped-electron orbit average. No uniform-in-`theta` replacement is allowed.

The pitch-space velocity element remains

\[
\boxed{
d^3v
=\sum_{\sigma=\pm1}
\frac{\pi v^2B\,dv\,d\lambda}
{\sqrt{1-\lambda B}},
}
\]

consistent with the same orbit geometry.

---

# 8. Electron slow-transit ordering and FLR convention

Carry forward the F2.1 electron ordering

\[
\boxed{
\delta_e
\sim
\frac{\omega}{\omega_{be}}
\sim
\frac{L_\parallel}{v_{Te}\tau_D}
\ll1.
}
\]

At leading order, trapped-electron `g_e^tr` is constant along each bounce orbit and evolves only through its bounce-averaged equation.

For the nonzonal ballooning/flux-tube sector,

\[
\boxed{g_e^{\rm passing}=0}
\]

at this leading order; passing electrons therefore supply only the adiabatic response retained in quasineutrality.

Also carry forward

\[
\boxed{k_\perp\rho_e\ll1}
\]

on the physically retained ballooning support, so

\[
J_{0e}=1+O(k_\perp^2\rho_e^2)
\]

and electron FLR is not retained in F2-R.

Because `k_perp(theta)` grows under magnetic shear on the infinite ballooning line, the later parameter/discretization qualification must verify `k_perp rho_e << 1` over the numerically significant support of the perturbation and trapped-electron wells. Failure of that ordering is a model-validity failure, not permission to retune an effect.

Finite ion FLR remains fully retained through `J0i(theta)` and the polarization/free-energy structure.

---

# 9. Ballooning-space boundary and periodicity convention

The primary reduced F2-R representation is frozen in **ballooning space**:

\[
\boxed{\theta\in\mathbb R.}
\]

The equilibrium field strength and circular geometric coefficients are `2pi` periodic,

\[
B(\theta+2\pi)=B(\theta),
\]

but the sheared perpendicular wavevector is not periodic because of (F2.2-twist).

The ion distribution and electrostatic perturbation are required to lie in the finite-free-energy ballooning domain; in particular they must be square-integrable/decay sufficiently as `|theta| -> infinity` for the continuous free-energy and quasineutrality integrals to exist.

No even/odd parity restriction is imposed. The circular equilibrium is up-down symmetric, but parity is not a physical admissibility constraint and must not be used to remove kinetic directions before a later input-geometry gate.

At each electron bounce point, the forward and backward branches are connected by the physical reflection condition

\[
\boxed{
g_e(\sigma=+1,\theta_b)
=g_e(\sigma=-1,\theta_b).}
\]

The leading bounce-averaged trapped state is therefore `sigma` independent within each well.

A later finite-domain numerical implementation may use the twist-and-shift-equivalent flux-tube representation only if it reproduces the frozen shear relation and the same physical ballooning solution space to stated accuracy. The finite-domain choice itself is a discretization decision and is not frozen here.

---

# 10. Frozen geometry package versus unfrozen numbers

## 10.1 Frozen in F2.2

The following are now frozen for the primary reduced F2-R lineage:

- Clebsch coordinates `B = grad psi x grad alpha`;
- outward-increasing `psi`;
- `l` increasing along `B`;
- `theta=0` at the outboard midplane and `dl/dtheta>0` for `q>0`;
- Fourier factor `exp[i(k_psi psi+k_alpha alpha)]` and nonzonal `k_alpha != 0`;
- large-aspect-ratio circular field-strength family `B(theta)=B0/(1+epsilon cos theta)`;
- circular line metric `dl/dtheta=qR0(1+epsilon cos theta)`;
- Clebsch spatial Jacobian `dV=dpsi dalpha dl/B`;
- circular `s-alpha` perpendicular metric through `Lambda(theta)` and `k_perp(theta)`;
- magnetic-shear/twist sign convention;
- signed magnetic-drift definition `omega_da=k_perp dot v_da` and source term `+i omega_da g_a`;
- curvature and grad-`B` separation;
- trapped/passing pitch classification and circular bounce-point relation;
- exact orbit-time bounce-average measure and well labeling;
- bounce-averaged trapped-electron / adiabatic-passing-electron split;
- `k_perp rho_e << 1` reduced-electron convention;
- finite ion FLR through `J0i`;
- infinite ballooning-line continuous boundary convention;
- no parity reduction.

## 10.2 Numerical geometry/physical parameters deliberately not frozen

The following remain symbolic and require a later MASTER-authorized physical parameter freeze:

\[
\boxed{
R_0,\ B_0,\ \epsilon,\ q,\ \hat s,\ \alpha_{\rm MHD},\
 k_y,\ k_{x0}\ \text{or}\ \theta_0.
}
\]

Also not frozen here are equilibrium density/temperature gradients, temperature ratio, species normalization point and any dimensional collision parameter for the fully kinetic reference.

The trapped-particle fraction is not an independent knob in this geometry family; after `epsilon` is frozen it follows from `Bmin/Bmax` and the pitch-space measure.

No CBC numerical values are imported in F2.2. `Cyclone-Base-Case-compatible` means only that the family can later receive a CBC-style parameter point without changing its equations or coordinate definitions.

## 10.3 Later discretization choices deliberately not frozen

The following remain outside F2.2:

- truncation length or finite number of poloidal turns in `theta`;
- spatial basis/grid and twist-and-shift implementation;
- ion energy, magnetic-moment/pitch and sign grids;
- trapped-electron energy/pitch/well quadrature;
- treatment of the separatrix singularity;
- numerical bounce-integral quadrature;
- quasineutrality solve representation;
- kinetic `B` and `R_in`;
- discrete `A`, free-energy matrix and flux matrices;
- spectral or finite-time calculations.

---

# 11. Mapping target for a fully kinetic local-GK / GENE-compatible reference

No code execution is performed. F2.2 freezes only the quantities a later mapping must reproduce.

A GENE-compatible local reference must map the frozen continuous package to code coordinates `(x,y,z)` with

\[
z\leftrightarrow\theta,
\qquad
x\leftrightarrow\text{outward radial coordinate},
\qquad
y\leftrightarrow\text{binormal/Clebsch coordinate}
\]

up to one fixed, documented scale/sign transformation.

The mapping must match, before any comparison:

1. `B(z)` and `Bmin/Bmax`;
2. `q`, `shat`, `alpha_MHD` and aspect ratio;
3. `grad-parallel`, equivalently `b dot grad theta = 1/[qR(theta)]` at the selected ordering;
4. the metric combination producing `k_perp^2(z)`;
5. radial and binormal curvature/grad-`B` drift coefficients whose combination reproduces `omega_da=k_perp dot v_da`;
6. the spatial Jacobian/flux-tube volume weight;
7. the twist-and-shift sign `kx(theta+2pi)-kx(theta)=+2pi shat ky` under the frozen orientation;
8. ion gyroaveraging argument `k_perp v_perp/|Omega_i|`;
9. the same equilibrium-gradient sign convention when gradients are frozen later;
10. the same physical radial particle/heat-flux sign convention.

The fully kinetic reference does not impose the bounce-averaged trapped/passing reduction; rather, its kinetic electron orbits must reproduce the same `B(z)` and drift geometry so that the F2-R reduction can be interpreted as a controlled electron-transit ordering of the same local geometry.

---

# 12. Source-consistency checks

## 12.1 Bounce-averaged-electron source

Costello & Plunk's reduced system is formulated in a local toroidal flux tube with perpendicular Fourier decomposition, general `B(l)`, magnetic drift `omega_da`, finite ion gyroaveraging and trapped-electron bounce averaging. Their leading electron reduction uses bounce points defined by

\[
\lambda B(l_{1,2})=1
\]

and the orbit-time measure

\[
\overline h
\propto
\int h\,\frac{dl}{v_\parallel}.
\]

The F2.2 circular family supplies exactly those objects through (F2.2-B), (F2.2-l), (F2.2-drift-sa) and (F2.2-bounce). No closure term is added.

## 12.2 Standard local-GK / `s-alpha` compatibility

The selected `s-alpha` family uses the standard local magnetic-shear parameter

\[
\hat s=(r/q)dq/dr
\]

and the standard sheared ballooning combination

\[
\hat s(\theta-\theta_0)-\alpha_{\rm MHD}\sin\theta.
\]

This is the conventional simplified local geometry used widely in flux-tube gyrokinetics and is directly compatible with later CBC-style parameterization.

## 12.3 No fidelity selected from an effect

No spectrum, instability threshold, nonnormality, transient amplification, heat-flux magnitude, trapped fraction scan or optimizer separation was calculated or used to select this family.

---

# 13. PASS / HOLD / FAIL assessment

The F2.2 PASS conditions are met:

- the F2-R source accepts a general toroidal flux-tube geometry, so the circular `s-alpha` family is a legitimate specialization;
- the family contains a genuine analytic trapped-electron magnetic well;
- `B(theta)`, `dl/dtheta`, `k_perp(theta)`, magnetic drifts, pitch classification and bounce average are explicit;
- the electron slow-transit and `k_perp rho_e << 1` assumptions are preserved;
- the chosen ballooning boundary is consistent with the trapped-electron source reduction and does not turn the system into a closed-field-line periodic-electron problem;
- the geometry is directly mappable to a later local-GK/GENE reference;
- all numerical geometry values, gradients, wavenumbers and discretization choices remain unfrozen;
- no effect-oriented selection criterion was used.

Therefore

\[
\boxed{
\text{F2.2 PASS — LOCAL MAGNETIC-GEOMETRY / KINETIC CONVENTIONS FROZEN — RETURN TO MASTER}
}
\]

---

# 14. Allowed interpretations

F2.2 establishes that:

- the primary reduced F2-R lineage now has one explicit local toroidal geometry family and a complete continuous trapping/bounce convention;
- finite ion FLR and bounce-averaged trapped-electron dynamics can be represented consistently in the same circular `s-alpha` flux-tube family;
- later numerical work has an unambiguous sign convention for shear, drifts, bounce averages and radial/binormal Fourier phases;
- a later fully kinetic local-GK/GENE-compatible reference can use the same geometry before relaxing the bounce-averaged electron reduction.

# 15. Forbidden interpretations

F2.2 does **not** establish:

- a preferred numerical aspect ratio, `q`, magnetic shear or `alpha_MHD`;
- a preferred CBC point;
- a preferred `kx`, `ky` or ballooning angle;
- spectral stability or instability;
- transient growth or finite-time transport;
- any energy/particle/heat optimizer, angle or gap;
- that circular geometry is quantitatively sufficient for a final fusion claim;
- that a shaped/Miller geometry would give a larger or smaller effect;
- a phase-space discretization or admissible kinetic input geometry.

---

# 16. Remaining pre-effect objects

After F2.2 the unresolved objects include, at minimum:

1. one physical geometry/gradient/wavenumber parameter point chosen without effect inspection;
2. kinetic admissible initial-condition geometry `B` and physical input cost `R_in`;
3. structure-preserving phase-space discretization and bounce/quasineutral quadrature;
4. discrete reconstruction of particle and ion/electron heat channels from the physical integrals;
5. numerical/free-energy/spectral qualification;
6. later fully kinetic collisional-reference parameters and code normalization mapping.

This branch does not choose the order or content of the next gate. MASTER must decide and commit it explicitly.

---

# 17. Literature/source anchors

- P. J. Costello and G. G. Plunk, *Energetic bounds on gyrokinetic instabilities. Part 4. Bounce-averaged electrons*, Journal of Plasma Physics **91**, E12 (2025), arXiv:2404.06081. Source for the local finite-FLR ion plus bounce-averaged trapped-electron reduction, trapped/passing boundary conditions, bounce-average measure and `k_perp rho_e << 1` ordering.
- Standard `s-alpha` local flux-tube geometry as used in gyrokinetic modelling, with `shat=(r/q)dq/dr` and field-aligned sheared perpendicular metric.
- A. M. Dimits et al., *Comparisons and physics basis of tokamak transport models and turbulence simulations*, Physics of Plasmas **7**, 969 (2000). Cyclone Base Case benchmark lineage; used only as a later-compatible parameterization target, not as a numerical point in F2.2.
- GENE local flux-tube geometry documentation/literature: mapping target for `B(z)`, field-aligned metric, curvature, shear and twist-and-shift conventions; no GENE execution is part of this gate.

**STOP / RETURN TO MASTER.**
