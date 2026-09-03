# Climate Intra-Domain Contrast Pilot 0.1 — Execution Results

**Status:** `EXECUTION COMPLETE`  
**Frozen one-shot verdict:** `CLIM-B-FAIL`  
**Failure reason:** preregistered resolution-robustness gate  
**Authority:** `research/master/climate_intra_domain_contrast_pilot_freeze_0_1.md` and `research/master/prompts/climate_intra_domain_contrast_pilot_execution_0_1.md`

This file records the single authorized finite-time execution of Climate-B. No physical parameter, jet profile, damping, basis, quadrature, state ordering, channel, input geometry, resolution role, horizon, numerical tolerance, degeneracy rule, denominator rule, robustness threshold, or verdict criterion was changed after effect inspection began. Climate-A remains permanently frozen as `CLIM-WEAK`.

## 1. Scope and frozen problem

Executed exactly the frozen equivalent-barotropic Bickley-jet pilot

\[
\partial_t\zeta'+U\partial_x\zeta'+(\beta-U'')\partial_x\psi'=-r\zeta',
\qquad
\zeta'=\nabla^2\psi',
\qquad
U(y)=U_0\operatorname{sech}^2(y/L),
\]

at the immutable point

\[
\beta=1.6\times10^{-11}\,\mathrm{m^{-1}s^{-1}},\quad
U_0=20\,\mathrm{m\,s^{-1}},\quad
L=1000\,\mathrm{km},\quad
r=(10\,\mathrm d)^{-1},
\]

\[
L_x=20000\,\mathrm{km},\qquad L_y=10000\,\mathrm{km},
\qquad \tau_{\rm ref}=L/U_0=50000\,\mathrm s.
\]

No parameter search, retuning, extra horizon, extra resolution, alternative jet/channel, third Climate candidate, manuscript rewrite, or novelty search was performed.

The retained qualified objects were

\[
(A_K,M_K,Q_{{\rm shift},K},B=I,R_{\rm in}=M_K),
\]

where `M_K` is perturbation kinetic energy and `Q_shift,K` is signed eddy forcing of the infinitesimal poleward translation tangent \(g=-U'\). `J_shift` is cumulative forcing/impulse under frozen tangent dynamics, not a realized nonlinear jet displacement.

## 2. Executed finite-time definitions

With \(x(0)=M_K^{-1/2}w\), \(\|w\|_2=1\),

\[
K_M=M_K^{-1/2}e^{A_K^\dagger T}M_Ke^{A_KT}M_K^{-1/2},
\]

\[
K_{\rm shift}=M_K^{-1/2}
\left[\int_0^T e^{A_K^\dagger t}Q_{{\rm shift},K}e^{A_Kt}\,dt\right]
M_K^{-1/2},
\]

\[
G_M=\lambda_{\max}(K_M),\qquad
J_{\rm shift}^{+}=\lambda_{\max}(K_{\rm shift}),\qquad
J_{\rm shift}^{-}=\lambda_{\min}(K_{\rm shift}).
\]

All six frozen horizons were executed:

\[
T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}.
\]

The mandatory effect roles remained primary `(16,32)`, confirmation `(20,40)`, and high audit `(24,48)`.

## 3. Numerical execution gates

Propagation used blockwise scaling-and-squaring Padé exponentials. The cumulative operator used the stable Lyapunov-tail identity as primary method and the frozen Van-Loan block exponential as an independent check. Hermiticity was checked before roundoff symmetrization.

| role | max eta_H(KM) | max eta_H(Kshift) | min eig(KM) | max Lyap-VL | max eig resid | max norm err | max Rayleigh err | max direct E err | max direct shift err | gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| primary | 3.692e-16 | 1.934e-15 | 0.011776 | 5.195e-13 | 2.437e-15 | 6.661e-16 | 1.870e-15 | 1.870e-15 | 8.676e-14 | PASS |
| confirmation | 2.751e-16 | 3.264e-15 | 0.0109308 | 9.153e-13 | 1.251e-15 | 8.882e-16 | 1.443e-15 | 1.055e-15 | 6.526e-14 | PASS |
| high | 2.895e-16 | 5.481e-15 | 0.0104981 | 1.055e-12 | 2.564e-15 | 6.661e-16 | 2.272e-15 | 2.272e-15 | 9.676e-14 | PASS |

All preregistered algebraic/direct tolerances passed. Across the three mandatory roles:

- worst Hermiticity residual: `5.49e-15` (`<=1e-11`);
- worst Lyapunov-tail / Van-Loan discrepancy: `1.06e-12` (`<=1e-10`);
- worst extremal eigenpair residual: `2.57e-15` (`<=1e-10`);
- worst normalization error: `8.89e-16` (`<=1e-12`);
- worst Rayleigh residual: `2.28e-15` (`<=1e-11`);
- worst direct terminal-energy error: `2.28e-15` (`<=1e-8`);
- worst direct reconstructed Reynolds-stress cumulative-shift error: `9.68e-14` (`<=1e-8`);
- minimum eigenvalue of `K_M` over mandatory calculations: `1.0498e-2`, so the PSD gate passed.

Thus the final failure is not caused by matrix assembly, integration, Hermiticity, eigensolver accuracy, PSD, or direct physical reproduction.

## 4. Complete mandatory finite-time results

All mandatory same-resolution optima were nondegenerate (`rank_M=rank_shift=1`).

| role | (Mx,Ny) | T/tau | G_M | J_shift+ | J_shift- | angle deg | Delta_shift | m_M | m_shift |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| primary | (16,32) | 0.25 | 1.13612538449 | 0.00842326709841 | -0.00842326709841 | 78.335985 | 1 | 16 | 16 |
| primary | (16,32) | 0.50 | 1.28852606098 | 0.0166804613143 | -0.0166804613143 | 77.447161 | 1 | 16 | 16 |
| primary | (16,32) | 1.00 | 1.64076115581 | 0.0330310539551 | -0.0330310539551 | 90.000000 | 1 | 14 | 15 |
| primary | (16,32) | 2.00 | 2.53595708218 | 0.0672409635209 | -0.0672409635209 | 90.000000 | 1 | 11 | 13 |
| primary | (16,32) | 4.00 | 5.22470562038 | 0.159791214148 | -0.159791214148 | 90.000000 | 1 | 8 | 9 |
| primary | (16,32) | 8.00 | 13.3276037897 | 0.526904307744 | -0.526904307744 | 90.000000 | 1 | 6 | 7 |
| confirmation | (20,40) | 0.25 | 1.14419221048 | 0.00906536441747 | -0.00906536441747 | 81.630286 | 1 | 20 | 20 |
| confirmation | (20,40) | 0.50 | 1.30683359676 | 0.0179697083856 | -0.0179697083856 | 80.577056 | 1 | 20 | 20 |
| confirmation | (20,40) | 1.00 | 1.68359414538 | 0.0356636156852 | -0.0356636156852 | 78.359691 | 1 | 20 | 20 |
| confirmation | (20,40) | 2.00 | 2.62953411297 | 0.0727055808295 | -0.0727055808295 | 90.000000 | 1 | 15 | 17 |
| confirmation | (20,40) | 4.00 | 5.3937450409 | 0.168925771128 | -0.168925771128 | 90.000000 | 1 | 9 | 11 |
| confirmation | (20,40) | 8.00 | 14.3582074471 | 0.574921216647 | -0.574921216647 | 90.000000 | 1 | 6 | 7 |
| high | (24,48) | 0.25 | 1.14986193666 | 0.00950415428384 | -0.00950415428384 | 84.271023 | 1 | 24 | 24 |
| high | (24,48) | 0.50 | 1.31982632599 | 0.0188556592596 | -0.0188556592596 | 83.222683 | 1 | 24 | 24 |
| high | (24,48) | 1.00 | 1.7171631299 | 0.0375398592055 | -0.0375398592055 | 80.893679 | 1 | 24 | 24 |
| high | (24,48) | 2.00 | 2.7084868712 | 0.0767513137858 | -0.0767513137858 | 90.000000 | 1 | 18 | 21 |
| high | (24,48) | 4.00 | 5.47277723322 | 0.174685553804 | -0.174685553804 | 90.000000 | 1 | 10 | 13 |
| high | (24,48) | 8.00 | 14.9499263072 | 0.596405332412 | -0.596405332413 | 90.000000 | 1 | 7 | 8 |

The signed extrema are symmetric to roundoff, \(J_{\rm shift}^-=-J_{\rm shift}^+\), as expected from the opposite-parity block structure.

At every fixed truncation the target-performance gap is

\[
\Delta_{\rm shift}=1
\]

to roundoff. The energy optimum lies in one preserved parity sector, while `K_shift` couples opposite parity sectors; hence the energy-optimal direction has zero cumulative signed shift forcing even though the positive shift optimum is nonzero.

This is a clean **same-resolution** result only. The frozen protocol does not allow it to be interpreted before refinement passes.

## 5. Resolution robustness — decisive failure

The frozen physical-claim gates require, for both primary→confirmation and confirmation→high refinement,

\[
\epsilon_Y\le0.02,\qquad
Y\in\{G_M,J_{\rm shift}^{+},|J_{\rm shift}^{-}|\},
\]

plus common-space captured mass

\[
\mu_c\ge0.95
\]

and maximum principal angle

\[
\theta_{\max}^{\rm res}\le10^\circ.
\]

| T/tau | eps G P-C | eps G C-H | eps J+ P-C | eps J+ C-H | mu_M P-C | theta_M P-C | mu_shift P-C | theta_shift P-C | mu_M C-H | theta_M C-H | mu_shift C-H | theta_shift C-H | robust |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.25 | 0.0071 | 0.0049 | 0.0708 | 0.0462 | 0.0000 | — | 0.0000 | — | 0.0000 | — | 0.0000 | — | FAIL |
| 0.50 | 0.0140 | 0.0098 | 0.0717 | 0.0470 | 0.0000 | — | 0.0000 | — | 0.0000 | — | 0.0000 | — | FAIL |
| 1.00 | 0.0254 | 0.0195 | 0.0738 | 0.0500 | 0.0000 | — | 0.0000 | — | 0.0000 | — | 0.0000 | — | FAIL |
| 2.00 | 0.0356 | 0.0292 | 0.0752 | 0.0527 | 0.6436 | 90.0000 | 0.0000 | — | 0.7010 | 90.0000 | 0.0000 | — | FAIL |
| 4.00 | 0.0313 | 0.0144 | 0.0541 | 0.0330 | 0.7832 | 90.0000 | 0.8428 | 90.0000 | 0.8890 | 90.0000 | 0.8818 | 90.0000 | FAIL |
| 8.00 | 0.0718 | 0.0396 | 0.0835 | 0.0360 | 0.7281 | 14.9831 | 0.7513 | 16.5056 | 0.7808 | 90.0000 | 0.8337 | 90.0000 | FAIL |

**Zero of the six frozen horizons is resolution robust.** Therefore the minimum requirement of two neighboring robust horizons fails.

At short horizons the optima migrate directly to newly admitted zonal wavenumbers: at `T/tau=0.25`, both objectives select `m=16` at primary, `m=20` at confirmation, and `m=24` at high audit, giving zero captured mass in the lower common zonal subspace.

At `T/tau=8`, where the optimum moves away from the immediate zonal cutoff, the failure persists: primary→confirmation captured masses are `0.7281` (energy) and `0.7513` (shift); confirmation→high masses are `0.7808` and `0.8337`. The signed objective also remains outside the frozen 2% value-convergence rule.

No extra rung, scale-selective damping, or other repair was added.

## 6. Physical/modal diagnostics

Primary-resolution initial-condition diagnostics are:

| T/tau | m_M | lambda_M km | M odd-n frac | m_shift | lambda_shift km | shift odd/even frac | dominant parity phase deg | q_shift(0) | q_shift(T) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.25 | 16 | 1250.0 | 1.000000 | 16 | 1250.0 | 0.500000/0.500000 | -89.84 | 0.0340718 | 0.033309 |
| 0.50 | 16 | 1250.0 | 1.000000 | 16 | 1250.0 | 0.500000/0.500000 | 88.41 | 0.0339027 | 0.0327982 |
| 1.00 | 14 | 1428.6 | 1.000000 | 15 | 1333.3 | 0.500000/0.500000 | 85.62 | 0.0332138 | 0.0327908 |
| 2.00 | 11 | 1818.2 | 1.000000 | 13 | 1538.5 | 0.500000/0.500000 | -97.30 | 0.0305166 | 0.0362111 |
| 4.00 | 8 | 2500.0 | 1.000000 | 9 | 2222.2 | 0.500000/0.500000 | -62.87 | 0.0193511 | 0.0595459 |
| 8.00 | 6 | 3333.3 | 1.000000 | 7 | 2857.1 | 0.500000/0.500000 | 111.46 | 0.00604288 | 0.110829 |

The energy optimum is pure odd-`n` parity to roundoff at every horizon. In the centered sine basis this is even about the jet center. Its reconstructed `q_shift(t)` remains at numerical zero (`~1e-16` or smaller), consistent with exact parity preservation.

The positive-shift optimum has essentially `50%/50%` initial kinetic-energy weight in the two parity sectors. Opposite-parity coefficients carry a near-quadrature phase and generate the Reynolds stress required for a signed projection onto \(g=-U'\).

At the longest primary horizon `T/tau=8`:

- energy optimum: `m=6`, wavelength `3333.3 km`, dominant `n=29,27,31,25,19`;
- shift optimum: `m=7`, wavelength `2857.1 km`, dominant `n=28,30,26,32,23`;
- shift parity fractions: `0.500000` odd and `0.500000` even;
- dominant opposite-parity phase: `111.46 deg`;
- initial Reynolds-stress extremum: `0.0190954` at `y/L=0.550`;
- momentum-flux-convergence extremum: `-0.055363` at `y/L=0.237`;
- initial positive translation projection: `q_shift(0)=0.00604288`.

Largest cumulative parity-pair contributions at primary `T/tau=8`:

- `(n_p,n_q)=(23,30)`: `0.015033619`
- `(n_p,n_q)=(25,30)`: `0.014885562`
- `(n_p,n_q)=(23,28)`: `0.014291711`
- `(n_p,n_q)=(25,28)`: `0.013952044`
- `(n_p,n_q)=(21,30)`: `0.012637457`

Representative primary positive-shift time histories:

| T/tau | q(0) | q(T/4) | q(T/2) | q(3T/4) | q(T) |
| --- | --- | --- | --- | --- | --- |
| 0.25 | 0.0340718 | 0.0338841 | 0.0336944 | 0.0335027 | 0.033309 |
| 0.50 | 0.0339027 | 0.0336378 | 0.0333666 | 0.0330865 | 0.0327982 |
| 1.00 | 0.0332138 | 0.033124 | 0.0330476 | 0.0329444 | 0.0327908 |
| 2.00 | 0.0305166 | 0.0319722 | 0.0337405 | 0.0353372 | 0.0362111 |
| 4.00 | 0.0193511 | 0.0275422 | 0.0398456 | 0.0526435 | 0.0595459 |
| 8.00 | 0.00604288 | 0.0177434 | 0.0634742 | 0.119514 | 0.110829 |

The apparent structure is itself resolution dependent. At `T/tau=8`, energy changes `m=6 → 6 → 7` and shift changes `m=7 → 7 → 8` from primary to confirmation to high audit, while meridional weight also redistributes strongly as `N_y` grows.

## 7. Gate ledger

| Gate | Result |
| --- | --- |
| inherited Candidate/Numerical Qualification freeze | PASS |
| all six fixed horizons reported | PASS |
| finite-time Hermiticity | PASS |
| `K_M` PSD | PASS |
| eigenpair / normalization / Rayleigh residuals | PASS |
| Lyapunov-tail vs Van-Loan cumulative operator | PASS |
| direct terminal-energy reproduction | PASS |
| direct reconstructed Reynolds-stress cumulative shift | PASS |
| positive signed denominator safely nonzero | PASS at all horizons |
| objective-value primary→confirmation robustness | **FAIL** |
| objective-value confirmation→high robustness | **FAIL** |
| common-space captured mass | **FAIL** |
| cross-resolution optimizer/subspace robustness | **FAIL** |
| at least two neighboring fully robust horizons | **FAIL (0 horizons)** |

## 8. Frozen one-shot verdict

The preregistered verdict precedence assigns `CLIM-B-FAIL` whenever the minimum two-neighbor resolution-robustness gate fails.

\[
\boxed{\text{CLIM-B-FAIL}}
\]

Reason:

\[
\boxed{\text{resolution robustness failure}}.
\]

`CLIM-B-STRONG` is not assigned. The large finite-resolution angles and \(\Delta_{\rm shift}=1\) are not permitted to support a physical demonstration because the optimizing scales and objective values do not survive the frozen refinement protocol.

## 9. Allowed / forbidden interpretation

Allowed:

- individual frozen truncations show strong energy-vs-shift objective dependence;
- energy-optimal perturbations occupy one parity sector and produce essentially zero signed translation impulse, while shift optima mix parities and produce positive impulse;
- this effect is strongly resolution sensitive, with optimizer mass migrating toward newly admitted small scales;
- the preregistered workflow correctly rejects the attractive finite-resolution result as non-robust;
- Climate-A remains independently frozen as `CLIM-WEAK`.

Forbidden:

- calling Climate-B a robust strong climate demonstration;
- quoting `90 deg` or `Delta_shift=1` without the resolution-failure qualification;
- interpreting `J_shift` as realized nonlinear jet displacement;
- retuning drag, adding hyperdiffusion, changing \(g=-U'\), adding localization/EOF/masks, changing horizons/resolutions, or opening a third Climate candidate to rescue the result.

## 10. Open issue

The one-shot execution exposes strong small-scale/truncation sensitivity under the frozen scale-independent Rayleigh damping. A future independently motivated study could investigate physically specified scale-selective dissipation or a separately justified admissible geometry. That question is outside Climate-B Pilot 0.1 and cannot repair this result.

## 11. Reproducibility

Machine-readable data:

`research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv`

Regression test:

`tests/test_climate_intra_domain_contrast_pilot_0_1.py`

Local regression result before commit: `3 passed`.

## 12. Final state

Climate-B has consumed the single additional Climate attempt authorized before the first manuscript. No third Climate candidate is authorized.

\[
\boxed{\text{CLIMATE-B EXECUTION COMPLETE — RETURN TO MASTER FOR RESULT INTEGRATION/FREEZE}}
\]

**STOP.**
