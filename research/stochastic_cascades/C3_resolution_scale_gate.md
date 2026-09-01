# C3 — Resolution and scale-coordinate gate

**Status:** completed as a falsification/selection gate on the exploratory stochastic-cascade branch.

**Date:** 2026-09-01

## Question

C2 left two possible explanations for the failure of the Pawula/Fokker–Planck gate:

1. the `32 x 32` grid did not resolve sufficiently small scale steps;
2. spatial increments were a poor scale coordinate.

C3 therefore tests both hypotheses before any transfer to GENE.

## C3a — `64 x 64` resolution check

The mHW benchmark is repeated at `64 x 64` with the same box `L=40`, `alpha=kappa=1`, `D_zeta=D_n=0.02`, RK4 and two-thirds dealiasing. The primary runs use `dt=0.05` to remain directly comparable to C2. A dedicated seed-1 control with `dt=0.025` reproduces the `380 <= t <= 490` statistics to approximately four significant digits, so the C3 analysis window is not a visible time-step artifact. A much later seed-1 continuation can undergo a large-energy excursion and is therefore not interpreted as physics without a separate CFL/convergence study.

At `64 x 64`, one grid shift is `0.625`. To compare with the physical separations used at `32 x 32`, C3 uses

\[
16\to14,12,10,8
\]

grid points, corresponding to

\[
r=10\to 8.75,7.5,6.25,5.
\]

The scale steps are therefore exactly the same

\[
\Delta s = \ln(16/r') = \ln(8/r'_{32})
\]

as in C2.

### Stationarity warning

The higher resolution does not automatically produce a simpler stationary ensemble. In `380 <= t <= 490`:

- seed 0: mean `f_ZF = 0.9561`, nearly flat ZF fraction;
- seed 1: mean `f_ZF = 0.9209`, but a strong late reorganization is still present;
- seed 2: mean `f_ZF = 0.9973`, essentially flat;
- seed 3: mean `f_ZF = 0.9965`, essentially flat in ZF fraction, although residual nonzonal energy still evolves.

For the scale-coordinate comparison below, seeds `0,2,3` are used as the plateau-like set and seed 1 is retained as an exclusion/falsification case rather than mixed into the statistics.

### Increment-coordinate result

For the same finite-step polynomial estimator as C2, the mean fitted diffusion intercepts over seeds `0,2,3` are

| physical step | `x` mean `b0` | `y` mean `b0` |
|---|---:|---:|
| 10 -> 8.75 | 0.2580 | 0.1429 |
| 10 -> 7.5 | 0.3498 | 0.2187 |
| 10 -> 6.25 | 0.3306 | 0.2180 |
| 10 -> 5 | 0.2797 | 0.1660 |

There is still no convincing small-`delta_s` plateau. The mean within-seed coefficient of variation of `b0` across the four steps is about `0.164` in `x` and `0.210` in `y`.

The fitted fourth-order extrapolation becomes smaller on average than at `32 x 32`:

\[
\bar c_{0,x}(64^2)\simeq 0.00746,
\qquad
\bar c_{0,y}(64^2)\simeq 0.00656,
\]

compared with the C2 values `0.03186` and `0.02196`. However the seed-to-seed fitted intercepts scatter strongly and can even change sign because the low-order polynomial fit is no longer stable enough to support a Pawula claim.

**C3a decision:** higher resolution improves the fourth-order tendency but does **not** establish step-independent `D2` or a converged Kramers–Moyal limit.

## C3b — Alternative scale coordinates

Two nested Fourier-space constructions were tested on the same `64 x 64` plateau-like realizations.

### Smooth Gaussian coarse graining

Define

\[
X_\ell(x,t)=\mathcal F^{-1}
\left[
\exp\left(-\frac12\left(\frac{k\ell}{2\pi}\right)^2\right)
\widehat\phi_{NZ}(k,t)
\right],
\]

with `ell = 10, 8.75, 7.5, 6.25, 5`.

For the triplet `ell = 10,7.5,5`, the Chapman–Kolmogorov TV error averaged over seeds `0,2,3` is

\[
\Delta_{CK}^{Gaussian}\simeq 0.0389,
\]

whereas the physical-increment coordinate gives about

\[
\Delta_{CK}^{inc,x}\simeq0.1042,
\qquad
\Delta_{CK}^{inc,y}\simeq0.1041.
\]

Thus the smooth coordinate looks substantially more Markovian by this diagnostic.

However its small-step conditional moments reveal why this is not a successful stochastic diffusion coordinate. The central estimates scale approximately as

\[
D^{(2)}_{\Delta s}(0)\propto \Delta s^{p_2},
\qquad
p_2 = 0.78,\ 0.83,\ 0.83,
\]

and

\[
D^{(4)}_{\Delta s}(0)\propto \Delta s^{p_4},
\qquad
p_4 = 2.68,\ 2.76,\ 2.86,
\]

for seeds `0,2,3` respectively.

These exponents are close to the differentiable-scale expectation

\[
\Delta X = O(\Delta s)
\Rightarrow
D^{(2)}_{\Delta s}=O(\Delta s),
\qquad
D^{(4)}_{\Delta s}=O(\Delta s^3).
\]

Therefore both higher KM coefficients vanish because the filtered field is smooth in scale; in particular the diffusion itself becomes degenerate:

\[
\lim_{\Delta s\to0}D^{(2)}_{\Delta s}=0.
\]

This is **not** the desired nontrivial Fokker–Planck cascade.

### Sharp spectral cumulative coordinate

As a non-smooth control, define a cumulative nonzonal field with sharp radial cutoff

\[
X_K(x,t)=\sum_{|k|\le K,\,k_y\ne0}\phi_k(t)e^{ik\cdot x},
\]

using `K=0.6,0.7,0.8,0.9,1.0`.

The average CK error for `0.6 -> 0.8 -> 1.0` is approximately `0.0896`, only modestly below the increment value. Its central `D2` is again strongly step dependent; fitted log-log slopes are approximately `-0.62`, `-1.23`, and `-0.70` across seeds `0,2,3`. It therefore also fails to produce a finite nonzero small-step diffusion plateau.

## Main methodological conclusion

C3 reveals a stronger criterion than “choose the coordinates that look most Markovian.” A smooth invertible/filter coordinate can reduce apparent memory while simultaneously making the scale evolution differentiable and the stochastic diffusion trivial.

A useful reduced scale coordinate must therefore satisfy at least two independent conditions:

1. **closure:** small conditional memory / Chapman–Kolmogorov error;
2. **non-degeneracy:** a finite, nonzero and step-stable stochastic generator (or an explicitly justified non-diffusive generator class).

In symbolic form, a future coordinate-selection objective should not minimize only

\[
\mathcal M(U)=I(X_{s+\Delta s};X_{s-\Delta s}\mid X_s),
\]

but should impose a generator regularity/non-degeneracy constraint as well.

## C3 gate decision

- **Resolution-only rescue: failed.** `64 x 64` reduces the apparent fourth-order contribution but does not yield a stable `D2` plateau.
- **Smooth Gaussian scale coordinate: rejected for a nontrivial diffusion model.** It improves CK closure mainly by producing a differentiable scale flow with `D2 -> 0`.
- **Sharp cumulative spectral coordinate: failed.** It remains strongly step dependent and only modestly improves CK closure.
- **Fokker–Planck transfer to GENE: not yet justified.**

The robust object remains the finite-scale transition kernel. The next theoretical/numerical branch should explicitly compare:

1. scale-normalized orthogonal/wavelet coefficients or shell variables designed to preserve a non-degenerate generator;
2. a non-Markov generalized-Langevin / Mori–Zwanzig representation with an inferred memory kernel.

This is now a model-selection question rather than a mere resolution question.
