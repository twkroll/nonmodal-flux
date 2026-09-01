# T3 — Multichannel balance: identifiability, no-go result, and channel-resolved bounds

**Date:** 2026-09-01  
**Status:** working theorem note; algebraic and numerical validation complete for the abstract finite-dimensional setting, pending physical plasma instantiation

## Setup

Let

```math
\dot x = A x,\qquad x(0)=Bu,
```

with a positive physical metric `M=M†>0`, Hermitian signed transport forms `Q_1,...,Q_r`, and dissipation `R=R†>=0`. Assume the physical balance

```math
A^\dagger M+MA=\sum_{\alpha=1}^r g_\alpha Q_\alpha-R.
```

For each channel define

```math
P_\alpha(T)=\int_0^T e^{A^\dagger t}Q_\alpha e^{At}\,dt,
\qquad
P_R(T)=\int_0^T e^{A^\dagger t}R e^{At}\,dt,
```

and

```math
P_M(T)=\int_0^T e^{A^\dagger t}Me^{At}\,dt,
\qquad
\Delta_M(T)=e^{A^\dagger T}Me^{AT}-M.
```

Integration gives the exact operator identity

```math
\sum_{\alpha=1}^r g_\alpha P_\alpha(T)=\Delta_M(T)+P_R(T).
```

For restricted initial conditions define the finite-horizon dynamically reachable subspace

```math
\mathcal R_T(B)
=\operatorname{span}\{e^{At}Bv:\;0\le t\le T,\ v\in\mathbb C^m\}.
```

Every trajectory starting from `x(0)=Bu` lies in `\mathcal R_T(B)` at each time `0<=t<=T`.

## Proposition T3.1 — Balance alone does not identify an individual transport channel

Assume `r>=2` and choose two indices with `g_1 g_2 != 0`. For any Hermitian `S=S†`, define

```math
Q_1'=Q_1+g_2S,
\qquad
Q_2'=Q_2-g_1S,
```

with all other `Q_alpha` unchanged. Then

```math
\sum_{\alpha=1}^r g_\alpha Q_\alpha'
=
\sum_{\alpha=1}^r g_\alpha Q_\alpha.
```

Hence the physical energy balance is unchanged although the individual transport forms, their finite-horizon Gramians, and their signed extremal gains generally change.

### Consequence

No theorem using only the total balance can identify, or produce a nontrivial universal bound on, one channel independently of the remaining channels. Additional channel-resolved physical structure is necessary.

### Interpretation

This formalizes why the Lülff-style construction rule is essential: each `Q_alpha` must be fixed by the underlying physical flux before optimization. The energy balance constrains only the weighted combination of channels.

## Proposition T3.2 — Channel-resolved bound: global and admissible versions

Fix a target channel `a` with `g_a>0`.

### T3.2a — Global operator version

Suppose that for every `beta != a` there exists `c_beta>=0` such that on the full state space

```math
g_\beta Q_\beta\succeq -c_\beta M.
```

Let

```math
C=\sum_{\beta\ne a}c_\beta.
```

Then the global state-space operator inequality

```math
g_a P_a(T)
\preceq
\Delta_M(T)+P_R(T)+C\,P_M(T)
```

holds.

#### Proof

From the exact balance identity,

```math
g_aP_a(T)
=
\Delta_M(T)+P_R(T)-\sum_{\beta\ne a}g_\beta P_\beta(T).
```

The global lower bound is preserved under congruence with `e^{At}` and integration:

```math
g_\beta P_\beta(T)
=\int_0^T e^{A^\dagger t}(g_\beta Q_\beta)e^{At}\,dt
\succeq
-c_\beta P_M(T).
```

Therefore

```math
-g_\beta P_\beta(T)\preceq c_\beta P_M(T),
```

and summing over the competing channels yields the result.

### T3.2b — Reachable-subspace / admissible-input version

Suppose instead that the lower bounds are known only on `\mathcal R_T(B)`:

```math
x^\dagger(g_\beta Q_\beta+c_\beta M)x\ge0
\quad
\text{for all }x\in\mathcal R_T(B),\ \beta\ne a.
```

Then one may not in general conclude the global state-space inequality of T3.2a. What follows is the projected quadratic-form inequality on the admissible input space:

```math
g_a B^\dagger P_a(T)B
\preceq
B^\dagger\bigl[\Delta_M(T)+P_R(T)+C P_M(T)\bigr]B.
```

Equivalently, for every admissible input `u`,

```math
g_a\,u^\dagger B^\dagger P_a(T)Bu
\le
u^\dagger B^\dagger
\bigl[\Delta_M(T)+P_R(T)+C P_M(T)\bigr]Bu.
```

#### Proof

For any admissible `u`, set `x(t)=e^{At}Bu`. By construction `x(t)\in\mathcal R_T(B)` for `0<=t<=T`, hence

```math
x(t)^\dagger g_\beta Q_\beta x(t)
\ge
-c_\beta x(t)^\dagger Mx(t).
```

Integrating gives

```math
u^\dagger B^\dagger g_\beta P_\beta(T)Bu
\ge
-c_\beta\,u^\dagger B^\dagger P_M(T)Bu.
```

Insert these scalar inequalities into the exact multichannel balance and sum over `beta != a`. Since the result holds for every `u`, it is exactly the projected Hermitian ordering stated above.

### Important distinction

A lower bound that is valid only on `\mathcal R_T(B)` supports only an admissible/reachable quadratic-form statement. Writing the resulting inequality as a global ordering on the entire state space would be stronger and is not justified without a global channel bound.

## Corollary T3.3 — Contractive-energy finite-horizon bounds

Assume in addition

```math
e^{A^\dagger t}Me^{At}\preceq M
\quad\text{for }0\le t\le T.
```

Then

```math
\Delta_M(T)\preceq0,
\qquad
P_M(T)\preceq TM.
```

### T3.3a — Global version

Under the global hypotheses of T3.2a,

```math
g_aP_a(T)\preceq P_R(T)+CTM.
```

### T3.3b — Admissible-input version

Under only the reachable-subspace hypotheses of T3.2b,

```math
g_a B^\dagger P_a(T)B
\preceq
B^\dagger P_R(T)B
+CT\,B^\dagger MB.
```

If the input cost is the physical initial energy,

```math
R_{\rm in}=B^\dagger MB,
```

then whitening the projected inequality gives

```math
\mathcal G_{a,+}(T)
\le
\frac{1}{g_a}
\left[
\lambda_{\max}\!\left(
R_{\rm in}^{-1/2}B^\dagger P_R(T)BR_{\rm in}^{-1/2}
\right)
+CT
\right].
```

Thus the scalar gain bound remains valid when the competing-channel estimates are available only on the dynamically reachable subspace; a global state-space operator inequality is not required.

## Reachable-subspace leakage constants

For each competing channel define the minimal nonnegative leakage constant on the dynamically reachable subspace by

```math
c_\beta(T,B)
=
\max\!\left\{
0,
\sup_{\substack{x\in\mathcal R_T(B)\\x\ne0}}
\frac{-x^\dagger g_\beta Q_\beta x}{x^\dagger Mx}
\right\}.
```

Then

```math
x^\dagger\bigl(g_\beta Q_\beta+c_\beta(T,B)M\bigr)x\ge0
\quad\text{for all }x\in\mathcal R_T(B).
```

The corresponding total leakage is

```math
C(T,B)=\sum_{\beta\ne a}c_\beta(T,B).
```

Using these constants in T3.2b and T3.3b can be substantially sharper than using global constants. The synthetic C8.4 witness demonstrates this possibility: the reachable constant is `0.2` whereas the global constant is `3.0`, a factor-15 reduction. This is a proof-of-principle for sharpness, not yet evidence that the same improvement survives in a physical plasma model.

In finite dimensions, if `V` is a basis matrix for `\mathcal R_T(B)`, then `c_beta(T,B)` can be obtained from the smallest generalized eigenvalue of the restricted pencil

```math
V^\dagger(g_\beta Q_\beta)V
\quad\text{versus}\quad
V^\dagger M V,
```

with the nonnegative truncation above. The remaining practical question is whether a useful reachable basis and sharp constants can be computed cheaply enough in the intended plasma discretizations.

## Interaction with transport-neutral initialization

For a target channel `a`, impose

```math
B^\dagger Q_aB=0.
```

Then T1 gives

```math
\mathcal G_{a,+}(T)
=
\frac{T^2}{2}\lambda_{\max}(H_{a,1})+O(T^3),
```

while T3.3b gives a finite-horizon upper bound based on dissipation and competing physical channels. The combination separates two questions: T1 describes how target transport is dynamically generated from a transport-neutral admissible subspace, while T3 constrains how large that channel can become in the presence of the physical balance and cross-channel leakage.

## Numerical validation status

The abstract finite-dimensional statements are covered by focused tests:

- T3.1: different channel decompositions preserve the total balance while changing individual channel Gramians and signed gains.
- T3.2a: a global competing-channel lower bound produces the predicted finite-horizon operator inequality.
- T3.3: contractive energy yields `P_M(T) <= T M` and the corresponding positive-gain bound under natural input normalization.
- Reachable-subspace sharpening: a restricted dynamically reachable space can yield a substantially smaller leakage constant, and the resulting projected/admissible inequality remains valid while the corresponding global inequality need not be valid.

These tests validate the algebra and the global-versus-reachable distinction; they do not establish physical sharpness for any plasma model.

## Literature positioning

Classical dissipativity theory already treats indefinite quadratic supply rates and LMI characterizations. The novelty therefore cannot be “a balance with indefinite quadratic forms.” The potentially distinctive contribution is the channel-resolved use of physics-derived signed transport observables, admissible/transport-neutral initial subspaces, and finite-horizon extremal transport under an independent positive physical metric.

## Next falsification tasks

1. Develop a practical construction of `\mathcal R_T(B)` and `c_beta(T,B)` for larger discretizations without circularly solving the target transport optimization.
2. Test whether the reachable constants remain substantially sharper than global generalized-eigenvalue bounds in the two-field plasma pilot.
3. Derive exact `Q_Gamma` from a fixed HW convention before evaluating the bound.
4. In a three-field model derive separate `Q_Gamma` and `Q_heat` and test whether one channel can be bounded sharply in the presence of the other.
5. Continue prior-art search for channel-resolved dissipativity or multiple quadratic supply-rate results that subsume T3.2.

## Current assessment

- T3.1 is a clean structural/no-go result, but algebraically elementary.
- T3.2/T3.3 are now separated into mathematically correct global and admissible/reachable formulations.
- The synthetic reachable-subspace example shows that restricted leakage constants can be nontrivially sharper than global constants, but publication value still depends on physically sharp estimates in the plasma pilot.
- The strongest likely contribution remains the combination of T1 (dynamic generation), T3 (channel-resolved physical bounds), and a nontrivial plasma example with independently derived Lülff-style flux forms.
