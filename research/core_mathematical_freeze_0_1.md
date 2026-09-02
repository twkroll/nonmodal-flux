# CORE Mathematical Freeze 0.1

**Date:** 2026-09-02  
**Scope:** project history through the current D10-ZF production branch (`D10.2`)  
**Purpose:** create a robust mathematical reference and rollback point without declaring the theory final.

This document is a **freeze of the current mathematical state**, not a claim that all open questions are resolved. It distinguishes branch-independent mathematics from working assumptions, branch-dependent model results, conjectures, and open problems. Later changes should refer back to this document explicitly rather than silently rewriting the historical state.

## 0. Status vocabulary

- **STABLE** — branch-independent mathematical object, identity, theorem, numerical-algebraic fact, or definition that has been proved/validated in the present finite-dimensional scope and does not depend on the plasma branch choice.
- **ASSUMPTION** — hypothesis, modeling principle, normalization choice, or workflow rule used by the present theory but not itself a proved mathematical consequence.
- **BRANCH** — result or construction that depends on a specific modeling/convention decision and must not be promoted to universal CORE theory.
- **CONJECTURE** — plausible structural statement or research direction that is not yet proved or not yet physically established.
- **OPEN** — unresolved mathematical, modeling, interpretation, or novelty question.

The same formula may be **STABLE within a branch** while the branch itself is tagged **BRANCH**. In this freeze the top-level classification follows the more conservative status.

---

# 1. Reconstruction of the development

## 1.1 Foundational separation: energy metric versus signed transport observable

The project began by separating two objects that are often conflated in ordinary transient-growth work:

```math
M=M^\dagger\succ0
```

for physical disturbance size / energy / free energy, and

```math
Q=Q^\dagger
```

for a directed physical transport observable that may be indefinite.

This became decision **D1**. The project then adopted the stronger modeling rule **D5**: `M` and every physical `Q_alpha` must be derived from the continuous physical energy/free-energy and flux expressions before discretization; ad-hoc weighted amplitude sums are not admissible transport objectives.

This separation produced the basic research question:

> Can finite-horizon directed transport be generated and optimized from physically admissible initial conditions, including initially transport-neutral ones, even when the positive physical energy behaves very differently or even decreases monotonically?

## 1.2 General finite-dimensional formulation

The abstract autonomous system was written as

```math
\dot x=Ax,\qquad x(0)=Bu,
```

with admissible-input map `B` and positive input cost

```math
R_{\rm in}=R_{\rm in}^\dagger\succ0.
```

For a signed observable `Q`, the terminal quadratic output is

```math
J_Q^{\rm term}(T;u)
=u^\dagger B^\dagger e^{A^\dagger T}Qe^{AT}Bu,
```

and the cumulative transport is

```math
J_Q^{\rm acc}(T;u)
=u^\dagger B^\dagger P_Q(T)Bu,
```

where

```math
P_Q(T)=\int_0^T e^{A^\dagger t}Qe^{At}\,dt.
```

After whitening with `R_in`, both problems reduce to Hermitian extremal eigenvalue problems. Positive and negative signed branches are retained separately.

The model-independent numerical core was then implemented and validated: problem validation, constant propagator, terminal outputs, cumulative Gramians, Cholesky whitening, signed extremal eigenpairs, coordinate/scaling invariance, and synthetic theorem witnesses. No explicit metric inverse is used in production whitening.

## 1.3 T1 — transport-generation hierarchy

The first main theorem package introduced

```math
\mathcal L_A(X)=A^\dagger X+XA
```

and

```math
H_j=R_{\rm in}^{-1/2}
B^\dagger\mathcal L_A^j(Q)B
R_{\rm in}^{-1/2}.
```

The exact expansion

```math
P_Q(T)
=\sum_{j=0}^\infty
\frac{T^{j+1}}{(j+1)!}\mathcal L_A^j(Q)
```

implies the **transport-generation order**

```math
\nu=\min\{j\ge0:H_j\ne0\}.
```

If `H_0=...=H_{nu-1}=0` and `H_nu != 0`, then

```math
K_Q(T)
=\frac{T^{\nu+1}}{(\nu+1)!}H_\nu+O(T^{\nu+2}),
```

with matching signed eigenvalue asymptotics.

The transport-neutral condition

```math
B^\dagger QB=0
```

is exactly `H_0=0`. If `H_1 != 0`, cumulative signed transport begins at order `T^2`. A positive-semidefinite output behaves differently: `Q>=0` and `B^dagger Q B=0` imply `QB=0`, so the cumulative onset is no earlier than order `T^3`.

## 1.4 T2 — exact balance identity and signed bounds

The next structural step assumed a one-channel physical balance

```math
A^\dagger M+MA=gQ-D,
\qquad D\succeq0.
```

Integration gives

```math
gP_Q(T)
=e^{A^\dagger T}Me^{AT}-M+P_D(T),
```

where

```math
P_D(T)=\int_0^T e^{A^\dagger t}De^{At}\,dt.
```

With the natural input normalization

```math
R_{\rm in}=B^\dagger MB,
```

the whitened identity becomes

```math
gH_Q(T)=H_E(T)-I+H_D(T).
```

Under `M`-contractive dynamics and `g>0`, this yields physically interpretable signed bounds. The theorem package also established a no-free-lunch point: the balance alone does not produce a universally sharp initial-energy-only bound without additional structure.

## 1.5 T3 — multichannel balance, identifiability, and reachable bounds

The one-channel structure was generalized to

```math
A^\dagger M+MA
=\sum_{\alpha=1}^r g_\alpha Q_\alpha-D.
```

The first result is an identifiability/no-go statement: the total balance cannot determine individual channels. For example,

```math
Q_1'=Q_1+g_2S,
\qquad
Q_2'=Q_2-g_1S
```

leaves the total balance unchanged for any Hermitian `S`. This mathematically reinforces D5: individual physical flux channels must be derived independently, not reconstructed from the total energy balance.

For a target channel `a`, competing-channel lower bounds of the form

```math
g_\beta Q_\beta\succeq-c_\beta M
```

produce channel-resolved finite-horizon bounds. The theorem was corrected to separate a **global operator version** from a **reachable/admissible version**. For

```math
\mathcal R_T(B)
=\operatorname{span}\{e^{At}Bv:0\le t\le T\},
```

bounds known only on `R_T(B)` imply only the projected ordering on admissible inputs, not a global matrix inequality.

The corresponding reachable leakage constants are

```math
c_\beta(T,B)
=\max\left\{0,
\sup_{x\in\mathcal R_T(B),x\ne0}
\frac{-x^\dagger g_\beta Q_\beta x}{x^\dagger Mx}
\right\}.
```

A synthetic witness showed that reachable constants can be much sharper than global constants, but physical sharpness remains unproved.

## 1.6 T4 — short-time separation of energy- and transport-optimal inputs

With natural input normalization, define

```math
K_E(T)
=R_{\rm in}^{-1/2}
B^\dagger e^{A^\dagger T}Me^{AT}B
R_{\rm in}^{-1/2},
```

and

```math
E_1
=R_{\rm in}^{-1/2}
B^\dagger(A^\dagger M+MA)B
R_{\rm in}^{-1/2}.
```

Then

```math
K_E(T)=I+TE_1+O(T^2).
```

Under target transport-neutrality,

```math
K_Q(T)=\frac{T^2}{2}H_1+O(T^3).
```

If the relevant top eigenvalues are simple, the short-time energy-optimal and transport-optimal directions converge to the top eigendirections of `E_1` and `H_1`, respectively. Their limiting phase-invariant angle is a coordinate invariant.

For a one-channel balance and a neutral input space,

```math
E_1
=-R_{\rm in}^{-1/2}B^\dagger D B R_{\rm in}^{-1/2},
```

so the energy optimum is the least initially dissipative direction, whereas the transport optimum is the direction of strongest first target-flux generation. Positive signed transport can therefore exist for small time even when

```math
A^\dagger M+MA\preceq0.
```

## 1.7 Numerical-core validation before plasma application

The abstract core was tested in a deliberate sequence before broad application:

1. validated `TransportProblem(A,M,Q,B,R_in)`;
2. constant propagator;
3. terminal signed outputs;
4. cumulative transport Gramian;
5. coordinate/scaling invariance;
6. T1 short-time witnesses, including higher generation order and the PSD contrast;
7. T4/T2 bridge examples, including positive transport under monotone energy decay and one-channel balance bounds;
8. T3 multichannel identifiability, global bounds, contractive bounds, and reachable-subspace sharpening.

This sequence is important historically: the plasma pilot was not used to define the mathematics retrospectively.

## 1.8 D2 branch point — first Hasegawa-Wakatani physical realization

A convention audit compared standard/original HW, modified HW, and flux-balanced HW for the first non-zonal linear pilot.

The chosen path, **D2-A**, fixed:

```text
x = radial, y = poloidal,
v_E = e_z x grad(phi),
v_x = -partial_y phi,
Fourier amplitudes exp(i k_x x + i k_y y),
state z_k=(phi_k,n_k)^T,
k_y != 0.
```

The frozen undamped matrix is

```math
L_k=
\begin{pmatrix}
-C/k^2&C/k^2\\
C-i\kappa k_y&-C
\end{pmatrix}.
```

The independently derived physical forms are

```math
M_k=\begin{pmatrix}k^2&0\\0&1\end{pmatrix},
```

```math
Q_{\Gamma,k}
=\frac{k_y}{2}
\begin{pmatrix}0&i\\-i&0\end{pmatrix},
```

with

```math
\Gamma_k=k_y\operatorname{Im}(n_k^*\phi_k).
```

They satisfy

```math
L_k^\dagger M_k+M_kL_k
=2\kappa Q_{\Gamma,k}
-2C\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
```

The convention was independently locked by tests before the production model constructor was introduced.

## 1.9 D8 — first stable single-mode falsification point

A single diagnostic case was selected:

```text
kx=0.5, ky=1, C=1, kappa=1, nu_k=0.15.
```

The added uniform damping was explicit and retained in the exact physical sink. The case is spectrally stable, metric-nonnormal, and strictly `M`-contractive.

For the pure-potential input

```math
B_\phi=(1,0)^T
```

one has

```math
B_\phi^\dagger Q_\Gamma B_\phi=0
```

but positive first transport generation. At `T=1`, cumulative outward particle transport is positive while the terminal physical energy ratio is below one.

A structural limitation was identified: because the single-mode `Q_Gamma` has signature `(1,1)`, a complex-linear totally `Q_Gamma`-isotropic subspace has dimension at most one. The single neutral line therefore cannot contain a nontrivial directional competition between energy and transport optima.

## 1.10 D9 — single- and multi-mode branches evaluated in parallel

Rather than choosing prematurely, two diagnostic branches were computed.

**Branch S:** the D8 single mode. It isolates dynamic transport generation from exactly zero initial flux under strictly decreasing physical energy. On the full two-dimensional state space, energy- and cumulative-transport-optimal directions differ, but not within the one-dimensional neutral line.

**Branch M:** two uncoupled D2-A blocks with `kx=0.5` and `kx=1.5`, common `ky=C=kappa=1`, and the same diagnostic damping. A two-dimensional pure-potential input space is exactly transport-neutral. In that common neutral space, the short-time and `T=1` rankings are reversed: the energy criterion selects one mode and the transport criterion the other, giving a `90 degree` whitened angle.

The limitation of Branch M is explicit: the `90 degree` result arises from competition between uncoupled blocks. This motivated the next coupling audit.

## 1.11 Coupling audit and D10 branch point

Several physically legitimate ways to remove the direct-sum simplification were compared:

1. prescribed nonuniform zonal-flow linearization;
2. homogeneous shear / shearing waves;
3. radially varying density gradient;
4. fully evolving zonal-flow/drift-wave triads.

The chosen path, **D10-ZF**, is the prescribed-zonal-flow branch. The parked alternatives remain live rollback routes.

With

```math
\phi=\Phi(x)+\varphi,
\qquad n=\eta,
\qquad U(x)=\Phi'(x),
```

and initially `N(x)=0`, the linearized non-zonal equations are

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

At fixed nonzero `k_y`, the problem remains autonomous.

The continuous perturbation-energy balance is

```math
\frac{dE_{\rm pert}}{dt}
=\kappa\Gamma+\mathcal P_U
-C\int|\varphi-\eta|^2dx,
```

with a new signed mean-flow exchange channel

```math
\mathcal P_U
=k_y\int U'(x)
\operatorname{Im}(\hat\varphi^*\partial_x\hat\varphi)dx.
```

Thus D10-ZF gives a direct physical two-channel realization of the abstract T3 structure:

```math
A_U^\dagger M+MA_U
=2\kappa Q_\Gamma+2Q_U-D_C.
```

`Q_Gamma` remains the particle-transport target; `Q_U` is not merged into it.

## 1.12 D10.1 — structure-preserving Fourier-Galerkin discretization

A periodic coefficient-space Fourier-Galerkin representation was selected at fixed `k_y`.

With

```math
D_x=\operatorname{diag}(ik_m),
\qquad
\Delta=D_x^2-k_y^2I,
```

and projected multiplication matrices built from the same Fourier coefficients of `U`, the commutators

```math
[D_x,\mathsf U]=\mathsf U_x,
\qquad
[D_x,\mathsf U_x]=\mathsf U_{xx}
```

hold algebraically. This reproduces the continuous integration-by-parts energy balance after projection.

The discrete physical forms are

```math
M=\operatorname{diag}(-\Delta,I),
```

```math
Q_\Gamma=\frac{k_y}{2}
\begin{pmatrix}0&iI\\-iI&0\end{pmatrix},
```

```math
Q_U=\operatorname{diag}\left[
\frac{k_y}{2i}
\left(\mathsf U_xD_x-(\mathsf U_xD_x)^\dagger\right),0
\right],
```

and

```math
D_C=2C
\begin{pmatrix}I&-I\\-I&I\end{pmatrix}.
```

The exact multichannel balance holds to floating-point roundoff. The `U=0` limit returns independent D2-A blocks; constant `U` gives only a Doppler shift; sinusoidal `U` generates the expected sideband coupling.

## 1.13 D10.2 — production coupled-model assembly

The D10.1 formulas were promoted to a production model constructor. It validates the real-profile Fourier symmetry `u_{-q}=u_q^*`, returns the separate matrices `(A_U,M,Q_Gamma,Q_U,D_C)`, and constructs a `TransportProblem` with **only** `Q_Gamma` as the optimization target. It was tested against an independently coded reference assembler and the exact multichannel balance.

No radial domain, sideband count, zonal harmonic, zonal-flow amplitude, or new damping law has yet been frozen.

---

# 2. Current mathematical core

## 2.1 Central objects

### STABLE

The branch-independent CORE state is the tuple

```math
(A,M,Q,B,R_{\rm in})
```

or, for multiple physical channels,

```math
(A,M,\{Q_\alpha\},B,R_{\rm in},D).
```

The roles are distinct:

- `A`: linear generator;
- `M=M^dagger>0`: positive physical energy/free-energy metric;
- `Q_alpha=Q_alpha^dagger`: signed physical transport/exchange forms, possibly indefinite;
- `B`: admissible initial-state map;
- `R_in>0`: input cost/normalization;
- `D>=0`: dissipative sink when supplied by a physical balance.

### ASSUMPTION

The current theory is finite-dimensional, linear, and autonomous unless a branch explicitly says otherwise. The preferred physical normalization is often

```math
R_{\rm in}=B^\dagger MB,
```

but the abstract theory permits any positive `R_in`.

## 2.2 Central equations

### STABLE — terminal signed output

```math
K_Q^{\rm term}(T)
=R_{\rm in}^{-1/2}
B^\dagger e^{A^\dagger T}Qe^{AT}B
R_{\rm in}^{-1/2}.
```

Signed terminal extrema are the largest and smallest eigenvalues.

### STABLE — cumulative signed transport

```math
P_Q(T)=\int_0^T e^{A^\dagger t}Qe^{At}dt,
```

```math
K_Q(T)=R_{\rm in}^{-1/2}B^\dagger P_Q(T)BR_{\rm in}^{-1/2}.
```

### STABLE — transport neutrality

```math
B^\dagger QB=0.
```

This removes the trivial cumulative `O(T)` term.

### STABLE — transport-generation hierarchy

```math
H_j=R_{\rm in}^{-1/2}B^\dagger\mathcal L_A^j(Q)BR_{\rm in}^{-1/2},
```

```math
\nu=\min\{j:H_j\ne0\}.
```

### STABLE — energy comparison

```math
K_E(T)=R_{\rm in}^{-1/2}
B^\dagger e^{A^\dagger T}Me^{AT}B
R_{\rm in}^{-1/2}.
```

With natural normalization,

```math
K_E(T)=I+TE_1+O(T^2).
```

### STABLE — physical balance architecture

Single channel:

```math
A^\dagger M+MA=gQ-D.
```

Multiple channels:

```math
A^\dagger M+MA
=\sum_\alpha g_\alpha Q_\alpha-D.
```

### STABLE — reachable admissible dynamics

```math
\mathcal R_T(B)
=\operatorname{span}\{e^{At}Bv:0\le t\le T\}.
```

This is the natural domain for admissible-only channel bounds.

## 2.3 Central mechanisms

### STABLE — dynamic generation from neutral input

An indefinite signed observable can satisfy

```math
B^\dagger QB=0,
\qquad QB\ne0,
```

so the dynamics can generate signed output at first derivative order and cumulative order `T^2`.

### STABLE — energy/transport separation

The leading energy-optimal direction is selected by `E_1`, while the leading neutral transport-optimal direction is selected by `H_1`. They coincide only under an additional eigenspace-alignment condition.

### STABLE — balance does not identify channels

In a multichannel system the total energy balance fixes only the weighted sum of channels. Individual `Q_alpha` require independent physical definition.

### STABLE — admissible geometry matters

Bounds and optimizers depend on `B`. Global channel inequalities may be unnecessarily pessimistic; dynamically reachable subspaces can yield sharper constants, although physical sharpness is still open.

### STABLE — coordinate invariance

Under invertible physical state changes

```math
x'=Sx,
```

with the corresponding congruence transformations of `M`, `Q`, and `B`, the projected operators, generation order, signed gains, and short-time angle are invariant.

### STABLE — nonnormality is not the defining mechanism

The T1 generation theorem does not assume nonnormality. Nonnormality can be present and physically important, but signed transport generation from a neutral subspace is mathematically controlled by the projected Lyapunov derivatives of `Q`. Therefore `nonmodal transport` should not be reduced to ordinary transient energy growth.

---

# 3. Status register

## 3.1 STABLE

1. Distinction between positive metric `M` and Hermitian signed observable `Q` as the mathematical architecture.
2. Generalized Hermitian terminal and cumulative extremal problems after input whitening.
3. Exact cumulative Gramian `P_Q(T)` and its Lyapunov/Taylor expansion.
4. T1 transport-generation order and signed short-time eigenvalue asymptotics.
5. Structural difference between indefinite signed `Q` and positive-semidefinite outputs under projected neutrality.
6. Coordinate invariance of the projected hierarchy and short-time separation diagnostics.
7. T2 exact one-channel balance identity and its whitened form.
8. T2 contractive-energy signed bounds under their explicit hypotheses.
9. T2 no-free-lunch statement: balance alone is insufficient for a universally sharp energy-only bound.
10. T3 multichannel non-identifiability of individual channels from the total balance.
11. T3 global channel-resolved bounds under global quadratic lower bounds.
12. T3 reachable/admissible projected bounds under reachable-only lower bounds.
13. Definition and generalized-eigenvalue characterization of reachable leakage constants.
14. T4 short-time energy/transport optimizer separation under simple extremal eigenvalues.
15. Positive signed transport despite monotone physical energy when `B^dagger Q B=0` and `lambda_max(H_1)>0`.
16. The numerical implementation of the present finite-dimensional autonomous machinery and its analytic validation suite.
17. The statement that a one-dimensional neutral input space cannot support a directional energy-versus-transport competition; this is linear-algebraic, independent of plasma details.

## 3.2 ASSUMPTION

1. Finite-dimensional linear dynamics are the present CORE scope.
2. The main implemented theory is autonomous: `A` is constant.
3. Physical disturbance size is represented by a coercive Hermitian `M>0`.
4. Physical outputs of interest admit Hermitian quadratic forms `Q_alpha` after discretization.
5. Input cost `R_in` is positive definite; natural physical-energy normalization is preferred when appropriate.
6. D5 modeling rule: derive `M` and `Q_alpha` from continuous physical expressions before discretization; preserve signs, cross terms, channel separation, and discretization weights.
7. D6 workflow rule: no broad parameter sweep before structural validation.
8. Transport-neutrality `B^dagger Q B=0` is the preferred algebraic definition for initially neutral target transport unless a physical model supplies a more appropriate constraint.
9. Simplicity of extremal eigenvalues is required only for unique short-time eigenvector tracking, not for eigenvalue asymptotics.

## 3.3 BRANCH

1. **D2-A HW convention** and every formula involving the specific state `(phi_k,n_k)`, orientation, Fourier sign, `M_k`, and `Q_Gamma,k`.
2. **D8 stable single-mode calibration**, including `nu_k=0.15` and the numerical values of gains/eigenvalues.
3. **D9 Branch S** single-mode physical witness.
4. **D9 Branch M** uncoupled two-mode direct sum and its `90 degree` optimizer separation.
5. **D10-ZF** prescribed-zonal-flow linearization with initially `N(x)=0`.
6. D10-ZF mean-flow exchange form `Q_U` and the specific two-channel balance for that model.
7. **D10.1** periodic coefficient-space Fourier-Galerkin radial representation.
8. **D10.2** production zonal-flow assembler and its exact projected balance.

## 3.4 CONJECTURE

1. The most publishable CORE contribution will come from the **combination** of transport-neutral signed generation, independent positive physical metric, multichannel balance constraints, and a nontrivial physical pilot rather than from any one theorem T1–T4 alone.
2. Reachable-subspace leakage constants will remain materially sharper than global bounds in a physically resolved plasma model.
3. Removing the uncoupled direct-sum structure with a physically coupled D10-ZF operator will preserve a nontrivial energy-versus-transport optimizer separation.
4. A homogeneous-shear/shearing-wave branch will require and support a useful nonautonomous extension of the transport-generation hierarchy, potentially a future T5.
5. The CORE objects may provide useful interfaces to modal decomposition, continuation/bifurcation, and cascade/scale-transfer theories without changing the fundamental `M`/`Q` separation.

## 3.5 OPEN

1. Whether the D10-ZF coupled pilot has a spectrally stable/subcritical, well-resolved parameter point with a robust multidimensional transport-neutral optimizer separation.
2. Which prescribed `U(x)`, radial domain, resolution family, and physical damping law, if any, should be used for that pilot.
3. Whether `N(x)=0` remains sufficient once the prescribed zonal state is interpreted more physically.
4. Whether the D8 single-mode damping is only a diagnostic device or can be embedded in a physically justified radial dissipation model.
5. Physical sharpness of T3 leakage constants.
6. A common theorem package unifying terminal signed gain and cumulative signed gain.
7. Infinite-dimensional / operator-theoretic extension of T1–T4.
8. Nonautonomous generalization for `A(t)` and the exact role of `dot A`, higher time derivatives, or time-ordered propagators in the generation hierarchy.
9. Degenerate optimizer continuation and branch switching at eigenvalue crossings.
10. Exact novelty positioning relative to dissipativity, quadratic-output optimization, nonmodal plasma theory, and channel-resolved transport literature.
11. Which physical/admissible input map `B` should be regarded as canonical in a final plasma application rather than merely diagnostically useful.
12. Whether nonnormality should remain a central interpretation or a secondary dynamical modifier in the final narrative.
13. Whether T3 is a headline structural component or a supporting bound package after coupled-plasma results are known.

---

# 4. Decision and rollback map

## 4.1 D2 — first plasma-model convention

**Chosen path:** D2-A, non-zonal standard/modified two-field HW subsystem with the frozen orientation and Fourier convention.

**Parked alternatives:**

- alternative sign/orientation/Fourier conventions, provided all of `L`, `M`, and `Q_Gamma` are transformed consistently;
- flux-balanced HW for later nonlinear/zonal work;
- a richer drift-fluid model if the two-field state proves insufficient.

**Later results depending on D2-A:**

- convention-lock tests;
- minimal HW model constructor;
- D8 stable pilot;
- Branch S and Branch M;
- D10-ZF baseline and all subsequent zonal-flow formulas.

**Rollback point if D2-A fails:** return to the HW convention audit, not to T1–T4. The abstract CORE theory remains intact. Any replacement must re-derive `A`, `M`, `Q_Gamma`, outward-flux sign, and balance before reusing plasma results.

## 4.2 D8 — stable single-mode diagnostic case

**Chosen path:** one D2-A mode with explicit uniform damping `nu_k=0.15`.

**Parked alternatives:**

- another single stable parameter point;
- a physically derived Laplacian/hyperdiffusive damping law;
- no damping if a suitable stable regime exists.

**Later results depending on D8:** Branch S numerical values and one block of Branch M.

**Rollback point if D8 fails:** return to D2-A after the model constructor. T1–T4 and D2-A remain unaffected.

## 4.3 D9 — single versus multi-mode diagnostic branch

**Chosen path:** compute **both** Branch S and Branch M rather than selecting one prematurely.

**Parked alternative:** declaring one of the two as the headline plasma result before a coupling test.

**Later results depending on D9:** the explicit recognition that Branch S tests generation while Branch M tests multidimensional neutral optimizer separation; the coupling audit was motivated by Branch M's direct-sum limitation.

**Rollback point if Branch M is judged trivial:** retain Branch S as the minimal physical transport-generation witness and replace only the multidimensional branch.

## 4.4 Coupling branch point leading to D10

**Chosen path:** prescribed nonuniform zonal flow, autonomous after linearization.

**Parked alternatives:**

1. homogeneous shear / shearing waves — preferred later nonautonomous theory branch;
2. radially varying density gradient — potentially useful for weighted/local flux and T3 questions;
3. evolving zonal mode / nonlinear triad — later nonlinear branch;
4. richer reduced drift-fluid model.

**Later results depending on chosen path:** D10-ZF equations, mean-flow exchange channel, Fourier-Galerkin discretization, production assembler.

**Rollback point if prescribed ZF fails:** return to the coupling audit. D2-A, Branch S, Branch M, and all abstract CORE theorems survive. The first parked alternative to test should be homogeneous shear if the goal shifts toward new theory, or a richer autonomous reduced model if the goal remains a robustness test of T1–T4.

## 4.5 D10-ZF — prescribed zonal-flow linearization

**Chosen path:** stationary `Phi(x)`, `U=Phi'`, initially `N(x)=0`, fixed nonzero `k_y`.

**Parked alternatives:** nonzero zonal density `N(x)`, varying density-gradient branch, homogeneous shear, fully dynamic zonal feedback.

**Later results depending on D10-ZF:** the two-channel balance `Q_Gamma + Q_U`, sideband coupling, D10.1 and D10.2.

**Rollback point if D10-ZF continuous balance or physical state is inconsistent:** return to the coupling audit. Do not modify the abstract T3 balance to rescue the model.

## 4.6 D10.1 — radial discretization

**Chosen path:** periodic coefficient-space Fourier-Galerkin projection.

**Parked alternatives:** structure-preserving real-space discretization; dealiased pseudospectral/collocation implementation shown to reproduce the same projected operators.

**Later results depending on D10.1:** production `A_U`, `M`, `Q_Gamma`, `Q_U`, `D_C` assembly.

**Rollback point if convergence/truncation behavior fails:** return to the continuous D10-ZF equations and choose a different structure-preserving radial representation. Do not alter the physical quadratic forms to fit the discretization.

## 4.7 Current unresolved branch point

No physical D10-ZF calibration has yet been frozen. The following remain deliberately open:

```text
U(x) profile,
L_x,
radial resolution family,
profile harmonic,
profile amplitude,
perpendicular damping law,
finite-horizon diagnostic point.
```

This is the correct rollback location for the next application decision.

---

# 5. Fundamental theory versus technical and model-dependent structure

## 5.1 Fundamental theory elements

- positive metric `M` separated from signed `Q`;
- admissible input map `B` and positive input cost `R_in`;
- terminal and cumulative signed Hermitian extremal problems;
- transport neutrality and generation order;
- physical one- and multichannel balance identities;
- reachable/admissible channel bounds;
- short-time energy/transport optimizer separation;
- coordinate invariance.

These are the present branch-independent CORE.

## 5.2 Technical simplifications

- finite dimension;
- constant `A`;
- dense small-matrix exponential in the current implementation;
- Cholesky whitening;
- simple-eigenvalue assumptions only where unique eigenvector tracking is desired;
- periodic radial geometry in D10.1;
- coefficient-space Galerkin rather than FFT/collocation for the first structural implementation.

These should not be interpreted as physical principles.

## 5.3 Model-dependent special cases

- two-field Hasegawa-Wakatani state;
- D2-A orientation and Fourier convention;
- modal particle flux `Q_Gamma`;
- D8 damping and parameters;
- Branch S and Branch M numerical values;
- prescribed zonal-flow `Q_U`;
- sinusoidal sideband coupling examples.

## 5.4 Application-dependent decisions

- actual physical admissible input map `B`;
- whether the application target is particle flux, heat flux, momentum flux, mean-flow exchange, or another channel;
- physical damping closure;
- domain and resolution;
- profile calibration;
- which finite horizon is physically meaningful;
- which branch becomes the headline application.

---

# 6. Interfaces to other project strands

The purpose of the interfaces below is to let the other strands interrogate CORE **without silently changing its definitions**. Their feedback should be returned as either (i) compatible structure, (ii) a proposed extension, or (iii) a counterexample/obstruction.

## 6.1 Interface to 30 — MODES

### CORE exports to MODES

1. The operator tuple `(A,M,{Q_alpha},B,R_in)`.
2. The projected generation hierarchy `H_j` and transport-generation order `nu`.
3. The energy-production matrix `E_1` and the energy/transport angle.
4. The reachable subspace `R_T(B)` and channel leakage constants.
5. The requirement that any reduced/modal basis preserve the physical distinction between `M` and each signed `Q_alpha`.
6. Coordinate invariance under invertible state transformations.

### Questions MODES should answer for CORE

1. Is there a mode decomposition that is **intrinsic to the pair or family `(M,Q_alpha)`**, rather than to `A` alone?
2. Can one construct reduced bases that preserve, exactly or controllably, the multichannel balance
   `A^dagger M+MA=sum g_alpha Q_alpha-D`?
3. Do transport-generation orders or leading `H_j` eigenspaces admit a meaningful modal hierarchy analogous to known energetic/coherent-mode decompositions?
4. Can modal truncation preserve a transport-neutral admissible subspace `B^dagger Q B=0` without creating artificial initial flux?
5. How should degeneracies of `H_j`, `E_1`, or signed `Q` be interpreted geometrically?
6. Can the ideas associated with Haken/Hutt/Friedrich-type mode decompositions supply a principled reduced coordinate system without replacing physical `Q` by a positive amplitude norm?
7. Which quantities are robust under projection: signed gain, generation order, optimizer angle, reachable leakage constants?

### Desired return to CORE

A short list of projection/reduction identities and failure modes, plus one recommended structure-preserving modal reduction candidate. No application detour is needed yet.

## 6.2 Interface to 40 — CONT

### CORE exports to CONT

A parameterized family

```math
\mu\mapsto(A(\mu),M(\mu),Q_\alpha(\mu),B(\mu),R_{\rm in}(\mu))
```

with diagnostics

```text
spectral abscissa,
lambda_max/min of terminal/cumulative signed operators,
transport-generation order nu,
E_1 and H_j spectra,
energy/transport optimizer angle,
reachable leakage constants,
multichannel balance residual.
```

D10-ZF later supplies a particularly natural continuation parameter: zonal-flow amplitude, but no value is frozen in this document.

### Questions CONT should answer for CORE

1. Which of the CORE diagnostics can be continued smoothly through parameter space, and which are only piecewise smooth because of eigenvalue crossings?
2. How should optimizer branch switches be distinguished from dynamical bifurcations of `A`?
3. Can one continue extremal eigenspaces rather than individual eigenvectors through degeneracies?
4. Can changes in transport-generation order `nu` be characterized as codimension conditions such as `H_0=...=H_{nu-1}=0`?
5. Can sign changes of the maximal/minimal signed transport gain be tracked as separate continuation events?
6. How do stability boundaries, energy-contractivity boundaries, and transport-optimality transitions intersect or differ?
7. Can the D10-ZF coupled pilot be continued from `U=0` while preserving a reliable branch connection to the D2-A limit?
8. Is there a natural local/global continuation formulation for transport-neutral input subspaces or reachable leakage constants?

### Desired return to CORE

A continuation taxonomy for CORE observables, especially around degeneracy, sign change, and stability boundaries, before CORE chooses a parameter-map strategy.

## 6.3 Interface to 20 — CASCADE

### CORE exports to CASCADE

1. Multichannel signed balance

```math
A^\dagger M+MA=\sum_\alpha g_\alpha Q_\alpha-D.
```

2. Independent signed channel observables rather than a single positive norm.
3. Channel-resolved cumulative Gramians `P_{Q_alpha}`.
4. Transport-neutral initialization and generation hierarchy.
5. Reachable/admissible bounds and leakage constants.

### Questions CASCADE should answer for CORE

1. Can scale-to-scale transfer or cascade fluxes be represented as physically derived signed quadratic forms `Q_alpha` in a finite-dimensional/local linearized setting?
2. Is the multichannel non-identifiability result the correct analogue of the fact that a global energy budget does not identify individual interscale transfers?
3. Do shell/band/local transfer channels satisfy useful lower bounds relative to `M` that would make T3 quantitatively sharp?
4. Is there a meaningful cascade analogue of target transport-neutrality and transport-generation order?
5. Can a hierarchy of `Q_alpha` across scales reveal a structural link between CORE and Kramers-Moyal / Friedrich-Peinke style cascade descriptions, or are the objects fundamentally different?
6. Can physically local or sparse coupling improve reachable-subspace leakage bounds?
7. Which parts of the cascade idea are genuinely branch-independent mathematical extensions and which are application analogies only?

### Desired return to CORE

A yes/no/conditional map from cascade concepts to the existing CORE objects, with explicit equations where the mapping is exact and explicit warnings where it is only analogy.

---

# 7. What the three strands must not silently change

Until CORE Interpretation Freeze 0.1 is complete, MODES/CONT/CASCADE should treat the following as fixed reference semantics:

1. `M` is positive physical disturbance energy/free energy.
2. `Q_alpha` are signed physical observables/exchange channels and need not be positive.
3. A modal basis or continuation parameterization does not redefine a physical `Q_alpha`.
4. The balance does not identify individual channels.
5. `B` is part of the problem definition, not a numerical afterthought.
6. Transport neutrality is a condition on the target physical channel.
7. Any proposed extension that requires replacing `Q` by an amplitude norm must be reported as a change of problem, not as an equivalent formulation.

---

# 8. Assessment of the freeze

## 8.1 Is CORE Mathematical Freeze 0.1 reached?

**Yes.** The current state is sufficiently consolidated to serve as a rollback and reference point because:

- the branch-independent finite-dimensional mathematical objects are explicit;
- T1–T4 have canonical theorem notes and numerical validation;
- the distinction between assumptions and proved statements is explicit;
- all active plasma results are marked as branch-dependent;
- D2 and D10-ZF have explicit rollback routes;
- the current D10-ZF branch has been carried through continuous derivation, structure-preserving discretization, production assembly, and balance validation without yet freezing a physical calibration;
- open conjectures and unresolved interpretation questions are separated from proved algebra.

This freeze does **not** certify novelty, physical universality, or the final paper narrative.

## 8.2 What is still missing for CORE Interpretation Freeze 0.1?

The interpretation freeze should not be made until feedback from MODES/CONT/CASCADE is integrated. At minimum it must settle:

1. the canonical one-sentence interpretation of the theory: signed directed output generation under an independent positive metric and physical balance, versus a narrower nonnormal-transient-growth framing;
2. the role of nonnormality — fundamental, enabling, or secondary;
3. whether transport-generation order is merely a short-time diagnostic or a central organizing invariant;
4. whether T3 multichannel structure is central or supporting;
5. the canonical geometric meaning of `B`, transport-neutrality, and the optimizer angle;
6. whether modal decomposition introduces a natural reduced geometry compatible with `M` and signed `Q`;
7. how optimizer degeneracies and branch changes should be interpreted through continuation;
8. whether cascade/scale-transfer structure is an exact extension or only an analogy;
9. novelty positioning against dissipativity/control, nonmodal plasma theory, and quadratic-output optimization;
10. the division between the autonomous CORE and a future nonautonomous/shearing extension.

## 8.3 CORE step that should wait for cross-stream feedback

CORE should **not** open a new large theorem branch now.

After the three handoffs return, the next CORE-level step should be:

> **CORE Interpretation Freeze 0.1:** synthesize the MODES/CONT/CASCADE feedback into one canonical interpretation, decide which invariants and extensions are genuinely part of CORE, and only then choose whether the next mathematical theorem package should be (a) nonautonomous transport generation, (b) a projection/modal theorem, (c) a continuation/degeneracy theorem, or (d) no new theorem before the D10-ZF physical falsification point.

The D10-ZF application calibration can be prepared separately, but a new *fundamental* CORE branch should wait for that cross-stream synthesis.

---

# 9. Canonical reference files at Freeze 0.1

- `decisions/registry.md` — D1 through D10-ZF.
- `research/theorems/T1_transport_generation_order.md`.
- `research/theorems/T2_balance_identity_and_bounds.md`.
- `research/theorems/T3_multichannel_bounds.md`.
- `research/theorems/T4_short_time_energy_transport_separation.md`.
- `research/hw_convention_audit.md` — D2-A source-level freeze.
- `research/hw_pilot_case.md` — D8 single-case pilot.
- `research/hw_branch_comparison.md` — D9 Branch S / Branch M comparison.
- `research/hw_coupled_mode_audit.md` — coupling alternatives before D10.
- `research/hw_zonal_flow_linearization.md` — D10-ZF continuous equations and balance.
- `research/hw_zonal_flow_discretization.md` — D10.1 Fourier-Galerkin design.
- `src/nonmodal_flux/models/hasegawa_wakatani.py` — D2-A production model.
- `src/nonmodal_flux/models/hasegawa_wakatani_zonal_flow.py` — D10.2 production coupled model.
- `research/roadmap.md` — operational status.

---

# 10. Freeze rule

Any future result that contradicts this freeze should be handled in one of four ways:

1. **Correction of a STABLE result:** document the mathematical error explicitly and update the relevant canonical theorem note.
2. **Failure of an ASSUMPTION:** replace the assumption and state which theorems need re-hypothesizing.
3. **Failure of a BRANCH:** jump back to the branch's rollback point; do not rewrite branch-independent CORE.
4. **Failure of a CONJECTURE:** record the falsification as a result rather than quietly removing the conjecture.

This makes CORE Mathematical Freeze 0.1 a genuine rollback point rather than a narrative snapshot.