# Fusion F2.3 — Physical Geometry / Gradient / Wavenumber Parameter Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER / `research/master/prompts/fusion_f2_3_physical_parameter_freeze_0_1.md`  
**Status:** `F2.3 PASS — PHYSICAL GEOMETRY/GRADIENT/WAVENUMBER POINT FROZEN — RETURN TO MASTER`

## Scope

This gate freezes exactly one pre-effect numerical benchmark point for the already-frozen F2-R architecture

\[
\boxed{
\text{finite-ion-FLR electrostatic local-GK ions}
+\text{collisionless bounce-averaged trapped electrons}
}
\]

inside the F2.2 large-aspect-ratio circular `s-alpha` ballooning-space geometry family.

No geometry, gradient, wavenumber, trapped fraction or species parameter was scanned. No eigenvalue, growth rate, transient quantity, propagator, Gramian, cumulative objective, optimizer, phase-space discretization, kinetic input map, discrete `A/M/Q`, or GENE run was constructed or inspected.

The point is selected from standard Cyclone-Base-Case (CBC) benchmark conventions and a minimal documented `s-alpha` mapping. It is not selected by expected nonnormality, stability or objective separation.

---

## 1. Frozen benchmark point

The frozen reference-surface geometry is

\[
\boxed{
\frac{R_0}{a}=2.77778,
\qquad
\frac{r_0}{a}=0.5,
\qquad
\epsilon\equiv\frac{r_0}{R_0}=0.18,
\qquad
q=1.4,
\qquad
\hat s=0.8,
\qquad
\alpha_{\rm MHD}=0.
}
\]

`alpha_MHD=0` is the standard electrostatic/CBC `s-alpha` benchmark convention used to suppress equilibrium-pressure-gradient shaping/Shafranov-shift effects while retaining the kinetic equilibrium density and temperature gradients in the gyrokinetic drive. It is not a statement that the plasma pressure gradients vanish.

The frozen species are singly charged deuterium ions and electrons,

\[
Z_i=+1,
\qquad
Z_e=-1,
\qquad
\frac{m_i}{m_e}=3672,
\qquad
\frac{T_i}{T_e}=1,
\qquad
n_i=n_e.
\]

The primary F2-R candidate remains collisionless by the F2.1 architecture freeze. Hence no collision frequency is introduced or tuned in F2.3.

---

## 2. Frozen equilibrium gradients

Use outward-decreasing equilibrium profiles and the positive inverse-scale-length convention

\[
\frac{a}{L_X}\equiv-a\frac{d\ln X}{dr}>0.
\]

Freeze the standard equal-species CBC gradients

\[
\boxed{
\frac{a}{L_{n_i}}=rac{a}{L_{n_e}}=0.8,
\qquad
\frac{a}{L_{T_i}}=rac{a}{L_{T_e}}=2.49.
}
\]

With `R0/a=2.77778`, the equivalent major-radius normalization is

\[
\boxed{
\frac{R_0}{L_n}=2.222224,
\qquad
\frac{R_0}{L_{T_i}}=rac{R_0}{L_{T_e}}=6.9166722.
}
\]

The corresponding temperature-to-density gradient ratios are

\[
\eta_i=\eta_e
=\frac{d\ln T}{d\ln n}
=\frac{2.49}{0.8}
=3.1125.
\]

Because the density gradient and both species temperature gradients are nonzero, the F2.1 source decomposition has

\[
\boxed{
G_\Gamma\neq0,
\qquad
G_{T,i}\neq0,
\qquad
G_{T,e}\neq0.
}
\]

The signs are those already frozen in F2.1: the positive coefficients correspond to outward-decreasing equilibrium profiles under the physical radial particle/heat-flux definitions. No channel coefficient is inferred backwards from the free-energy balance.

---

## 3. Frozen perpendicular wavenumber / ballooning representative

Choose the positive nonzonal representative

\[
\boxed{k_y\rho_i=+0.3}
\]

in the F2.2 Fourier orientation. The negative-`k_y` partner remains the complex-conjugate representation of the same real physical perturbation and is not a second parameter point.

Freeze the canonical zero-ballooning-angle representative

\[
\boxed{
\theta_0=0
\quad\Longleftrightarrow\quad
k_{x0}=0.
}
\]

This is a coordinate/convention representative, not an effect-selected radial wavenumber. With `alpha_MHD=0`, the F2.2 metric factor is therefore

\[
\Lambda(\theta)=\hat s\,\theta=0.8\,\theta,
\]

and

\[
k_\perp^2(\theta)
=k_y^2\left[1+(0.8\theta)^2\right].
\]

At the outboard ballooning centre,

\[
k_\perp(0)\rho_i=0.3,
\]

so finite ion FLR is retained rather than expanded away.

---

## 4. Common normalization

Use the ion-temperature thermal-speed convention

\[
\boxed{
v_{Ti}=\sqrt{\frac{T_i}{m_i}}}
\]

and ion cyclotron frequency

\[
\Omega_i=\frac{eB_0}{m_i}
\]

in SI notation. Define

\[
\boxed{
\rho_i=\frac{v_{Ti}}{\Omega_i},
\qquad
\tau_{\rm ref}=\frac{R_0}{v_{Ti}}.
}
\]

Length is normalized by `R0`, time by `R0/vTi`, velocity by `vTi`, and perpendicular wavenumber by `rho_i^{-1}`.

Because `Ti=Te`, the usual sound gyroradius based on `c_s=sqrt(Te/mi)` equals this `rho_i`. Thus the common CBC notation `k_y rho_s=0.3` maps directly to the frozen `k_y rho_i=0.3` convention.

For later code mappings that use `v_th=sqrt(2T/m)`, the conversion is purely conventional:

\[
v_{th,i}=\sqrt2\,v_{Ti},
\qquad
\rho_{th,i}=\sqrt2\,\rho_i.
\]

No physical parameter is changed by that mapping.

---

## 5. Trapped-electron geometry implied by epsilon

For the frozen circular field family

\[
B(\theta)=\frac{B_0}{1+\epsilon\cos\theta},
\qquad \epsilon=0.18,
\]

one has

\[
\frac{B_{\min}}{B_0}=\frac1{1+\epsilon}=0.8474576,
\qquad
\frac{B_{\max}}{B_0}=\frac1{1-\epsilon}=1.2195122.
\]

With the F2.2 pitch variable `lambda` satisfying

\[
v_\parallel^2\propto1-\lambda B,
\]

and normalized pitch

\[
\widehat\lambda=\lambda B_0,
\]

the trapped interval is fixed geometrically as

\[
\boxed{
1-\epsilon<\widehat\lambda<1+\epsilon
\quad\Longrightarrow\quad
0.82<\widehat\lambda<1.18.
}
\]

The bounce points obey

\[
\cos\theta_b=\frac{\widehat\lambda-1}{\epsilon}.
\]

At the outboard field minimum, the corresponding trapped pitch-cosine interval is

\[
|\xi|<\xi_c,
\qquad
\xi_c
=\sqrt{1-\frac{B_{\min}}{B_{\max}}}
=\sqrt{\frac{2\epsilon}{1+\epsilon}}
\approx0.552345.
\]

Thus an isotropic local distribution at the outboard midplane has a pitch-cosine trapped fraction `xi_c ~= 0.5523`. This is a derived local geometric measure only; no independently tunable trapped-particle fraction is introduced. Any later flux-surface/bounce-weighted trapped density fraction must be computed from the frozen phase-space measure during the discretization/qualification gate rather than inserted as a new parameter.

---

## 6. Ordering checks

### 6.1 Finite ion FLR

At `theta=0`,

\[
k_\perp\rho_i=0.3,
\]

so the ion Bessel/gyroaverage operators are genuinely finite-FLR.

### 6.2 Electron FLR ordering

For `Ti=Te` and `mi/me=3672`,

\[
\frac{\rho_e}{\rho_i}
=\sqrt{\frac{m_e}{m_i}}
=0.0165025.
\]

Hence at the ballooning centre

\[
\boxed{k_\perp(0)\rho_e=0.0049507\ll1.}
\]

Because `k_perp(theta)` grows along the infinite ballooning line when `shat != 0`, the later finite-domain/discretization gate must verify `k_perp rho_e << 1` on the retained electron-support region. F2.3 does not choose a ballooning-domain cutoff.

### 6.3 Slow-electron-transit ordering

The thermal-speed ratio is

\[
\frac{v_{Te}}{v_{Ti}}
=\sqrt{\frac{m_i}{m_e}\frac{T_e}{T_i}}
=\sqrt{3672}
\approx60.60.
\]

Using `q=1.4`, the characteristic electron parallel-transit rate is approximately

\[
\frac{v_{Te}}{qR_0}
\approx43.3\,\frac{v_{Ti}}{R_0}.
\]

The ion-scale diamagnetic drive rate associated with `k_y rho_i=0.3` and `R0/L_T=6.9167` is only order

\[
(k_y\rho_i)\frac{R_0}{L_T}\frac{v_{Ti}}{R_0}
\approx2.08\,\frac{v_{Ti}}{R_0}.
\]

Thus the source ordering that passing electrons equilibrate rapidly along the field compared with the retained ion-scale dynamics is parametrically plausible by more than an order of magnitude. This is an ordering check only, not a spectral calculation.

### 6.4 Nonzero trapped-electron measure

`epsilon=0.18` gives a finite magnetic well and a nonzero trapped interval. The bounce-averaged electron sector is therefore nonempty at the frozen point.

---

## 7. Source table

| Frozen object | Value/convention | Source role |
|---|---|---|
| `R0/a`, `r/a`, `q`, `shat`, circular shape | `2.77778`, `0.5`, `1.4`, `0.8`, circular | Standard modern CBC stella/GS2 benchmark; consistent with the original Dimits CBC family. |
| `epsilon` | `0.18` | Derived from the CBC reference surface and independently standard in `s-alpha` CBC work. |
| `Ti/Te`, `ni/ne`, `mi/me` | `1`, `1`, `3672` | Two-species CBC benchmark convention for deuterium/electron local GK. |
| `a/Ln_i = a/Ln_e` | `0.8` | Standard equal-species CBC density gradient. |
| `a/LTi = a/LTe` | `2.49` | Kinetic-electron CBC extension with equal ion/electron temperature gradients. |
| `alpha_MHD` | `0` | Standard electrostatic `s-alpha` CBC benchmark mapping; kinetic pressure gradients remain finite. |
| `k_y rho_i` | `+0.3` | Canonical ion-scale CBC representative; with `Ti=Te`, `rho_i=rho_s` in the frozen convention. |
| `theta0`, `kx0` | `0`, `0` | F2.2 zero-ballooning-angle symmetry representative; a convention choice, not a fitted plasma parameter. |
| collision frequency | `0` in F2-R | Not selected in F2.3; inherited from the source-faithful collisionless F2.1 reduced architecture. |

Primary benchmark references used for the numerical conventions:

1. A. M. Dimits et al., *Comparisons and physics basis of tokamak transport models and turbulence simulations*, **Physics of Plasmas 7**, 969 (2000), DOI `10.1063/1.873896` — canonical Cyclone Base Case lineage.
2. A. von Boetticher et al., *Plasma Physics and Controlled Fusion* **66** (2024) 105016 — modern collisionless stella/GS2 CBC table with `R0/a=2.77778`, `r/a=0.5`, `q=1.4`, `shat=0.8`, equal species density/temperature gradients and deuterium/electron mass ratio.
3. N. R. Mandell et al., *GX: a GPU-native gyrokinetic turbulence code for tokamak and stellarator design*, **Journal of Plasma Physics 90**, 905900402 (2024), DOI `10.1017/S0022377824000631` — two-kinetic-species CBC mapping, circular geometry, equal species gradients and standard kinetic-electron mass-ratio conventions.
4. J. Candy and R. E. Waltz, *An Eulerian gyrokinetic-Maxwell solver*, **Journal of Computational Physics 186**, 545–581 (2003), DOI `10.1016/S0021-9991(03)00079-2` — CBC `s-alpha` benchmark usage with `alpha_MHD=0` and nonadiabatic-electron benchmarking.
5. Standard `s-alpha` CBC linear benchmarks use `epsilon ~= 0.18`, `q ~= 1.4`, `shat ~= 0.786-0.8` and `k_y rho_s=0.3`; F2.3 uses the rounded modern CBC table values above consistently rather than mixing different effect-selected points.

---

## 8. What is frozen and what remains unfrozen

### Frozen by F2.3

\[
\boxed{
\begin{gathered}
R_0/a=2.77778,
\quad r_0/a=0.5,
\quad \epsilon=0.18,
\quad q=1.4,
\quad \hat s=0.8,
\quad \alpha_{\rm MHD}=0,\\
Z_i=+1,
\quad Z_e=-1,
\quad m_i/m_e=3672,
\quad T_i/T_e=1,
\quad n_i=n_e,\\
a/L_n=0.8,
\quad a/L_{T_i}=a/L_{T_e}=2.49,\\
k_y\rho_i=+0.3,
\quad \theta_0=0,
\quad k_{x0}=0,\\
v_{Ti}=\sqrt{T_i/m_i},
\quad \rho_i=v_{Ti}/\Omega_i,
\quad \tau_{\rm ref}=R_0/v_{Ti}.
\end{gathered}
}
\]

### Still deliberately unfrozen

- kinetic admissible input map `B` and physical input cost `R_in`;
- ballooning-line truncation and parallel grid;
- ion energy/pitch/sign quadrature;
- trapped-electron energy/pitch/well quadrature and separatrix treatment;
- discrete quasineutrality solve;
- discrete `A`, `M`, particle-flux and species heat-flux operators;
- numerical/free-energy/spectral qualification;
- any finite-time propagator, cumulative operator or optimizer;
- fully kinetic reference collision-operator parameters and GENE execution details;
- an absolute dimensional realization `(R0, B0, n0, Ti)` because the local electrostatic benchmark is fixed by the dimensionless ratios above and does not require `rho_*` for the reduced linear operator.

---

## 9. Anti-bias record

No alternate geometry, gradient, temperature ratio, mass ratio, trapped fraction, `k_y`, `theta0`, or `alpha_MHD` value was evaluated for spectral stability, transient growth, heat flux, nonnormality or optimizer separation. The point was frozen directly from benchmark/source conventions before numerical kinetic execution.

No collision term was added to alter the F2-R balance. No R1 repair or FLR-only rescue was opened.

---

## 10. Verdict

The required geometry, species, thermodynamic-gradient and perpendicular-wavenumber quantities can be assigned coherently from a standard CBC two-species benchmark plus the already-frozen `s-alpha` mapping, without effect-guided mixing.

\[
\boxed{
\text{F2.3 PASS — PHYSICAL GEOMETRY/GRADIENT/WAVENUMBER POINT FROZEN — RETURN TO MASTER}
}
\]

The exact next pre-effect gate is intentionally not self-authorized here. MASTER must decide the kinetic admissible-input geometry / input-cost gate before any phase-space discretization or numerical optimization.

**STOP / RETURN TO MASTER.**
