# Fusion F2.5R — Ion-FLR Magnetic-Moment Quadrature Repair / Discretization Requalification Gate 0.1

**Date:** 2026-09-07  
**Authority:** MASTER / `research/master/prompts/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`  
**Status:** `F2.5R PASS — ION-FLR MAGNETIC-MOMENT QUADRATURE REPAIRED / LADDER FROZEN — RETURN TO MASTER`

## Executive verdict

F2.5R repairs exactly the single numerical object released by MASTER: the ion Gauss--Laguerre magnetic-moment order \(N_\mu\) on the already-frozen K0/K1/K2 geometry ladder.

All upstream physical objects remain unchanged, including the controlling local-\(B\) ion-FLR convention

\[
\rho_{i0}=v_{Ti}/\Omega_i(B_0),
\qquad
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right),
\]

\[
\boxed{
b_i(\theta)
=(k_\perp(\theta)\rho_{i0})^2
\left(\frac{B_0}{B(\theta)}\right)^2,
\qquad
\Gamma_{0i}=I_0(b_i)e^{-b_i}.
}
\]

The deterministic pre-spectral search yields the smallest passing candidates in the predeclared order sequence,

\[
\boxed{
N_{\mu,K0}=16,\qquad
N_{\mu,K1}=24,\qquad
N_{\mu,K2}=40.
}
\]

This ladder is monotone and satisfies every F2.5R active-node and between-node manufactured-structure tolerance without changing the Gauss--Laguerre representation family.

Therefore

\[
\boxed{
\text{F2.5R PASS — ION-FLR MAGNETIC-MOMENT QUADRATURE REPAIRED / LADDER FROZEN — RETURN TO MASTER}.
}
\]

No generator spectrum, eigenvalue, propagator, Gramian, transport objective, optimizer or GENE calculation was performed or inspected.

---

## 1. Frozen objects preserved

The following remain exactly as frozen upstream:

- F2.1 reduced physics and physical particle / ion-heat / trapped-electron-heat channel definitions;
- F2.2 circular `s-alpha` ballooning geometry, Fourier orientation, local gyroaverage, trapping and bounce conventions;
- F2.3 physical benchmark point, including `epsilon=0.18`, `shat=0.8`, `k_y rho_i0=0.3`, `theta0=0`, and all equilibrium gradients/species ratios;
- F2.4 admissible continuous input space and input cost,
  \[
  B=I_{\mathcal H_{F2}},
  \qquad
  R_{\rm in}=\mathcal M_{F2};
  \]
- the MASTER local-\(B\) ion-FLR erratum;
- K0/K1/K2 ballooning windows, theta elements, LGL degrees, compact-support boundary treatment and ion Hermite orders;
- trapped-electron energy/pitch/well representation and bounce quadrature;
- algebraic quasineutrality elimination;
- absence of damping, filtering, hypercollision, loading, clipping and physical-direction deletion.

The Gauss--Laguerre coordinate remains

\[
\zeta=\mu_iB_0/T_i\in[0,\infty).
\]

Only \(N_\mu\) is changed.

---

## 2. Deterministic search rule frozen before evaluation

Before evaluating any repair candidate, the candidate sequence was declared as

\[
\boxed{
\mathcal N_\mu=
\{8,12,16,20,24,28,32,40,48,56,64,80,96,112,128\}.
}
\]

At each K level the candidates are evaluated in this order and the search stops at the first candidate that passes all structural tolerances.

The required active-node tolerances are:

\[
\max_\theta|\langle J_0^2\rangle_K-\Gamma_0|\le10^{-10},
\]

\[
\max_{\Gamma_0\ge10^{-6}}
\frac{|\langle J_0^2\rangle_K-\Gamma_0|}{\Gamma_0}
\le10^{-8},
\]

and for the positive-Helmholtz versus \(g\)-form ion field block,

\[
\frac{\|\Delta_{\rm FLR}\|_{F,w}}{\|C_{\rm QN}\|_{F,w}}
\le10^{-10},
\qquad
\max_\theta\frac{|\Delta_{\rm FLR}(\theta)|}{|C_{\rm QN}(\theta)|}
\le10^{-10}.
\]

The representative \(\theta=0,\pi\) tests must meet the same scale, Maxwellian density/energy/heat-weight moments must remain at least as well resolved as the historical checks up to roundoff, and all Laguerre weights must remain strictly positive.

---

## 3. Independent geometry-only between-node envelope

To prevent accidental fitting only to the active LGL nodes, each frozen \(\pi\)-wide theta element is also sampled by a deterministic 257-point Chebyshev--Lobatto geometry-only grid.

Adjacent element endpoints are identified, and the two removed global compact-support endpoints are excluded exactly as in the physical coefficient space. No \(A_K\), transport channel, spectrum or effect quantity enters this check.

The same manufactured FLR absolute and relative tolerances are imposed on this independent envelope.

Envelope point counts are:

- K0: 1535 points;
- K1: 2559 points;
- K2: 3583 points.

---

## 4. Candidate history and minimal passing orders

### K0

| \(N_\mu\) | active abs | active rel | field Fro/C | field local/C | envelope abs | envelope rel | result |
|---:|---:|---:|---:|---:|---:|---:|:---:|
| 8 | `8.303e-05` | `3.698e-04` | `3.981e-06` | `4.151e-05` | `9.406e-05` | `4.222e-04` | FAIL |
| 12 | `1.295e-08` | `5.765e-08` | `4.676e-10` | `6.473e-09` | `1.576e-08` | `7.075e-08` | FAIL |
| **16** | **`5.209e-13`** | **`2.320e-12`** | **`1.615e-14`** | **`2.604e-13`** | **`6.780e-13`** | **`3.043e-12`** | **PASS** |

Thus the smallest passing predeclared K0 candidate is

\[
\boxed{N_{\mu,K0}=16}.
\]

### K1

| \(N_\mu\) | active abs | active rel | field Fro/C | field local/C | envelope abs | envelope rel | result |
|---:|---:|---:|---:|---:|---:|---:|:---:|
| 8 | `5.889e-02` | `4.504e-01` | `9.137e-03` | `2.945e-02` | `5.999e-02` | `4.599e-01` | FAIL |
| 12 | `1.701e-03` | `1.301e-02` | `1.091e-04` | `8.506e-04` | `1.787e-03` | `1.370e-02` | FAIL |
| 16 | `7.704e-06` | `5.892e-05` | `2.893e-07` | `3.852e-06` | `8.332e-06` | `6.388e-05` | FAIL |
| 20 | `9.630e-09` | `7.365e-08` | `2.771e-10` | `4.815e-09` | `1.071e-08` | `8.209e-08` | FAIL |
| **24** | **`4.587e-12`** | **`3.508e-11`** | **`1.115e-13`** | **`2.293e-12`** | **`5.236e-12`** | **`4.015e-11`** | **PASS** |

Thus

\[
\boxed{N_{\mu,K1}=24}.
\]

### K2

| \(N_\mu\) | active abs | active rel | field Fro/C | field local/C | envelope abs | envelope rel | result |
|---:|---:|---:|---:|---:|---:|---:|:---:|
| 8 | `1.010e-01` | `9.908e-01` | `1.591e-02` | `5.051e-02` | `1.011e-01` | `9.988e-01` | FAIL |
| 12 | `8.685e-02` | `9.986e-01` | `1.739e-02` | `4.343e-02` | `8.708e-02` | `9.990e-01` | FAIL |
| 16 | `2.308e-02` | `3.047e-01` | `4.010e-03` | `1.154e-02` | `2.309e-02` | `3.050e-01` | FAIL |
| 20 | `1.033e-03` | `1.113e-02` | `1.267e-04` | `5.164e-04` | `1.067e-03` | `1.151e-02` | FAIL |
| 24 | `1.661e-05` | `1.790e-04` | `9.337e-07` | `8.305e-06` | `1.740e-05` | `1.878e-04` | FAIL |
| 28 | `1.060e-07` | `1.143e-06` | `3.431e-09` | `5.301e-08` | `1.126e-07` | `1.215e-06` | FAIL |
| 32 | `3.160e-10` | `3.406e-09` | `7.809e-12` | `1.580e-10` | `3.400e-10` | `3.669e-09` | FAIL |
| **40** | **`6.939e-16`** | **`5.684e-15`** | **`1.209e-16`** | **`3.469e-16`** | **`6.661e-16`** | **`6.440e-15`** | **PASS** |

The \(N_\mu=32\) candidate already meets the relative identity tolerance, but fails the absolute identity criterion and the maximum-local field-block criterion. Therefore it cannot be accepted. The first passing predeclared candidate is

\[
\boxed{N_{\mu,K2}=40}.
\]

---

## 5. Repaired ladder and state dimensions

All unchanged F2.5 orders are retained. Only the ion Laguerre row changes:

| quantity | K0 | K1 | K2 |
|---|---:|---:|---:|
| `Theta_max` | `3 pi` | `5 pi` | `7 pi` |
| theta DOF | 71 | 159 | 279 |
| ion Hermite order \(N_u\) | 16 | 24 | 32 |
| **repaired ion Laguerre order \(N_\mu\)** | **16** | **24** | **40** |
| trapped-e energy order | 12 | 18 | 24 |
| trapped-e pitch order | 12 | 18 | 24 |
| bounce quadrature order | 24 | 36 | 48 |

The repaired ion-state dimensions are

\[
N_i=N_\theta N_uN_\mu,
\]

hence

\[
\boxed{
N_i(K0,K1,K2)
=
(18176,\ 91584,\ 357120).
}
\]

Relative to the historical F2.5 dimensions this is a factor \(2,2,2.5\) increase respectively. The representation remains a tensor-product Gauss--Hermite / Gauss--Laguerre kinetic space and remains computationally credible for later sparse/matrix-free pre-spectral assembly.

The trapped-electron dimensions remain unchanged:

\[
N_e=(432,\ 1620,\ 4032).
\]

---

## 6. Selected-level structural diagnostics

| diagnostic | K0 | K1 | K2 |
|---|---:|---:|---:|
| active max FLR abs error | `5.209e-13` | `4.587e-12` | `6.939e-16` |
| active max FLR relative error | `2.320e-12` | `3.508e-11` | `5.684e-15` |
| weighted Frobenius field-block defect / C | `1.615e-14` | `1.115e-13` | `1.209e-16` |
| max local field-block defect / C | `2.604e-13` | `2.293e-12` | `3.469e-16` |
| envelope max FLR abs error | `6.780e-13` | `5.236e-12` | `6.661e-16` |
| envelope max FLR relative error | `3.043e-12` | `4.015e-11` | `6.440e-15` |

The envelope extends through local-\(b_i\) values up to approximately

\[
b_{i,\max}^{\rm env}
\simeq
3.788,\ 13.307,\ 29.143
\]

on K0/K1/K2. Thus the passing result is not restricted to small-\(b_i\) locations or to the central ballooning region.

---

## 7. Representative local-B checks

For every selected order, at \(\theta=0\),

\[
b_i=0.125316,
\qquad
\Gamma_0=0.8856850888548305,
\]

and the quadrature error is at roundoff:

\[
|\langle J_0^2\rangle-\Gamma_0|
\simeq1.1\times10^{-16}.
\]

At \(\theta=\pi\),

\[
b_i=0.44276814715924695,
\qquad
\Gamma_0=0.6741214459594775,
\]

with selected-level absolute errors no larger than

\[
4.5\times10^{-16}.
\]

The MASTER local-\(B\) erratum therefore remains correctly implemented.

---

## 8. Maxwellian moments and positive weights

The selected orders give maximum manufactured Maxwellian moment errors:

| level | density | energy | heat-weight |
|---|---:|---:|---:|
| K0 | `4.44e-16` | `6.66e-16` | `1.11e-15` |
| K1 | `4.44e-16` | `1.55e-15` | `1.55e-15` |
| K2 | `3.33e-16` | `4.44e-16` | `1.11e-15` |

These remain at floating-point roundoff and materially improve the historical worst moment residuals. The K0 density residual differs from the historical value by only one machine-precision unit and is not a physical/numerical degradation.

All selected Gauss--Laguerre weights are strictly positive. Their minimum values are approximately

\[
4.16\times10^{-22},\quad
5.58\times10^{-35},\quad
2.70\times10^{-61}
\]

for K0/K1/K2, and the weight sums equal 1 to roundoff. The physical positive phase-space measure is therefore preserved; no signed quadrature, clipping or reweighting is introduced.

---

## 9. Supersession rule

Historical F2.5 remains an immutable audit record.

For all subsequent F2-R numerical work, F2.5R supersedes **only** the historical ion magnetic-moment orders

\[
(8,12,16)
\]

by the repaired frozen orders

\[
\boxed{(16,24,40)}.
\]

Every other F2.5 numerical choice remains controlling and unchanged.

The historical F2.6 `0_2` FAIL remains the canonical record that motivated this repair. F2.5R does not itself re-run or overturn F2.6. A later F2.6 requalification requires an explicit new MASTER handoff.

---

## 10. Anti-bias / forbidden-work audit

The repair used only:

- the analytic local-\(B\) FLR manufactured identity;
- the positive-metric ion field-block defect;
- Maxwellian moment reproduction;
- positivity of Gauss--Laguerre weights;
- an independent geometry-only between-node envelope.

No eigenvalue, eigenvector, growth rate, spectral abscissa, pseudospectrum, matrix exponential, propagator, Gramian, finite-time objective, optimizer, angle, performance gap, transport magnitude, GENE output or parameter scan was calculated or inspected.

No physical parameter, input geometry, ballooning window, ion Hermite order, trapped-electron discretization, bounce rule or quasineutrality representation was changed.

---

## 11. Verdict

The released Gauss--Laguerre order repair is sufficient and computationally defensible. The repaired monotone ladder passes all predeclared manufactured local-\(B\) FLR and positive-metric criteria at active nodes and on an independent between-node geometry envelope.

\[
\boxed{
\text{F2.5R PASS — ION-FLR MAGNETIC-MOMENT QUADRATURE REPAIRED / LADDER FROZEN — RETURN TO MASTER}.
}
\]

**Next instruction:** none in this branch.

**STOP / RETURN TO MASTER.**
