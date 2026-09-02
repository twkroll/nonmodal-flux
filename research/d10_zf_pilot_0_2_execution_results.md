# D10-ZF Pilot 0.2 Execution

**Date:** 2026-09-02  
**Status:** COMPLETE; frozen execution only; no retuning and no new theory.

## Scope lock

This execution uses exactly the frozen Pilot-0.2 point

```math
U(x)=\cos x,\qquad L_x=2\pi,\qquad k_y=1,
```

```math
C=\kappa=1,\qquad N=0,\qquad \nu_\perp=0.020,
```

with the existing physical `M_K`, `Q_{Gamma,K}`, full-state input map `B=I`, and natural input metric `R_in=M_K`.  Only

```math
K\in\{32,64,96\},\qquad T\in\{0.25,0.5,1,2,4,8\}
```

are evaluated.  No parameter, damping, input map, observable, horizon, or resolution is changed after seeing any CORE/objective result.

Uniform damping is the already selected physical axis

```math
A_{K,\nu}=A_{K,0}-0.020 I.
```

For objective calculations the natural whitened coordinates are

```math
w=M_K^{1/2}u,\qquad \|w\|_2=1,
```

so `w_E^star` and `w_Gamma^star` below are the unit-cost optimizers in the common energy-whitened geometry.

The dimensionless transport gap is

```math
\Delta_{\Gamma,K}(T)=
\frac{\mathcal G_{\Gamma,+,K}(T)-J_\Gamma(T;u_{E,K}^\star)}
{\mathcal G_{\Gamma,+,K}(T)}.
```

## 1. Spectral stability

The spectral abscissae are

| K | state dimension | alpha(A_K) |
|---:|---:|---:|
| 32 | 130 | -0.007578597929 |
| 64 | 258 | -0.013381761021 |
| 96 | 386 | -0.015492437971 |

All three preregistered resolutions are therefore asymptotically stable.  The weakest margin is

```math
-\alpha(A_{32})=7.5786\times10^{-3}.
```

No unstable or marginal resolution occurs in the frozen execution set.

## 2. Preregistered scalar finite-time results

The objective values are resolution-converged to roundoff already at `K=32`.  The following table therefore applies to each of `K=32,64,96`; the stored CSV contains all 18 rows separately.

| T | G_E | G_Gamma,+ | G_Gamma,- | J_Gamma(u_E^star) | Delta_Gamma | theta |
|---:|---:|---:|---:|---:|---:|---:|
| 0.25 | 1.1747400205 | 0.1103473702 | -0.0873636748 | 0.0321642075 | 0.7085185859 | 65.5296 deg |
| 0.5 | 1.3776079078 | 0.1986923277 | -0.1266899931 | 0.0707957476 | 0.6436915889 | 61.6673 deg |
| 1 | 1.8782757947 | 0.3535169303 | -0.1462216197 | 0.1752252032 | 0.5043371669 | 53.3960 deg |
| 2 | 3.3716592477 | 0.7698794268 | -0.1336496625 | 0.5450513071 | 0.2920302996 | 40.9758 deg |
| 4 | 9.4117456811 | 2.7627379748 | -0.1190611943 | 2.3497970490 | 0.1494680022 | 28.6897 deg |
| 8 | 39.7632346459 | 16.0639684299 | -0.1151541443 | 13.7647568509 | 0.1431284921 | 28.0302 deg |

Thus, at every preregistered horizon,

```math
G_{E,K}(T)>1,
```

while simultaneously

```math
\mathcal G_{\Gamma,-,K}(T)<0<\mathcal G_{\Gamma,+,K}(T),
```

and

```math
\Delta_{\Gamma,K}(T)>0,\qquad \vartheta_K(T)>0.
```

The stable system therefore exhibits finite-time free-energy amplification and a signed cumulative particle-transport operator, while energy and positive-transport optimization select different initial directions.

## 3. Resolution comparison K=32,64,96

Across the three preregistered resolutions and all six horizons, the largest observed pairwise discrepancies are approximately

```text
G_E:          3.4e-13 absolute
G_Gamma,+:    1.5e-13 absolute
G_Gamma,-:    1.2e-15 absolute
Delta_Gamma:  2.1e-14 absolute
theta:        3.9e-12 degrees
phi fractions: < 2e-14
phase metrics: < 2e-14 rad
```

For the optimizer vectors themselves, the `K=96` optimizers were projected onto the common `|m|<=32` subspace before comparison with `K=32`.  For every horizon and for both optimizer families,

```math
\frac{|\langle P_{32}w_{96},w_{32}\rangle|}
{\|P_{32}w_{96}\|\,\|w_{32}\|}
=1
```

to floating-point precision, and the `K=96` energy outside `|m|<=32` is below approximately `2e-15`.  The separation is therefore not an artifact of comparing raw vectors of different dimension.

## 4. Fourier structure of the optimizers

Define the whitened radial-mode weight

```math
p_m(w)=|w_{\phi,m}|^2+|w_{\eta,m}|^2,\qquad \sum_m p_m=1.
```

Representative dominant modes at `K=64` are:

| T | energy-optimal dominant m | transport-optimal dominant m |
|---:|:---|:---|
| 0.25 | ±1, ±2, 0 | 0 overwhelmingly |
| 0.5 | ±1, ±2, 0 | 0, then ±1 |
| 1 | ±2, ±1, ±3 | 0, then ±1 |
| 2 | ±2, ±3, ±1 | 0 and ±1, then ±2 |
| 4 | ±3, ±4, ±2 | ±2, ±3, ±1 |
| 8 | ±6, ±5, ±7 | ±4, ±5, ±3 |

Selected weights illustrate the distinction.  At `T=1`, the energy optimizer has about `0.17584` on each of `m=±2`, while the transport optimizer has about `0.62772` at `m=0` and `0.16765` on each of `m=±1`.  At `T=8`, the energy optimizer is centered around `|m|=6`, whereas the transport optimizer is centered around `|m|=4-5`.

These distributions are identical across `K=32,64,96` to numerical precision in the retained common modes.

## 5. phi/eta structure and phase structure

The whitened potential fraction

```math
f_\phi(w)=\sum_m |w_{\phi,m}|^2
```

is:

| T | f_phi energy | f_phi transport |
|---:|---:|---:|
| 0.25 | 0.794525 | 0.556998 |
| 0.5 | 0.807310 | 0.603069 |
| 1 | 0.827660 | 0.669590 |
| 2 | 0.859830 | 0.754212 |
| 4 | 0.913538 | 0.853136 |
| 8 | 0.969082 | 0.947423 |

For a dimension-robust global phase diagnostic, define from the physical optimizer `u=M^{-1/2}w`

```math
c_{\phi\eta}=
\frac{\eta^\dagger\phi}{\|\eta\|\,\|\phi\|},
\qquad
\delta_{\phi\eta}=\arg c_{\phi\eta}.
```

The phases are:

| T | delta_phi-eta energy | delta_phi-eta transport |
|---:|---:|---:|
| 0.25 | 0.422376 rad | 1.550526 rad |
| 0.5 | 0.379601 rad | 1.491227 rad |
| 1 | 0.305805 rad | 1.279332 rad |
| 2 | 0.220594 rad | 0.809558 rad |
| 4 | 0.136615 rad | 0.325111 rad |
| 8 | 0.054186 rad | 0.092599 rad |

The corresponding coherence magnitudes remain high (`|c|>0.97` for the energy optimizer and `|c|>0.96` for the transport optimizer), so the phase difference is a meaningful structural diagnostic rather than a phase of a nearly vanishing cross-correlation.

## 6. Direct trajectories

Direct propagation was performed for the least-damped modal direction, the energy-optimal direction, and the positive-transport-optimal direction.  All initial conditions were normalized to unit physical energy cost.

A representative `K=64` summary is:

| T | family | E(T) | Gamma(0) | Gamma(T) | J_Gamma(T) |
|---:|:---|---:|---:|---:|---:|
| 0.25 | modal | 0.993331 | 0.101219 | 0.100544 | 0.025220 |
|  | energy | 1.174740 | 0.103006 | 0.154410 | 0.032164 |
|  | transport | 0.874935 | 0.492525 | 0.389763 | 0.110347 |
| 0.5 | modal | 0.986707 | 0.101219 | 0.099874 | 0.050273 |
|  | energy | 1.377608 | 0.087942 | 0.196234 | 0.070796 |
|  | transport | 0.915521 | 0.470562 | 0.324792 | 0.198692 |
| 1 | modal | 0.973591 | 0.101219 | 0.098546 | 0.099877 |
|  | energy | 1.878276 | 0.063191 | 0.297483 | 0.175225 |
|  | transport | 1.230948 | 0.392026 | 0.317388 | 0.353517 |
| 2 | modal | 0.947880 | 0.101219 | 0.095944 | 0.197116 |
|  | energy | 3.371659 | 0.035732 | 0.590283 | 0.545051 |
|  | transport | 2.491950 | 0.222037 | 0.551651 | 0.769879 |
| 4 | modal | 0.898477 | 0.101219 | 0.090943 | 0.383959 |
|  | energy | 9.411746 | 0.012883 | 1.692620 | 2.349797 |
|  | transport | 7.933604 | 0.054759 | 1.555477 | 2.762738 |
| 8 | modal | 0.807261 | 0.101219 | 0.081710 | 0.728937 |
|  | energy | 39.763235 | 0.001716 | 6.495652 | 13.764759 |
|  | transport | 33.158786 | 0.005077 | 5.421335 | 16.063968 |

The leading modal trajectory decays at all horizons, as required by spectral stability.  By contrast, the optimal finite-time perturbations can display very large transient free-energy growth.  This is a property of the frozen stable operator; no parameter was retuned after observing it.

For the transport-optimal trajectory the direct trapezoidal integral of `Gamma(t)` agrees with the Gramian optimum to a worst-case absolute error below `7.1e-8` over the checked runs.

## 7. Numerical consistency checks

The execution tests verify:

- spectral abscissae against the blind stability qualification;
- Hermiticity defects before symmetrization;
- unit-cost normalization of `w_E^star` and `w_Gamma^star`;
- Rayleigh quotient versus transport eigenvalue;
- transport eigenpair residual;
- direct terminal energy versus `G_E`;
- direct time integration of `Gamma(t)` versus `G_Gamma,+`;
- modal decay in the stable system;
- common-subspace optimizer comparison across different state dimensions.

Observed maxima in the independent calculation were approximately

```text
relative Hermiticity defect K_E:       8.9e-17
relative Hermiticity defect K_Gamma:   3.7e-13
optimizer normalization error:         1.4e-15
transport Rayleigh error:              2.2e-14
transport eigen-residual:              3.2e-14
direct terminal-energy error:          7.2e-14
direct J_Gamma integration error:      7.1e-8
```

All preregistered numerical checks pass.

## 8. S0-S5 gate reading

The frozen execution gives the following gate status:

```text
S0: PASS  -- negative spectral abscissa with margin at K=32,64,96.
S1: PASS  -- finite-time free-energy amplification G_E>1 at every frozen horizon.
S2: PASS  -- signed cumulative transport: G_Gamma,-<0<G_Gamma,+ at every horizon.
S3: PASS  -- energy/transport optimizer separation remains nonzero; theta >= 28.03 deg.
S4: PASS  -- dimensionless transport gap remains nonzero; Delta_Gamma >= 0.1431, with distinct Fourier/phi-eta/phase structure.
S5: PASS  -- scalar objectives and optimizer structure are resolution-converged across K=32,64,96 and all consistency checks pass.
```

No failed gate is repaired by post-hoc parameter selection; the same blindly selected `nu_perp=0.020` is used throughout.

## 9. Frozen classification

With all six preregistered gates satisfied, Pilot 0.2 receives exactly one class:

```text
PILOT 0.2 CLASS = P2-A
```

This classification is limited to the frozen Pilot-0.2 execution.  It does not alter CORE theory, does not change `B=I`, and does not imply transport-neutral initialization because `B^H Q_Gamma B=Q_Gamma != 0` for the full-state input map.

No retuning or follow-up parameter search is performed here.

**STOP.**
