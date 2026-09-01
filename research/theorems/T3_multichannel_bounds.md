# T3 — Multichannel balance: identifiability, no-go result, and a first channel-resolved bound

**Date:** 2026-09-01  
**Status:** working theorem note; next Gate-0 step

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
\Delta_M(T)=e^{A^\dagger T}Me^{AT}-M.
```

Integration gives the exact operator identity

```math
\sum_{\alpha=1}^r g_\alpha P_\alpha(T)=\Delta_M(T)+P_R(T).
```

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

No theorem using only the total balance can produce a nontrivial universal bound on one channel independently of the remaining channels. Additional channel-resolved physical structure is necessary.

### Interpretation

This formalizes why the Lülff-style construction rule is essential: each `Q_alpha` must be fixed by the underlying physical flux before optimization. The energy balance constrains only the weighted combination of channels.

## Proposition T3.2 — First channel-resolved bound under cross-channel lower bounds

Fix a target channel `a` with `g_a>0`. Suppose that for every `beta != a` there exists `c_beta>=0` such that on the dynamically reachable subspace over `[0,T]`,

```math
g_\beta Q_\beta\succeq -c_\beta M.
```

Then

```math
g_a P_a(T)
\preceq
\Delta_M(T)+P_R(T)+C\,P_M(T),
```

where

```math
C=\sum_{\beta\ne a}c_\beta,
\qquad
P_M(T)=\int_0^T e^{A^\dagger t}Me^{At}\,dt.
```

### Proof

From the exact balance identity,

```math
g_aP_a(T)
=
\Delta_M(T)+P_R(T)-\sum_{\beta\ne a}g_\beta P_\beta(T).
```

The assumed lower bound gives

```math
g_\beta P_\beta(T)
=
\int_0^T e^{A^\dagger t}(g_\beta Q_\beta)e^{At}\,dt
\succeq
-c_\beta P_M(T).
```

Therefore `-g_beta P_beta(T) <= c_beta P_M(T)`, and summing yields the result.

## Corollary T3.3 — Contractive-energy finite-horizon bound

Assume in addition

```math
e^{A^\dagger t}Me^{At}\preceq M
\quad\text{for }0\le t\le T.
```

Then

```math
\Delta_M(T)\preceq0,
\qquad
P_M(T)\preceq TM,
```

and hence

```math
g_aP_a(T)\preceq P_R(T)+CTM.
```

If the input cost is the physical initial energy,

```math
R_{\rm in}=B^\dagger MB,
```

then

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

This is useful only if the constants `c_beta` can be made physically sharp.

## Reachable-subspace sharpening

Define

```math
\mathcal R_T(B)=\operatorname{span}\{e^{At}Bv:\;0\le t\le T\}.
```

A sharper channel-leakage constant is

```math
c_\beta(T,B)
=
\sup_{\substack{x\in\mathcal R_T(B)\\x\ne0}}
\frac{-x^\dagger g_\beta Q_\beta x}{x^\dagger Mx}.
```

This explicitly incorporates the admissible input map `B` and may be much sharper than a global operator norm.

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

while T3.3 gives a finite-horizon bound based on dissipation and competing channels. The combination is a stronger foundations-paper candidate than either result alone.

## Literature positioning

Classical dissipativity theory already treats indefinite quadratic supply rates and LMI characterizations. The novelty therefore cannot be “a balance with indefinite quadratic forms.” The potentially distinctive contribution is the channel-resolved use of physics-derived signed transport observables, admissible/transport-neutral initial subspaces, and finite-horizon extremal transport under an independent positive physical metric.

## Next falsification tasks

1. Determine whether `c_beta(T,B)` can be computed or bounded without circularly solving the full transport optimization.
2. Test whether the constants collapse to trivial global operator norms in the two-field plasma pilot.
3. Derive exact `Q_Gamma` from a fixed HW convention before evaluating the bound.
4. In a three-field model derive separate `Q_Gamma` and `Q_heat` and test whether one channel can be bounded sharply in the presence of the other.
5. Continue prior-art search for channel-resolved dissipativity or multiple quadratic supply-rate results that subsume T3.2.

## Current assessment

- T3.1 is a clean structural/no-go result, but algebraically elementary.
- T3.2/T3.3 are useful first bounds, but publication value depends on physically sharp, nontrivial estimates of `c_beta(T,B)`.
- The strongest likely contribution is the combination of T1 (dynamic generation), T3 (channel-resolved physical bounds), and a nontrivial plasma example with independently derived Lülff-style flux forms.
