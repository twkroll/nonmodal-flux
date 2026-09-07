# Fusion F2.7 `0_2` — Numerical / Spectral Qualification on F2.6B Source-Level Operator

**Date:** 2026-09-07  
**Authority:** MASTER / `research/master/prompts/fusion_f2_7_rerun_on_f2_6b_source_operator_0_1.md`  
**Status:** `F2.7 PASS — SPECTRALLY UNSTABLE / NUMERICALLY QUALIFIED — RETURN TO MASTER`

## Executive verdict

The frozen F2.6B source-level operator is spectrally unstable on every member of the frozen K0/K1/K2 ladder.

All spectral quantities in this report belong exclusively to the new canonical F2.6B realization

`research/fusion/fusion_f2_6b_operator_0_1.py`

at commit `83f004412183d43a1653d3a3a2f9ad104482de7d`. They do **not** belong to the unrecoverable historical F2.6 `0_3` source realization.

The retained, directly certified eigenvalues are

\[
\boxed{
\lambda_{K0}=0.0221552877943+0.0463690913769\,i,
}
\]

\[
\boxed{
\lambda_{K1}=0.00730158359482590+0.0333949532678270\,i,
}
\]

\[
\boxed{
\lambda_{K2}=0.00621516166872793+0.0273172444169728\,i.
}
\]

Therefore

\[
\alpha_K\equiv\max\operatorname{Re}\sigma(A_K)
\ge \operatorname{Re}\lambda_K>0
\]

for K0, K1 and K2. Hence the sign of the spectral abscissa is unambiguous on the complete frozen ladder:

\[
\boxed{\alpha_{K0}>0,\qquad\alpha_{K1}>0,\qquad\alpha_{K2}>0.}
\]

This gate does **not** claim that the three reported eigenvalues are globally exact maximizers of `Re(lambda)`. A global maximizer is unnecessary for the stable/unstable decision: one residual-certified positive eigenvalue already proves `alpha_K>0`. The reported values are therefore rigorous positive lower bounds on the spectral abscissa and the retained unstable branch used for classification.

## 1. Frozen operator and dimensions

No source-level change was made to F2.6B. The generator remains

\[
A_K=E_K^{-1}F_K
\]

through the committed public interfaces `apply_F` and `solve_E`.

The state dimensions are

\[
N(K0,K1,K2)=(18608,\ 93204,\ 361152),
\]

with repaired magnetic-moment orders

\[
N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.
\]

The F2.6B normalized `E`-Schur condition numbers remain modest:

\[
2.77156,\qquad2.91289,\qquad2.95377.
\]

No damping, collision, filter, loading, clipping, parameter change or resolution change was introduced.

## 2. Final spectral method

Direct unshifted `which=LR` Krylov attempts were inefficient because the conservative kinetic spectrum spans a broad imaginary range. They were not used as retained certification results.

The final calculation instead exploits the exact low-rank electrostatic field coupling of the frozen F2.6B operator. In kinetic `D^{1/2}` similarity coordinates, which leave the spectrum unchanged, the eigenproblem can be reduced exactly to the field-space dispersion relation

\[
\boxed{
\det H_K(\lambda)=0,
\qquad
H_K(\lambda)
=C_K+S_K(K_K-\lambda I)^{-1}(U_K+\lambda R_K).
}
\]

Ion kinetic resolvents are evaluated independently for every frozen Gauss--Laguerre magnetic-moment node with sparse LU. The trapped-electron contribution is evaluated analytically from its diagonal bounce-averaged kinetic block. The field matrix has dimensions only `Ntheta x Ntheta`: 71, 159 and 279 on K0/K1/K2.

The nonlinear field root is refined with an SVD/Newton step using the left/right singular vectors associated with the smallest singular value. Final state vectors are reconstructed from the kinetic resolvents and then checked directly against the **original** frozen `op.apply_A` implementation. Thus the field reduction is only a solver representation; the acceptance residual is taken on the canonical full operator.

Final acceptance tolerance was

\[
\frac{\|A_Kx-\lambda x\|_D}
{\|A_Kx\|_D+|\lambda|\|x\|_D}
\le10^{-10}.
\]

No retained ARPACK Ritz set is used in the verdict (`Ritz requested/converged = 0/0`); one targeted eigenpair was requested and converged on each level.

## 3. K0 qualification

At

\[
\lambda_{K0}=0.0221552877943+0.0463690913769i
\]

the field dispersion singular-value ratio is

\[
\sigma_{\min}/\sigma_{\max}=3.66\times10^{-13},
\]

and the residual on the original full F2.6B operator is

\[
\boxed{r_{D,K0}=9.16\times10^{-13}.}
\]

The equivalent generalized residual of `F-lambda E` is `9.22e-13`.

An independent full-field Newton repetition started at

\[
0.0229552877943+0.0457690913769i
\]

and converged to

\[
0.022155287794280967+0.04636909137688153i,
\]

only `2.65e-14` from the primary value. Its terminal field singular ratio is `5.82e-16`.

Hence

\[
\alpha_{K0}\ge0.0221552877943>0.
\]

## 4. K1 qualification

At

\[
\lambda_{K1}=0.0073015835948259025+0.03339495326782699i
\]

the field singular ratio is

\[
6.80\times10^{-16},
\]

and the direct full-operator residual is

\[
\boxed{r_{D,K1}=6.93\times10^{-14}.}
\]

The generalized residual is `6.99e-14`.

An independent repetition started at

\[
0.007701583594825903+0.03369495326782699i
\]

and converged to

\[
0.007301583594824753+0.033394953267829035i,
\]

only `2.35e-15` from the primary value.

Hence

\[
\alpha_{K1}\ge0.00730158359482590>0.
\]

## 5. K2 qualification

K2 was the controlling refinement test. Low-order 4-/8-/16-magnetic-moment subsets were used only to localize the same field-coupled branch; none of those truncated results was accepted as a final spectral result.

The 16-node localization gave

\[
0.006215161649482904+0.027317244460574392i.
\]

A **full 40-node** Newton solve shifted this by only

\[
(1.92-4.36i)\times10^{-11},
\]

and the next full Newton step was only `2.78e-17`. The final full 40-node result is

\[
\boxed{
\lambda_{K2}
=0.006215161668727925+0.027317244416972773i.
}
\]

The final 279-dimensional dispersion matrix has

\[
\boxed{
\sigma_{\min}/\sigma_{\max}=2.97\times10^{-16}.
}
\]

Reconstruction of **all 40 ion magnetic-moment blocks** followed by direct application of the original 361152-dimensional F2.6B generator gives

\[
\boxed{r_{D,K2}=5.21\times10^{-14},}
\]

with generalized residual

\[
5.20\times10^{-14}.
\]

The largest raw sparse kinetic-block solve residual is `1.14e-5`, occurring in extremely weakly weighted high-`zeta` blocks; this does not control the canonical result. The directly evaluated full `D`-weighted state residual above is the acceptance quantity and is at roundoff-scale relative accuracy.

For the required independent repetition, a separate full 40-node solve was started at

\[
0.006389143+0.02757067i.
\]

Three full Newton updates produced

\[
0.006215161668746496+0.027317244416965134i,
\]

only

\[
2.01\times10^{-14}
\]

from the primary full-K2 result.

Hence

\[
\alpha_{K2}\ge0.006215161668727925>0.
\]

## 6. Frozen-ladder robustness

The certified positive real parts are

\[
0.0221552877943,
\qquad
0.00730158359483,
\qquad
0.00621516166873.
\]

They shift materially from K0 to K1, but the sign remains positive and K1-to-K2 changes are much smaller. Most importantly, each positive value exceeds its direct numerical residual by many orders of magnitude. There is therefore no marginal-sign ambiguity on any frozen level.

The robust classification is

\[
\boxed{
\text{spectrally unstable on K0, K1 and K2}.
}
\]

No no-rescue action is taken. The point is reported as unstable exactly as frozen.

## 7. Sensitivity and scope

No left eigenvectors of the full generator were computed, so no standard left/right eigenvalue condition number is reported. The field SVD was used only to solve and certify the dispersion root; it is not interpreted as a transport optimizer or nonmodal object.

No pseudospectral analysis was required. No matrix exponential, propagator, Gramian, cumulative channel operator, finite-time objective, optimal perturbation, principal angle, gap or horizon curve was constructed.

## Verdict

The F2.6B benchmark point has a residual-certified positive eigenvalue on every member of the frozen refinement ladder. Therefore the sign of the spectral abscissa is numerically qualified as positive:

\[
\boxed{
\text{F2.7 PASS — SPECTRALLY UNSTABLE / NUMERICALLY QUALIFIED — RETURN TO MASTER}.
}
\]

**STOP / RETURN TO MASTER.**
