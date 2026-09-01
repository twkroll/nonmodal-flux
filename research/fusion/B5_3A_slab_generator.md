# B5.3A — Closed slab generator after adiabatic-electron elimination

**Status:** completed algebraic construction of the nonzonal slab generator; no free-energy metric or transport matrix constructed yet  
**Date:** 2026-09-01  
**Parent notes:** `research/fusion/B5_2A_slab_linearization.md`, `research/fusion/B5_3_electrostatic_closure_audit.md`

## Scope

This step does one thing only: insert the common nonzonal adiabatic-electron closure

\[
\Phi=\mathcal C_k N,
\qquad
\mathcal C_k=\frac{1}{\tau_i+b_P},
\qquad
b_P=k_\perp^2\rho_i^2,
\]

into the already derived slab moment equations and write the resulting explicit \(4\times4\) generator.

No perturbation free-energy Hessian \(M_k\), heat-flux matrix \(Q_{q,k}\), optimization, or numerical implementation is introduced here.

The closure is restricted to the nonzonal sector \(k_y\neq0\). Since \(\tau_i>0\) and \(b_P\ge0\), \(\mathcal C_k\) is real, positive, and nonsingular.

---

## A. Starting slab equations

For the isotropic equilibrium subset used for the slab/curvature comparison, define

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

The slab equations obtained previously are

\[
\dot N=G_n\Phi-i k_\parallel u,
\tag{S1}
\]

\[
\dot u=-i k_\parallel c_s^2(\Phi+P_\parallel),
\tag{S2}
\]

\[
\dot P_\parallel=G_p\Phi-3i k_\parallel u,
\tag{S3}
\]

\[
\dot P_\perp=G_p\Phi-i k_\parallel u,
\tag{S4}
\]

where

\[
G_n=i\frac{ck_yT_{i0}}{eB_0}\frac{d\ln n_0}{dx},
\qquad
G_p=i\frac{ck_yT_{i0}}{eB_0}\frac{d\ln p_0}{dx}.
\]

No sign-normalized gradient lengths are introduced in this step.

---

## B. Dimensionless velocity coordinate

For a homogeneous matrix representation it is convenient to use the dimensionless parallel velocity

\[
U\equiv\frac{u}{c_s},
\qquad
\kappa_\parallel\equiv k_\parallel c_s.
\]

This is only a coordinate rescaling, not a new physical model assumption. The state is

\[
\boxed{
z_k^{\rm slab}
=\begin{pmatrix}
N\\ U\\ P_\parallel\\ P_\perp
\end{pmatrix}.
}
\]

All components are dimensionless and every entry of the generator has units of inverse time.

After substituting \(\Phi=\mathcal C_kN\), the equations become

\[
\boxed{
\dot N
=\mathcal C_kG_n N-i\kappa_\parallel U,
}
\tag{CS1}
\]

\[
\boxed{
\dot U
=-i\kappa_\parallel\left(\mathcal C_kN+P_\parallel\right),
}
\tag{CS2}
\]

\[
\boxed{
\dot P_\parallel
=\mathcal C_kG_p N-3i\kappa_\parallel U,
}
\tag{CS3}
\]

\[
\boxed{
\dot P_\perp
=\mathcal C_kG_p N-i\kappa_\parallel U.
}
\tag{CS4}
\]

---

## C. Explicit slab generator

Thus

\[
\dot z_k^{\rm slab}=A_k^{\rm slab}z_k^{\rm slab}
\]

with

\[
\boxed{
A_k^{\rm slab}=
\begin{pmatrix}
\mathcal C_kG_n & -i\kappa_\parallel & 0 & 0\\
-i\kappa_\parallel\mathcal C_k & 0 & -i\kappa_\parallel & 0\\
\mathcal C_kG_p & -3i\kappa_\parallel & 0 & 0\\
\mathcal C_kG_p & -i\kappa_\parallel & 0 & 0
\end{pmatrix}.
}
\tag{A-slab}
\]

This is the first explicit finite-dimensional R1 generator in the fusion branch.

The electrostatic potential is no longer an independent coordinate; when needed it is reconstructed from

\[
\Phi=\mathcal C_k e_1^\top z_k^{\rm slab},
\qquad
e_1=(1,0,0,0)^\top.
\]

---

## D. Algebraic checks

### D.1 Reconstruction of the DAE

Using \(u=c_sU\) and \(\Phi=\mathcal C_kN\), multiplying (CS2) by \(c_s\) reproduces

\[
\dot u=-ik_\parallel c_s^2(\Phi+P_\parallel),
\]

while (CS1), (CS3), and (CS4) reproduce the normalized slab equations exactly. No dynamic term is created by the elimination.

### D.2 Closure denominator

For the intended nonzonal adiabatic-electron sector,

\[
\tau_i>0,
\qquad
b_P\ge0,
\]

so

\[
\mathcal C_k=\frac{1}{\tau_i+b_P}>0.
\]

Hence the algebraic elimination introduces no pole in the admissible parameter range.

### D.3 Long-wavelength polarization limit

As \(b_P\to0\),

\[
\mathcal C_k\to\frac{1}{\tau_i},
\]

and (A-slab) reduces smoothly to the strict long-wavelength adiabatic-electron form.

This limit does not mean that the zonal sector is included: the derivation still assumes \(k_y\neq0\).

### D.4 Parallel-decoupling limit

As already anticipated in B5.2A, if

\[
\kappa_\parallel\to0,
\]

the generator becomes

\[
A_k^{\rm slab}\to
\begin{pmatrix}
\mathcal C_kG_n&0&0&0\\
0&0&0&0\\
\mathcal C_kG_p&0&0&0\\
\mathcal C_kG_p&0&0&0
\end{pmatrix}.
\]

The parallel-velocity and pressure-compression pathways then collapse. This confirms algebraically that the useful slab control should retain \(k_\parallel\neq0\).

### D.5 No particle-flux channel is restored by elimination

Because \(\Phi=\mathcal C_kN\) with real \(\mathcal C_k\),

\[
\operatorname{Im}(N^*\Phi)=0.
\]

Thus the explicit ODE does not restore a hidden ion-particle-flux channel. On the constrained R1 state space,

\[
Q_{\Gamma,k}=0
\]

for this adiabatic-electron closure.

---

## E. Useful structural observations, without interpreting them yet

The matrix has three distinct coupling mechanisms:

1. profile drive through \(\mathcal C_kG_n\) and \(\mathcal C_kG_p\);
2. parallel acoustic/electrostatic coupling through \(\kappa_\parallel\mathcal C_k\);
3. anisotropic pressure compression through the unequal coefficients \(3\kappa_\parallel\) and \(\kappa_\parallel\).

The perpendicular pressure does not feed back directly into the slab density or momentum equations at this stage, whereas the parallel pressure does. Nevertheless \(P_\perp\) remains dynamically generated and is required by the physical ion heat-flux combination to be constructed later.

No claim about modal stability, nonnormality, transient growth, or heat-flux optimality is made from the matrix structure alone. Those require the positive metric and the physical output operator.

---

## F. Coordinate relation to the mixed-unit state

If one instead keeps

\[
x_k=(N,u,P_\parallel,P_\perp)^\top,
\]

then

\[
x_k=S z_k,
\qquad
S=\operatorname{diag}(1,c_s,1,1),
\]

and the two generators are related by the similarity transformation

\[
A_x=S A_k^{\rm slab}S^{-1}.
\]

Therefore the use of \(U=u/c_s\) does not change the spectrum or physical dynamics. Later, the free-energy metric and transport operators must be transformed covariantly if another coordinate convention is used.

---

## G. Stop condition after B5.3A

B5.3A fixes only \(A_k^{\rm slab}\) for the nonzonal adiabatic-electron R1 branch.

Still deliberately open:

- \(A_k^{\rm curv}\);
- the perturbation free-energy Hessians \(M_k\);
- the physical ion heat-flux matrix \(Q_{q,k}\);
- admissible input maps \(B\) and transport-neutral input subspaces;
- any optimization or parameter sweep.

The next safe algebraic step is to insert the **same** closure into the completed minimal-curvature four-moment equations and construct \(A_k^{\rm curv}\) in the same state coordinates. The required check is then

\[
\boxed{
A_k^{\rm curv}\xrightarrow{\omega_d\to0}A_k^{\rm slab}.
}
\]

Only after that branch comparison should the free-energy Hessian be derived.
