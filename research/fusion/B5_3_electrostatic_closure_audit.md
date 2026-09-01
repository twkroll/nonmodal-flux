# B5.3 — Electrostatic closure audit for the slab/curvature comparison

**Status:** completed closure audit; no finite-dimensional matrix, free-energy Hessian, or transport matrix constructed yet  
**Date:** 2026-09-01  
**Parent notes:** `research/fusion/B5_1_source_convention.md`, `research/fusion/B5_2A_slab_linearization.md`, `research/fusion/B5_2B_2_pressure_sector.md`

## Scope

This step asks one question only: can the same **adiabatic-electron electrostatic closure** be used consistently for both the slab and minimal-curvature R1 branches?

The answer is **yes for the nonzonal local Fourier modes relevant to radial transport**, provided the comparison is kept in the standard quasineutral drift ordering: electron inertia and Debye-scale true space charge are neglected, while the long-wavelength ion polarization density is retained.

No matrix \(A_k\) is written in this note.

---

## A. Normalization

Keep the ion normalization introduced in B5.2B.2,

\[
N \equiv \frac{\widetilde n_i}{n_0},
\qquad
\Phi \equiv \frac{e\widetilde\phi}{T_{i0}},
\qquad
\tau_i \equiv \frac{T_{i0}}{T_{e0}}>0,
\]

with singly charged ions and an equilibrium satisfying

\[
n_{i0}=n_{e0}=n_0.
\]

Define the normalized electron-density perturbation

\[
N_e\equiv\frac{\widetilde n_e}{n_0}.
\]

---

## B. Adiabatic electron response

Scott's local gyrofluid discussion derives the adiabatic response from quasistatic balance of the parallel electric and electron-pressure forces. With electron temperature flattened along the field, the nonzonal perturbation satisfies

\[
\frac{\widetilde n_e}{n_0}
=
\frac{e\widetilde\phi}{T_{e0}}
\]

up to the standard flux-surface-average subtraction. More precisely,

\[
N_e
=
\frac{e}{T_{e0}}
\left(\widetilde\phi-\langle\widetilde\phi\rangle\right).
\tag{AE-1}
\]

For a local nonzonal Fourier mode with \(k_y\neq0\),

\[
\langle\widetilde\phi\rangle=0,
\]

so in the present ion-temperature normalization

\[
\boxed{
N_e=\tau_i\Phi.
}
\tag{AE-2}
\]

This closure is a parallel force-balance statement and contains no magnetic-curvature frequency \(\omega_d\).

---

## C. Long-wavelength ZLR polarization relation

The parent Strintzi–Scott–Brizard polarization equation retained in B5.1 is

\[
\sum_j\left[
 e_j n_j
+\nabla_\perp\cdot\left(
 \frac{n_jm_jc^2}{B^2}\nabla_\perp\phi
\right)
\right]
+\frac{1}{4\pi}\nabla^2\phi=0.
\]

For the reduced ion model, take the standard gyrofluid/quasineutral ordering used in Scott's local model:

- retain ion polarization inertia;
- neglect electron polarization inertia, \(m_e/m_i\to0\);
- neglect true space charge / Debye corrections.

For one local perpendicular Fourier mode this gives

\[
N-N_e-b_P\Phi=0,
\tag{POL-1}
\]

where

\[
\boxed{
b_P\equiv k_\perp^2\rho_i^2,
\qquad
\rho_i^2\equiv
\frac{m_i c^2T_{i0}}{e^2B_0^2}
}
\tag{POL-2}
\]

in the long-wavelength convention inherited from the parent polarization term.

The label \(b_P\) is used deliberately: R1 is ZLR in the **gyroaveraging/moment** operators, but still retains the long-wavelength polarization inertia required to determine \(\phi\). It should not be confused with restoring the full FLR gyroaveraging of R2.

Combining (AE-2) and (POL-1) yields

\[
\boxed{
N=(\tau_i+b_P)\Phi,
}
\tag{CL-1}
\]

and hence

\[
\boxed{
\Phi=\mathcal C_k N,
\qquad
\mathcal C_k\equiv\frac{1}{\tau_i+b_P}.
}
\tag{CL-2}
\]

Because \(\tau_i>0\) and \(b_P\ge0\), this nonzonal algebraic closure is nonsingular.

---

## D. Cross-check against Scott's normalized gyrofluid polarization

Scott writes the single-ion polarization relation, with electron FLR neglected, schematically as

\[
N_e
=
\Gamma_1 N
+\Gamma_2\Theta_\perp
+\frac{\Gamma_0-1}{\tau_i}\,\varphi_e,
\]

where

\[
\varphi_e=\frac{e\widetilde\phi}{T_{e0}}.
\]

In the R1 ZLR restriction,

\[
\Gamma_1\to1,
\qquad
\Gamma_2\to0,
\qquad
1-\Gamma_0\to b_P
\]

at long wavelength. With adiabatic electrons \(N_e=\varphi_e\) and \(\varphi_e=\tau_i\Phi\), the same result follows:

\[
N=(\tau_i+b_P)\Phi.
\]

Thus the closure obtained directly from the parent long-wavelength polarization equation agrees with the ZLR/low-\(b\) limit of Scott's energy-consistent local gyrofluid polarization structure.

---

## E. The same closure is valid for slab and minimal curvature

Neither the adiabatic response (AE-2) nor the local algebraic polarization relation (CL-1) contains \(\omega_d\). Therefore, if the two branches are compared at the same

\[
(n_0,T_{i0},T_{e0},B_0,k_\perp),
\]

they use the identical map

\[
\boxed{
\Phi=\frac{N}{\tau_i+b_P}.
}
\]

Curvature changes the **moment dynamics**, not this closure, in the present minimal local ordering.

This statement would cease to be literally scalar if a later model retained field-line variation of \(k_\perp\), full FLR operators, kinetic electrons, or nonlocal geometry. Those belong to R2/R3 and are not part of the present comparison.

---

## F. Zonal mode is a separate closure sector

For \(k_y=0\), the adiabatic response contains the flux-surface-average subtraction and one cannot replace it by (AE-2). In that sector the electron response to the zonal component is absent in the simple adiabatic approximation.

This does **not** obstruct the present transport pilot, because the radial \(E\times B\) velocity of a single local Fourier mode is

\[
v_{E,x}=-i\frac{ck_y}{B_0}\widetilde\phi,
\]

so the direct radial particle/heat-flux observable vanishes when \(k_y=0\).

The nonzonal closure (CL-2) is therefore the relevant one for the first signed-transport calculation.

---

## G. Important consequence: particle flux collapses under this closure

For the ion density channel,

\[
\Gamma_{i,k}
\propto
k_y\,\operatorname{Im}
\left(\widetilde n_i^*\widetilde\phi\right).
\]

But (CL-2) makes \(N\) and \(\Phi\) related by a **real positive scalar** at every instant. Hence

\[
\boxed{
\operatorname{Im}(N^*\Phi)=0,
\qquad
\Gamma_{i,k}=0
}
\tag{PF-0}
\]

for this single-ion adiabatic-electron R1 closure. The adiabatic electron particle flux vanishes for the same reason.

This is not a defect in the algebra; it is a physical restriction of the reduced closure. It means:

- R1 with adiabatic electrons is suitable for a first **heat-flux** finite-horizon test;
- it cannot carry the intended nontrivial particle-flux channel;
- a later particle/heat multi-channel study requires a nonadiabatic electron response or a richer species model.

This reproduces the warning already identified in the fusion model audit: adiabatic-electron reductions may remove an independent particle-transport channel.

---

## H. Heat transport remains nontrivial

The closure does **not** force the pressure/temperature perturbations to be in phase with \(\Phi\). Therefore correlations between radial \(E\times B\) velocity and the thermal moments remain nonzero in general.

Scott's adiabatic-electron ITG example measures an ion thermal transport flux proportional to

\[
Q_i
\propto
\left\langle
\left(\frac12\widetilde T_{i\parallel}
+\widetilde T_{i\perp}\right)v_{E,x}
\right\rangle.
\]

In the present variables, the corresponding temperature combination is

\[
\frac12\Theta_\parallel+\Theta_\perp
=
\frac12P_\parallel+P_\perp-\frac32N.
\]

This observation is recorded only as a source anchor for the later physical derivation of \(Q_{q,k}\); no heat-flux matrix is constructed in B5.3.

---

## I. Energy-structure check at the closure level

Scott's adiabatic-electron polarization/free-energy construction combines the electron adiabatic contribution with the ion polarization energy. For a nonzonal mode, both contributions have positive coefficients when

\[
\tau_i>0,
\qquad
b_P\ge0.
\]

The same positivity appears algebraically in the denominator \(\tau_i+b_P\) of (CL-2). This is a useful consistency check, but it is **not** yet a derivation of the full four-moment perturbation metric \(M_k\). That remains B5.4.

---

## J. Result

For the first controlled slab/curvature comparison, the source-supported closure is

\[
\boxed{
\Phi=\frac{N}{\tau_i+k_\perp^2\rho_i^2},
\qquad k_y\neq0.
}
\]

It can be used identically in both branches.

The closure also gives a strong modelling result before any numerical work:

\[
\boxed{
Q_{\Gamma}=0\ \text{on the adiabatic-electron constrained R1 state space},
}
\]

while the ion heat-flux channel remains potentially nontrivial.

Therefore the next safe step is to substitute (CL-2) into the already derived slab and curvature moment equations and write the two explicit \(4\times4\) generators

\[
A_k^{\rm slab},
\qquad
A_k^{\rm curv},
\]

without yet optimizing them.

No user-level decision is required before that algebraic step.

---

## Literature anchors

- D. Strintzi, B. D. Scott, A. J. Brizard, *Nonlocal Nonlinear Electrostatic Gyrofluid Equations: A four-moment model*, Phys. Plasmas **12**, 052517 (2005), arXiv:physics/0410276. Parent polarization equation and four-moment energetics.
- B. D. Scott, *GEM — An Energy Conserving Electromagnetic Gyrofluid Model*, Phys. Plasmas **12**, 102307 (2005), arXiv:physics/0501124. Adiabatic electron response, polarization Eqs. (45), (49), (82), (92), and positive potential/free-energy construction; the paper also reports the adiabatic-electron ITG heat-flux diagnostic \(Q_i\propto\langle(0.5T_{i\parallel}+T_{i\perp})v_E^x\rangle\).
