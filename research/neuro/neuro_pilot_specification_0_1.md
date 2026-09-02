# Neuro Pilot Specification 0.1

**Status:** SPECIFICATION COMPLETE — RETURN TO MASTER FOR PILOT FREEZE  
**Date:** 2026-09-02  
**Scope:** exact first-pilot model/specification freeze only. No CORE optimization, no parameter/effect search, and no calculation or inspection of `K_M(T)`, `K_Q(T)`, optimizer directions, `vartheta(T)`, or `Delta_Q(T)`.

## 0. Inherited frozen objects

The only nominated first Neuro demonstrator remains

\[
\boxed{\text{multi-region canonical microcircuit (CMC/DCM)}}.
\]

The primary physiological signed pathway remains

\[
\boxed{\mathrm{SP}_j\rightarrow\mathrm{SS}_i}
\]

with

\[
Q_{j\to i}^{\rm CORE}
=
\frac12\left(A_{j\to i}^{\dagger}M+MA_{j\to i}\right).
\]

The admissible initial-condition geometry remains the `NB-A` two-component fixed preparation protocol through a physiological afferent drive to `SS_j`. No `B=I`, arbitrary hidden-state kick, or time-dependent optimal-control problem is introduced.

---

## 1. Concrete source identities and architecture

Freeze exactly two cortical sources:

\[
\boxed{j=\mathrm{V1}},
\qquad
\boxed{i=\mathrm{V4}},
\]

interpreted as macaque primary visual cortex and extrastriate area V4. This hierarchy is chosen before any CORE calculation because V1/V4 is a canonical empirically studied CMC/DCM pair with anatomically veridical forward V1→V4 and backward V4→V1 connections.

Each source contains the four standard CMC populations

\[
\mathrm{SS},\quad \mathrm{SP},\quad \mathrm{II},\quad \mathrm{DP},
\]

where `SS` = spiny stellate, `SP` = superficial pyramidal, `II` = inhibitory interneuron and `DP` = deep pyramidal.

The interregional architecture is frozen as the standard reciprocal two-source CMC:

- forward V1 SP → V4 SS;
- forward V1 SP → V4 DP;
- backward V4 DP → V1 SP;
- backward V4 DP → V1 II.

The **primary CORE channel is only the first of these**, V1 SP → V4 SS. The other three remain part of the full generator `A` but not of `A_{j->i}`.

### Reference implementation

The dynamical convention is pinned to the SPM12 CMC state equation

`spm/spm12: toolbox/dcm_meeg/spm_fx_cmc.m`

as read at blob SHA

`66606f2e8c45b896ba239d26d98a45cd1b94b33d`.

The V1/V4 anatomical choice is independently motivated by Bastos et al., *NeuroImage* 108 (2015), 460–475, DOI `10.1016/j.neuroimage.2014.12.081`.

---

## 2. ODE scope and delay convention

Pilot 0.1 uses the autonomous instantaneous-effective-coupling CMC ODE generated directly by `spm_fx_cmc` before application of the optional SPM delay operator.

Therefore

\[
\boxed{\text{propagation-delay module disabled for Pilot 0.1}}.
\]

Equivalently, no `P.D` delay operator is applied. This is a scope restriction to the finite-dimensional autonomous CMC model and **not** a claim that biological V1↔V4 conduction delays are physically zero. A delayed/DDE CMC would constitute a later problem-class extension and is not silently folded into this pilot.

No modulatory connectivity, plasticity or trial-dependent parameter is used.

---

## 3. State ordering and operating point

Use region-major first-order coordinates

\[
x=
( v_{1,SS},z_{1,SS},v_{1,SP},z_{1,SP},v_{1,II},z_{1,II},v_{1,DP},z_{1,DP},
  v_{4,SS},z_{4,SS},v_{4,SP},z_{4,SP},v_{4,II},z_{4,II},v_{4,DP},z_{4,DP})^T,
\]

where `1` denotes V1, `4` denotes V4, and

\[
z_{r,p}=\dot v_{r,p}.
\]

The state dimension is

\[
\boxed{n_x=16}.
\]

SPM uses a baseline-subtracted sigmoid

\[
S(v)=\frac{1}{1+e^{-Rv}}-\frac12,
\qquad
R=\frac23,
\]

so

\[
S(0)=0,
\qquad
S'(0)=\frac16.
\]

With zero exogenous drive the exact fixed point is therefore

\[
\boxed{x^\ast=0_{16}}.
\]

No operating point is searched.

---

## 4. Frozen model parameters

All multiplicative log-parameter deviations are zero for the retained connections and time constants. Structural absences are treated as exact zeros in the fixed pilot model rather than as the numerical `exp(-32)` device used internally to encode absent SPM priors.

### Synaptic time constants

Identical in V1 and V4:

| population | `T_p` |
|---|---:|
| SS | 2 ms |
| SP | 2 ms |
| II | 16 ms |
| DP | 28 ms |

Thus

\[
\kappa_p=T_p^{-1}
=(500,500,62.5,35.7142857143)\;\mathrm{s}^{-1}.
\]

### Intrinsic connection rates

Use the current pinned SPM12 defaults from `spm_fx_cmc.m`:

\[
G=(800,800,1600,800,800,400,800,800,400,200)\;\mathrm{s}^{-1},
\]

with ordering

1. SS→SS self inhibitory;
2. SP→SS recurrent inhibitory;
3. II→SS inhibitory;
4. II→II self inhibitory;
5. SS→II excitatory;
6. DP→II excitatory;
7. SP→SP self inhibitory;
8. SS→SP excitatory;
9. II→DP inhibitory;
10. DP→DP self inhibitory.

### Extrinsic connection rates

Use the pinned SPM12 defaults

\[
E=(200,100,200,100)\;\mathrm{s}^{-1},
\]

corresponding to

1. V1 SP→V4 SS: `200`;
2. V1 SP→V4 DP: `100`;
3. V4 DP→V1 SP: `200` with the CMC backward sign;
4. V4 DP→V1 II: `100` with the CMC backward sign.

### Sigmoid and input constants

\[
R=2/3,
\qquad B_{\rm sigmoid}=0,
\qquad S'(0)=1/6.
\]

For the single accepted exogenous afferent input, set the SPM exogenous input parameter to its unit prior value

\[
C_{V1}=1,
\qquad C_{V4}=0,
\]

with the standard SPM external-input multiplier `32`.

No endogenous stochastic input is part of the deterministic Pilot-0.1 generator.

---

## 5. Exact autonomous linear generator `A`

Linearization at `x*=0`, `u=0` gives

\[
\dot x=Ax+b_{\rm aff,V1}u(t).
\]

The following sparse triplet list uniquely defines the frozen `16 x 16` generator in the state ordering above; all unlisted entries are zero. Time is in seconds.

| row | col | `A[row,col]` |
|---:|---:|---:|
| 1 | 2 | 1 |
| 2 | 1 | -316666.666667 |
| 2 | 2 | -1000 |
| 2 | 3 | -66666.6666667 |
| 2 | 5 | -133333.333333 |
| 3 | 4 | 1 |
| 4 | 1 | 66666.6666667 |
| 4 | 3 | -316666.666667 |
| 4 | 4 | -1000 |
| 4 | 15 | -16666.6666667 |
| 5 | 6 | 1 |
| 6 | 1 | 8333.33333333 |
| 6 | 5 | -12239.5833333 |
| 6 | 6 | -125 |
| 6 | 7 | 4166.66666667 |
| 6 | 15 | -1041.66666667 |
| 7 | 8 | 1 |
| 8 | 5 | -2380.95238095 |
| 8 | 7 | -2465.98639456 |
| 8 | 8 | -71.4285714286 |
| 9 | 10 | 1 |
| 10 | 3 | 16666.6666667 |
| 10 | 9 | -316666.666667 |
| 10 | 10 | -1000 |
| 10 | 11 | -66666.6666667 |
| 10 | 13 | -133333.333333 |
| 11 | 12 | 1 |
| 12 | 9 | 66666.6666667 |
| 12 | 11 | -316666.666667 |
| 12 | 12 | -1000 |
| 13 | 14 | 1 |
| 14 | 9 | 8333.33333333 |
| 14 | 13 | -12239.5833333 |
| 14 | 14 | -125 |
| 14 | 15 | 4166.66666667 |
| 15 | 16 | 1 |
| 16 | 3 | 595.238095238 |
| 16 | 13 | -2380.95238095 |
| 16 | 15 | -2465.98639456 |
| 16 | 16 | -71.4285714286 |

The pre-CORE stability qualification gives

\[
\boxed{\alpha(A)=\max\Re\lambda(A)=-33.0964092356\;\mathrm{s}^{-1}<0}.
\]

Thus the frozen operating point is asymptotically stable. This is only a qualification check, not a CORE effect calculation.

---

## 6. Exact positive storage matrix `M`

For each second-order synaptic filter use the already accepted model-internal storage

\[
S_{r,p}
=
\frac12\left(z_{r,p}^2+\kappa_p^2v_{r,p}^2\right).
\]

The total storage is

\[
\boxed{
S=\frac12x^\dagger Mx
}
\]

with

\[
\boxed{
M=\operatorname{diag}(
250000,1,
250000,1,
3906.25,1,
1275.51020408163,1,
250000,1,
250000,1,
3906.25,1,
1275.51020408163,1
).
}
\]

`M=M^dagger>0` exactly in this model. If `v` is expressed in the SPM depolarization coordinate, `z` has depolarization-units/s and each storage term has depolarization-units²/s². No identification with metabolic or thermodynamic brain energy is made.

---

## 7. Exact primary pathway block and signed channel

The primary path is fixed as

\[
\boxed{\mathrm{V1\,SP}\rightarrow\mathrm{V4\,SS}}.
\]

In the frozen ordering its linearized pathway block has exactly one nonzero entry,

\[
\boxed{
(A_{j\to i})_{10,3}
=
\frac{200}{0.002}\frac16
=
16666.6666666667.
}
\]

All other entries of `A_{j->i}` are zero. The second forward path V1 SP→V4 DP remains in the full `A` at entry `(16,3)` but is **not** part of the primary channel.

With the required convention,

\[
Q_{j\to i}^{\rm CORE}
=
\frac12(A_{j\to i}^{\dagger}M+MA_{j\to i}),
\]

so the exact sparse signed-channel matrix has only

\[
\boxed{
(Q_{j\to i}^{\rm CORE})_{10,3}
=(Q_{j\to i}^{\rm CORE})_{3,10}
=8333.33333333333
}
\]

nonzero. It is real symmetric/Hermitian and signed/indefinite. The instantaneous quantity

\[
x^\dagger Q_{j\to i}^{\rm CORE}x
\]

means only the signed contribution of the pre-defined V1-SP→V4-SS pathway to the rate of the frozen synaptic-filter storage; its sign is not a synonym for excitatory versus inhibitory synaptic sign.

The later cumulative channel remains

\[
J_{j\to i}(T)
=
\int_0^T x(t)^\dagger Q_{j\to i}^{\rm CORE}x(t)\,dt.
\]

No value of this integral is computed here.

---

## 8. Exact afferent input vector

Only the already accepted exogenous afferent drive to V1 spiny-stellate cells is permitted.

In the frozen model, `U=32 u(t)` enters the V1 SS filter-rate equation and `T_SS=0.002 s`, hence

\[
\boxed{
b_{\rm aff,V1}=16000\,e_2.
}
\]

No other hidden-state actuator is present.

---

## 9. Fixed finite two-pulse preparation protocol

Observation begins at `t=0`. The preparation input is

\[
u(t)=a_1h_1(t)+a_2h_2(t).
\]

Both pulse shapes are unit-height rectangular afferent-drive pulses of width

\[
\boxed{\delta=1\;\mathrm{ms}}.
\]

Their end-to-observation delays are fixed **before any CORE calculation** from two native CMC synaptic time scales:

\[
\boxed{\tau_1=T_{SS}=2\;\mathrm{ms}},
\qquad
\boxed{\tau_2=T_{II}=16\;\mathrm{ms}}.
\]

Thus

\[
h_1(t)=1\quad\text{for }t\in[-3,-2]\;\mathrm{ms},
\]

\[
h_2(t)=1\quad\text{for }t\in[-17,-16]\;\mathrm{ms},
\]

and both vanish otherwise.

These are two independently amplitude-controlled components of one fixed preparation protocol. Their times and shapes are not later adjustable.

The corresponding effective initial-state columns are

\[
\boxed{
b_k^{\rm eff}
=
\int_{\tau_k}^{\tau_k+\delta}e^{As}b_{\rm aff,V1}\,ds,
\qquad
B=B_{\rm prep}^{(2)}=[b_1^{\rm eff},b_2^{\rm eff}].
}
\]

Because `A` is nonsingular this is equivalently

\[
b_k^{\rm eff}
=A^{-1}
\left(e^{A(\tau_k+\delta)}-e^{A\tau_k}\right)b_{\rm aff,V1}.
\]

The frozen numerical columns are:

| # | state | `b1_eff` | `b2_eff` |
|---:|---|---:|---:|
| 1 | `V1 v_SS` | 0.0105854484001 | -0.000754745464864 |
| 2 | `V1 z_SS` | -1.619010579 | 0.0256978115799 |
| 3 | `V1 v_SP` | 0.000761404056852 | -0.000151784974269 |
| 4 | `V1 z_SP` | 0.49819253297 | -0.0136399076799 |
| 5 | `V1 v_II` | 0.000176257880614 | 0.00164048222898 |
| 6 | `V1 z_II` | 0.159830237429 | -0.0795637825863 |
| 7 | `V1 v_DP` | -1.74883533187e-07 | -0.000188936583356 |
| 8 | `V1 z_DP` | -0.000301353787007 | -0.0290576150485 |
| 9 | `V4 v_SS` | 4.24993575413e-06 | -4.89290774524e-06 |
| 10 | `V4 z_SS` | 0.00598068521783 | -0.00548833133967 |
| 11 | `V4 v_SP` | 4.70584858656e-08 | 4.57944938867e-06 |
| 12 | `V4 z_SP` | 0.00010005602825 | -0.00187163913585 |
| 13 | `V4 v_II` | 8.25559161236e-09 | 1.92190462477e-05 |
| 14 | `V4 z_II` | 1.85484986071e-05 | 0.00143065820783 |
| 15 | `V4 v_DP` | 2.36612056996e-07 | 3.99330546577e-05 |
| 16 | `V4 z_DP` | 0.000374190011704 | 0.00196392483643 |

The two columns were computed from the frozen matrix-exponential integral, with an adaptive quadrature cross-check agreeing to relative error below `3e-13`.

---

## 10. Stimulus calibration and `R_in`

The pulse amplitudes `a_1,a_2` are expressed in the normalized exogenous CMC input coordinate. Unit amplitude means

\[
u=1,
\qquad C_{V1}=1,
\]

which the pinned SPM state equation maps to `U=32` before the V1 SS synaptic-filter equation. No conversion to absolute luminance, current or metabolic dose is asserted.

The experimental/model input cost is the fixed pulse-dose Gram metric

\[
(R_{\rm in})_{k\ell}
=
E_{\rm ref}^{-1}\int h_k(t)h_\ell(t)\,dt.
\]

Choose the reference dose independently as the dose of one unit-height `1 ms` pulse,

\[
\boxed{E_{\rm ref}=1\;\mathrm{ms}}.
\]

The two pulses have equal width and do not overlap, hence

\[
\boxed{R_{\rm in}=I_2.}
\]

This identity is in the **two-dimensional preparation-input coordinate space only**; it is not `B=I` in neural-state space.

---

## 11. Frozen rank and conditioning qualification

The qualification rule is:

1. exact/numerical rank must be `2`;
2. in the physically relevant storage/input-whitened map
   \[
   \widehat B=M^{1/2}BR_{\rm in}^{-1/2},
   \]
   require
   \[
   \sigma_2/\sigma_1\ge10^{-2}
   \quad\Longleftrightarrow\quad
   \kappa_2(\widehat B)\le100.
   \]
3. failure would STOP the pilot; pulse times would not be retuned after inspection.

For the frozen protocol:

\[
\operatorname{rank}(B)=2,
\]

raw Euclidean singular values are

\[
(\sigma_1,\sigma_2)=(1.70187544,0.08227666),
\]

so

\[
\kappa_2(B)=20.6848.
\]

For the storage/input-whitened map,

\[
(\sigma_1,\sigma_2)=(5.58509106,0.16285932),
\]

\[
\boxed{
\sigma_2/\sigma_1=0.0291597,
\qquad
\kappa_2(\widehat B)=34.2940<100.
}
\]

Therefore the fixed `B` passes without retuning.

---

## 12. Time normalization and horizon ladder

Choose the model-native slowest local synaptic time constant as the pre-CORE reference time:

\[
\boxed{\tau_{\rm ref}=T_{DP}=28\;\mathrm{ms}}.
\]

This is fixed from the CMC model and not from any CORE response.

The inherited dimensionless ladder

\[
T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}
\]

therefore corresponds to

\[
\boxed{T\in\{7,14,28,56,112,224\}\;\mathrm{ms}}.
\]

No additional or interpolated horizons may be used to rescue a demonstration criterion.

---

## 13. Later numerical method and sanity checks — preregistered only

No later objective operator is evaluated in this document. If MASTER subsequently authorizes execution, use the following fixed numerical protocol.

### Matrix propagation

- IEEE double precision.
- Scaling-and-squaring matrix exponential equivalent to `scipy.linalg.expm`.
- Semigroup relative Frobenius check below `1e-10` at representative fixed horizon pairs.

### Cumulative channel integral

For

\[
W_Q(T)=\int_0^T e^{A^\dagger t}Q_{j\to i}^{\rm CORE}e^{At}\,dt,
\]

use a matrix-exponential/finite-horizon Lyapunov evaluation as primary and adaptive matrix-valued quadrature as an independent cross-check.

Require relative Frobenius disagreement below

\[
\boxed{10^{-8}}.
\]

### Structural checks before any optimization

Require:

- `alpha(A)<0`;
- `M=M^dagger`, `lambda_min(M)>0`;
- `Q=Q^dagger` to relative norm `<=1e-12`;
- `R_in=R_in^dagger>0`;
- `rank(B)=2` and the conditioning rule in Section 11;
- later `K_M(T)` Hermitian positive semidefinite up to relative numerical tolerance `1e-10`;
- later `K_Q(T)` Hermitian to relative tolerance `1e-10`.

Any structural failure triggers STOP rather than parameter, timing, calibration or horizon adjustment.

---

## 14. Shared cross-domain reporting protocol frozen for later use

If and only if MASTER authorizes a later pilot execution, the positive terminal objective is

\[
K_M(T)=R_{\rm in}^{-1/2}B^\dagger e^{A^\dagger T}Me^{AT}BR_{\rm in}^{-1/2},
\]

interpreted only as **final synaptic-filter storage per fixed experimental input cost**.

The signed cumulative pathway operator is

\[
K_Q(T)=R_{\rm in}^{-1/2}B^\dagger
\left[
\int_0^T e^{A^\dagger t}Q_{j\to i}^{\rm CORE}e^{At}\,dt
\right]
BR_{\rm in}^{-1/2}.
\]

The positive signed branch is primary, but the negative extremum must also be reported.

The inherited project-level operational demonstration thresholds are frozen as

\[
\boxed{\vartheta(T)\ge20^\circ},
\qquad
\boxed{\Delta_Q(T)\ge0.25}
\]

for at least two neighboring horizons of the fixed ladder. These are **project operational thresholds, not universal neurophysiological constants**.

In addition to any vector angle, later reporting must include domain-specific composition:

- the two-pulse preparation mixture in the fixed `(h_1,h_2)` basis;
- V1/V4 and SS/SP/II/DP state composition of the resulting response;
- the sign and temporal distribution of the fixed V1-SP→V4-SS pathway contribution.

No target region, pathway, pulse timing, waveform, input source or horizon may be changed after inspecting such results.

---

## 15. Optional fixed observation proxy for later validation

This observation map is not a CORE objective and is frozen only to support later model/measurement interpretation. If an LFP-like source output is needed, use the published V1/V4 CMC population weights

\[
y_r=0.2v_{r,SS}+0.8v_{r,SP}+0\,v_{r,II}+0.2v_{r,DP}.
\]

No observation weight is optimized.

---

## 16. Anti-bias and STOP boundary

The following remain prohibited:

- changing V1/V4 to another pair after seeing a CORE effect;
- changing the operating point or any `G`, `E`, `T`, sigmoid or input parameter to increase an effect;
- enabling `B=I` or arbitrary latent-state perturbations;
- retiming or reshaping the preparation pulses after inspecting rank-qualified CORE results;
- replacing the fixed two-amplitude preparation problem by time-dependent waveform optimization;
- calling the storage brain energy or metabolic energy;
- adding propagation delays during execution without a new MASTER-approved model freeze;
- adding extra horizons after inspecting the fixed ladder.

This specification performs no CORE optimization and no objective-separation calculation.

---

## 17. Frozen Pilot-0.1 tuple

```text
model                  = 2-source multi-region CMC/DCM
reference dynamics     = SPM12 spm_fx_cmc.m, blob 66606f2e8c45b896ba239d26d98a45cd1b94b33d
source j               = macaque V1
source i               = macaque V4
primary channel        = V1 SP -> V4 SS
state dimension        = 16
operating point        = x* = 0
propagation delays     = disabled for this autonomous ODE pilot
T (ms)                 = (2, 2, 16, 28)
G (1/s)                = (800,800,1600,800,800,400,800,800,400,200)
E (1/s)                = (200,100,200,100)
sigmoid R              = 2/3
sigmoid derivative     = 1/6 at baseline
exogenous input        = V1 SS only, standard SPM factor 32
b_aff,V1               = 16000 * e_2
M                      = fixed synaptic-filter storage matrix in Sec. 6
A                      = fixed 16x16 sparse generator in Sec. 5
A_j->i                 = only entry (10,3)=16666.6666666667
Q_j->i^CORE            = only symmetric entries (10,3),(3,10)=8333.33333333333
pulse width            = 1 ms
pre-observation delays = (2 ms, 16 ms)
R_in                    = I_2
rank(B)                 = 2
kappa_2(M^1/2 B)        = 34.2940
tau_ref                 = 28 ms
horizon ladder          = (7,14,28,56,112,224) ms
```

---

## 18. Verdict and handoff

Every object required for a first autonomous CMC Neuro pilot is now frozen without inspecting a CORE optimizer or objective-separation effect. The frozen full-system preparation map has rank two and passes the preregistered conditioning qualification.

\[
\boxed{\text{NEURO PILOT SPECIFICATION 0.1 COMPLETE}}
\]

This document does **not** authorize execution.

\[
\boxed{\text{RETURN TO MASTER FOR PILOT FREEZE}}
\]

**STOP.**
