# CORE 0.2 — Branch A: Generation-Hierarchy / Generation-Geometry

**Date:** 2026-09-02  
**Status:** COUNTEREXAMPLE / BRANCH FAILURE REACHED in first algebraic package; theory development stopped by user-defined Event B rule

## Scope lock

This note opens only CORE 0.2 Branch A. It does **not** open:

- a nonautonomous `A(t)` extension;
- a new application;
- global continuation theory;
- cascade/Markov/Kramers–Moyal extensions;
- universal model reduction theory;
- a new D10/plasma branch.

The starting objects are the frozen autonomous finite-dimensional CORE objects

```math
\dot x=Ax,\qquad x(0)=Bu,
```

with Hermitian signed observable `Q=Q^\dagger` and positive input metric

```math
R_{\rm in}=R_{\rm in}^\dagger\succ0.
```

Define

```math
\mathcal L_A(X)=A^\dagger X+XA,
```

and

```math
H_j=R_{\rm in}^{-1/2}B^\dagger\mathcal L_A^j(Q)B R_{\rm in}^{-1/2}.
```

The generation order is

```math
\nu=\min\{j\ge0:H_j\ne0\},
```

when such a `j` exists.

The Branch-A question is whether `H_j` and `nu` admit a useful geometric characterization through the dynamical/Krylov directions

```math
B,\ AB,\ldots,A^jB
```

and the associated spaces

```math
\mathcal K_j(A,B)=\operatorname{span}\{B,AB,\ldots,A^jB\}
```

relative to the Hermitian signed form `Q`.

---

## 1. Exact algebraic pairing formula

Introduce the two-index `Q`-pairing matrices

```math
M_{p,q}:=(A^pB)^\dagger Q(A^qB)
=B^\dagger(A^\dagger)^pQA^qB.
```

The left and right multiplication superoperators commute, hence the binomial identity

```math
\mathcal L_A^j(Q)
=\sum_{p=0}^j\binom{j}{p}(A^\dagger)^pQA^{j-p}.
```

Therefore

```math
\boxed{
B^\dagger\mathcal L_A^j(Q)B
=\sum_{p+q=j}\binom{j}{p}M_{p,q}.
}
```

Since `R_in` is positive definite, congruence by `R_in^{-1/2}` is invertible. Thus

```math
\boxed{
H_j=0
\iff
\sum_{p+q=j}\binom{j}{p}(A^pB)^\dagger Q(A^qB)=0,
}
```

and

```math
\boxed{
H_j\ne0
\iff
\sum_{p+q=j}\binom{j}{p}(A^pB)^\dagger Q(A^qB)\ne0.
}
```

This is the sharp algebraic characterization available without extra assumptions.

Equivalently, for the propagated admissible frame

```math
B(t)=e^{At}B,
```

define its restricted `Q`-Gram matrix

```math
G_Q(t)=B(t)^\dagger Q B(t)
=B^\dagger e^{A^\dagger t}Qe^{At}B.
```

Then

```math
G_Q^{(j)}(0)=B^\dagger\mathcal L_A^j(Q)B,
```

so `nu` is exactly the first nonzero derivative order of the matrix-valued restricted `Q`-Gram curve after whitening.

### Minimal assumptions for this package

- No stability, normality, diagonalizability, or invertibility assumption on `A` is needed.
- Hermiticity of `Q` is not needed for the binomial identity itself, but is needed for the CORE signed-form interpretation and for all `H_j` to be Hermitian.
- `B` may have arbitrary rank. If `B=0`, every `H_j` vanishes and `nu` is undefined/infinite rather than a finite generation order.
- Positive definiteness of `R_in` is stronger than needed for the zero/nonzero equivalence; invertibility suffices algebraically. CORE retains `R_in\succ0` for the input-cost interpretation and Hermitian whitening.
- No dimension or nondegeneracy assumption is needed for the identities.

---

## 2. First plausible Krylov-geometric strengthening

A natural candidate interpretation is:

> the generation order is the first Krylov depth at which the signed form `Q` becomes nontrivial on the dynamically generated space, or equivalently the first depth at which a nonzero `Q`-pairing appears between generated directions.

The exact pairing formula shows immediately that this is stronger than what `H_j` states: `H_j` contains a **binomially weighted anti-diagonal sum** of the pairings `M_{p,q}`, not the pairings separately.

The question is whether Hermitian symmetry prevents cancellation strongly enough to recover the proposed geometric statement. It does not.

---

## 3. Minimal counterexample: normal `A`, indefinite Hermitian `Q`

Take

```math
A=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
Q=\begin{pmatrix}0&i\\-i&0\end{pmatrix},
\qquad
B=e_1,
\qquad
R_{\rm in}=1.
```

Properties:

1. `A=A^\dagger` is Hermitian, hence normal.
2. `Q=Q^\dagger` is Hermitian, nonsingular, and indefinite with signature `(1,1)`.
3. The initial admissible line is transport-neutral:

```math
B^\dagger QB=0.
```

4. The first generated direction is

```math
AB=e_2,
```

so

```math
\mathcal K_1(A,B)=\operatorname{span}\{e_1,e_2\}=\mathbb C^2.
```

Thus the first Krylov space is already the whole state space and `Q` is certainly nontrivial/nondegenerate on it.

5. There is already a nonzero cross-level pairing:

```math
B^\dagger QAB=i\ne0.
```

Nevertheless

```math
H_1
=B^\dagger(A^\dagger Q+QA)B
=i+(-i)=0.
```

In fact this example is sharper:

```math
A^\dagger Q+QA=AQ+QA=0.
```

Hence

```math
\mathcal L_A(Q)=0
```

and therefore

```math
H_j=0\qquad\text{for every }j\ge0.
```

There is no finite generation order, even though `K_1(A,B)` is already the full state space and a nonzero `Q`-pairing between `B` and `AB` exists.

### Why the proposed characterization fails

For `j=1`, Hermitian symmetry gives

```math
H_1\propto
M_{0,1}+M_{1,0}
=M_{0,1}+M_{0,1}^\dagger.
```

Thus only the Hermitian part of the cross-level pairing contributes. A nonzero purely skew-Hermitian pairing can be completely invisible to `H_1`.

At higher order the same structural issue persists in a broader form: `H_j` sees only the binomially weighted sum over the anti-diagonal `p+q=j`. Individual Krylov pairings can cancel.

---

## 4. Statement that fails

The following plausible Branch-A statement is false without additional assumptions:

```text
nu equals the smallest Krylov depth j for which Q becomes nonzero on
K_j(A,B), or for which a nonzero Q-pairing appears among B,AB,...,A^jB.
```

The 2 x 2 example above disproves both formulations.

It also disproves the more local implication

```math
(A^pB)^\dagger Q(A^qB)\ne0,\quad p+q=j
\quad\Longrightarrow\quad
H_j\ne0.
```

---

## 5. Weaker statement that survives

The exact statement surviving the counterexample is:

```math
H_j=0
\iff
\sum_{p+q=j}\binom{j}{p}(A^pB)^\dagger Q(A^qB)=0.
```

Therefore a **sufficient**, but not necessary, condition is

```math
(A^pB)^\dagger Q(A^qB)=0
\quad\text{for all }p+q=j.
```

Likewise, if all such pairings vanish for every anti-diagonal below order `r` and the weighted anti-diagonal sum at `r` is nonzero, then `nu=r`.

What does **not** survive is replacement of the weighted, ordered pairing data by the unweighted subspace geometry of `K_j(A,B)` alone.

A possible future refinement, if Branch A continues after this stop, is to treat the two-index pairing array

```math
\{M_{p,q}\}_{p,q\ge0}
```

or the matrix-valued curve `G_Q(t)` as the primary geometric object rather than the nested Krylov spaces alone. No such refinement is frozen in this note.

---

## 6. Known mathematical neighbors: first positioning only

This package already separates several neighboring structures.

### Krylov structure

The spaces `K_j(A,B)` are standard block Krylov spaces. They remember generated **spans**, but not the complete ordered two-index `Q`-pairing data. The counterexample shows that this information loss matters for generation order.

### Linear Markov parameters / moments

For an ordinary linear output `y=Cx`, classical Markov parameters have the one-index form

```math
CA^kB.
```

They are directly tied to Krylov moment matching and to linear relative degree. The present quantities

```math
(A^pB)^\dagger Q(A^qB)
```

are two-sided/quadratic-output pairings. Literature on linear systems with quadratic outputs already uses bivariate quadratic transfer functions and Krylov/moment-matching constructions, so the mere appearance of two-index moments is not a CORE novelty claim.

### Relative degree

Classical LTI relative degree is determined by the first nonzero one-sided Markov parameter `CA^{r-1}B`. CORE generation order is not identical to that object: it comes from derivatives of a quadratic signed output along an initial-condition trajectory and therefore involves binomial anti-diagonal combinations of two-sided pairings.

### Lie-derivative analogy

`L_A^j(Q)` is literally the repeated derivative of the quadratic observable along the linear vector field at the matrix level. Calling this a Lie-derivative hierarchy would be mathematically natural, but terminology alone would not constitute novelty.

### Early literature warning

Krylov/moment matching for linear systems with quadratic outputs is an active established literature, including work that uses a bivariate quadratic transfer function and two-sided Krylov projection. Therefore any future CORE-specific theorem must exploit something beyond the existence of quadratic moments/Krylov spaces themselves — for example the signed-Hermitian/isotropic-input structure, the anti-diagonal cancellation geometry, or an invariant statement about the first nonzero diagonal jet.

---

## 7. Stop status

**COUNTEREXAMPLE / BRANCH FAILURE REACHED**

Under the user-defined automatic stop rule, Branch-A theory development stops here.

1. **Failed statement:** generation order can be read off as the first Krylov depth at which `Q` becomes nontrivial, or at which any nonzero `Q`-pairing between generated directions appears.
2. **Smallest counterexample found:** `2 x 2`, scalar input, normal Hermitian `A`, Hermitian indefinite `Q`, rank-one `B` as given above.
3. **Failure mechanism:** `H_j` contains weighted anti-diagonal sums of two-sided `Q`-moments; nonzero individual pairings can cancel. At first order a purely skew-Hermitian cross-pairing is invisible after Hermitian symmetrization.
4. **Weaker statement retained:** `H_j` is exactly the binomially weighted anti-diagonal sum of the two-sided pairings `M_{p,q}`; pairwise vanishing is sufficient but not necessary for `H_j=0`.
5. **Return point:** return to the algebraic anti-diagonal pairing representation before quotienting the data down to the nested spaces `K_j(A,B)`. A later continuation should compare at least (i) two-index pairing geometry, (ii) diagonal-jet geometry of `G_Q(t)`, and (iii) strengthened Krylov-space statements under extra assumptions.

Because Event B has been reached, this package deliberately does **not** proceed to the requested 3 x 3, nonnormal, rank-varied counterexample suite or to a theorem candidate. Those belong to the next package only after the counterexample and return point are reviewed.