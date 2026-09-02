# D10-ZF Pilot 0.2 — Blind Stability Qualification

**Date:** 2026-09-02  
**Status:** COMPLETE; stability-only selection; STOP after qualification

## Scope lock

This qualification follows the prior commit `research/d10_zf_pilot_0_2_blind_stability_preregistration.md` exactly.

Fixed throughout:

```math
U(x)=\cos x,\qquad L_x=2\pi,\qquad k_y=1,
```

```math
C=\kappa=1,\qquad N=0,
```

with the existing physical `M`, `Q_Gamma`, and `B=I` unchanged.

The only varied parameter is the already existing uniform perpendicular damping axis

```math
A_{K,\nu}=A_{K,0}-\nu_\perp I.
```

No `K_Gamma`, `K_E`, `theta`, `Delta_Gamma`, energy optimizer, or transport optimizer was computed or inspected.

## Preregistered screen

Damping values:

```text
nu_perp = {0, 0.005, 0.010, 0.015, 0.020, 0.030, 0.050}.
```

High Fourier resolutions:

```text
K = {32, 64, 96, 128},
```

with centered modes `m=-K,...,K`.

Qualification criterion:

```math
\max_K \alpha_K(\nu_\perp)\le -5\times10^{-3}.
```

The selected value must be the smallest preregistered damping satisfying the criterion at all four resolutions.

## Undamped high-resolution spectral abscissae

| K | state dimension | alpha_K(0) |
|---:|---:|---:|
| 32 | 130 | 0.012421402071 |
| 64 | 258 | 0.006618238979 |
| 96 | 386 | 0.004507562029 |
| 128 | 514 | 0.003421875235 |

These values are consistent with the preceding Resolution & Stability Qualification 0.1.

## Damping screen

Because the allowed damping acts as a uniform scalar shift,

```math
\sigma(A_{K,\nu})=\sigma(A_{K,0})-\nu_\perp,
```

and therefore exactly

```math
\alpha_K(\nu_\perp)=\alpha_K(0)-\nu_\perp.
```

The preregistered screen gives:

| nu_perp | alpha_32 | alpha_64 | alpha_96 | alpha_128 | worst alpha | criterion |
|---:|---:|---:|---:|---:|---:|:---|
| 0.000 | 0.01242140 | 0.00661824 | 0.00450756 | 0.00342188 | 0.01242140 | FAIL |
| 0.005 | 0.00742140 | 0.00161824 | -0.00049244 | -0.00157812 | 0.00742140 | FAIL |
| 0.010 | 0.00242140 | -0.00338176 | -0.00549244 | -0.00657812 | 0.00242140 | FAIL |
| 0.015 | -0.00257860 | -0.00838176 | -0.01049244 | -0.01157812 | -0.00257860 | FAIL margin |
| 0.020 | -0.00757860 | -0.01338176 | -0.01549244 | -0.01657812 | -0.00757860 | PASS |
| 0.030 | -0.01757860 | -0.02338176 | -0.02549244 | -0.02657812 | -0.01757860 | PASS |
| 0.050 | -0.03757860 | -0.04338176 | -0.04549244 | -0.04657812 | -0.03757860 | PASS |

Thus `nu_perp=0.015` makes all four tested truncations spectrally stable, but it does **not** satisfy the preregistered safety margin because the worst case is only

```math
\alpha_{32}(0.015)=-0.00257860>-0.005.
```

The smallest preregistered value satisfying the full criterion is therefore

```math
\boxed{\nu_\perp=0.020}.
```

## Leading spectrum at the selected damping

Representative leading eigenvalues after the exact shift by `nu_perp=0.020` are:

### K = 32

```text
-0.007578597929 + 0.035285568732 i
-0.007840198694 + 0.121172675435 i
-0.008088870267 - 0.051549845180 i
-0.008898273153 + 0.206336975293 i
```

### K = 64

```text
-0.013381761021 + 0.064428643411 i
-0.013423725833 + 0.018554159776 i
-0.013478077115 + 0.110100307106 i
-0.013582302474 - 0.027491628791 i
```

### K = 96

```text
-0.015492437971 + 0.043870792757 i
-0.015495647468 + 0.075077841423 i
-0.015531840723 + 0.012588773559 i
-0.015544810925 + 0.106195588469 i
```

### K = 128

```text
-0.016578124765 + 0.056948868537 i
-0.016587328476 + 0.080599308074 i
-0.016588608208 + 0.033255102199 i
-0.016617010872 + 0.104198797503 i
```

Hence the selected point is negative at every preregistered high resolution, with the weakest tested margin

```math
-\alpha_{32}(0.020)=0.00757860>0.005.
```

## Blind Pilot-0.2 selection

The stability-only qualification therefore selects

```math
\boxed{\nu_\perp=0.020}
```

while leaving every other frozen D10-ZF quantity unchanged.

This selection was made entirely from spectrum and spectral abscissa. No CORE/transport or energy-optimizer information entered the choice.

## Final status

```text
preregistered candidate set exhausted as specified: YES
smallest value with alpha_K < 0 at all tested K: 0.015
smallest value with preregistered -0.005 safety margin at all tested K: 0.020
blind Pilot-0.2 damping selection: nu_perp = 0.020
search-set expansion: NO
other parameter variation: NO
CORE/transport evaluation: NONE
```

**STOP.**
