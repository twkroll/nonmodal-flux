# B5.3B — Closed minimal-curvature generator after adiabatic-electron elimination

**Status:** completed algebraic construction of the nonzonal minimal-curvature generator; no free-energy metric or heat-flux matrix constructed yet  
**Date:** 2026-09-01  
**Parent notes:** `research/fusion/B5_2B_2_pressure_sector.md`, `research/fusion/B5_3_electrostatic_closure_audit.md`, `research/fusion/B5_3A_slab_generator.md`

## Scope

This step inserts the same nonzonal adiabatic-electron closure used in the slab branch,

\[
\Phi=\mathcal C_k N,
\qquad
\mathcal C_k=\frac{1}{\tau_i+b_P},
\qquad
b_P=k_\perp^2\rho_i^2,
\]

into the completed minimal-curvature four-moment equations and writes the explicit \(4\times4\) generator in exactly the same state coordinates as B5.3A.

No perturbation free-energy Hessian \(M_k\), ion heat-flux matrix \(Q_{q,k}\), optimization, or numerical implementation is introduced here.

The closure is restricted to the nonzonal sector \(k_y\neq0\), with \(\tau_i>0\), \(b_P\ge0\), and hence \(\mathcal C_k>0\).

---

## A. Starting curvature equations

Use the normalized variables

\[
N=\frac{\widetilde n_i}{n_0},
\qquad
P_\parallel=\frac{\widetilde p_\parallel}{p_0},
\qquad
P_\perp=\frac{\widetilde p_\perp}{p_0},
\qquad
\Phi=\frac{e\widetilde\phi}{T_{i0}},
\]

with

\[
c_s^2=\frac{T_{i0}}{m_i}.
\]

B5.2B.2 established the minimal local-curvature differential-algebraic system

\[
\dot N=G_n\Phi-i k_\parallel u
-2i\omega_d\Phi-i\omega_d(P_\parallel+P_\perp),
\tag{C1}
\]

\[
\dot u=-2i\omega_d u
-i k_\parallel c_s^2(\Phi+P_\parallel),
\tag{C2}
\]

\[
\dot P_\parallel=G_p\Phi-3i k_\parallel u
-2i\omega_d\left(2\Phi-2N+\frac72P_\parallel+\frac12P_\perp\right),
\tag{C3}
\]

\[
\dot P_\perp=G_p\Phi-i k_\parallel u
-2i\omega_d\left(\frac32\Phi-\frac32N+\frac12P_\parallel+\frac52P_\perp\right).
\tag{C4}
\]

The profile-drive coefficients remain

\[
G_n=i\frac{ck_yT_{i0}}{eB_0}\frac{d\ln n_0}{dx},
\qquad
G_p=i\frac{ck_yT_{i0}}{eB_0}\frac{d\ln p_0}{dx}.
\]

---

## B. Common state coordinates

As in B5.3A, define

\[
U\equiv\frac{u}{c_s},
\qquad
\kappa_\parallel\equiv k_\parallel c_s,
\]

and use

\[
\boxed{
z_k^{\rm curv}
=\begin{pmatrix}
N\\ U\\ P_\parallel\\ P_\perp
\end{pmatrix}.
}
\]

After substituting \(\Phi=\mathcal C_kN\), equations (C1)–(C4) become

\[
\boxed{
\dot N=
(\mathcal C_kG_n-2i\omega_d\mathcal C_k)N
-i\kappa_\parallel U
-i\omega_d P_\parallel
-i\omega_d P_\perp,
}
\tag{CC1}
\]

\[
\boxed{
\dot U=
-i\kappa_\parallel\mathcal C_kN
-2i\omega_dU
-i\kappa_\parallel P_\parallel,
}
\tag{CC2}
\]

\[
\boxed{
\begin{aligned}
\dot P_\parallel={}&
\left[\mathcal C_kG_p+4i\omega_d(1-\mathcal C_k)\right]N
-3i\kappa_\parallel U\\
&-7i\omega_d P_\parallel-i\omega_d P_\perp,
\end{aligned}
}
\tag{CC3}
\]

\[
\boxed{
\begin{aligned}
\dot P_\perp={}&
\left[\mathcal C_kG_p+3i\omega_d(1-\mathcal C_k)\right]N
-i\kappa_\parallel U\\
&-i\omega_d P_\parallel-5i\omega_d P_\perp.
\end{aligned}
}
\tag{CC4}
\]

The factors \(4(1-\mathcal C_k)\) and \(3(1-\mathcal C_k)\) arise only from combining the electrostatic curvature pieces with the explicit \(-2N\) and \(-3N/2\) terms of the pressure equations; they are not additional closure assumptions.

---

## C. Explicit curvature generator

Thus

\[
\dot z_k^{\rm curv}=A_k^{\rm curv}z_k^{\rm curv}
\]

with

\[
\boxed{
A_k^{\rm curv}=
\begin{pmatrix}
\mathcal C_kG_n-2i\omega_d\mathcal C_k
&-i\kappa_\parallel
&-i\omega_d
&-i\omega_d\\
-i\kappa_\parallel\mathcal C_k
&-2i\omega_d
&-i\kappa_\parallel
&0\\
\mathcal C_kG_p+4i\omega_d(1-\mathcal C_k)
&-3i\kappa_\parallel
&-7i\omega_d
&-i\omega_d\\
\mathcal C_kG_p+3i\omega_d(1-\mathcal C_k)
&-i\kappa_\parallel
&-i\omega_d
&-5i\omega_d
\end{pmatrix}.
}
\tag{A-curv}
\]

The electrostatic potential is reconstructed, exactly as in the slab branch, from

\[
\Phi=\mathcal C_k e_1^\top z_k^{\rm curv},
\qquad
e_1=(1,0,0,0)^\top.
\]

---

## D. Exact slab-limit check

The slab generator from B5.3A is

\[
A_k^{\rm slab}=
\begin{pmatrix}
\mathcal C_kG_n & -i\kappa_\parallel & 0 & 0\\
-i\kappa_\parallel\mathcal C_k & 0 & -i\kappa_\parallel & 0\\
\mathcal C_kG_p & -3i\kappa_\parallel & 0 & 0\\
\mathcal C_kG_p & -i\kappa_\parallel & 0 & 0
\end{pmatrix}.
\]

Setting \(\omega_d=0\) in (A-curv) gives this matrix entry by entry. Therefore

\[
\boxed{
A_k^{\rm curv}\xrightarrow{\omega_d\to0}A_k^{\rm slab}.
}
\tag{limit}
\]

This is the required branch-consistency test.

---

## E. Curvature as a controlled deformation of the slab operator

It is useful to expose the difference without yet interpreting it dynamically:

\[
A_k^{\rm curv}=A_k^{\rm slab}+\Delta A_k^{\rm curv},
\]

with

\[
\boxed{
\Delta A_k^{\rm curv}
=-i\omega_d
\begin{pmatrix}
2\mathcal C_k & 0 & 1 & 1\\
0 & 2 & 0 & 0\\
-4(1-\mathcal C_k) & 0 & 7 & 1\\
-3(1-\mathcal C_k) & 0 & 1 & 5
\end{pmatrix}.
}
\tag{DeltaA}
\]

Thus curvature does more than add a common drift frequency. It creates direct density–pressure coupling, different phase rotations of the two pressure moments, and closure-dependent density feedback through \(1-\mathcal C_k\).

No conclusion about instability or nonnormal amplification is drawn from this structure alone.

---

## F. Algebraic checks

### F.1 Reconstruction of the curvature DAE

Replacing \(U\) by \(u/c_s\) and inserting \(\Phi=\mathcal C_kN\) in (CC1)–(CC4) reproduces (C1)–(C4) exactly. The elimination introduces no additional dynamic term.

### F.2 Same electrostatic closure in both branches

The closure factor \(\mathcal C_k\) contains no \(\omega_d\). Hence the slab-to-curvature comparison changes only the moment generator while keeping the electrostatic constraint fixed.

### F.3 Nonsingular admissible closure

For

\[
\tau_i>0,
\qquad b_P\ge0,
\]

we retain

\[
\mathcal C_k>0,
\]

so no curvature-dependent singularity is introduced by eliminating \(\Phi\).

### F.4 Particle-flux channel remains identically zero

As in B5.3A,

\[
\Phi=\mathcal C_kN
\]

with real \(\mathcal C_k\), so

\[
\operatorname{Im}(N^*\Phi)=0.
\]

Curvature changes the heat-carrying pressure dynamics but does not restore a nontrivial ion particle-flux observable under this adiabatic-electron closure.

---

## G. What is now fixed

For the first R1 branch comparison we now have two explicit generators in identical coordinates:

\[
A_k^{\rm slab},
\qquad
A_k^{\rm curv},
\]

connected continuously by \(\omega_d\to0\).

Still deliberately open:

- the positive perturbation free-energy Hessian \(M_k\);
- the physical ion heat-flux matrix \(Q_{q,k}\);
- admissible input maps \(B\) and transport-neutral subspaces;
- modal/nonmodal analysis;
- numerical parameter sweeps.

The next safe step is therefore **not** optimization. It is the free-energy step: derive the quadratic perturbation metric in these coordinates and verify its positivity and consistency with the closed generator before any finite-horizon calculation is run.
