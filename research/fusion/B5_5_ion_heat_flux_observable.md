# B5.5 — Physical ion radial heat-flux observable

**Status:** `PASS — PHYSICAL ION HEAT-FLUX OPERATOR DERIVED AND BALANCE-CONSISTENT`  
**Date:** 2026-09-04  
**Parent notes:** `research/fusion/B5_1_source_convention.md`, `research/fusion/B5_2A_slab_linearization.md`, `research/fusion/B5_2B_curvature_linearization.md`, `research/fusion/B5_2B_1_local_curvature_source_audit.md`, `research/fusion/B5_2B_2_pressure_sector.md`, `research/fusion/B5_3A_slab_generator.md`, `research/fusion/B5_3B_curvature_generator.md`, `research/fusion/B5_4A_slab_free_energy_metric.md`, `research/fusion/B5_4B_curvature_free_energy_check.md`

## Scope

This note completes B5.5 only. It derives the instantaneous signed ion radial heat/thermal-energy transport observable directly from the physical radial \(E\times B\) transport of the retained anisotropic ion thermal moments, then checks the result against the already-derived B5.4 free-energy balance.

No finite-time operator, optimizer, horizon scan, parameter scan, stability search, FLR/R2 extension, kinetic-electron extension, six-moment GEM calculation, or GENE calculation is performed here.

The frozen state and closure are

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad
\Phi=\mathcal C_k N,
\qquad
\mathcal C_k=\frac{1}{\tau_i+b_P}>0,
\]

with

\[
N=\frac{\widetilde n_i}{n_0},\qquad
U=\frac{\widetilde u_\parallel}{c_s},\qquad
P_\parallel=\frac{\widetilde p_\parallel}{p_0},\qquad
P_\perp=\frac{\widetilde p_\perp}{p_0},
\]

\[
p_0=n_0T_{i0},\qquad
\Theta_\parallel=P_\parallel-N,
\qquad
\Theta_\perp=P_\perp-N,
\]

and the nonzonal local Fourier convention

\[
\propto e^{i(k_xx+k_yy+k_\parallel z)},
\qquad k_y\neq0.
\]

Temperature is measured in energy units, consistently with \(p=nT\).

---

## 1. Physical ion thermal-energy / heat-flux definition

For the anisotropic four-moment ion model, the thermal energy per particle carried by the retained parallel/perpendicular temperatures is

\[
\epsilon_{T,i}=\frac12T_{i\parallel}+T_{i\perp}.
\]

This is the same anisotropic thermal combination that appears in the Scott adiabatic-electron ITG transport diagnostic retained as a source anchor in B5.3,

\[
Q_i\propto\left\langle
\left(\frac12\widetilde T_{i\parallel}+\widetilde T_{i\perp}\right)v_{E,x}
\right\rangle.
\]

Therefore the dimensional radial ion thermal-energy flux used here is

\[
\boxed{
q_i
=n_0\left\langle
\left(\frac12\widetilde T_{i\parallel}+\widetilde T_{i\perp}\right)
\widetilde v_{E,x}
\right\rangle .
}
\tag{1}
\]

It has units of energy per area per time (equivalently pressure times velocity).

Because

\[
\widetilde T_{i\parallel}=T_{i0}\Theta_\parallel,
\qquad
\widetilde T_{i\perp}=T_{i0}\Theta_\perp,
\]

(1) can be written

\[
q_i
=p_0\left\langle
\left(\frac12\Theta_\parallel+\Theta_\perp\right)
\widetilde v_{E,x}
\right\rangle.
\tag{2}
\]

This is independently a physical transport definition; no use of \(A^\dagger M+MA\) has been made.

### Equivalent pressure/internal-energy form on the frozen constrained state

The perturbation of the parent-model ion internal-energy density is

\[
\delta\mathcal E_{T,i}
=\frac12\widetilde p_\parallel+\widetilde p_\perp
=p_0\left(\frac12P_\parallel+P_\perp\right).
\]

The difference between this pressure form and the temperature form in (2) is

\[
\frac32T_{i0}\widetilde n_i.
\]

Its radial \(E\times B\) transport is \((3/2)T_{i0}\Gamma_i\). Under the frozen adiabatic-electron closure, \(\Gamma_i=0\) identically (shown again in Sec. 10), so the pressure/internal-energy and temperature forms give exactly the same physical flux on the admissible R1 state space.

Thus no ambiguity between these two natural reduced-model thermal-energy conventions survives the frozen closure.

---

## 2. Radial \(E\times B\) velocity and sign

The frozen slab/local coordinate convention is

\[
\mathbf B=B_0\widehat{\mathbf z},
\qquad
\mathbf u_E=\frac{c}{B_0}\widehat{\mathbf z}\times\nabla\widetilde\phi.
\]

With \(+x\) taken as the positive radial direction,

\[
\boxed{
\widetilde v_{E,x}
=-\frac{c}{B_0}\partial_y\widetilde\phi.
}
\tag{3}
\]

For the frozen Fourier convention,

\[
\boxed{
\widetilde v_{E,x,k}
=-i\frac{ck_y}{B_0}\widetilde\phi_k
=-i\mathcal V_k\Phi_k,
}
\tag{4}
\]

where the signed velocity scale is

\[
\boxed{
\mathcal V_k
\equiv\frac{ck_yT_{i0}}{eB_0}.
}
\tag{5}
\]

The sign of \(\mathcal V_k\) follows the sign of \(k_y\); no absolute value is inserted.

---

## 3. Exact thermodynamic combination

Define

\[
S_T
\equiv\frac12\Theta_\parallel+\Theta_\perp
=\frac12P_\parallel+P_\perp-\frac32N.
\tag{6}
\]

Then the physical flux is the cross-phase between \(S_T\) and radial \(E\times B\) velocity.

Because the frozen electrostatic closure is real,

\[
\Phi=\mathcal C_kN,
\qquad \mathcal C_k\in\mathbb R_{>0},
\]

we have

\[
\operatorname{Im}(\Phi^*N)=0.
\tag{7}
\]

Therefore

\[
\boxed{
\operatorname{Im}(\Phi^*S_T)
=
\operatorname{Im}\left[
\Phi^*\left(\frac12P_\parallel+P_\perp\right)
\right].
}
\tag{8}
\]

The density term is not discarded by hand; its transport contribution vanishes because the particle channel collapses under the frozen closure.

---

## 4. Complex single-\(k\) and real conjugate-pair conventions

For one complex Fourier amplitude, define the single-\(k\) covariance contribution by

\[
\langle a b\rangle_k^{(c)}
\equiv\operatorname{Re}(a_k^*b_k).
\tag{9}
\]

Using (2)–(5),

\[
\boxed{
q_{i,k}^{(c)}
=-p_0\mathcal V_k
\operatorname{Im}(\Phi_k^*S_{T,k}).
}
\tag{10}
\]

With (8) and \(\Phi=\mathcal C_kN\),

\[
\boxed{
q_{i,k}^{(c)}
=-p_0\mathcal V_k\mathcal C_k
\operatorname{Im}\left[
N_k^*\left(\frac12P_{\parallel,k}+P_{\perp,k}\right)
\right].
}
\tag{11}
\]

For a real field reconstructed from the conjugate pair,

\[
a^{\rm pair}=a_ke^{ik\cdot r}+a_k^*e^{-ik\cdot r},
\]

spatial averaging gives

\[
\langle a^{\rm pair}b^{\rm pair}\rangle
=2\operatorname{Re}(a_k^*b_k).
\]

Hence

\[
\boxed{
q_{i,\{k,-k\}}^{\rm pair}=2q_{i,k}^{(c)}.
}
\tag{12}
\]

The corresponding pair free energy is likewise twice the single-complex-mode convention, so all balance identities below are unchanged by choosing the real-pair convention.

Under \(k\mapsto-k\), \(k_y\mapsto-k_y\) and \(z_{-k}=z_k^*\); the two sign changes cancel and

\[
q_{i,-k}^{(c)}=q_{i,k}^{(c)}.
\]

Thus the physical value is invariant under the permitted real-field conjugate reconstruction.

---

## 5. Dimensional and nondimensional prefactors

Equation (11) separates the dimensional flux scale and the dimensionless state geometry:

\[
\boxed{
p_0\mathcal V_k
=n_0T_{i0}\frac{ck_yT_{i0}}{eB_0}
}
\tag{13}
\]

has units of heat/thermal-energy flux, while \(\mathcal C_k\) and the state amplitudes are dimensionless.

A convenient signed normalized flux is

\[
\boxed{
\widehat q_{i,k}
\equiv\frac{q_{i,k}^{(c)}}{p_0\mathcal V_k}
=-\mathcal C_k
\operatorname{Im}\left[
N^*\left(\frac12P_\parallel+P_\perp\right)
\right].
}
\tag{14}
\]

For the balance identity it is also useful to use the transport-velocity form

\[
\mathcal F_{q_i,k}\equiv\frac{q_{i,k}^{(c)}}{p_0},
\tag{15}
\]

which has units of velocity.

---

## 6. Hermitian matrix in the frozen state ordering

Let

\[
\mathsf Q_0
\equiv
\begin{pmatrix}
0&0&\frac{i}{4}&\frac{i}{2}\\
0&0&0&0\\
-\frac{i}{4}&0&0&0\\
-\frac{i}{2}&0&0&0
\end{pmatrix}.
\tag{16}
\]

Then \(\mathsf Q_0=\mathsf Q_0^\dagger\), and (11) is exactly

\[
\boxed{
q_{i,k}^{(c)}
=z_k^\dagger Q_{q_i,k}z_k,
}
\tag{17}
\]

with

\[
\boxed{
Q_{q_i,k}
=p_0\mathcal V_k\mathcal C_k\,\mathsf Q_0.
}
\tag{18}
\]

Thus

\[
\boxed{
Q_{q_i,k}=Q_{q_i,k}^\dagger.
}
\]

For the real conjugate-pair convention, the pair matrix is simply

\[
Q_{q_i,\{k,-k\}}^{\rm pair}=2Q_{q_i,k}.
\tag{19}
\]

In temperature coordinates \(y=(N,U,\Theta_\parallel,\Theta_\perp)^T\), the same physical quadratic form couples \(N\) to \((\Theta_\parallel/2+\Theta_\perp)\); the apparent pressure-coordinate density term is absent from the value because of (7). This is a coordinate representation change, not a change of observable.

---

## 7. Slab/minimal-curvature consistency

The same \(Q_{q_i,k}\) applies to both the slab and minimal-curvature generators.

Reason: the instantaneous physical observable depends only on

1. the common state variables;
2. the common nonzonal adiabatic-electron closure \(\Phi=\mathcal C_kN\);
3. the common local radial \(E\times B\) kinematics (3)–(4); and
4. the same anisotropic ion thermal-energy combination (6).

The curvature frequency \(\omega_d\) changes the generator \(A_k\), but it does not alter the local \(E\times B\) velocity relation or the definition of the retained ion thermal-energy moment. Therefore no \(\omega_d\) appears in \(Q_{q_i,k}\).

---

## 8. Rank, signature, and signed character

For the allowed nonzonal sector \(k_y\neq0\),

\[
\mathcal V_k\neq0,
\qquad
\mathcal C_k>0.
\]

The dimensionless matrix \(\mathsf Q_0\) has

\[
\operatorname{rank}(\mathsf Q_0)=2,
\]

with eigenvalues

\[
\left\{\frac{\sqrt5}{4},-\frac{\sqrt5}{4},0,0\right\}.
\]

Therefore

\[
\boxed{
\operatorname{rank}(Q_{q_i,k})=2,
\qquad
\operatorname{signature}(Q_{q_i,k})=(1,1,2),
}
\tag{20}
\]

where the signature notation means one positive, one negative, and two zero eigenvalues.

The physical heat-flux form is therefore nontrivial and indefinite. Its nullspace contains the parallel-velocity direction and the pressure combination satisfying

\[
\frac12P_\parallel+P_\perp=0
\]

when \(N=0\).

A direct sign witness is immediate: for \(k_y>0\), real \(N>0\), and \(P_\parallel=0\), choosing \(P_\perp=-i|P_\perp|\) gives positive outward flux, while reversing that phase gives negative inward flux. No finite-time optimization is involved.

---

## 9. Mandatory B5.4 free-energy balance consistency gate

B5.4 fixed

\[
W_k=\frac{p_0}{2}z_k^\dagger M_kz_k,
\]

with

\[
M_k=
\begin{pmatrix}
\frac52+\mathcal C_k&0&-\frac12&-1\\
0&1&0&0\\
-\frac12&0&\frac12&0\\
-1&0&0&1
\end{pmatrix}\succ0,
\]

and independently established for both slab and curvature

\[
A_k^\dagger M_k+M_kA_k
=\mathcal C_k\gamma_T
\begin{pmatrix}
0&0&-\frac{i}{2}&-i\\
0&0&0&0\\
\frac{i}{2}&0&0&0\\
i&0&0&0
\end{pmatrix},
\tag{21}
\]

where

\[
\gamma_T
=\mathcal V_k\frac{d\ln T_{i0}}{dx}.
\tag{22}
\]

From (16),

\[
\begin{pmatrix}
0&0&-\frac{i}{2}&-i\\
0&0&0&0\\
\frac{i}{2}&0&0&0\\
i&0&0&0
\end{pmatrix}
=-2\mathsf Q_0.
\]

Using the independently derived physical matrix (18) therefore gives

\[
\boxed{
A_k^\dagger M_k+M_kA_k
=2g_T\,\frac{Q_{q_i,k}}{p_0},
\qquad
g_T\equiv-\frac{d\ln T_{i0}}{dx}.
}
\tag{23}
\]

This identity holds for both \(A_k^{\rm slab}\) and \(A_k^{\rm curv}\).

The factor of two in (23) is exactly the project convention

\[
W_k=\frac{p_0}{2}z_k^\dagger M_kz_k.
\]

Indeed,

\[
\begin{aligned}
\frac{dW_k}{dt}
&=\frac{p_0}{2}
 z_k^\dagger(A_k^\dagger M_k+M_kA_k)z_k\\
&=g_T\,z_k^\dagger Q_{q_i,k}z_k,
\end{aligned}
\]

so

\[
\boxed{
\frac{dW_k}{dt}
=-\frac{d\ln T_{i0}}{dx}\,q_{i,k}^{(c)}.
}
\tag{24}
\]

For an outward-decreasing equilibrium temperature, \(d\ln T_{i0}/dx<0\), outward positive heat flux injects positive perturbation free energy, as expected.

Equation (24) is exactly the B5.4B source term rewritten using the physical flux derived in Secs. 1–6. No coefficient or sign in \(Q_{q_i,k}\) was chosen to force this identity.

---

## 10. Particle-flux channel under the same closure

The ion particle flux for one complex mode is

\[
\Gamma_{i,k}^{(c)}
=n_0\operatorname{Re}(N_k^*\widetilde v_{E,x,k})
=-n_0\mathcal V_k\operatorname{Im}(\Phi_k^*N_k).
\]

Since \(\Phi_k=\mathcal C_kN_k\) with real \(\mathcal C_k\),

\[
\boxed{
\Gamma_{i,k}^{(c)}=0.
}
\tag{25}
\]

The adiabatic electron perturbation is likewise a real scalar multiple of \(\Phi\), so its particle flux also vanishes.

Therefore B5.5 confirms the previously identified channel collapse:

\[
\boxed{Q_{\Gamma_i,k}=0}
\]

on the frozen adiabatic-electron R1 state space. No new particle channel is introduced.

This also means that alternative thermal-energy/heat conventions differing by a fixed equilibrium-energy or enthalpy multiple of \(\Gamma_i\) are identical on this constrained state space. The nontrivial independent signed channel at B5.5 is the ion thermal/heat flux (17).

---

## Structural gate summary

- **Physical definition:** radial \(E\times B\) transport of \(\frac12\widetilde T_{i\parallel}+\widetilde T_{i\perp}\), multiplied by \(n_0\).
- **Radial sign:** \(v_{E,x}=-(c/B_0)\partial_y\phi\), with \(+x\) outward.
- **Thermodynamic combination:** \(\frac12\Theta_\parallel+\Theta_\perp\); equivalently \(\frac12P_\parallel+P_\perp\) in the flux value because \(\Gamma_i=0\).
- **Hermiticity:** \(Q_{q_i,k}=Q_{q_i,k}^\dagger\).
- **Nontriviality:** yes for \(k_y\neq0\).
- **Rank/signature:** rank 2, one positive and one negative eigenvalue, two null directions.
- **Real-field reconstruction:** pair value is exactly twice the single-complex-mode value and is invariant under \(k\leftrightarrow-k\).
- **Slab/curvature:** identical physical \(Q_{q_i,k}\); curvature changes only \(A_k\).
- **Units:** \(Q_{q_i,k}\) has units pressure times velocity; \(Q_{q_i,k}/p_0\) has units velocity.
- **Balance:** exact identity (23), equivalently \(\dot W_k=(-\partial_x\ln T_{i0})q_{i,k}\).
- **Particle channel:** identically zero under the same closure.

## Gate verdict

\[
\boxed{
\text{PASS — PHYSICAL ION HEAT-FLUX OPERATOR DERIVED AND BALANCE-CONSISTENT}
}
\]

B5.5 is complete. The next scientifically safe topic is the admissible input geometry/input-cost gate, but this Fusion branch does **not** self-authorize it. Return to MASTER for a separate handoff.

**STOP — B5.5 COMPLETE; NO FINITE-TIME EFFECT INSPECTION.**
