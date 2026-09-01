# T3 — Multichannel balance: identifiability, no-go result, and channel-resolved bounds

**Date:** 2026-09-01  
**Status:** working theorem note; abstract finite-dimensional algebra and numerical validation complete, pending physical plasma instantiation

## Setup

Let

```math
\dot x=Ax,\qquad x(0)=Bu,
```

with a positive physical metric `M=M†>0`, Hermitian signed transport forms `Q_1,...,Q_r`, and dissipation `R=R†>=0`. Assume

```math
A^\dagger M+MA=\sum_{\alpha=1}^r g_\alpha Q_\alpha-R.
```

Define

```math
P_\alpha(T)=\int_0^T e^{A^\dagger t}Q_\alpha e^{At}\,dt,
\qquad
P_R(T)=\int_0^T e^{A^\dagger t}R e^{At}\,dt,
```

```math
P_M(T)=\int_0^T e^{A^\dagger t}Me^{At}\,dt,
\qquad
\Delta_M(T)=e^{A^\dagger T}Me^{AT}-M.
```

Integration gives the exact identity

```math
\sum_{\alpha=1}^r g_\alpha P_\alpha(T)=\Delta_M(T)+P_R(T).
```

For restricted initial conditions define

```math
\mathcal R_T(B)
=\operatorname{span}\{e^{At}Bv:\;0\le t\le T,\ v\in\mathbb C^m\}.
```

Every admissible trajectory `x(t)=e^{At}Bu` lies in `\mathcal R_T(B)` for `0<=t<=T`.

## Proposition T3.1 — Balance alone does not identify an individual transport channel

Assume `r>=2` and `g_1 g_2 != 0`. For any Hermitian `S=S†`, define

```math
Q_1'=Q_1+g_2S,
\qquad
Q_2'=Q_2-g_1S,
```

with all other channels unchanged. Then

```math
\sum_{\alpha=1}^r g_\alpha Q_\alpha'
=
\sum_{\alpha=1}^r g_\alpha Q_\alpha.
```

Thus the physical energy balance is unchanged although the individual transport forms, their finite-horizon Gramians, and their signed extremal gains generally change.

### Consequence

The total balance alone cannot identify an individual transport channel. Additional channel-resolved physical structure is required. In particular, each `Q_alpha` must be derived independently from the corresponding physical flux rather than inferred from the total balance.

## Proposition T3.2 — Channel-resolved bound: global and admissible versions

Fix a target channel `a` with `g_a>0` and define

```math
C=\sum_{\beta\ne a}c_\beta.
```

### T3.2a — Global operator version

Suppose that, on the full state space, every competing channel satisfies

```math
g_\beta Q_\beta\succeq-c_\beta M,
\qquad c_\beta\ge0.
```

Then

```math
g_aP_a(T)
\preceq
\Delta_M(T)+P_R(T)+C P_M(T).
```

Indeed,

```math
g_aP_a(T)
=
\Delta_M(T)+P_R(T)-\sum_{\beta\ne a}g_\beta P_\beta(T),
```

and congruence with `e^{At}` plus integration gives

```math
g_\beta P_\beta(T)\succeq-c_\beta P_M(T).
```

### T3.2b — Reachable-subspace / admissible-input version

Suppose instead that the competing-channel lower bounds hold only on `\mathcal R_T(B)`:

```math
x^\dagger(g_\beta Q_\beta+c_\beta M)x\ge0
\quad
\text{for all }x\in\mathcal R_T(B),\ \beta\ne a.
```

Then the justified conclusion is the projected ordering

```math
g_aB^\dagger P_a(T)B
\preceq
B^\dagger\bigl[\Delta_M(T)+P_R(T)+C P_M(T)\bigr]B,
```

not, in general, the global state-space ordering of T3.2a.

Equivalently, for every admissible input `u`,

```math
g_a\,u^\dagger B^\dagger P_a(T)Bu
\le
u^\dagger B^\dagger
\bigl[\Delta_M(T)+P_R(T)+C P_M(T)\bigr]Bu.
```

### Proof of T3.2b

For `x(t)=e^{At}Bu`, the reachable-subspace assumption gives

```math
x(t)^\dagger g_\beta Q_\beta x(t)
\ge
-c_\beta x(t)^\dagger Mx(t).
```

Integration yields, for every `u`,

```math
u^\dagger B^\dagger g_\beta P_\beta(T)Bu
\ge
-c_\beta\,u^\dagger B^\dagger P_M(T)Bu.
```

Substitution into the exact multichannel balance gives the projected inequality. The distinction is essential: a quadratic-form bound known only on `\mathcal R_T(B)` does not imply a global operator inequality outside that subspace.

## Corollary T3.3 — Contractive-energy finite-horizon bounds

Assume

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

Under the hypotheses of T3.2a,

```math
g_aP_a(T)\preceq P_R(T)+CTM.
```

### T3.3b — Admissible-input version

Under the reachable-subspace hypotheses of T3.2b,

```math
g_aB^\dagger P_a(T)B
\preceq
B^\dagger P_R(T)B+CT\,B^\dagger MB.
```

With the natural input metric

```math
R_{\rm in}=B^\dagger MB,
```

whitening gives

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

Thus the scalar gain bound remains valid with channel estimates that are available only on the dynamically reachable subspace; no global state-space ordering is needed for that conclusion.

## Reachable-subspace leakage constants

For each competing channel define the minimal nonnegative leakage constant

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

Set

```math
C(T,B)=\sum_{\beta\ne a}c_\beta(T,B).
```

These restricted constants can be much sharper than their global analogues. The synthetic C8.4 witness gives `c_reach=0.2` and `c_global=3.0`, a factor-15 reduction. This is a proof of principle for mathematical sharpness, not yet evidence for physical sharpness in a plasma model.

If `V` is a basis matrix for `\mathcal R_T(B)`, then in finite dimensions

```math
c_\beta(T,B)
=
\max\{0,-\lambda_{\min}(V^\dagger g_\beta Q_\beta V,\,V^\dagger MV)\},
```

where `lambda_min(K,G)` denotes the smallest generalized Hermitian eigenvalue of `K v=lambda G v`.

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

while T3.3b supplies a finite-horizon upper bound from dissipation and competing channels. T1 therefore describes how target transport is dynamically generated from a transport-neutral admissible subspace, whereas T3 constrains how large that channel may become under the physical multichannel balance.

## Numerical validation status

Focused tests now cover:

- T3.1: different channel decompositions preserve the total balance while changing individual channel Gramians and signed gains.
- T3.2a: a global competing-channel lower bound produces the predicted finite-horizon operator inequality.
- T3.3: contractive energy yields `P_M(T) <= T M` and the corresponding positive-gain bound under natural input normalization.
- Reachable-subspace sharpening: a restricted dynamically reachable space can yield a much smaller leakage constant, while only the projected/admissible inequality is guaranteed.

These tests validate the abstract algebra and the global-versus-reachable distinction. They do not establish physical sharpness for a plasma model.

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
