# T2 — Balance identity, signed bounds, and a no-free-lunch result

**Status:** working theorem package for Gate 0  
**Date:** 2026-09-01

## Setup

Let

```math
\dot x = A x,\qquad x(0)=Bu,
```

with a positive physical metric `M=M^†>0`, a Hermitian signed transport form `Q=Q^†`, positive input metric `R_in`, and a physical balance

```math
A^\dagger M + M A = g Q - R,\qquad R\succeq 0,
```

for a scalar coupling/drive `g != 0`.

Define

```math
P_Q(T)=\int_0^T e^{A^\dagger t}Qe^{At}\,dt,
```

```math
P_R(T)=\int_0^T e^{A^\dagger t}Re^{At}\,dt,
```

and `Phi(T)=e^{AT}`.

## Proposition T2.1 — Exact projected balance identity

For every `T>=0`,

```math
g P_Q(T)=\Phi(T)^\dagger M\Phi(T)-M+P_R(T).
```

Consequently, after restriction to admissible initial conditions,

```math
g B^\dagger P_Q(T)B
=
B^\dagger\Phi(T)^\dagger M\Phi(T)B
-B^\dagger MB
+B^\dagger P_R(T)B.
```

### Proof

Differentiate the propagated energy metric:

```math
\frac{d}{dt}\left(e^{A^\dagger t}Me^{At}\right)
=
e^{A^\dagger t}(A^\dagger M+MA)e^{At}
=
g e^{A^\dagger t}Qe^{At}-e^{A^\dagger t}Re^{At}.
```

Integrating from `0` to `T` gives the result.

---

## Corollary T2.2 — Input-whitened identity

Let

```math
H_Q(T)=R_{in}^{-1/2}B^\dagger P_Q(T)BR_{in}^{-1/2},
```

```math
H_E(T)=R_{in}^{-1/2}B^\dagger\Phi(T)^\dagger M\Phi(T)BR_{in}^{-1/2},
```

```math
H_{E0}=R_{in}^{-1/2}B^\dagger MBR_{in}^{-1/2},
```

and

```math
H_R(T)=R_{in}^{-1/2}B^\dagger P_R(T)BR_{in}^{-1/2}\succeq0.
```

Then

```math
gH_Q(T)=H_E(T)-H_{E0}+H_R(T).
```

This is an operator identity, not merely an inequality.

---

## Corollary T2.3 — Natural-energy normalization

If the input cost is the physical initial energy on the admissible subspace,

```math
R_{in}=B^\dagger M B,
```

then `H_E0=I` and

```math
gH_Q(T)=H_E(T)-I+H_R(T).
```

If, in addition, the dynamics are globally contractive in the `M` metric on the admissible trajectories,

```math
\Phi(T)^\dagger M\Phi(T)\preceq M,
```

then

```math
H_E(T)\preceq I
```

and therefore, for `g>0`,

```math
H_Q(T)\preceq \frac{1}{g}H_R(T).
```

Hence the maximal positive signed transport satisfies

```math
\mathcal G_{Q,+}(T)
\le
\frac{1}{g}\lambda_{max}(H_R(T)).
```

Because `H_E(T)\succeq0` and `H_R(T)\succeq0`, one also has

```math
H_Q(T)\succeq -\frac{1}{g}I,
```

and thus

```math
\mathcal G_{Q,-}(T)\ge -\frac{1}{g}.
```

For `g<0`, the corresponding signed inequalities reverse in the obvious way.

### Interpretation

In this single-channel balance, cumulative signed transport is not independent of energy and dissipation. Under monotone physical energy, positive transport is limited by accumulated dissipation, while the negative cumulative direction has a lower bound set by the initial physical energy scale.

This is stronger physically than an unstructured operator-norm bound because the right-hand side is a measurable/derivable dissipation functional. It is not yet obviously novel mathematically.

---

## Corollary T2.4 — Infinite-horizon identity for a stable system

If `A` is Hurwitz, then `Phi(T)^† M Phi(T) -> 0` and

```math
gP_Q(\infty)=-M+P_R(\infty).
```

With `R_in=B^†MB`,

```math
H_Q(\infty)=\frac{1}{g}\left(H_R(\infty)-I\right).
```

Thus the entire infinite-horizon signed transport spectrum is determined by the competition between accumulated dissipation and initial physical energy in the admissible subspace.

---

## Proposition T2.5 — What the balance alone does *not* give

The balance identity by itself does not produce a universally sharp scalar upper bound on `G_Q` in terms of initial energy alone. Such a bound requires additional structure, for example:

- a coercive or relative bound on `R` with respect to `M`;
- a known `M`-contraction rate;
- sign information on additional transport channels in a multi-channel balance;
- a restriction of the admissible input subspace;
- locality/topology structure of `Q`.

This is important for Gate 0: a theorem that merely rewrites the balance is insufficient. The publishable target should add one of these structures and obtain a quantitatively sharper, physically interpretable result.

---

## Multi-channel direction

For

```math
A^\dagger M+MA=\sum_{\alpha=1}^r g_\alpha Q_\alpha-R,
```

one obtains

```math
\sum_\alpha g_\alpha P_{Q_\alpha}(T)
=
\Phi(T)^\dagger M\Phi(T)-M+P_R(T).
```

This is likely more physically relevant for plasma, where particle and heat fluxes can enter the free-energy budget separately. A strong theorem would bound one target channel using the balance plus sign/geometry information on the others rather than collapsing all transport into one scalar objective.

## Gate-0 assessment

- **T2.1–T2.4:** mathematically clean and physically useful; likely supporting results rather than standalone novelty.
- **Most promising extension:** channel-resolved bound with physically derived `Q_alpha`, admissible subspace `B`, and transport-neutrality.
- **Critical warning:** in a one-channel model, the balance may make cumulative transport partly a repackaging of energy change plus dissipation. This must be tested explicitly in the HW pilot.
