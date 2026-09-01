# C2 — Falsification of the zonal-flow conditioned cascade signal

**Status:** completed at pilot resolution; association gate passed, Kramers-Moyal/Pawula convergence gate failed.

**Date:** 2026-09-01

## Question

C1 found, in one transient modified-Hasegawa-Wakatani (mHW) realization, an approximately threefold reduction of the fitted finite-step diffusion intercept under strong zonal flow. C2 asks whether that signal survives four controls:

1. independent seeds and a much later analysis window;
2. radial (`x`) and poloidal (`y`) increments kept separate;
3. original HW as a control for the Numata `ky=0` coupling modification;
4. finite-step `D1`, `D2`, `D4` over progressively smaller scale steps, with a Pawula-oriented extrapolation.

The purpose is falsification, not parameter optimization.

## Numerical ensemble

Both models use the same `32 x 32`, `L=40`, `alpha=kappa=1`,
`D_zeta=D_n=0.02`, `dt=0.05` setup. Seeds `0,1,2,3` are integrated
independently from `t=0` to `t=500`. Only `380 <= t <= 490` is analyzed.

The mHW model removes `alpha(phi-n)` from `ky=0`; the original-HW control keeps
that coupling on the zonal modes.

Mean zonal kinetic-energy fractions in the analysis window are

| seed | mHW | HW |
|---:|---:|---:|
| 0 | 0.93080 | 0.05864 |
| 1 | 0.95111 | 0.04578 |
| 2 | 0.95755 | 0.04193 |
| 3 | 0.90398 | 0.04823 |

Thus the control produces the intended strong separation in zonal organization.
The mHW zonal fraction itself is near a plateau, although the residual nonzonal
energy still has seed-dependent slow trends. The window is therefore better
described as **late/quasi-stationary**, not as a rigorously stationary ensemble.

## Direction-resolved within-mHW test

Each mHW seed is split at its own median zonal fraction inside the late window.
For the `4 dx -> 2 dx` step, low/high groups share the same normalization within
that seed. The fitted form remains

\[
D^{(1)}(u)\simeq a_1u+a_3u^3,\qquad
D^{(2)}(u)\simeq b_0+b_2u^2.
\]

Uncertainty below is a seed-level bootstrap of the mean across the four
independent realizations (`20,000` resamples). With only four seeds this is a
pilot uncertainty estimate, not a publication-grade confidence interval.

### Diffusion signal

| direction | mean `b0(high)/b0(low)` | bootstrap 95% interval |
|---|---:|---:|
| x / radial | 0.80188 | [0.71009, 0.89366] |
| y / poloidal | 0.86447 | [0.84857, 0.88448] |

Every seed has `b0(high) < b0(low)` in both directions. The C1 effect is therefore
smaller than the transient single-run estimate but survives independent seeds
and direction separation.

For the drift coefficient the mean high-minus-low change in `a1` is

- x: `+0.00058`, bootstrap interval `[-0.00995, +0.00666]`;
- y: `-0.00825`, bootstrap interval `[-0.01414, -0.00236]`.

The dominant robust change is still in the diffusion-like term, not in the
radial drift fit.

## The Markov-improvement hypothesis does not survive

C1 suggested that strong zonal flow might also make the scale process more
Markovian. Direction separation shows that this is not robust.

For the Chapman-Kolmogorov total-variation error, high minus low ZF gives

| direction/triplet | mean change | bootstrap 95% interval |
|---|---:|---:|
| x, 8-4-2 | -0.00306 | [-0.00745, +0.00452] |
| x, 4-2-1 | -0.00213 | [-0.00488, +0.00061] |
| y, 8-4-2 | **+0.01341** | [+0.00366, +0.02119] |
| y, 4-2-1 | -0.00513 | [-0.01066, +0.00039] |

The radial changes are consistent with zero at this seed count, while the
poloidal `8-4-2` error becomes worse at higher zonal fraction. Therefore:

> **C2 falsifies the general claim that stronger zonal flow improves Markov
> closure of the spatial-increment process.**

Markov closure must be treated as scale- and direction-dependent and remains a
gate to be established, not an observed consequence of zonal flow.

## Original-HW control: diffusion suppression survives self-normalization

To distinguish a mere amplitude reduction from a change of scale-transition
statistics, each model/seed/direction is normalized by its own `r=8 dx`
standard deviation before fitting finite-step coefficients.

Even after that self-normalization the mHW diffusion intercept is lower than HW.

| step | x: mHW/HW `b0` | 95% interval | y: mHW/HW `b0` | 95% interval |
|---|---:|---:|---:|---:|
| 8 -> 7 | 0.70686 | [0.67239, 0.73490] | 0.52698 | [0.48195, 0.57200] |
| 8 -> 4 | 0.73844 | [0.64518, 0.83361] | 0.61841 | [0.57258, 0.68577] |

This is the strongest C2 result. mHW also has much smaller raw increment
amplitudes, but the lower normalized `b0` means the difference is not exhausted
by that amplitude suppression.

The physically conservative interpretation is:

\[
\boxed{\text{strong zonal organization is associated with reduced
finite-step stochastic spreading of the nonzonal scale process}}
\]

at this benchmark resolution.

This is an association statement. Because HW and mHW differ in their equations,
the control does not by itself isolate a causal `ZF -> D2` mechanism.

## Small-delta-s / Pawula gate

At fixed current separation `r=8 dx`, the next separation is varied over

\[
r' = 7,6,5,4\;dx,\qquad
\Delta s=\ln(8/r'),
\]

so the smallest tested step is

\[
\Delta s_{\min}=\ln(8/7)\simeq0.1335.
\]

The mean fitted diffusion intercepts are

| model/direction | 8->7 | 8->6 | 8->5 | 8->4 |
|---|---:|---:|---:|---:|
| mHW x | 0.52627 | 0.66145 | 0.55804 | 0.41018 |
| mHW y | 0.51473 | 0.65760 | 0.61463 | 0.45771 |
| HW x | 0.74600 | 0.92691 | 0.77099 | 0.55781 |
| HW y | 0.98276 | 1.21100 | 1.01931 | 0.74598 |

`D2` is clearly not step-independent over this range.

Using

\[
D^{(4)}_{\Delta s}(u)=
\frac{\langle(\Delta u)^4\mid u\rangle}{24\,\Delta s}
\]

and fitting its constant part as `c0`, the values decrease strongly at the
smallest step but a simple linear extrapolation in `delta_s` gives nonzero
intercepts:

| case | extrapolated `c0(delta_s -> 0)` | seed-bootstrap 95% interval |
|---|---:|---:|
| mHW x | 0.03186 | [0.02945, 0.03426] |
| mHW y | 0.02196 | [0.01266, 0.03125] |
| HW x | 0.05968 | [0.05430, 0.06444] |
| HW y | 0.09816 | [0.08597, 0.11034] |

A linear extrapolation over four discrete grid separations is itself only a
diagnostic. The correct conclusion is not that a genuine fourth KM coefficient
has been measured; it is that the present data **do not justify the Pawula/Fokker-
Planck truncation**.

## C2 gate decision

### Passed

- the C1 diffusion modulation survives four independent mHW seeds;
- it survives explicit separation of radial and poloidal increments;
- it is weaker but still present when comparing high/low ZF states inside the
  late mHW regime;
- mHW has lower finite-step `b0` than original HW even after each model is
  normalized by its own increment amplitude.

### Falsified / not supported

- a general claim that stronger ZF makes the scale process more Markovian;
- the original single-run factor-of-three magnitude as a stationary estimate.

### Failed gate

- converged `delta_s -> 0` Kramers-Moyal coefficients;
- Pawula justification for a Fokker-Planck description at `32 x 32`.

## Consequence for the research program

The hypothesis should now be narrowed from

`zonal flow makes the cascade more Markovian and reduces diffusion`

to

> **Zonal organization changes the finite-scale transition kernel, with the
> most reproducible signature appearing in its second conditional moment.
> Whether a genuine Markov-in-scale diffusion limit exists remains unresolved.**

This is a stronger scientific position because one part of the original
interpretation has survived and one part has been falsified.

## Next gate before GENE

Do **not** transfer the Fokker-Planck claim to GENE yet. The next package should
be a resolution/observable gate:

1. repeat the same ensemble logic at higher spatial resolution;
2. test whether `D2` develops a plateau as `delta_s -> 0`;
3. test whether the finite-step `D4` intercept moves toward zero with resolution;
4. compare raw increments with filtered/wavelet scale variables that may provide
   a better separated scale coordinate;
5. retain x/y anisotropy throughout;
6. only if the Markov/Pawula gate passes, promote `D1,D2` to genuine
   Kramers-Moyal coefficients and map the definitions to gyrokinetic data.

Until then, the robust object is the **ZF-conditioned finite-scale transition
kernel**, not yet a Fokker-Planck cascade.
