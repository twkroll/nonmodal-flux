# D10-ZF Objective Resolution Qualification 0.1

**Date:** 2026-09-02  
**Status:** COMPLETE; classification = **RESOLUTION-ROBUST SEPARATION**.

## Scope lock

The physical D10-ZF point is unchanged from Pilot 0.1:

```math
U(x)=\cos x,\qquad L_x=2\pi,\qquad k_y=1,
```

```math
C=1,\qquad \kappa=1,\qquad N(x)=0,\qquad \nu_\perp=0.
```

The profile coefficients remain `u_{-1}=u_{+1}=1/2`, `k_0=1`, the target observable remains the physics-derived `Q_Gamma`, and the full retained state remains admissible (`B=I`, `R_in=M` at each truncation). No physical parameter, observable, input map, or horizon is changed.

Only the centered symmetric Fourier-Galerkin truncation is varied in the fixed sequence

```math
K\in\{1,2,4,8,16,32,64\},\qquad m=-K,\ldots,K,
```

with the already preregistered horizons

```math
T\in\{0.25,0.5,1,2,4,8\}.
```

No parameter search, MODES/CONT/CASCADE extension, or new theory is performed.

## Definitions used in this qualification

With the natural energy whitening, `v=M^{1/2}u`, the terminal free-energy operator and cumulative transport operator are evaluated exactly as in Pilot 0.1. The extremal values are

```math
G_{E,K}(T)=\lambda_{\max}(K_{E,K}(T)),
```

```math
\mathcal G_{\Gamma,+,K}(T)=\lambda_{\max}(K_{\Gamma,K}(T)),
\qquad
\mathcal G_{\Gamma,-,K}(T)=\lambda_{\min}(K_{\Gamma,K}(T)).
```

For this resolution qualification the transport-separation gap is reported in the explicitly dimensionless form

```math
\Delta_{\Gamma,K}(T)
=\frac{\mathcal G_{\Gamma,+,K}(T)-J_\Gamma(T;u_{E,K}^\star)}
       {\mathcal G_{\Gamma,+,K}(T)}.
```

All tested positive extrema are strictly positive, so this normalization is well-defined. Thus `Delta_Gamma=0` would mean that the energy-optimal input is also transport-optimal, whereas positive `Delta_Gamma` gives the fractional transport loss incurred by using the energy optimizer instead of the transport optimizer.

The earlier Pilot-0.1 report used the dimensional numerator under the same informal name. This qualification uses the normalized dimensionless quantity required here; no Pilot-0.1 numerical result is otherwise altered.

## 1. Terminal free-energy gains

| K | 0.25 | 0.5 | 1 | 2 | 4 | 8 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1.132542 | 1.278912 | 1.606778 | 2.371873 | 3.743614 | 4.046989 |
| 2 | 1.171103 | 1.368186 | 1.844865 | 3.177685 | 7.214765 | 9.510772 |
| 4 | 1.186199 | 1.404542 | 1.951677 | 3.628863 | 10.543888 | 31.982848 |
| 8 | 1.186546 | 1.405437 | 1.954930 | 3.652474 | 11.044496 | 54.220733 |
| 16 | 1.186546 | 1.405437 | 1.954930 | 3.652475 | 11.044786 | 54.759054 |
| 32 | 1.186546 | 1.405437 | 1.954930 | 3.652475 | 11.044786 | 54.759054 |
| 64 | 1.186546 | 1.405437 | 1.954930 | 3.652475 | 11.044786 | 54.759054 |

The minimal `K=1` truncation substantially under-resolves the long-horizon energy gain. The values stabilize by `K=16` for all preregistered horizons.

## 2. Positive cumulative signed transport extrema

| K | 0.25 | 0.5 | 1 | 2 | 4 | 8 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.110877 | 0.200464 | 0.356795 | 0.730105 | 1.858140 | 3.810892 |
| 2 | 0.110879 | 0.200566 | 0.360264 | 0.795396 | 2.627990 | 8.023394 |
| 4 | 0.110879 | 0.200567 | 0.360394 | 0.805985 | 3.066942 | 16.521478 |
| 8 | 0.110879 | 0.200567 | 0.360394 | 0.806023 | 3.087565 | 20.525180 |
| 16 | 0.110879 | 0.200567 | 0.360394 | 0.806023 | 3.087566 | 20.552377 |
| 32 | 0.110879 | 0.200567 | 0.360394 | 0.806023 | 3.087566 | 20.552377 |
| 64 | 0.110879 | 0.200567 | 0.360394 | 0.806023 | 3.087566 | 20.552377 |

The positive branch also converges rapidly at short horizons and requires higher sidebands at `T=4,8`. It is stable by `K=16` over the full horizon set.

## 3. Negative cumulative signed transport extrema

| K | 0.25 | 0.5 | 1 | 2 | 4 | 8 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | -0.087746 | -0.127625 | -0.147603 | -0.135418 | -0.110428 | -0.079051 |
| 2 | -0.087748 | -0.127657 | -0.147878 | -0.134891 | -0.117627 | -0.094773 |
| 4 | -0.087748 | -0.127658 | -0.147887 | -0.134950 | -0.119326 | -0.113318 |
| 8 | -0.087748 | -0.127658 | -0.147887 | -0.134950 | -0.119332 | -0.114901 |
| 16 | -0.087748 | -0.127658 | -0.147887 | -0.134950 | -0.119332 | -0.114902 |
| 32 | -0.087748 | -0.127658 | -0.147887 | -0.134950 | -0.119332 | -0.114902 |
| 64 | -0.087748 | -0.127658 | -0.147887 | -0.134950 | -0.119332 | -0.114902 |

The signed nature of the cumulative transport operator is therefore resolution robust: every tested `(K,T)` satisfies

```math
\mathcal G_{\Gamma,-,K}(T)<0<\mathcal G_{\Gamma,+,K}(T).
```

## 4. Dimensionless transport-separation gap

| K | 0.25 | 0.5 | 1 | 2 | 4 | 8 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.549660 | 0.468896 | 0.321208 | 0.158680 | 0.112693 | 0.378117 |
| 2 | 0.639476 | 0.562525 | 0.403233 | 0.190140 | 0.087435 | 0.151149 |
| 4 | 0.705080 | 0.638822 | 0.494999 | 0.273156 | 0.118223 | 0.110851 |
| 8 | 0.708365 | 0.643014 | 0.501743 | 0.286519 | 0.143520 | 0.127652 |
| 16 | 0.708365 | 0.643014 | 0.501744 | 0.286521 | 0.143576 | 0.132478 |
| 32 | 0.708365 | 0.643014 | 0.501744 | 0.286521 | 0.143576 | 0.132478 |
| 64 | 0.708365 | 0.643014 | 0.501744 | 0.286521 | 0.143576 | 0.132478 |

The dimensionless gap remains strictly positive for all 42 preregistered resolution/horizon pairs and converges to a nonzero value at every horizon. This is the first direct resolution test of the Pilot-0.1 objective mismatch.

At `K=64`, the converged fractional transport loss from using the energy optimizer is approximately

```text
T=0.25 : 70.84 %
T=0.5  : 64.30 %
T=1    : 50.17 %
T=2    : 28.65 %
T=4    : 14.36 %
T=8    : 13.25 %
```

No interpretation as a stable-nonmodal benchmark is made here; this qualification concerns only objective resolution at the unchanged physical point.

## 5. Optimizer comparison without cross-dimension raw-vector angles

Raw eigenvectors from different `K` live in different state spaces, so they are not compared directly. Instead the comparison uses the common physical energy whitening and three dimension-robust diagnostics.

### 5.1 Fourier-mode energy distributions

For an `M`-normalized optimizer let `v=M^{1/2}u`. Define the per-radial-mode input-energy weight

```math
w_m(v)=|v_{\phi,m}|^2+|v_{\eta,m}|^2,
\qquad
\sum_m w_m=1.
```

This produces a probability-like distribution on the retained radial Fourier indices and is directly comparable after embedding lower-resolution distributions into the larger mode set with zero tail weights.

At `K=64` the dominant `|m|` locations are:

| T | energy optimizer dominant `|m|` | transport optimizer dominant `|m|` |
|---:|---:|---:|
| 0.25 | 1 | 0 |
| 0.5 | 1 | 0 |
| 1 | 2 | 0 |
| 2 | 2 | 0 |
| 4 | 3 | 2 |
| 8 | 6 | 4 |

Thus the longer-horizon optimizers genuinely require sidebands absent from the original `K=1` pilot. The energy and transport optimizers do not converge to the same Fourier distribution.

Using total-variation distance between the embedded mode-weight distributions and `K=64`, the worst error over all six horizons is:

| K | energy optimizer max TV distance | transport optimizer max TV distance |
|---:|---:|---:|
| 1 | 0.997802 | 0.993049 |
| 2 | 0.996388 | 0.945395 |
| 4 | 0.837031 | 0.525433 |
| 8 | 0.076272 | 0.012819 |
| 16 | `3.1e-8` | `3.2e-10` |
| 32 | `4.1e-13` | `2.9e-14` |

The large errors for `K<=4` are dominated by the long horizons. The distributions themselves are numerically converged by `K=16`.

### 5.2 `phi/eta` structure

In the same whitened coordinates define

```math
f_\phi(v)=\sum_m |v_{\phi,m}|^2,
\qquad
f_\eta(v)=1-f_\phi(v).
```

At `K=64`:

| T | `f_phi` energy | `f_phi` transport |
|---:|---:|---:|
| 0.25 | 0.794525 | 0.557099 |
| 0.5 | 0.807310 | 0.603440 |
| 1 | 0.827660 | 0.670759 |
| 2 | 0.859830 | 0.756514 |
| 4 | 0.913538 | 0.855087 |
| 8 | 0.969082 | 0.948848 |

The two optimizer families retain distinct `phi/eta` composition at every horizon. The `K=16` fractions agree with `K=64` to below `1e-7` for the energy optimizer and below `1e-8` for the transport optimizer over the complete horizon set.

### 5.3 Common low-mode projections

Let `P_1` retain only the common modes `|m|<=1` in both fields. For each optimizer family compare the normalized low-mode projection at finite `K` with the `K=64` low-mode projection through the phase-invariant overlap

```math
\rho_{\rm low}(K,64)
=\frac{|\langle P_1v_K,P_1v_{64}\rangle|}
{\|P_1v_K\|\,\|P_1v_{64}\|}.
```

The minimum over all six horizons is:

| K | min `rho_low` energy | min `rho_low` transport |
|---:|---:|---:|
| 1 | 0.801684 | 0.932930 |
| 2 | 0.523745 | 0.805747 |
| 4 | 0.959242 | 0.988249 |
| 8 | 0.999986 | 0.999999 |
| 16 | 1.000000 | 1.000000 |
| 32 | 1.000000 | 1.000000 |

Thus even when the long-horizon optimizers move most of their weight to higher sidebands, their common low-mode content converges consistently rather than wandering with resolution.

For context only, within a fixed `K` it is legitimate to compute the ordinary phase-invariant angle between the two optimizers because they then live in the same space. At `K=64` these angles are approximately

```text
65.52, 61.62, 53.21, 40.53, 27.99, 26.74 degrees
```

for increasing horizon. These angles are not used as the cross-resolution convergence criterion.

## 6. Numerical convergence summary

Taking `K=64` as the reference within the prescribed sequence, the maximum discrepancy over all six horizons is:

| K | max rel. error `G_E` | max rel. error `G_Gamma,+` | max rel. error `G_Gamma,-` | max abs. error `Delta_Gamma` |
|---:|---:|---:|---:|---:|
| 1 | 0.926 | 0.815 | 0.312 | 0.246 |
| 2 | 0.826 | 0.610 | 0.175 | 0.0985 |
| 4 | 0.416 | 0.196 | 0.0138 | 0.0254 |
| 8 | 0.00983 | 0.00132 | `5.2e-6` | 0.00483 |
| 16 | `8.4e-10` | `7.9e-12` | `6.8e-15` | `1.6e-9` |
| 32 | `8.8e-15` | `1.0e-14` | `3.2e-14` | `5.9e-15` |

The strongest resolution demand occurs at `T=8`, not at the short horizons. Nevertheless all objective values, the normalized gap, the `phi/eta` fractions, the Fourier distributions, and the common low-mode projections are converged by `K=16` within the prescribed sequence.

## 7. Classification

The three allowed classifications are:

- `RESOLUTION-ROBUST SEPARATION`
- `SEPARATION COLLAPSES`
- `NONCONVERGENT / INCONCLUSIVE`

The data support

```text
RESOLUTION-ROBUST SEPARATION
```

because:

1. `G_Gamma,- < 0 < G_Gamma,+` at every tested `(K,T)`;
2. the dimensionless `Delta_Gamma,K(T)` remains positive for every tested `(K,T)` and converges to a nonzero value at all six horizons;
3. the optimizer Fourier distributions converge by `K=16` and remain different between the two objective families;
4. the `phi/eta` composition converges and remains different;
5. the projected common-low-mode optimizer content converges phase-invariantly;
6. all scalar objective values are stable between `K=16,32,64`.

This classification does **not** change the separate stability qualification: Pilot 0.1 still fails its original `K=1` spectral-stability gate, while the preceding stability-resolution study found `alpha(A_K)->0+` numerically. The present result says only that the energy-versus-signed-transport objective separation is itself resolution robust at the unchanged D10-ZF physical point.

The complete numerical rows are stored in `research/d10_zf_objective_resolution_qualification_0_1_data.csv`.

**STOP.**