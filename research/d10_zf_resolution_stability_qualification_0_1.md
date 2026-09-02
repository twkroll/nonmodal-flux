# D10-ZF Resolution & Stability Qualification 0.1

**Date:** 2026-09-02  
**Status:** COMPLETE; no CORE/transport optimization performed.

## Scope lock

This qualification keeps the frozen Pilot-0.1 physics unchanged:

```math
U(x)=\cos x,\qquad L_x=2\pi,\qquad k_y=1,
```

```math
C=1,\qquad \kappa=1,\qquad N(x)=0,\qquad \nu_\perp=0.
```

Only the centered consecutive Fourier-Galerkin truncation is varied,

```math
m=-K,\ldots,K,
```

with state dimension

```math
N=2(2K+1)=4K+2.
```

The profile coefficients remain exactly `u_{-1}=u_{+1}=1/2`, and `k_0=2\pi/L_x=1`.

No `K_Gamma(T)`, `K_E(T)`, `theta(T)`, `Delta_Gamma(T)`, transport optimizer, or energy optimizer is computed or inspected in this qualification.

## Numerical procedure

For each centered truncation, assemble the already validated D10-ZF generator `A_K` with `hasegawa_wakatani_zonal_flow_matrices`, compute its eigenvalues, and define

```math
\alpha_K=\max_{\lambda\in\sigma(A_K)}\operatorname{Re}\lambda.
```

The natural family is sampled consecutively for `K=1,...,40`.  Additional tail checkpoints `K=60,80,100,120` are used only to determine whether the positive growth-rate envelope settles to a positive value or continues to collapse with resolution.  No physical parameter is varied.

## Spectral-abscissa results

Selected values are:

| K | state dimension N | alpha(A_K) |
|---:|---:|---:|
| 1 | 6 | 0.080363511232 |
| 2 | 10 | 0.067509765635 |
| 3 | 14 | 0.063151083339 |
| 4 | 18 | 0.051352742830 |
| 5 | 22 | 0.048955020567 |
| 6 | 26 | 0.042503928116 |
| 8 | 34 | 0.036064067055 |
| 10 | 42 | 0.031248196391 |
| 12 | 50 | 0.027531179766 |
| 16 | 66 | 0.022195160649 |
| 20 | 82 | 0.018565580415 |
| 24 | 98 | 0.015944552408 |
| 28 | 114 | 0.013966187092 |
| 32 | 130 | 0.012421402071 |
| 36 | 146 | 0.011182477584 |
| 40 | 162 | 0.010167156919 |
| 60 | 242 | 0.007025905909 |
| 80 | 322 | 0.005365699885 |
| 100 | 402 | 0.004334058340 |
| 120 | 482 | 0.003641659925 |

Across every consecutive truncation `K=1,...,120` checked in the qualification, `alpha_K` remains positive and decreases monotonically.

However, it does **not** settle to a positive value.  In the tail,

```text
K alpha_K
40  0.4066863
60  0.4215544
80  0.4292560
100 0.4334058
120 0.4369992
```

which is numerically consistent with an approximately `O(1/K)` collapse.  A simple tail fit over `K=20,...,120` of the form

```math
\alpha_K\approx a_0+\frac{a_1}{K}+\frac{a_2}{K^2}
```

gives `a_0 approximately 7.6e-5`, i.e. an intercept numerically compatible with zero on the scale of the finite-resolution values.  This fit is only a convergence diagnostic, not a theorem about the infinite-dimensional spectrum.

## Leading eigenvalues

Sorting eigenvalues by decreasing real part gives the following representative leading triples.

### K = 1, N = 6

```text
0.0803635112 + 0.0295198586 i
0.0608944633 - 0.3083015254 i
0.0389925259 - 0.8187469847 i
```

### K = 8, N = 34

```text
0.0360640671 + 0.1107021446 i
0.0337979233 - 0.1520375602 i
0.0257096775 + 0.3669096637 i
```

### K = 16, N = 66

```text
0.0221951606 + 0.0644254922 i
0.0208732416 - 0.0919277343 i
0.0196312913 + 0.2171715413 i
```

### K = 32, N = 130

```text
0.0124214021 + 0.0352855687 i
0.0121598013 + 0.1211726754 i
0.0119111297 - 0.0515498452 i
```

### K = 60, N = 242

```text
0.0070259059 + 0.0684356986 i
0.0069880515 + 0.0197226086 i
0.0068981221 + 0.1169140329 i
```

### K = 80, N = 322

```text
0.0053656999 + 0.0522000281 i
0.0053371902 + 0.0892811268 i
0.0053213169 + 0.0149999622 i
```

### K = 100, N = 402

```text
0.0043340583 + 0.0722054148 i
0.0043338636 + 0.0421876440 i
0.0042959284 + 0.0121024408 i
```

### K = 120, N = 482

```text
0.0036416599 + 0.0606083964 i
0.0036325808 + 0.0353966185 i
0.0036268558 + 0.0857689824 i
```

The ordering of the imaginary parts changes with `K`, so a single eigenvalue branch should not be identified merely by sorting at each truncation.  What is robust in this qualification is the real-part envelope: the first several leading real parts collapse toward zero together as resolution increases.

For the checked family there are positive-real-part eigenvalues at every finite `K`; for example the count is `3,5,7,...` for `K=1,2,3,...`.  This finite-truncation positivity alone is therefore not evidence for a converged positive instability growth rate.

## Qualification answers

### 1. Is the Pilot-0.1 instability resolution robust?

**Not as a finite positive growth rate.**

The six-state Pilot 0.1 value

```math
\alpha_1=0.0803635
```

shrinks continuously under the same physical model and centered Galerkin family to

```math
\alpha_{120}=0.00364166.
```

Thus the original magnitude and the statement of a clearly positive converged growth rate are not resolution robust.  Every finite truncation checked remains weakly positive, but the positive envelope collapses with increasing `K`.

### 2. Does alpha(A_N) converge?

The numerical evidence is consistent with

```math
\alpha(A_N)\to0^+
```

rather than convergence to a positive constant.  This is a numerical resolution conclusion only.  It does not establish the exact spectrum of the untruncated continuous operator.

Accordingly Pilot Interpretation 0.1 must be refined in one precise way: the `K=1` frozen pilot **does fail its own spectral-stability gate**, but this qualification does not support interpreting its growth rate as a resolution-converged physical modal instability.

### 3. Minimal physical parameter axis for a later stability-constrained Pilot 0.2

The trigger for selecting such an axis was: **only if the instability remains robustly positive under resolution.**  That trigger is not met.

Therefore this qualification deliberately selects **no parameter axis** and performs no parameter search.  Choosing an amplitude, `C`, `kappa`, or damping axis now would mix a resolution issue with a new physical calibration decision before the spectral limit has been cleanly qualified.

## Final qualification

```text
finite-K positivity:          YES
positive converged alpha:     NOT SUPPORTED
resolution trend:             alpha_K -> 0+ numerically
Pilot-0.1 K=1 gate verdict:   still FAIL at its frozen truncation
robust physical instability:  NOT ESTABLISHED
Pilot-0.2 parameter axis:      NOT TRIGGERED / NOT SELECTED
```

No retuning and no CORE/transport optimization was performed.

**STOP.**
