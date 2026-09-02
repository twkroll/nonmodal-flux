# D10-ZF Pilot Execution 0.1 — frozen point, no retuning

**Date:** 2026-09-02  
**Status:** EXECUTED; overall preregistered pilot verdict = **FAILURE** because the frozen operator is spectrally unstable. No parameter, input map, observable, damping, or horizon was changed.

## Scope lock

Execution uses exactly `research/d10_zf_pilot_0_1_specification.md`: `U(x)=cos x`, `L_x=2*pi`, `ky=C=kappa=1`, modes `(-1,0,1)`, no additional damping, `B=I_6`, `R_in=M`, and horizons `T={0.25,0.5,1,2,4,8}`. No parameter optimization or post-hoc retuning is performed.

For the full-state natural normalization,

```math
K_E(T)=M^{-1/2}e^{A^\dagger T}Me^{AT}M^{-1/2},
\qquad
K_\Gamma(T)=M^{-1/2}P_\Gamma(T)M^{-1/2},
\quad
P_\Gamma(T)=\int_0^T e^{A^\dagger t}Q_\Gamma e^{At}\,dt.
```

The positive transport optimizer is the top eigenvector of `K_Gamma`; the energy optimizer is the top eigenvector of `K_E`. Physical input vectors below are reconstructed and normalized to `u^H M u=1`. Their arbitrary complex phase is fixed only for printing.

The optimizer angle is

```math
\vartheta(T)=\arccos\left(|(u_E^\star)^\dagger M u_\Gamma^\star|\right),
```

and the transport advantage reported here is

```math
\Delta_\Gamma(T)=J_\Gamma(T;u_\Gamma^\star)-J_\Gamma(T;u_E^\star)
=\mathcal G_{\Gamma,+}(T)-J_\Gamma(T;u_E^\star).
```

## 1. Spectrum

Eigenvalues sorted by decreasing real part:

1. `0.0803635112+0.0295198586i`
2. `0.0608944633-0.3083015254i`
3. `0.0389925259-0.8187469847i`
4. `-1.5608944633+0.3083015254i`
5. `-1.7577783738-0.0119434095i`
6. `-1.8615776633+0.8011705356i`

Therefore the spectral abscissa is `alpha(A) = 0.080363511232 > 0`. There are three eigenvalues with positive real part. The frozen Pilot 0.1 is **not spectrally stable/subcritical**.

The modal baseline is the eigenvector belonging to the spectral-abscissa eigenvalue, M-normalized:

```text
u_modal = [-0.24275872-0.05577107i, 0.47367389+0.21175830i, -0.24275872-0.05577107i, -0.27848390-0.07906739i, 0.56125997, -0.27848390-0.07906739i]
```

## 2. Finite-horizon energy and signed cumulative transport

| T | G_E,max | G_Gamma,- | G_Gamma,+ | J_Gamma(u_E*) | Delta_Gamma | Delta/G+ | theta [deg] |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.25 | 1.132542007 | -0.087746005 | 0.110876586 | 0.049932150 | 0.060944436 | 0.549660 | 46.223981 |
| 0.5 | 1.278912497 | -0.127624858 | 0.200464157 | 0.106467263 | 0.093996894 | 0.468896 | 41.547300 |
| 1 | 1.606778373 | -0.147602619 | 0.356794735 | 0.242189531 | 0.114605204 | 0.321208 | 33.832873 |
| 2 | 2.371872784 | -0.135417955 | 0.730104586 | 0.614251483 | 0.115853103 | 0.158680 | 26.052467 |
| 4 | 3.743613923 | -0.110427851 | 1.858139513 | 1.648739759 | 0.209399754 | 0.112693 | 23.119706 |
| 8 | 4.046988701 | -0.079051286 | 3.810891981 | 2.369928413 | 1.440963568 | 0.378117 | 58.483216 |

All six horizons have both negative and positive cumulative-transport branches. The energy and positive-transport optimizers are distinct at every preregistered horizon. This does not override the spectral-stability failure.

## 3. Physical optimizers

### T = 0.25

```text
u_E*     = [0.00584820+0.29198821i, 0.55335687, 0.00584820+0.29198821i, 0.11813687+0.24520709i, 0.40798784-0.19496447i, 0.11813687+0.24520709i]
u_Gamma* = [0.00754166+0.04932286i, 0.73968814, 0.00754166+0.04932286i, 0.08461146-0.00891472i, 0.01299679-0.65441341i, 0.08461146-0.00891472i]
```

### T = 0.5

```text
u_E*     = [0.00961187+0.30510520i, 0.54153306, 0.00961187+0.30510520i, 0.12195850+0.26471258i, 0.37011927-0.16472441i, 0.12195850+0.26471258i]
u_Gamma* = [0.03000345+0.10514264i, 0.74535004, 0.03000345+0.10514264i, 0.15925184-0.02801665i, 0.04564322-0.58502745i, 0.15925184-0.02801665i]
```

### T = 1

```text
u_E*     = [0.01357176+0.33225625i, 0.49797664, 0.01357176+0.33225625i, 0.12513629+0.29602355i, 0.30142165-0.11078152i, 0.12513629+0.29602355i]
u_Gamma* = [0.09778567+0.19778909i, 0.68784931, 0.09778567+0.19778909i, 0.25436388-0.05261019i, 0.13283812-0.42373279i, 0.25436388-0.05261019i]
```

### T = 2

```text
u_E*     = [0.38001534, 0.01961993-0.36831973i, 0.38001534, 0.33876878-0.10963152i, -0.02561870-0.17912558i, 0.33876878-0.10963152i]
u_Gamma* = [0.18686573+0.26665390i, 0.54316006, 0.18686573+0.26665390i, 0.30126528+0.01223359i, 0.23846829-0.20541848i, 0.30126528+0.01223359i]
```

### T = 4

```text
u_E*     = [0.42409346, -0.01119003-0.07899983i, 0.42409346, 0.35287696-0.09203970i, 0.05442996+0.07254801i, 0.35287696-0.09203970i]
u_Gamma* = [0.39106753, 0.24286533-0.22543335i, 0.39106753, 0.30201991-0.15949562i, 0.14869877-0.15178896i, 0.30201991-0.15949562i]
```

### T = 8

```text
u_E*     = [-0.28779648+0.18249996i, 0.50114362, -0.28779648+0.18249996i, -0.15004620+0.24102852i, 0.28102962-0.21006670i, -0.15004620+0.24102852i]
u_Gamma* = [0.39128212, 0.27583747-0.01224977i, 0.39128212, 0.32622844-0.09860542i, 0.28117589-0.00094971i, 0.32622844-0.09860542i]
```

## 4. Full whitened cumulative transport matrices K_Gamma(T)

### T = 0.25

```text
[             0.012848   0.000345+0.000981i              0.000059   0.000729+0.073866i   0.000230+0.000099i   0.000006+0.000158i ]
[  0.000345-0.000981i              0.022717   0.000345-0.000981i   0.005667-0.000070i   0.001814+0.097927i   0.005667-0.000070i ]
[             0.000059   0.000345+0.000981i              0.012848   0.000006+0.000158i   0.000230+0.000099i   0.000729+0.073866i ]
[  0.000729-0.073866i   0.005667+0.000070i   0.000006-0.000158i              0.000061   0.000460+0.000011i              0.000001 ]
[  0.000230-0.000099i   0.001814-0.097927i   0.000230-0.000099i   0.000460-0.000011i              0.000219   0.000460-0.000011i ]
[  0.000006-0.000158i   0.005667+0.000070i   0.000729-0.073866i              0.000001   0.000460+0.000011i              0.000061 ]
```

### T = 0.5

```text
[             0.043222   0.002154+0.005719i              0.000695   0.004748+0.125276i   0.001687+0.001110i   0.000132+0.000862i ]
[  0.002154-0.005719i              0.067926   0.002154-0.005719i   0.016876-0.000784i   0.010371+0.155717i   0.016876-0.000784i ]
[             0.000695   0.002154+0.005719i              0.043222   0.000132+0.000862i   0.001687+0.001110i   0.004748+0.125276i ]
[  0.004748-0.125276i   0.016876+0.000784i   0.000132-0.000862i              0.000767   0.002671+0.000228i              0.000033 ]
[  0.001687-0.001110i   0.010371-0.155717i   0.001687-0.001110i   0.002671-0.000228i              0.002390   0.002671-0.000228i ]
[  0.000132-0.000862i   0.016876+0.000784i   0.004748-0.125276i              0.000033   0.002671+0.000228i              0.000767 ]
```

### T = 1

```text
[             0.129297   0.011499+0.026114i              0.006532   0.026837+0.187294i   0.010164+0.009116i   0.002291+0.003275i ]
[  0.011499-0.026114i              0.164308   0.011499-0.026114i   0.040917-0.006698i   0.045390+0.208793i   0.040917-0.006698i ]
[             0.006532   0.011499+0.026114i              0.129297   0.002291+0.003275i   0.010164+0.009116i   0.026837+0.187294i ]
[  0.026837-0.187294i   0.040917+0.006698i   0.002291-0.003275i              0.007943   0.012125+0.003286i              0.000999 ]
[  0.010164-0.009116i   0.045390-0.208793i   0.010164-0.009116i   0.012125-0.003286i              0.018373   0.012125-0.003286i ]
[  0.002291-0.003275i   0.040917+0.006698i   0.026837-0.187294i              0.000999   0.012125+0.003286i              0.007943 ]
```

### T = 2

```text
[             0.345246   0.049660+0.087920i              0.047319   0.126485+0.243203i   0.042972+0.044289i   0.026091+0.008843i ]
[  0.049660-0.087920i              0.312809   0.049660-0.087920i   0.086117-0.036958i   0.135228+0.238834i   0.086117-0.036958i ]
[             0.047319   0.049660+0.087920i              0.345246   0.026091+0.008843i   0.042972+0.044289i   0.126485+0.243203i ]
[  0.126485-0.243203i   0.086117+0.036958i   0.026091-0.008843i              0.060843   0.041439+0.023058i              0.016141 ]
[  0.042972-0.044289i   0.135228-0.238834i   0.042972-0.044289i   0.041439-0.023058i              0.079711   0.041439-0.023058i ]
[  0.026091-0.008843i   0.086117+0.036958i   0.126485-0.243203i              0.016141   0.041439+0.023058i              0.060843 ]
```

### T = 4

```text
[             0.935851   0.155626+0.177289i              0.265552   0.482236+0.330490i   0.157040+0.062906i   0.162711+0.031655i ]
[  0.155626-0.177289i              0.493827   0.155626-0.177289i   0.176887-0.085990i   0.273175+0.258042i   0.176887-0.085990i ]
[             0.265552   0.155626+0.177289i              0.935851   0.162711+0.031655i   0.157040+0.062906i   0.482236+0.330490i ]
[  0.482236-0.330490i   0.176887+0.085990i   0.162711-0.031655i              0.290037   0.121734+0.030173i              0.105564 ]
[  0.157040-0.062906i   0.273175-0.258042i   0.157040-0.062906i   0.121734-0.030173i              0.205245   0.121734-0.030173i ]
[  0.162711-0.031655i   0.176887+0.085990i   0.482236-0.330490i              0.105564   0.121734+0.030173i              0.290037 ]
```

### T = 8

```text
[             2.139685   0.248496+0.065443i              0.420513   1.201130+0.500427i   0.366016-0.145533i   0.236995+0.014756i ]
[  0.248496-0.065443i              1.242977   0.248496-0.065443i   0.291086-0.059660i   0.905809+0.491369i   0.291086-0.059660i ]
[             0.420513   0.248496+0.065443i              2.139685   0.236995+0.014756i   0.366016-0.145533i   1.201130+0.500427i ]
[  1.201130-0.500427i   0.291086+0.059660i   0.236995-0.014756i              0.755617   0.262188-0.052835i              0.141704 ]
[  0.366016+0.145533i   0.905809-0.491369i   0.366016+0.145533i   0.262188+0.052835i              0.857590   0.262188+0.052835i ]
[  0.236995-0.014756i   0.291086+0.059660i   1.201130-0.500427i              0.141704   0.262188-0.052835i              0.755617 ]
```

## 5. Direct trajectory summary

Physical free energy is `E(t)=0.5*x(t)^H M x(t)`. All displayed initial vectors have `u^H M u=1`, hence `E(0)=0.5`. `J_Gamma(T)` is checked both from the Gramian and by direct time integration of `Gamma(t)`.

| T | trajectory | E(T)/E(0) | Gamma(0) | Gamma(T) | min Gamma | max Gamma | J_Gamma(T) |
|---:|:---|---:|---:|---:|---:|---:|---:|
| 0.25 | modal | 1.040999965 | 0.111525548 | 0.116098091 | 0.111525548 | 0.116098091 | 0.028449127 |
| 0.25 | energy | 1.132542007 | 0.174006039 | 0.223140460 | 0.174006039 | 0.223140460 | 0.049932150 |
| 0.25 | transport | 0.883553707 | 0.492542860 | 0.393646805 | 0.393646805 | 0.492542860 | 0.110876586 |
| 0.5 | modal | 1.083680940 | 0.111525548 | 0.120857829 | 0.111525548 | 0.120857829 | 0.058064878 |
| 0.5 | energy | 1.278912497 | 0.158535136 | 0.258750282 | 0.158535136 | 0.258750282 | 0.106467263 |
| 0.5 | transport | 0.930315922 | 0.471219677 | 0.330440551 | 0.330440551 | 0.471219677 | 0.200464157 |
| 1 | modal | 1.174363670 | 0.111525548 | 0.130971764 | 0.111525548 | 0.130971764 | 0.120988229 |
| 1 | energy | 1.606778373 | 0.130286135 | 0.329129637 | 0.130286135 | 0.329129637 | 0.242189531 |
| 1 | transport | 1.216406322 | 0.402374409 | 0.314176518 | 0.314176518 | 0.402374409 | 0.356794735 |
| 2 | modal | 1.379132148 | 0.111525548 | 0.153807540 | 0.111525548 | 0.153807540 | 0.263073405 |
| 2 | energy | 2.371872784 | 0.096274338 | 0.473416356 | 0.096274338 | 0.473416356 | 0.614251483 |
| 2 | transport | 2.002023122 | 0.267669821 | 0.445578751 | 0.267669821 | 0.445578751 | 0.730104586 |
| 4 | modal | 1.902004400 | 0.111525548 | 0.212122327 | 0.111525548 | 0.212122327 | 0.625883670 |
| 4 | energy | 3.743613923 | 0.074579453 | 0.663879524 | 0.074579453 | 0.663879524 | 1.648739759 |
| 4 | transport | 3.281942067 | 0.128090366 | 0.630611727 | 0.128090366 | 0.640935311 | 1.858139513 |
| 8 | modal | 3.617619040 | 0.111525548 | 0.403457332 | 0.111525548 | 0.403457332 | 1.816318045 |
| 8 | energy | 4.046988701 | 0.189240970 | 0.485494926 | 0.189240970 | 0.485494926 | 2.369928413 |
| 8 | transport | 2.546328021 | 0.073983481 | 0.460479880 | 0.073983481 | 0.683562153 | 3.810891981 |

For all three displayed positive-oriented trajectories, `Gamma(t)` remains positive on the sampled interval, so `J_Gamma(t)` is monotone increasing. The energy-optimal trajectory attains the tabulated terminal free-energy gain by construction; the transport-optimal trajectory attains `G_Gamma,+` by construction. The modal trajectory grows exponentially because its eigenvalue has positive real part.

The downsampled direct time series (`E(t)`, `Gamma(t)`, and trapezoidal `J_Gamma(t)`) for every horizon and trajectory family are stored in `research/d10_zf_pilot_execution_0_1_trajectories.csv`.

## 6. Numerical consistency checks

The execution was checked without changing the matrices or symmetrizing away defects:

- max Frobenius Hermiticity defect of `K_E(T)`: `1.446e-16`;
- max absolute / relative Hermiticity defect of `K_Gamma(T)`: `4.276e-10` / `8.799e-11`;
- max M-normalization error of reconstructed optimizers: `4.441e-16`;
- max direct terminal-energy vs eigenvalue mismatch: `8.882e-15`;
- max positive transport Rayleigh mismatch: `5.773e-15`;
- max negative transport Rayleigh mismatch: `3.331e-16`;
- max positive transport eigen-residual: `1.134e-10`;
- max direct-trajectory trapezoidal `J_Gamma(T)` error over all modal/energy/transport trajectories: `5.672e-08`;
- max relative Van-Loan Gramian vs independent Lyapunov-ODE integration mismatch: `4.791e-11`.

These checks are numerically consistent with the preregistered execution tolerances; the largest loss of raw Hermiticity occurs at `T=8` from the finite-horizon block exponential but remains below `1e-9` relative.

## 7. Preregistered Success / Failure evaluation

### Overall verdict: FAILURE

The current coupled-pilot gate requires a spectrally stable/subcritical frozen point before optimizer differences are interpreted as the intended nonmodal benchmark. The execution gives

```math
\alpha(A)=0.080363511232>0,
```

so Pilot 0.1 fails that mandatory condition. No retuning is performed.

Secondary diagnostics are nontrivial but do not rescue the gate:

- `G_E,max(T)>1` at every registered horizon;
- `G_Gamma,-(T)<0<G_Gamma,+(T)` at every horizon;
- `Delta_Gamma(T)>0` at every horizon;
- `vartheta(T)` ranges from about `23.12 deg` to `58.48 deg`;
- direct trajectories and quadratic operators agree within the reported numerical errors.

Because spectral instability is already a preregistered failure condition for this benchmark role, these separation results are recorded only as diagnostics of the failed frozen point, not as a successful pilot claim.

## STOP

No parameter, damping, `B`, `Q_Gamma`, horizon, truncation, or theory statement is changed after observing the result. No parameter search or follow-on branch is opened in this execution package.