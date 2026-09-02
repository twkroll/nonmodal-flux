# Neuro Pilot 0.1 Execution Results

**Status:** EXECUTION COMPLETE — RETURN TO MASTER FOR RESULT INTEGRATION  
**Date:** 2026-09-02  
**Authority:** `research/master/cross_domain_pilot_freeze_0_1.md` and `research/master/prompts/neuro_pilot_execution_0_1.md`  
**Verdict:** `NEURO-STRONG`

## 0. Scope and anti-bias compliance

This report executes only the pre-effect frozen two-source macaque V1/V4 CMC/DCM pilot. No model, region, pathway, operating point, parameter, pulse, input metric, time normalization, horizon, threshold, or numerical gate was changed after the first CORE-effect quantity was computed.

Frozen tuple:

- state dimension: 16;
- sources: macaque V1 and V4;
- operating point: `x*=0`;
- propagation-delay module disabled;
- primary signed pathway: V1 superficial-pyramidal -> V4 spiny-stellate;
- positive metric: model-internal synaptic-filter storage `M`, **not** brain/metabolic energy;
- preparation map: the two fixed V1-SS 1-ms afferent pulses ending 2 ms and 16 ms before observation;
- `R_in=I_2`;
- `tau_ref=28 ms`;
- horizons: `(7,14,28,56,112,224) ms`.

No parameter search or retuning was performed.

## 1. Numerical method

Let `E(T)=exp(A T)`. The terminal storage operator was evaluated directly as

```math
K_M(T)=B^T E(T)^T M E(T) B
```

because `R_in=I_2`.

For the cumulative signed pathway operator, the primary calculation used the stable finite-horizon Lyapunov identity. Since `alpha(A)<0`, first solve

```math
A^T P_inf + P_inf A = -Q,
```

then evaluate

```math
P_Q(T)=P_inf-E(T)^T P_inf E(T),
\qquad
K_Q(T)=B^T P_Q(T)B.
```

This was independently checked by adaptive quadrature of

```math
int_0^T exp(A^T t) Q exp(A t) dt
```

at every frozen horizon. Eigenanalysis was performed on the Hermitian symmetrization only after the raw Hermiticity residual had been recorded.

The semigroup test used the nontrivial decomposition `T=T/3+2T/3` at every frozen horizon.

## 2. Structural and numerical gates

| Check | Result | Gate |
|---|---:|---|
| alpha(A) | -33.096409235604 s^-1 | PASS (<0) |
| lambda_min(M) | 1 | PASS (>0) |
| rel Hermiticity M | 0.000e+00 | PASS |
| rel Hermiticity Q | 0.000e+00 | PASS (<=1e-12) |
| lambda_min(R_in) | 1 | PASS (>0) |
| rank(B) | 2 | PASS (=2) |
| kappa_2(M^1/2 B) | 34.293960 | PASS (<=100) |
| max semigroup rel. Frobenius error | 6.636e-14 | PASS (<1e-10) |
| max P_Q primary/adaptive rel. disagreement | 2.291e-12 | PASS (<1e-8) |
| max rel Hermiticity K_M | 1.990e-16 | PASS (<=1e-10) |
| max rel Hermiticity K_Q | 1.361e-13 | PASS (<=1e-10) |
| min eigenvalue K_M over ladder | 8.291e-10 | PASS (PSD) |

The relative residual of the infinite-horizon Lyapunov equation was `6.153e-11`. All preregistered structural and numerical gates pass. Therefore the execution is not `NEURO-NUMERICAL-FAIL`.

Direct trajectory validation also passes:

- maximum relative difference between `x(T)^T M x(T)` and `w_M^T K_M w_M`: `4.229e-16`;
- maximum relative difference between direct time integration of the pathway signal for `w_Q` and `J_Q^+`: `3.634e-10`;
- maximum relative difference between direct time integration for `w_M` and `w_M^T K_Q w_M`: `4.972e-10`.

No optimizer eigenvalue is near-degenerate on the frozen ladder; the two-dimensional eigengaps are large for both objectives.

## 3. Finite-time results

| T (ms) | T/tau_ref | G_M | J_Q^+ | J_Q^- | theta (deg) | Delta_Q | w_M=(h1,h2) | w_Q=(h1,h2) |
|---:|---:|---:|---:|---:|---:|---:|---|---|
| 7 | 0.25 | 3.215544887e-01 | 1.322210704e-03 | 9.262343075e-07 | 6.237106 | 0.011795 | (+0.998904, -0.046796) | (+0.987908, -0.155043) |
| 14 | 0.50 | 1.748263416e-01 | 1.216507699e-03 | 7.321610987e-06 | 19.752824 | 0.113532 | (+0.975509, +0.219960) | (+0.992448, -0.122669) |
| 28 | 1.00 | 2.328171948e-02 | 1.243249974e-03 | 4.814979400e-06 | 30.886147 | 0.262491 | (+0.787151, -0.616761) | (+0.992128, -0.125226) |
| 56 | 2.00 | 4.101503784e-03 | 1.242526860e-03 | 6.580964321e-06 | 11.053367 | 0.036563 | (+0.997576, +0.069586) | (+0.992411, -0.122964) |
| 112 | 4.00 | 2.407725382e-05 | 1.242225387e-03 | 6.542318358e-06 | 46.824271 | 0.529017 | (+0.768725, +0.639580) | (+0.992410, -0.122974) |
| 224 | 8.00 | 3.495988837e-09 | 1.242228882e-03 | 6.543981023e-06 | 65.058256 | 0.817841 | (+0.530000, +0.847998) | (+0.992410, -0.122972) |

`J_Q^+` is safely nonzero at every horizon, so `Delta_Q` is interpretable throughout. The minimum eigenvalue `J_Q^-` is reported mandatorily; it happens to remain positive on the frozen two-dimensional admissible preparation space even though the full-state instantaneous `Q` is indefinite.

The preregistered simultaneous thresholds

```math
theta >= 20 deg,
\qquad
Delta_Q >= 0.25
```

are met at:

- 28 ms: `theta=30.886 deg`, `Delta_Q=0.262`;
- 112 ms: `theta=46.824 deg`, `Delta_Q=0.529`;
- 224 ms: `theta=65.058 deg`, `Delta_Q=0.818`.

The required neighboring-horizon rule is satisfied by the adjacent frozen pair **112 ms and 224 ms**.

## 4. Physical/input-space distinction of the optimizers

The optimizer coordinates are amplitudes of the two fixed preparation pulses:

- `h1`: the recent pulse ending 2 ms before observation;
- `h2`: the older pulse ending 16 ms before observation.

At the two neighboring threshold-supporting horizons:

```text
112 ms:
  storage-optimal      w_M = (+0.768725, +0.639580)
  pathway-optimal      w_Q = (+0.992410, -0.122974)

224 ms:
  storage-optimal      w_M = (+0.530000, +0.847998)
  pathway-optimal      w_Q = (+0.992410, -0.122972)
```

This is a physically distinct preparation protocol, not just a vector-angle artifact. The pathway optimum is almost horizon-independent and uses a dominant recent afferent pulse combined with a **small opposite-sign older pulse**. The terminal-storage optimum at the two long horizons instead uses the two pulses with the **same sign**, and at 224 ms the older pulse dominates.

Thus the separation has an immediate experimental interpretation in the already frozen pulse-amplitude basis.

## 5. Initial-state composition

The table below gives the fraction of the frozen quadratic synaptic-filter storage in each region/population at `t=0` after applying `x0=Bw`. It is a composition diagnostic, not an additional objective.

| T (ms) | optimizer | V1_SS | V1_SP | V1_II | V1_DP | V4_SS | V4_SP | V4_II | V4_DP |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | w_M | 98.645% | 1.269% | 0.086% | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% |
| 7 | w_Q | 98.631% | 1.275% | 0.094% | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% |
| 14 | w_M | 98.676% | 1.253% | 0.071% | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% |
| 14 | w_Q | 98.635% | 1.273% | 0.091% | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% |
| 28 | w_M | 98.526% | 1.315% | 0.157% | 0.002% | 0.000% | 0.000% | 0.000% | 0.000% |
| 28 | w_Q | 98.635% | 1.274% | 0.091% | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% |
| 56 | w_M | 98.660% | 1.262% | 0.078% | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% |
| 56 | w_Q | 98.635% | 1.273% | 0.091% | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% |
| 112 | w_M | 98.713% | 1.220% | 0.065% | 0.002% | 0.000% | 0.000% | 0.000% | 0.000% |
| 112 | w_Q | 98.635% | 1.273% | 0.091% | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% |
| 224 | w_M | 98.677% | 1.186% | 0.128% | 0.009% | 0.000% | 0.000% | 0.000% | 0.000% |
| 224 | w_Q | 98.635% | 1.273% | 0.091% | 0.000% | 0.000% | 0.000% | 0.000% | 0.000% |

Both preparations begin overwhelmingly in V1-SS, as required by the admissible afferent actuator. The difference between optimizers is therefore not generated by adding a hidden-state actuator; it arises from the different fixed pulse mixtures propagated through the same CMC preparation dynamics.

For exact reproduction, the initial state vectors in the frozen ordering

`(V1 vSS,zSS,vSP,zSP,vII,zII,vDP,zDP,V4 vSS,zSS,vSP,zSP,vII,zII,vDP,zDP)`

are:

| T (ms) | optimizer | x0 = B w in frozen 16-state ordering |
|---:|---|---|
| 7 | w_M | `[0.0106092, -1.61844, 0.000767673, 0.498285, 9.92963e-05, 0.163378, 8.66684e-06, 0.00105876, 4.47425e-06, 0.00623097, -1.67294e-07, 0.000187532, -8.91133e-07, -4.84213e-05, -1.63237e-06, 0.000281876]` |
| 7 | w_Q | `[0.0105745, -1.60342, 0.00077573, 0.494283, -8.02195e-05, 0.170233, 2.91206e-05, 0.00420748, 4.95716e-06, 0.00675929, -6.63524e-07, 0.000389031, -2.97163e-06, -0.00020349, -5.95761e-06, 6.51716e-05]` |
| 14 | w_M | `[0.0101602, -1.57371, 0.00070937, 0.482991, 0.000532781, 0.138415, -4.17291e-05, -0.00668548, 3.06961e-06, 0.004627, 1.0532e-06, -0.00031408, 4.23547e-06, 0.000332782, 9.01449e-06, 0.00079701]` |
| 14 | w_Q | `[0.0105981, -1.60994, 0.000774273, 0.496103, -2.63091e-05, 0.168383, 2.3003e-05, 0.00326538, 4.81805e-06, 0.00660876, -5.15052e-07, 0.000328892, -2.34938e-06, -0.000157089, -4.66371e-06, 0.000130452]` |
| 28 | w_M | `[0.00879784, -1.29025, 0.000692955, 0.400565, -0.000873044, 0.174882, 0.000116391, 0.0176844, 6.36309e-06, 0.00809269, -2.78738e-06, 0.00123311, -1.18471e-05, -0.000867773, -2.44429e-05, -0.000916728]` |
| 28 | w_Q | `[0.0105966, -1.60948, 0.000774418, 0.495979, -3.05611e-05, 0.168536, 2.34863e-05, 0.0033398, 4.8292e-06, 0.00662089, -5.26779e-07, 0.000333647, -2.39854e-06, -0.000160754, -4.76592e-06, 0.000125309]` |
| 56 | w_M | `[0.0105073, -1.6133, 0.000748996, 0.496036, 0.000289984, 0.153906, -1.33217e-05, -0.00232261, 3.89916e-06, 0.00558428, 3.65608e-07, -3.04255e-05, 1.3456e-06, 0.000118057, 3.0148e-06, 0.000509944]` |
| 56 | w_Q | `[0.0105979, -1.60988, 0.00077429, 0.496089, -2.67997e-05, 0.168401, 2.30588e-05, 0.00327397, 4.81933e-06, 0.00661016, -5.16405e-07, 0.000329441, -2.35505e-06, -0.000157511, -4.67551e-06, 0.000129859]` |
| 112 | w_M | `[0.00765458, -1.22814, 0.000488232, 0.374249, 0.00118471, 0.0719781, -0.000120974, -0.0188163, 1.37627e-07, 0.00108728, 2.9651e-06, -0.00112015, 1.22985e-05, 0.000929279, 2.57223e-05, 0.00154374]` |
| 112 | w_Q | `[0.0105979, -1.60988, 0.000774291, 0.496089, -2.68171e-05, 0.168401, 2.30608e-05, 0.00327427, 4.81938e-06, 0.00661021, -5.16453e-07, 0.00032946, -2.35526e-06, -0.000157527, -4.67592e-06, 0.000129838]` |
| 224 | w_M | `[0.00497026, -0.836283, 0.00027483, 0.252475, 0.00148454, 0.01724, -0.000160311, -0.0248005, -1.89671e-06, -0.00148433, 3.9083e-06, -0.00153412, 1.63021e-05, 0.00122303, 3.39886e-05, 0.00186372]` |
| 224 | w_Q | `[0.0105979, -1.60988, 0.00077429, 0.496089, -2.68139e-05, 0.168401, 2.30604e-05, 0.00327422, 4.81937e-06, 0.00661021, -5.16445e-07, 0.000329457, -2.35522e-06, -0.000157524, -4.67585e-06, 0.000129841]` |

## 6. Terminal storage composition

Population-wise shares of `x(T)^T M x(T)`:

| T (ms) | optimizer | V1_SS | V1_SP | V1_II | V1_DP | V4_SS | V4_SP | V4_II | V4_DP |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | w_M | 43.703% | 48.057% | 7.888% | 0.041% | 0.296% | 0.009% | 0.001% | 0.005% |
| 7 | w_Q | 42.060% | 48.945% | 8.649% | 0.021% | 0.310% | 0.009% | 0.001% | 0.005% |
| 14 | w_M | 84.236% | 3.811% | 11.271% | 0.649% | 0.023% | 0.004% | 0.002% | 0.003% |
| 14 | w_Q | 86.521% | 3.421% | 9.549% | 0.475% | 0.022% | 0.006% | 0.002% | 0.004% |
| 28 | w_M | 61.827% | 5.799% | 30.069% | 2.208% | 0.088% | 0.005% | 0.003% | 0.002% |
| 28 | w_Q | 41.870% | 6.407% | 48.170% | 3.311% | 0.204% | 0.012% | 0.010% | 0.016% |
| 56 | w_M | 63.427% | 4.936% | 17.941% | 13.683% | 0.001% | 0.000% | 0.001% | 0.011% |
| 56 | w_Q | 65.765% | 4.908% | 17.539% | 11.776% | 0.001% | 0.000% | 0.001% | 0.010% |
| 112 | w_M | 56.040% | 2.190% | 5.320% | 36.298% | 0.086% | 0.005% | 0.015% | 0.046% |
| 112 | w_Q | 50.726% | 1.645% | 5.478% | 41.919% | 0.149% | 0.008% | 0.022% | 0.052% |
| 224 | w_M | 63.351% | 1.991% | 8.595% | 25.889% | 0.061% | 0.005% | 0.018% | 0.091% |
| 224 | w_Q | 17.597% | 0.256% | 16.909% | 64.596% | 0.275% | 0.018% | 0.060% | 0.290% |

The terminal patterns are not identical. In particular, at 224 ms the storage-optimal preparation leaves about `63.4%` in V1-SS and `25.9%` in V1-DP, whereas the pathway-optimal preparation leaves about `17.6%` in V1-SS and `64.6%` in V1-DP. This provides a state-structure distinction in addition to the pulse-mixture distinction.

## 7. Signed pathway time distribution

For the pathway-optimal trajectory, decompose the cumulative signed quantity into the integral over times where the instantaneous fixed-pathway contribution is positive and where it is negative.

| T (ms) | net J_Q(w_Q) | positive-time integral | negative-time integral | sign crossings | q_max at ms | q_min at ms |
|---:|---:|---:|---:|---:|---:|---:|
| 7 | 1.322210704e-03 | 1.366123501e-03 | -4.391279705e-05 | 1 | 3.836315e-01 @ 2.485 | -6.108344e-02 @ 7.000 |
| 14 | 1.216507699e-03 | 1.402787542e-03 | -1.862798439e-04 | 2 | 3.839713e-01 @ 2.492 | -6.499096e-02 @ 7.434 |
| 28 | 1.243249974e-03 | 1.435980163e-03 | -1.927301890e-04 | 3 | 3.839739e-01 @ 2.492 | -6.499764e-02 @ 7.448 |
| 56 | 1.242526860e-03 | 1.438574643e-03 | -1.960477834e-04 | 5 | 3.839228e-01 @ 2.464 | -6.499016e-02 @ 7.448 |
| 112 | 1.242225387e-03 | 1.438575641e-03 | -1.963502547e-04 | 8 | 3.839228e-01 @ 2.464 | -6.495434e-02 @ 7.392 |
| 224 | 1.242228882e-03 | 1.438579133e-03 | -1.963502518e-04 | 11 | 3.839228e-01 @ 2.464 | -6.495433e-02 @ 7.392 |

The cumulative positive optimum is not obtained by making the instantaneous pathway signal positive at all times. The frozen pathway signal changes sign and contains a reproducible negative contribution; the signed integral is retained exactly as preregistered.

At the long horizons the positive and negative pathway contributions have essentially saturated, explaining why the pathway-optimal pulse mixture becomes nearly horizon-independent.

## 8. Gap interpretation

At 112 ms:

```math
J_Q^+ = 1.242225387e-03,
```

while the terminal-storage optimizer achieves only

```math
w_M^T K_Q w_M = 5.850220180e-04,
```

giving

```math
Delta_Q = 0.529017.
```

At 224 ms:

```math
J_Q^+ = 1.242228882e-03,
```

while

```math
w_M^T K_Q w_M = 2.262776424e-04,
```

giving

```math
Delta_Q = 0.817841.
```

Therefore the terminal-storage-optimal admissible preparation misses about `52.9%` and `81.8%`, respectively, of the maximum positive cumulative contribution of the **predefined V1-SP -> V4-SS pathway** available within the same fixed two-pulse input space.

## 9. Frozen verdict

The preregistered `NEURO-STRONG` conditions are satisfied:

1. all structural/numerical checks pass;
2. `J_Q^+` is nonzero and interpretable;
3. `theta>=20 deg` and `Delta_Q>=0.25` hold at the neighboring fixed horizons 112 and 224 ms;
4. the separation has a direct physical/input interpretation: the pathway optimum uses a dominant recent pulse plus a small opposite-sign older pulse, whereas the storage optimum uses same-sign pulses and progressively favors the older component at long horizons;
5. terminal population composition provides an additional state-space distinction.

Hence

```text
NEURO-STRONG
```

is the unique frozen verdict.

## 10. Allowed interpretation

Allowed:

> In the frozen stable two-source V1/V4 CMC/DCM demonstrator and the frozen two-pulse afferent preparation space, the preparation maximizing final model-internal synaptic-filter storage is nonredundant with the preparation maximizing the signed cumulative contribution of the predefined V1-SP -> V4-SS pathway. The preregistered strong-separation criteria are met at two neighboring long horizons.

Also allowed:

> The pathway-optimal and storage-optimal preparations correspond to experimentally distinct mixtures of the same two admissible afferent pulse components.

## 11. Forbidden interpretation

This result does **not** establish:

- a universal property of cortex or all neural-mass models;
- metabolic or thermodynamic brain-energy optimization;
- generic neural information flow;
- causal superiority of V1/V4 over another network chosen after the fact;
- a claim about delayed CMC/DDE dynamics;
- a claim that the two-pulse protocol is already an experimentally optimal stimulation waveform;
- novelty over all quadratic-output/control mathematics;
- robustness to parameter, subject, pathway, delay, or model variation not preregistered here.

No follow-on tuning is performed in this execution.

## 12. Reproducibility outputs

Canonical machine-readable results:

`research/neuro/neuro_pilot_0_1_execution_data.csv`

Canonical numerical tests:

`tests/test_neuro_pilot_0_1.py`

The test reconstructs the frozen `A`, `M`, `Q`, afferent pulse map `B`, structural gates, semigroup check, cumulative-channel quadrature check and finite-time operator Hermiticity/PSD checks.

**STOP.**
