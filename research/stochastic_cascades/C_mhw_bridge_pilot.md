# C — Modified Hasegawa-Wakatani bridge pilot

**Status:** exploratory parallel track; not yet a canonical plasma convention for the main nonmodal theory.

**Date:** 2026-09-01

## Purpose

This pilot tests the proposed bridge

`drift-wave turbulence -> zonal/nonzonal split -> scale increments -> Markov test -> finite-step Kramers-Moyal diagnostics`

before attempting the same logic on gyrokinetic/GENE data.

The implementation is deliberately isolated under `nonmodal_flux.benchmarks`: it must not silently resolve the separate Hasegawa-Wakatani convention audit in the main roadmap.

## Model convention

The benchmark uses the Numata-style modified Hasegawa-Wakatani equations

\[
\partial_t \zeta + \{\phi,\zeta\}
=\alpha(\widetilde\phi-\widetilde n)-D_\zeta\nabla^4\zeta,
\]

\[
\partial_t n + \{\phi,n\}
=\alpha(\widetilde\phi-\widetilde n)-\kappa\partial_y\phi-D_n\nabla^4 n,
\]

with

\[
\zeta=\nabla_\perp^2\phi,
\qquad
\widetilde f=f-\langle f\rangle_y.
\]

Thus the parallel/resistive coupling is removed for the zonal modes `ky = 0`.

References used for this convention:

- R. Numata, R. Ball, R. L. Dewar, *Nonlinear Simulation of Drift Wave Turbulence*, arXiv:physics/0703274 (2007).
- A. Hakim, *Solving (Modified) Hasegawa-Wakatani equations*, Simulation Journal JE17 (2026), as an independent implementation cross-check.

## Numerical pilot

Reference run:

- grid: `32 x 32`;
- periodic box: `Lx = Ly = 40`;
- `alpha = 1`, `kappa = 1`;
- `D_zeta = D_n = 0.02`;
- pseudo-spectral Poisson brackets;
- 2/3 dealiasing;
- RK4 with `dt = 0.05`;
- random perturbation amplitude `1e-3`;
- seed `3`;
- final time `320`;
- diagnostics sampled every `0.5` time units.

This is a low-resolution method-development run, not a converged turbulence calculation.

## Zonal/nonzonal split

The ExB kinetic energy is split as

\[
E_K=E_{ZF}+E_{NZ},
\]

where the zonal contribution contains `ky=0` and the nonzonal contribution contains `ky != 0`.

Over the analysis window `120 <= t <= 310`, snapshots were divided at the median zonal kinetic-energy fraction

\[
f_{ZF}=\frac{E_{ZF}}{E_{ZF}+E_{NZ}}.
\]

The split was

\[
f_{ZF,\mathrm{median}}=0.84656.
\]

The two conditional ensembles had

- low-ZF mean: `0.61492` (191 snapshots);
- high-ZF mean: `0.90633` (190 snapshots).

Important caveat: in this single realization the ZF fraction evolves strongly with time. Therefore this split is partially confounded with the transient and cannot yet be interpreted causally.

## Shell-resolved nonzonal kinetic energy

For radial Fourier shells with edges

`[0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.6, 3.5]`,

the mean nonzonal kinetic energies were:

| shell | low ZF | high ZF | high/low |
|---|---:|---:|---:|
| 0.0-0.4 | 0.002388 | 0.001234 | 0.517 |
| 0.4-0.8 | 0.024953 | 0.013018 | 0.522 |
| 0.8-1.2 | 0.072721 | 0.019795 | 0.272 |
| 1.2-1.6 | 0.034627 | 0.010959 | 0.316 |
| 1.6-2.0 | 0.010620 | 0.003630 | 0.342 |
| 2.0-2.6 | 0.000446 | 0.000101 | 0.225 |

The high-ZF ensemble therefore has substantially reduced nonzonal activity across all resolved energetic shells. This is consistent with the expected qualitative role of zonal flow but is not by itself evidence for a changed Markov cascade.

## Scale-process observable

For the first Markov/KM test, zonal modes are removed from the potential and spatial increments are formed at separations

\[
r/\Delta x\in\{8,4,2,1\}.
\]

Both x- and y-directed increments are pooled in this pilot. That pooling is intentionally temporary; anisotropy must be kept explicit in a later plasma-quality analysis.

The scale variable advances from large to small separation with

\[
\Delta s=\ln 2.
\]

## Markov diagnostics

### Gaussian conditional-information proxy

The Gaussian proxy

\[
I(X_{r/4};X_r\mid X_{r/2})
\]

was:

| triplet | low ZF | high ZF |
|---|---:|---:|
| 8-4-2 | 0.05034 nat | 0.01010 nat |
| 4-2-1 | 0.21144 nat | 0.20541 nat |

The larger-scale triplet becomes substantially closer to Gaussian-Markov under strong ZF, while the smallest-scale triplet remains comparably non-Markovian.

### Chapman-Kolmogorov test

A discretized transition-matrix test compared direct `P(X2|X0)` with the composed Markov prediction `P(X2|X1) P(X1|X0)`. The reported number is an occupancy-weighted total-variation error; zero would be exact agreement.

| triplet | low ZF | high ZF |
|---|---:|---:|
| 8-4-2 | 0.09387 | 0.06119 |
| 4-2-1 | 0.08364 | 0.08688 |

This supports the same cautious statement: strong ZF improves closure at the larger of the tested scale triplets, but not at the smallest one.

## Finite-step drift/diffusion pilot

For the `4 -> 2` scale step, increments were normalized by the *same* low-ZF reference standard deviation, so the two conditional ensembles remain directly comparable. Local conditional moments were fitted as

\[
D^{(1)}(u)\approx a_1 u+a_3u^3,
\qquad
D^{(2)}(u)\approx b_0+b_2u^2.
\]

The fitted coefficients were

| coefficient | low ZF | high ZF |
|---|---:|---:|
| `a1` | -0.72497 | -0.72289 |
| `a3` | 0.00337 | 0.00207 |
| `b0` | 0.34951 | 0.11664 |
| `b2` | 0.19309 | 0.17742 |

The dominant pilot signal is therefore not a large change of the fitted drift but an approximately threefold reduction of the diffusion intercept `b0` in the high-ZF ensemble.

This is compatible with the hypothesis that zonal organization suppresses stochastic nonzonal fluctuations. However, these are finite-scale coefficients and must not yet be called converged Kramers-Moyal coefficients.

## What is established by this pilot

1. The Numata mHW benchmark produces a useful drift-wave/zonal-flow bridge case with a clean `ky=0` decomposition.
2. Zonal and nonzonal kinetic energy and radial shell energies can be separated exactly at the diagnostic level.
3. A spatial-increment process can be conditioned on instantaneous ZF strength and subjected to Markov diagnostics.
4. The pilot shows a measurable ZF-conditioned change in both shell activity and finite-step diffusion statistics.
5. At least one tested large-scale triplet is more nearly Markovian in the high-ZF ensemble.

## What is *not* established

- no causal claim that ZF strength alone causes the statistical differences;
- no converged DNS claim;
- no delta-s -> 0 Kramers-Moyal extrapolation;
- no Pawula/D4 validation yet;
- no full Chapman-Kolmogorov uncertainty analysis;
- no separation of radial and poloidal increment statistics yet;
- no claim that the Numata convention is the final convention for the main plasma/nonmodal program;
- no gyrokinetic/GENE claim.

## Gate for the next step

Before using this as evidence for a mode-conditioned stochastic cascade, the next package should:

1. generate several statistically independent runs or a truly stationary forced ensemble;
2. compare low/high ZF states *within* stationary windows rather than primarily across a transient;
3. retain x/y increment direction separately;
4. estimate local D1, D2 and D4 at several scale ratios and extrapolate toward small delta-s;
5. bootstrap the Chapman-Kolmogorov error and KM coefficients;
6. compare mHW with a control in which the zonal coupling modification is disabled;
7. only after those gates, map the same observable definitions onto gyrokinetic/GENE quantities.

The current result is therefore a successful **method-development bridge**, not yet a physics result.
