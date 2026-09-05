# Fusion F2.5 — Structure-Preserving Phase-Space Discretization / Quadrature Specification Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER / `research/master/prompts/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`  
**Status:** `F2.5 PASS — STRUCTURE-PRESERVING DISCRETIZATION / QUADRATURE SPECIFICATION FROZEN — RETURN TO MASTER`

## Scope

This gate freezes one numerical state-space architecture and one predeclared three-level refinement ladder for the already-frozen reduced F2-R model

\[
\boxed{
\text{finite-ion-FLR electrostatic local-GK ions}
+\text{collisionless bounce-averaged trapped electrons}
}
\]

at the F2.3 single CBC-compatible point and with the F2.4 continuous input geometry

\[
B=I_{\mathcal H_{F2}},
\qquad
R_{\rm in}=\mathcal M_{F2}.
\]

No discrete generator, physical channel matrix, spectrum, growth rate, propagator, Gramian, cumulative objective, optimizer, principal angle, performance gap or GENE run is constructed or inspected here. No cutoff or resolution below was chosen from spectral or transport behavior.

The purpose is to provide a fixed numerical representation on which the next gate can reconstruct the discrete generator, Helmholtz metric and physical transport forms and then test the exact algebraic balance before any spectral calculation.

---

# 1. Frozen primary numerical package

The primary semidiscrete representation is

\[
\boxed{
\text{compact-support ballooning Galerkin/SBP spectral elements in }\theta
\;\times\;
\text{Hermite--Laguerre ion velocity quadrature}
\; + \;
\text{orbit-regularized trapped-electron quadrature}.
}
\]

The representation is continuous-time. F2.5 freezes no time integrator.

The design principles are:

1. use the physical phase-space measures and positive quadrature weights in every mass/free-energy form;
2. represent the collisionless ion parallel/mirror flow variationally in a split/skew form rather than by an ad hoc dissipative stencil;
3. keep the electrostatic potential algebraic and eliminate it from the physical state;
4. retain both signs of ion parallel velocity with no parity reduction;
5. treat trapped/passing separatrices and turning sets as measure-zero geometric sets, not extra state variables;
6. use the same quadratures for the later free-energy and physical particle/heat-flux forms;
7. add no hyperdiffusion, hypercollision, filtering, diagonal loading or artificial damping.

These choices follow established gyrokinetic numerical structure: Laguerre/Hermite velocity representations can preserve gyrokinetic free-energy structure when assembled consistently, and weak/DG-type Hamiltonian gyrokinetic discretizations can preserve energy identities when the physical phase-space weak form is retained. These literature facts are used only as numerical-design support; F2.5 does not import a different physical model.

Literature anchors:

- Parker & Dellar, *J. Plasma Phys.* 81 (2015), Laguerre–Hermite pseudo-spectral velocity formulation of gyrokinetics;
- Mandell et al., *J. Plasma Phys.* 86 (2020), energy-conserving weak/DG gyrokinetic phase-space discretization principles;
- Costello & Plunk, *J. Plasma Phys.* 91, E12 (2025), bounce-averaged trapped-electron state, ballooning incoming-boundary logic and orbit-time bounce measure.

---

# 2. Ballooning-line truncation and spatial basis

## 2.1 Finite-window family

The continuous F2.2 domain is

\[
\theta\in\mathbb R.
\]

Approximate it by compact-support Galerkin subspaces on

\[
\boxed{
-\Theta_W\le\theta\le\Theta_W,
\qquad
\Theta_W=(2W+1)\pi,
\qquad W=1,2,3
}
\]

for the three frozen resolution levels.

The endpoints are therefore always at circular-geometry magnetic-field maxima,

\[
\theta=\pm(2W+1)\pi,
\]

rather than cutting through the middle of a trapping well.

The finite-window basis is constrained to vanish at the two outer endpoints. This is not interpreted as a physical reflecting wall. It is a compact-support Galerkin approximation to the finite-free-energy state space on the infinite line. Smooth compactly supported functions are dense in the relevant finite-energy space, and increasing `W` moves the artificial boundary outward while keeping the central physical geometry unchanged.

No incoming/outgoing numerical damping is added at the boundary. The later qualification must verify domain convergence; it may not compensate a failed domain-convergence test by adding absorbing layers or damping.

## 2.2 Spectral elements

Partition the retained interval at every integer multiple of `pi`,

\[
[j\pi,(j+1)\pi],
\]

so every outboard/inboard magnetic extremum is an element boundary.

On each element use a continuous nodal Legendre--Gauss--Lobatto (LGL) polynomial basis. Adjacent elements share endpoint degrees of freedom. The two global outer endpoint degrees of freedom are removed to impose compact support. No even/odd parity reduction is made.

The spatial weak derivative must be assembled with the LGL mass/quadrature pair in summation-by-parts form. In the later ion generator, the parallel-streaming and mirror pieces must be assembled together from the conservative phase-space characteristic flow so that the source-free collisionless phase-space advection has the correct discrete adjoint relation with respect to the physical phase-space mass form.

A plain pointwise differentiation matrix followed by independent clipping or damping is not an admissible implementation of this freeze.

---

# 3. Ion phase-space representation

## 3.1 Fixed tensor-product coordinates

For numerical representation only, map the F2.1 invariant-coordinate ion state to the equivalent local coordinates

\[
\boxed{
(\theta,u,\zeta),
\qquad
u\equiv\frac{v_\parallel}{v_{Ti}}\equiv u,
\qquad
\zeta\equiv\frac{\mu_i B_0}{T_i}\ge0.
}
\]

Thus

\[
\mu_i=\frac{T_i}{B_0}\zeta,
\qquad
\frac{E_i}{T_i}
=\frac{u^2}{2}+\zeta\frac{B(\theta)}{B_0}.
\]

This is an invertible coordinate representation of the same physical ion phase space away from the measure-zero turning set. It does not change the F2.1 model. In these coordinates the parallel dynamics contains the corresponding mirror-force advection in `u`; that term must be included in the later variational generator assembly.

The physical velocity element is

\[
 d^3v
 =\frac{2\pi B}{m_i}\,d\mu_i\,dv_\parallel,
\]

while the F2.2 flux-tube spatial element contains `dl/B`. The magnetic-field factors therefore cancel in the combined spatial/velocity Jacobian before the Maxwellian/free-energy weights are applied. The later mass and weak-advection forms must use this physical combined measure, not a Euclidean coefficient norm.

## 3.2 Parallel velocity: both sigma branches

Use an even-order Gauss--Hermite nodal/Galerkin representation in

\[
u=u\in(-\infty,\infty)
\]

with the standard Maxwellian-compatible weight `exp(-u^2/2)`.

Because the node set is symmetric, every positive-`u` node has a negative-`u` partner. Hence both F2.1 orbit-sign branches

\[
\sigma=+1,
\qquad
\sigma=-1
\]

are retained automatically. No parity relation between them is imposed.

The exact turning set `u=0` has zero phase-space measure and is not introduced as an extra degree of freedom. The global Hermite representation is smooth across `u=0`; the later mirror term transports information continuously across the sign change. No bounce reflection rule, sign-copy rule or special `u=0` state is permitted.

## 3.3 Magnetic moment

Use Gauss--Laguerre nodal/Galerkin quadrature in

\[
\zeta\in[0,\infty)
\]

with reference weight `exp(-zeta)`.

The actual Maxwellian factor in these coordinates contains

\[
\exp\!\left[-\zeta\frac{B(\theta)}{B_0}\right],
\]

so the residual positive factor

\[
\exp\!\left[-\zeta\left(\frac{B}{B_0}-1\right)\right]
\]

is evaluated pointwise inside the physical quadrature. This keeps all quadrature weights in the entropy/free-energy form positive; it does not replace the local Maxwellian by a reference-field approximation.

No finite `v_parallel` or `mu` cutoff is introduced in F2.5; Hermite and Laguerre order are the velocity-space truncations.

---

# 4. Trapped-electron representation

## 4.1 State coordinates

The reduced nonadiabatic electron state remains

\[
g_e^{\rm tr}=g_e^{\rm tr}(E_e,\lambda,w),
\]

with no independent parallel-coordinate degree of freedom.

Use

\[
 x_e\equiv E_e/T_e\in[0,\infty),
\qquad
\widehat\lambda\equiv\lambda B_0.
\]

At the frozen circular geometry

\[
\boxed{1-\epsilon<\widehat\lambda<1+\epsilon}
\]

is the trapped interval.

For energy use generalized Gauss--Laguerre quadrature with the three-dimensional energy weight

\[
x_e^{1/2}e^{-x_e}.
\]

For pitch map the trapped interval affinely to

\[
y\equiv\frac{\widehat\lambda-(1-\epsilon)}{2\epsilon}\in(0,1)
\]

and use interior Gauss--Legendre nodes. Neither trapped/passing endpoint is a node.

## 4.2 Well labels

For

\[
\Theta_W=(2W+1)\pi
\]

retain exactly the complete circular wells centered at

\[
\theta=2\pi w,
\qquad
w=-W,\ldots,W.
\]

Hence the three frozen levels contain 3, 5 and 7 electron wells respectively. The well label remains an explicit electron-state index; geometrically identical wells are not identified because the ballooning-space potential and `k_perp(theta)` are not periodic under magnetic shear.

No partially cut boundary well is included.

## 4.3 Bounce points and regularized bounce quadrature

For a trapped pitch node, the circular bounce points in well `w` are

\[
\theta_{b,\pm}
=2\pi w\pm\theta_b,
\qquad
\cos\theta_b
=\frac{\widehat\lambda-1}{\epsilon}.
\]

The physical bounce average remains exactly

\[
\overline f
=\frac{\int_{\theta_{b,-}}^{\theta_{b,+}}f\,(dl/d\theta)\,d\theta/|v_\parallel|}
{\int_{\theta_{b,-}}^{\theta_{b,+}}(dl/d\theta)\,d\theta/|v_\parallel|}.
\]

Do not quadrature this expression directly at the square-root bounce singularities. Regularize each half orbit using the analytic circular-well substitution

\[
\boxed{
\sin\frac{\theta-2\pi w}{2}
=\sin\frac{\theta_b}{2}\,\sin\chi,
\qquad
-\frac{\pi}{2}<\chi<\frac{\pi}{2},
}
\]

which converts the endpoint singularity into a smooth integrand. Use interior Gauss--Legendre quadrature in `chi` for both numerator and denominator with the same nodes and weights.

The normalized bounce operator must be formed as a ratio of those two quadrature sums; no separately fitted bounce frequency or effective trapped fraction is introduced.

---

# 5. Separatrix and turning-point policy

The trapped/passing separatrix

\[
\widehat\lambda=1-\epsilon
\]

and the deeply trapped endpoint

\[
\widehat\lambda=1+\epsilon
\]

are measure-zero endpoints of the trapped pitch interval. They receive no electron state degree of freedom because the interior Gauss--Legendre rule contains neither endpoint.

Passing nonadiabatic electrons remain absent by the F2.1 model freeze:

\[
g_e^{\rm pass}=0.
\]

For ions, the `u=0` turning set is likewise not an independent state. Both ion velocity signs are represented in the same Hermite space and joined dynamically by the mirror term.

No artificial separatrix averaging, endpoint clipping, half-weight state or numerical detrapping operator is authorized.

---

# 6. Finite ion FLR

At every retained ion quadrature point evaluate

\[
v_\perp^2=\frac{2\mu_i B(\theta)}{m_i}
\]

and the exact frozen ion gyroaverage

\[
\boxed{
J_{0i}
=J_0\!\left(\frac{k_\perp(\theta)v_\perp}{\Omega_i}\right).
}
\]

No small-argument expansion is allowed.

The polarization/free-energy geometry uses the same frozen

\[
b_i(\theta)=k_\perp^2(\theta)\rho_i^2
\]

and

\[
\Gamma_{0i}(b_i)=I_0(b_i)e^{-b_i}
\]

convention as F2.1/F2.3. The later discrete field and free-energy forms must evaluate these quantities on the same `theta` representation and may not use a second FLR approximation for transport diagnostics.

For electrons the reduced ordering remains

\[
J_{0e}=1,
\qquad
\Gamma_{0e}=1.
\]

---

# 7. Quasineutrality: algebraic field elimination

Use the same LGL spectral-element space for the electrostatic potential as for the physical `theta` dependence, but do not include potential coefficients in the state/input vector.

At each resolution assemble the quasineutrality weak form from the same physical quadratures used for the kinetic state. The ion charge moment is obtained from the Hermite--Laguerre quadrature. The trapped-electron charge contribution is projected onto the potential test basis by orbit integration over the appropriate well support using the regularized bounce/orbit quadrature.

This gives an algebraic relation of the form

\[
C_{\rm QN,K}\,\phi_K=S_{\rm QN,K}x_K,
\]

with the field coefficient matrix inherited from the positive nonzonal electrostatic susceptibility.

Freeze the elimination rule

\[
\boxed{
\phi_K=P_{\rm QN,K}x_K,
\qquad
P_{\rm QN,K}=C_{\rm QN,K}^{-1}S_{\rm QN,K}.
}
\]

The solve must be done to algebraic precision. `phi_K` is never appended as an independent input coordinate, and no gauge pinning, diagonal loading or pseudo-inverse cutoff is permitted unless a later algebraic gate demonstrates a genuine physical nullspace; F2.1/F2.4 predict none in this nonzonal sector.

---

# 8. Discrete Helmholtz metric target

The later `M_K` must be generated directly from the discrete positive F2.1 Helmholtz functional, not inferred from `A_K` and not manufactured from a desired balance identity.

Evaluate

\[
2W_K
=\sum_a\left\langle
T_a\int\frac{|\delta F_{a,K}|^2}{F_{a0}}d^3v
+\frac{ne_a^2}{T_a}[1-\Gamma_{0a}]|\phi_K|^2
\right\rangle_K
\]

using the frozen positive phase-space quadratures and then substitute

\[
\phi_K=P_{\rm QN,K}x_K.
\]

The resulting quadratic form defines the later matrix `M_K`.

Required algebraic target:

\[
\boxed{M_K=M_K^\dagger\succ0}
\]

on the physical kinetic coefficient vector after field elimination.

No diagonal shift, eigenvalue clipping or nullspace deletion may be used to force this property. Failure of positivity at a frozen resolution is a discretization/algebraic failure to be reported, not regularized away.

Because the coefficient representation is conforming and directly parameterizes all retained kinetic degrees of freedom, F2.4 is inherited as

\[
\boxed{
B_K=I,
\qquad
R_{{\rm in},K}=M_K.
}
\]

If implementation details introduce an explicit coefficient-to-physical inclusion map, only the congruent equivalent

\[
R_{{\rm in},K}=B_K^\dagger M_KB_K
\]

is allowed; the physical input space may not be pruned.

---

# 9. Physical transport-channel bookkeeping for the next gate

F2.5 does not construct `Q_Gamma`, `Q_qi` or `Q_qe`. It freezes the bookkeeping required to do so later without changing quadrature or state space.

At every kinetic quadrature location retain or reproducibly reconstruct:

1. the physical phase-space weight;
2. `F_a0` and `delta F_a` after quasineutrality elimination;
3. `J0i` for ions and `J0e=1` for reduced electrons;
4. the signed radial gyrocentre-velocity kernel `V_psi,a` in the F2.2 Fourier orientation;
5. the energy `E_a` and heat factor `E_a-5T_a/2`;
6. the `theta` geometry factors and field basis values;
7. for trapped electrons, the well/pitch support and the same regularized orbit quadrature used to evaluate `bar(phi)`.

The later particle and heat forms must be assembled from the already frozen physical definitions

\[
\Gamma_a
=\operatorname{Re}\left\langle\int\delta F_aV_{\psi,a}^*d^3v\right\rangle,
\]

\[
q_a
=\operatorname{Re}\left\langle\int\delta F_a
\left(E_a-\frac52T_a\right)V_{\psi,a}^*d^3v\right\rangle.
\]

No channel may use a coarser diagnostic grid, independent interpolation, fitted flux coefficient or balance-derived surrogate.

---

# 10. Frozen three-level resolution ladder

No level below was inspected through `A`, eigenvalues, transport or finite-time objectives.

| quantity | Level K0 — primary | Level K1 — refinement 1 | Level K2 — refinement 2 |
|---|---:|---:|---:|
| `W` in `Theta=(2W+1)pi` | 1 | 2 | 3 |
| `Theta_max` | `3 pi` | `5 pi` | `7 pi` |
| complete electron wells | 3 | 5 | 7 |
| `theta` elements, width `pi` | 6 | 10 | 14 |
| LGL polynomial degree per element `p_theta` | 12 | 16 | 20 |
| global interior `theta` DOF | 71 | 159 | 279 |
| ion Gauss–Hermite order `N_u` | 16 | 24 | 32 |
| ion Gauss–Laguerre order `N_mu` | 8 | 12 | 16 |
| trapped-e generalized Laguerre energy order `N_Ee` | 12 | 18 | 24 |
| trapped-e pitch order `N_lambda` | 12 | 18 | 24 |
| bounce `chi` quadrature order `N_b` | 24 | 36 | 48 |

Approximate kinetic-state sizes before any implementation-specific sparse elimination are therefore of order

\[
N_i\sim N_\theta N_uN_\mu,
\qquad
N_e\sim N_{\rm well}N_{Ee}N_\lambda,
\]

giving approximately

- `K0`: `N_i=9088`, `N_e=432`;
- `K1`: `N_i=45792`, `N_e=1620`;
- `K2`: `N_i=142848`, `N_e=4032`.

These dimensions are bookkeeping estimates, not a statement that the later matrices must be stored densely.

No additional hidden intermediate resolution may replace this ladder for qualification. If the ladder proves computationally infeasible, the branch must return to MASTER rather than silently changing the numerical architecture after seeing physics results.

---

# 11. Reduced-electron ordering on the retained support

At the frozen F2.3 point,

\[
\frac{\rho_e}{\rho_i}=\frac1{\sqrt{3672}}\approx0.0165025,
\]

and with `alpha_MHD=0`, `kx0=0`, `shat=0.8`, `ky rho_i=0.3`,

\[
k_\perp(\theta)\rho_e
=0.3\frac{\rho_e}{\rho_i}
\sqrt{1+(0.8\theta)^2}.
\]

Therefore the maximum value at the frozen window edge is

- `K0`, `|theta|=3pi`: `max k_perp rho_e ~= 0.03765`;
- `K1`, `|theta|=5pi`: `max k_perp rho_e ~= 0.06241`;
- `K2`, `|theta|=7pi`: `max k_perp rho_e ~= 0.08724`.

Thus every predeclared level remains below `0.1` on its retained support. This is only an ordering check; it is not a numerical convergence or effect claim.

If a later implementation evaluates the exact metric `k_perp` and obtains a materially larger value, that discrepancy must be resolved before spectral work.

---

# 12. Predeclared convergence and algebraic observables

The next numerical gates must report the following quantities at `K0`, `K1`, `K2` before interpreting any spectrum or finite-time result.

## 12.1 Geometry / quadrature only

1. Gauss--Hermite/Laguerre reproduction of selected Maxwellian density, energy and heat-weight moments.
2. Convergence of `J0i`-weighted and `Gamma0i` polarization test integrals for fixed manufactured smooth kinetic functions.
3. Convergence of regularized bounce denominators and bounce averages for fixed analytic test functions `1`, `cos(theta)` and the frozen `B(theta)`.
4. Trapped-electron charge projection consistency between direct orbit quadrature and the weak potential-space projection.
5. `max(k_perp rho_e)` on the full retained support.

## 12.2 State / field algebra once assembled

6. quasineutrality reconstruction residual `||C_QN phi-S_QN x||` for fixed manufactured/random coefficient vectors;
7. Hermiticity residual of the free-energy form;
8. successful positive-definite factorization of `M_K` with no shift or clipping;
9. equality `R_in,K=M_K` and full-rank `B_K=I` in the conforming representation;
10. convergence of `W_K` for fixed smooth manufactured states under projection/prolongation between levels.

## 12.3 Later operator/channel gate

11. source-free collisionless adjoint/skew residual of the conservative ion phase-space advection;
12. Hermiticity of the three physical channel forms after reconstruction;
13. discrete quasineutral ambipolarity residual for the particle channels;
14. complete F2.1 algebraic free-energy-balance residual using the independently reconstructed physical channels.

These are structure/convergence observables. They are not permission to inspect generator eigenvalues, transient growth, pseudospectra, propagators or objective separation.

---

# 13. What remains unfrozen

F2.5 intentionally leaves the following to later authorized gates:

- the actual assembled discrete `A_K`;
- the actual assembled `M_K` and physical `Q_Gamma,K`, `Q_qi,K`, `Q_qe,K` matrices;
- numerical values of the algebraic residuals listed above;
- any spectrum or growth rate;
- any finite-time propagator, Gramian or cumulative channel operator;
- any optimizer direction, principal angle or performance gap;
- any time-integration method;
- any GENE or fully kinetic collisional-reference implementation.

No physical parameter from F2.3 and no continuous input-space decision from F2.4 may be changed in response to later numerical behavior.

---

# 14. Source-fidelity / anti-bias audit

The discretization was selected before any F2-R spectrum or finite-time calculation.

The choices are driven by:

- the F2.2 infinite ballooning geometry and magnetic-well layout;
- the F2.1/F2.4 finite-free-energy state space;
- exact preservation of both ion velocity signs;
- direct treatment of the bounce singularity;
- positive physical quadrature for the Helmholtz metric;
- exact algebraic quasineutrality elimination;
- compatibility with later physical flux reconstruction;
- a predeclared refinement path whose largest domain remains within the reduced-electron `k_perp rho_e` ordering target.

No eigenvalue, transient-growth quantity, transport amplitude, optimizer angle or objective-separation magnitude was used to choose any cutoff or order.

---

# 15. Verdict

The F2-R state admits a concrete conforming numerical architecture that preserves the physical input geometry and provides a fixed path to algebraic qualification without ad hoc regularization or effect-guided tuning.

Therefore

\[
\boxed{
\text{F2.5 PASS — STRUCTURE-PRESERVING DISCRETIZATION / QUADRATURE SPECIFICATION FROZEN — RETURN TO MASTER}.
}
\]

No branch-side next gate is self-authorized.

**STOP / RETURN TO MASTER.**
