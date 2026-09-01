# B5.4B — Curvature free-energy consistency check

**Status:** completed energetic consistency check of the minimal-curvature generator; no heat-flux matrix or optimization constructed yet  
**Date:** 2026-09-01  
**Parent notes:** `research/fusion/B5_3B_curvature_generator.md`, `research/fusion/B5_4A_slab_free_energy_metric.md`

## Scope

This step asks one question only: does the source-derived positive metric obtained in B5.4A remain the correct conservative free-energy metric when the minimal local curvature terms of B5.3B are switched on?

The answer is **yes** for the present R1 reduction. The curvature deformation is exactly skew-adjoint in the B5.4A free-energy inner product. Moreover, after restoring the equilibrium-gradient terms, the Hermitian part of the generator is independent of curvature and collapses to a single temperature-gradient injection channel.

No transport observable is defined in this note. The final identification and normalization of the physical ion heat-flux matrix remain B5.5.

---

## A. Metric carried over from B5.4A

Use the common state

\[
z_k=(N,U,P_\parallel,P_\perp)^\top
\]

and closure

\[
\Phi=\mathcal C_kN,
\qquad
\mathcal C_k=\frac{1}{\tau_i+b_P}>0.
\]

B5.4A derived

\[
W_k=\frac{n_0T_{i0}}{2}\,z_k^\dagger M_k z_k
\]

with

\[
\boxed{
M_k=
\begin{pmatrix}
\frac52+\mathcal C_k & 0 & -\frac12 & -1\\
0 & 1 & 0 & 0\\
-\frac12 & 0 & \frac12 & 0\\
-1 & 0 & 0 & 1
\end{pmatrix}
\succ0.
}
\tag{M}
\]

Equivalently,

\[
W_k=\frac{n_0T_{i0}}{2}
\left[
(1+\mathcal C_k)|N|^2+|U|^2
+\frac12|P_\parallel-N|^2
+|P_\perp-N|^2
\right].
\]

No curvature coefficient enters this quadratic functional.

---

## B. Source-free curvature generator

Set the profile drives to zero,

\[
G_n=G_p=0.
\]

From B5.3B,

\[
A_{0,k}^{\rm curv}=A_{0,k}^{\rm slab}+\Delta A_k^{\rm curv},
\]

where

\[
\Delta A_k^{\rm curv}
=-i\omega_d D_k
\]

and

\[
D_k=
\begin{pmatrix}
2\mathcal C_k & 0 & 1 & 1\\
0 & 2 & 0 & 0\\
-4(1-\mathcal C_k) & 0 & 7 & 1\\
-3(1-\mathcal C_k) & 0 & 1 & 5
\end{pmatrix}.
\tag{D}
\]

For real \(\omega_d\) and \(\mathcal C_k\), direct multiplication gives the exact matrix identity

\[
\boxed{
D_k^\top M_k=M_kD_k.
}
\tag{MD}
\]

Therefore

\[
(\Delta A_k^{\rm curv})^\dagger M_k
+M_k\Delta A_k^{\rm curv}
=i\omega_d(D_k^\top M_k-M_kD_k)=0.
\]

B5.4A already established

\[
(A_{0,k}^{\rm slab})^\dagger M_k
+M_kA_{0,k}^{\rm slab}=0.
\]

Adding the two results yields

\[
\boxed{
(A_{0,k}^{\rm curv})^\dagger M_k
+M_kA_{0,k}^{\rm curv}=0.
}
\tag{FE-curv}
\]

Hence

\[
\boxed{
\frac{dW_k}{dt}=0
}
\]

for the homogeneous nondissipative minimal-curvature system.

This is the central B5.4B gate: the local curvature reduction has not introduced an artificial free-energy source or sink.

---

## C. Consequence: the same positive metric applies to both branches

Within the present local R1 comparison,

\[
\boxed{
M_k^{\rm curv}=M_k^{\rm slab}=M_k.
}
\]

Thus slab and curvature can be compared in exactly the same physical norm. Curvature changes the generator but not the positive free-energy constraint.

This is stronger than merely recovering the slab limit as \(\omega_d\to0\): for arbitrary retained \(\omega_d\), the curvature part is conservative in the same inner product.

The result also gives a useful implementation check for any later numerical matrix construction:

\[
\left\|
(A_{0,k}^{\rm curv})^\dagger M_k+M_kA_{0,k}^{\rm curv}
\right\|
\]

must vanish to numerical roundoff when profile drive and dissipation are absent.

---

## D. Gradient-drive Hermitian part

Now restore the local equilibrium gradients. The only gradient-dependent entries of both slab and curvature generators are

\[
A_{G,k}=
\begin{pmatrix}
\mathcal C_kG_n&0&0&0\\
0&0&0&0\\
\mathcal C_kG_p&0&0&0\\
\mathcal C_kG_p&0&0&0
\end{pmatrix}.
\tag{AG}
\]

For real equilibrium profiles and real \(k_y\), write

\[
G_n=i\gamma_n,
\qquad
G_p=i\gamma_p,
\]

where

\[
\gamma_n=
\frac{ck_yT_{i0}}{eB_0}\frac{d\ln n_0}{dx},
\qquad
\gamma_p=
\frac{ck_yT_{i0}}{eB_0}\frac{d\ln p_0}{dx}.
\]

Because \(p_0=n_0T_{i0}\), define

\[
\boxed{
\gamma_T\equiv\gamma_p-\gamma_n
=
\frac{ck_yT_{i0}}{eB_0}\frac{d\ln T_{i0}}{dx}.
}
\tag{gammaT}
\]

Using (M), direct multiplication gives

\[
\boxed{
A_k^\dagger M_k+M_kA_k
=\mathcal C_k\gamma_T
\begin{pmatrix}
0&0&-\frac{i}{2}&-i\\
0&0&0&0\\
\frac{i}{2}&0&0&0\\
i&0&0&0
\end{pmatrix}.
}
\tag{balance-matrix}
\]

This identity is valid for **both** \(A_k^{\rm slab}\) and \(A_k^{\rm curv}\), because their source-free parts are separately conservative and they share the same gradient-drive matrix.

Two structural consequences follow immediately:

1. the density-gradient contribution cancels from the free-energy injection under the present adiabatic-electron closure;
2. the remaining injection depends only on the ion temperature gradient.

This is consistent with the earlier result that the independent particle-flux channel collapses for the same closure.

---

## E. Phase-sensitive form of the free-energy injection

Let

\[
S_T\equiv\frac12P_\parallel+P_\perp.
\]

From (balance-matrix),

\[
z_k^\dagger
(A_k^\dagger M_k+M_kA_k)z_k
=2\mathcal C_k\gamma_T\,
\operatorname{Im}(N^*S_T).
\]

Since \(\Phi=\mathcal C_kN\), this becomes

\[
\boxed{
\frac{dW_k}{dt}
=n_0T_{i0}\,\gamma_T\,
\operatorname{Im}\!\left[
\Phi^*\left(\frac12P_\parallel+P_\perp\right)
\right].
}
\tag{drive-1}
\]

The physical temperature combination is

\[
\frac12\Theta_\parallel+\Theta_\perp
=\frac12P_\parallel+P_\perp-\frac32N.
\]

Because \(\Phi=\mathcal C_kN\) with real \(\mathcal C_k\),

\[
\operatorname{Im}(\Phi^*N)=0,
\]

and therefore

\[
\boxed{
\operatorname{Im}\!\left[
\Phi^*\left(\frac12P_\parallel+P_\perp\right)
\right]
=
\operatorname{Im}\!\left[
\Phi^*\left(\frac12\Theta_\parallel+\Theta_\perp\right)
\right].
}
\tag{thermal-combination}
\]

Thus the free-energy balance independently selects exactly the same anisotropic thermal combination that was identified from Scott's ion heat-transport diagnostic in B5.3.

This is an important cross-check, but it is **not yet** the definition of \(Q_{q,k}\): the sign, dimensional prefactor, Fourier-pair convention, and radial-velocity normalization must still be derived directly from the physical heat-flux expression.

---

## F. What B5.4B resolves

The energetic gate is passed:

\[
\boxed{
M_k^{\rm curv}=M_k^{\rm slab}\succ0,
}
\]

and, without equilibrium gradients,

\[
\boxed{
(A_{0,k}^{\rm curv})^\dagger M_k
+M_kA_{0,k}^{\rm curv}=0.
}
\]

With gradients present, curvature contributes no additional Hermitian free-energy production term; the exact source term is proportional only to

\[
\gamma_T\,
\operatorname{Im}\!\left[
\Phi^*\left(\frac12\Theta_\parallel+\Theta_\perp\right)
\right].
\]

This gives a stringent bridge from the positive norm to the physical heat-transport channel without yet guessing a transport matrix.

Still deliberately open:

- the physical normalization and sign of the ion radial heat flux;
- the Hermitian heat-flux matrix \(Q_{q,k}\);
- admissible input maps and transport-neutral subspaces;
- finite-horizon optimization or parameter sweeps.

The next safe step is B5.5: derive the ion heat-flux observable directly from the physical radial ExB thermal-energy flux and check that its quadratic form reproduces the free-energy injection identity above.

---

## Source basis

- `research/fusion/B5_4A_slab_free_energy_metric.md`: source-derived positive delta-f free-energy metric and slab conservation identity.
- `research/fusion/B5_3B_curvature_generator.md`: closed minimal-curvature generator and its controlled deformation from the slab branch.
- The Scott/Strintzi literature anchors and equation provenance for those two ingredients are recorded in the parent notes; no additional external closure assumption is introduced in B5.4B.
