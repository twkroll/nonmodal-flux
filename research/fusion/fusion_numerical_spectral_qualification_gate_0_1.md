# Fusion F1.4 — Numerical / Spectral Qualification Gate 0.1

**Date:** 2026-09-05  
**Authority:** MASTER / `research/master/prompts/fusion_numerical_spectral_qualification_gate_0_1.md`  
**Status:** `F1.4 HOLD — MARGINAL SPECTRUM — RETURN TO MASTER`

## Scope and prohibitions

This gate qualifies exactly the F1.3-frozen anisotropic-ZLR four-moment R1 minimal-curvature candidate at the single frozen CBC-projected point. It performs only exact matrix reconstruction, algebraic/free-energy checks, physical heat-channel reconstruction, coordinate consistency, complete eigenvalue calculation and numerical-conditioning checks.

No parameter, wavenumber or horizon scan was performed. No damping, viscosity/diffusion, collisions, Landau-fluid term or other spectral rescue was added. No finite-time free-energy/heat propagator objective, Gramian, cumulative channel operator, optimizer, principal angle, performance gap, transient-growth curve or effect size was constructed or inspected. No FLR/R2, kinetic-electron, six-moment GEM or GENE extension was opened.

---

## 1. Exact frozen inputs and dimensionless coefficients

The frozen state is

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad
\Phi=\mathcal C_kN,
\]

with

\[
\tau_i=1,
\quad
R_0/L_n=2.2,
\quad
R_0/L_T=6.9,
\quad
q=1.4,
\quad
k_x\rho_i=0,
\quad
k_y\rho_i=0.3,
\quad
\tau_{\rm ref}=R_0/c_s.
\]

Hence

\[
b_P=k_\perp^2\rho_i^2=0.09,
\qquad
\mathcal C_k=\frac{1}{1.09}=0.9174311926605504.
\]

Using

\[
\widetilde A=\tau_{\rm ref}A,
\qquad
\widehat Q_q=\frac{Q_{q_i,k}}{p_0c_s},
\]

the dimensionless rates are

\[
\widetilde\omega_d=\tau_{\rm ref}\omega_d=k_y\rho_i=0.3,
\]

\[
\widetilde\kappa_\parallel
=\tau_{\rm ref}k_\parallel c_s
=\frac1q
=0.7142857142857143,
\]

\[
\widetilde G_n
=-i(k_y\rho_i)\frac{R_0}{L_n}
=-0.66i,
\]

\[
\widetilde G_p
=-i(k_y\rho_i)\left(\frac{R_0}{L_n}+\frac{R_0}{L_T}\right)
=-2.73i.
\]

No other dimensional or closure coefficient enters the frozen single-block R1 matrix.

---

## 2. Numerical matrix reconstruction

The exact frozen primary dimensionless generator is

\[
\boxed{
\widetilde A=
\begin{pmatrix}
-1.155963302752i&-0.714285714286i&-0.300000000000i&-0.300000000000i\\
-0.655307994758i&-0.600000000000i&-0.714285714286i&0\\
-2.405504587156i&-2.142857142857i&-2.100000000000i&-0.300000000000i\\
-2.430275229358i&-0.714285714286i&-0.300000000000i&-1.500000000000i
\end{pmatrix}.
}
\]

The frozen free-energy metric is

\[
\boxed{
M_k=
\begin{pmatrix}
3.417431192661&0&-0.5&-1\\
0&1&0&0\\
-0.5&0&0.5&0\\
-1&0&0&1
\end{pmatrix}.
}
\]

The dimensionless physical heat-flux matrix is

\[
\boxed{
\widehat Q_q=
\begin{pmatrix}
0&0&0.068807339450i&0.137614678899i\\
0&0&0&0\\
-0.068807339450i&0&0&0\\
-0.137614678899i&0&0&0
\end{pmatrix}.
}
\]

The admissible-input objects remain

\[
\boxed{B=I_4,\qquad R_{\rm in}=M_k.}
\]

The slab implementation control is obtained only by setting `omega_d=0`; it was not used as an alternative candidate or effect comparison.

---

## 3. Algebraic structure checks

All numerical structure checks were evaluated in IEEE double precision with structural tolerance `1e-12`, supplemented below by exact-rational/high-precision reproduction.

### 3.1 Metric

The eigenvalues of `M_k` are

\[
0.339983130263,
\quad
0.733614381410,
\quad
1.000000000000,
\quad
3.843833680988.
\]

Therefore

\[
\boxed{M_k=M_k^\dagger\succ0.}
\]

Because `R_in=M_k`, the input-cost metric is likewise Hermitian positive definite. `rank(B)=4` exactly.

### 3.2 Heat channel

The eigenvalues of `\widehat Q_q` are

\[
-0.153857888360,
\quad 0,
\quad 0,
\quad +0.153857888360.
\]

Thus

\[
\boxed{
\widehat Q_q=\widehat Q_q^\dagger,
\qquad
\operatorname{rank}(\widehat Q_q)=2,
\qquad
\operatorname{signature}(\widehat Q_q)=(1,1,2).
}
\]

The frozen channel remains non-neutral and indefinite; no transport-neutral projection was introduced.

---

## 4. Free-energy balance and source-free curvature check

The required dimensionless balance is

\[
\widetilde A^\dagger M_k+M_k\widetilde A
=2\frac{R_0}{L_T}\widehat Q_q
=13.8\,\widehat Q_q.
\]

The maximum absolute entrywise residual is

\[
\boxed{6.66\times10^{-16}},
\]

and the matrix 2-norm residual is

\[
7.55\times10^{-16}.
\]

This is at roundoff level.

Removing only the equilibrium-gradient entries while retaining parallel and minimal-curvature dynamics gives `\widetilde A_0`. The conservative identity

\[
\widetilde A_0^\dagger M_k+M_k\widetilde A_0=0
\]

has maximum absolute entrywise residual

\[
\boxed{2.22\times10^{-16}}.
\]

Thus the frozen gradient source, metric, closure, parallel terms and curvature terms reproduce the B5.4B free-energy structure numerically without modification.

---

## 5. Physical heat-channel reconstruction

The independently frozen normalized cross-phase expression is

\[
\frac{q_{i,k}}{p_0c_s}
=-(k_y\rho_i)\mathcal C_k
\operatorname{Im}\left[
N^*\left(\frac12P_\parallel+P_\perp\right)
\right].
\]

Four fixed, non-optimized deterministic states were checked against `z^dagger \widehat Q_q z`:

| Test state `z=(N,U,P_parallel,P_perp)` | matrix value | cross-phase value | absolute difference |
|---|---:|---:|---:|
| `(1,0,i,0)` | `-0.137614678899083` | `-0.137614678899083` | `0` |
| `(1+i,0.2,0.3-0.4i,-0.2+0.7i)` | `-0.151376146788991` | `-0.151376146788991` | `0` |
| `(0.2-0.5i,-0.1i,1.2+0.3i,-0.4-0.2i)` | `-0.024770642201835` | `-0.024770642201835` | `6.94e-18` |
| `(0,1+2i,0.3+0.1i,-0.7+0.4i)` | `0` | `0` | `0` |

The physical matrix implementation therefore reproduces the independently derived radial-ion-heat cross phase to machine precision.

---

## 6. Coordinate consistency

Use temperature coordinates

\[
y=(N,U,\Theta_\parallel,\Theta_\perp)^T,
\qquad
z=Ty,
\]

with

\[
T=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
1&0&1&0\\
1&0&0&1
\end{pmatrix}.
\]

Congruence gives

\[
T^\dagger M_kT
=\operatorname{diag}(1.917431192661,1,0.5,1),
\]

which is positive definite, and

\[
T^\dagger\widehat Q_qT
=
\begin{pmatrix}
0&0&0.068807339450i&0.137614678899i\\
0&0&0&0\\
-0.068807339450i&0&0&0\\
-0.137614678899i&0&0&0
\end{pmatrix}.
\]

The channel inertia remains `(1,1,2)`. A fixed complex test vector gave energy-value agreement to `4.44e-16` and heat-value agreement to below `6e-18`. This confirms that the pressure-coordinate and temperature-coordinate forms represent the same physical metric/channel and not different admissible subspaces.

---

## 7. Complete spectrum and spectral decision

The matrix scale is

\[
\|\widetilde A\|_2=4.886570583605431.
\]

The scale-aware spectral classification tolerance is frozen for this gate as

\[
\boxed{
\varepsilon_{\rm spec}
=100\,\epsilon_{\rm mach}\max(1,\|\widetilde A\|_2)
=1.0850\times10^{-13}.
}
\]

The complete double-precision spectrum is

\[
\boxed{
\begin{aligned}
\lambda_1&=-3.592939609690i,\\
\lambda_2&=-1.563190668779i,\\
\lambda_3&=-0.276482492169i,\\
\lambda_4&=+0.076649467886i,
\end{aligned}
}
\]

with computed real parts at the `10^{-17}` level. The numerical spectral abscissa is

\[
\alpha(\widetilde A)=7.34\times10^{-17},
\]

which satisfies

\[
|\alpha(\widetilde A)|\ll\varepsilon_{\rm spec}.
\]

Therefore the frozen point is **numerically marginal**, not asymptotically stable and not clearly unstable.

### Independent exact-rational/high-precision reproduction

At this frozen point all coefficients are rational. In exact arithmetic

\[
\mathcal C_k=\frac{100}{109},
\]

and the generator can be written

\[
\widetilde A=-iH,
\]

with the real rational matrix

\[
H=
\begin{pmatrix}
126/109&5/7&3/10&3/10\\
500/763&3/5&5/7&0\\
1311/545&15/7&21/10&3/10\\
2649/1090&5/7&3/10&3/2
\end{pmatrix}.
\]

Its characteristic polynomial is

\[
\frac{1}{13352500}
\left(
13352500\mu^4
-71515500\mu^3
+88468625\mu^2
-13527180\mu
-1589283
\right).
\]

A 40-digit root calculation gives four distinct **real** roots

\[
-0.07664946788568589536,
\quad
0.27648249216884434991,
\quad
1.56319066877946168284,
\quad
3.59293960968967344059.
\]

Hence `\lambda=-i\mu` is purely imaginary to high precision. The same exact-rational path gives zero identically for both the free-energy balance residual and the source-free `M_k`-skew-adjoint residual. This independently reproduces the double-precision classification.

The four roots are distinct, so the frozen matrix is diagonalizable.

---

## 8. Numerical conditioning and nonnormality descriptor

Relevant 2-norm condition numbers are

\[
\boxed{
\kappa_2(M_k)=11.3059541455,
}
\]

\[
\boxed{
\kappa_2(W)=3.3624327719,
}
\]

where `W=L^dagger` and `M_k=LL^dagger` is a Cholesky whitening factor, and

\[
\boxed{
\kappa_2(V)=3.3383254402
}
\]

for the right-eigenvector basis of `\widetilde A`. In the whitened representation the eigenvector-basis condition number is `3.8528455979`.

The eigen-decomposition residual satisfies

\[
\|\widetilde AV-V\Lambda\|_2/\|\widetilde A\|_2
=3.53\times10^{-16}.
\]

These values do not indicate a conditioning failure for the present 4x4 qualification.

For descriptive purposes only, the Euclidean normality commutator is nonzero; the normalized value

\[
\frac{\|\widetilde A^\dagger\widetilde A-\widetilde A\widetilde A^\dagger\|_2}
{\|\widetilde A\|_2^2}
\approx0.6575.
\]

This records that the matrix is nonnormal. No transient-growth or finite-time objective was computed from that fact.

---

## 9. Qualification verdict

All algebraic, physical-reconstruction and conditioning checks pass. The spectrum, however, is marginal under the prescribed scale-aware rule:

\[
\boxed{
\text{F1.4 HOLD — MARGINAL SPECTRUM — RETURN TO MASTER}
}
\]

This is a genuine qualification outcome, not a failure to find a stable point. The F1.3 candidate and CBC-projected point were frozen before spectral inspection and were not altered after the marginal spectrum was found.

---

## 10. Allowed interpretations

The F1.4 result supports the following statements:

- the frozen minimal-curvature R1 matrices are reconstructed consistently at the exact frozen point;
- the free-energy metric and signed heat-flux matrix satisfy all frozen Hermiticity, positivity, rank and inertia requirements;
- the physical heat-flux matrix reproduces the independently derived radial `E x B` thermal cross phase;
- the exact free-energy balance and conservative curvature/parallel identities hold to roundoff and exactly in a rational audit;
- the matrix is numerically well-conditioned for this four-dimensional qualification;
- the frozen collisionless CBC-projected R1 point has a four-eigenvalue spectrum on the imaginary axis and is therefore marginal under the F1.4 decision rule.

## 11. Forbidden interpretations

This result does **not** establish:

- finite-time free-energy growth or heat-transport growth;
- any energy-optimal or heat-optimal initial direction;
- any optimizer angle, performance gap or cumulative heat-flux magnitude;
- that marginality should be repaired by damping, collisions or parameter retuning;
- that another CBC wavenumber or parameter would be stable;
- that the slab control has better or worse finite-time behavior;
- that FLR, kinetic-electron, six-moment or gyrokinetic fidelity would preserve this spectrum.

MASTER must decide explicitly whether a marginal conservative frozen point is acceptable for the subsequent scientific program or whether the roadmap requires a new pre-effect model/closure decision.

## Reproducibility

Transparent single-point qualification code is committed alongside this file as

`research/fusion/fusion_numerical_spectral_qualification_0_1.py`.

The code hard-codes exactly one frozen point, contains no parameter/horizon loops and constructs no finite-time objective.

**STOP — F1.4 COMPLETE; RETURN TO MASTER.**
