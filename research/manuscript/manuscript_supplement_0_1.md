# Supplement to “Physics-informed diagnosis of objective nonredundancy in stable linear dynamics across plasma, neural and geophysical models”

**Supplement:** 0.1  
**Status:** SUBMISSION-ORIENTED COMPANION — FROZEN-EVIDENCE ONLY  
**Authority:** `research/master/prompts/manuscript_pre_submission_integration_revision_0_4.md`  
**Source:** Supplement S1–S6 content from `research/manuscript/manuscript_draft_0_3.md`, reorganized without new scientific content.

## S1. Analysis freeze chronology and reproducibility protocol

The analysis record uses a version-controlled sequence of model/candidate freezes, numerical qualifications, execution specifications, execution releases, frozen execution results, literature-positioning audits, result-integration freezes, manuscript claim freezes, and the manuscript structure freeze. The manuscript-facing terminology is **pre-specified and frozen before objective-separation evaluation** or **prospectively frozen in the version-controlled analysis record before effect inspection**.

Across applications, execution used fixed horizon ladders and prospectively defined structural/numerical gates. The common factor-of-two convention is: physical storage is `S_M=1/2 x^\dagger Mx`, whereas the finite-time terminal operator is written for `x^\dagger Mx`; this does not alter optimizer directions or normalized performance gaps.

The common study-specific strong application rule is `\vartheta>=20 deg` and `\Delta_Q>=0.25` on at least two neighboring frozen horizons, subject to all application-specific gates. Climate-A and Climate-B additionally use explicit cross-resolution objective-value and common-subspace tests. Failure of a frozen gate is retained as the result; no parameter, horizon, resolution, objective, or admissible geometry is changed to repair it.

The produced operational-rules/outcomes asset is reproduced as Supplement Table S1 in Sec. S6.1. The thresholds in that table are operational study rules, not universal physical constants.

## S2. Plasma detailed specification and numerical checks

The frozen D10-ZF point is `U(x)=cos x`, `L_x=2pi`, `k_y=C=kappa=1`, `N(x)=0`, with Pilot-0.2 damping `A=A_0-0.020I`. At resolution `K`, modes `m=-K,...,K` are retained and the state is ordered as all `phi_m` followed by all `eta_m`. With `Delta=diag[-(m^2+k_y^2)]`,

\[
M=
\begin{pmatrix}-\Delta&0\\0&I\end{pmatrix},
\qquad
Q_\Gamma=
\frac{k_y}{2}
\begin{pmatrix}0&iI\\-iI&0\end{pmatrix}.
\]

The input geometry is `B=I`, `R_in=M`. The frozen resolutions `K=32,64,96` have state dimensions 130, 258, and 386; the horizon ladder is `T={0.25,0.5,1,2,4,8}`.

All `S0-S5` gates pass. Maximum reported numerical defects include raw Hermiticity defects below about `3.7e-13`, optimizer-normalization error `1.4e-15`, transport eigen-residual `3.2e-14`, direct terminal-energy error `7.2e-14`, and direct cumulative-flux integration error `7.1e-8`. Projecting `K=96` optimizers onto the common `|m|<=32` subspace gives overlap one to floating-point precision and unresolved energy below about `2e-15`. The full horizon ledger is stored in `research/d10_zf_pilot_0_2_execution_data.csv`.

## S3. Neuro detailed specification and numerical checks

The frozen state is ordered region-major in `(v,z)` coordinates for V1 and V4 populations `(SS,SP,II,DP)`. The operating point is `x*=0`; synaptic time constants are `(2,2,16,28)` ms. The positive matrix is

\[
M={\rm diag}(
250000,1,250000,1,3906.25,1,1275.51020408163,1,
250000,1,250000,1,3906.25,1,1275.51020408163,1).
\]

For the frozen V1-SP -> V4-SS pathway,

\[
(A_{j\to i})_{10,3}=16666.6666666667\ {\rm s}^{-1},
\]

and

\[
(Q_{j\to i})_{10,3}=(Q_{j\to i})_{3,10}=8333.33333333333.
\]

The afferent vector is `b_aff,V1=16000e_2`. Two fixed unit-height 1-ms pulses occupy `[-3,-2]` ms and `[-17,-16]` ms relative to observation onset. Their effective propagated columns define `B`; `rank(B)=2`, the storage/input-whitened condition number is `34.294<100`, and `R_in=I_2`.

All frozen structural and numerical gates pass. The maximum semigroup error is `6.636e-14`; maximum primary/adaptive cumulative-operator disagreement is `2.291e-12`; raw finite-time Hermiticity residuals are below `1.361e-13`; direct trajectory reproduction errors are below `5e-10`. The full ledger is stored in `research/neuro/neuro_pilot_0_1_execution_data.csv` and `research/neuro/neuro_pilot_0_1_execution_results.md`.

## S4. Climate-A detailed specification and numerical checks

Climate-A uses the basis

\[
\phi_{mn}(x,y)
=
\exp\left(i\frac{2\pi m}{L_x}x\right)
\sin\left(\frac{\pi n}{L_y}y\right),
\qquad m\ne0,\ n\ge1,
\]

with mode state `x_mn=(psi_mn,tau_mn)^T` and exact real-field conjugacy. With `L_ref=L_D`, `U_ref=beta L_D^2=16 m s^-1`, `tau_ref=62500 s`, define

\[
k_m^*=\frac{2\pi m}{30},
\quad
\ell_n^*=\frac{\pi n}{10},
\quad
a_{mn}=k_m^{*2}+\ell_n^{*2},
\quad
b_{mn}=a_{mn}+1.
\]

The frozen modal blocks are

\[
A_{mn}=
\begin{pmatrix}
-r^*+ik_m^*/a_{mn}&-ik_m^*U^*\\
ik_m^*U^*(1-a_{mn})/b_{mn}&-r^*+ik_m^*/b_{mn}
\end{pmatrix},
\]

\[
M_{mn}=150
\begin{pmatrix}a_{mn}&0\\0&b_{mn}\end{pmatrix},
\qquad
Q_{{\rm heat},mn}=75
\begin{pmatrix}0&-ik_m^*\\ik_m^*&0\end{pmatrix},
\]

with `U^*=1/2` and `r^*=0.072337962962963`.

All mandatory algebraic, augmented-exponential/Lyapunov-tail, eigenpair, terminal-energy, direct heat-integral, and resolution gates pass. For all six horizons the objective values are invariant to reported precision under `(12,12)->(16,16)->(24,24)`, common-space captured mass is one, optimal-subspace rank remains two, and cross-resolution principal angles remain below `1.5e-6 deg`. The full ledger is stored in `research/climate/climate_ocean_pilot_0_1_execution_data.csv`.

## S5. Climate-B one-shot robustness-rejection case

Supplement Fig. S5 is the compact frozen-data visual summary of this section. It explicitly separates local numerical/direct PASS gates from cross-resolution FAIL gates and carries the frozen verdict **`CLIM-B-FAIL — resolution robustness failure`** together with `0/6` robust horizons.

### S5.1 Frozen model, metric, and signed channel

Climate-B is the single authorized equivalent-barotropic Bickley-jet candidate,

\[
\partial_t\zeta'
+U(y)\partial_x\zeta'
+[\beta-U''(y)]\partial_x\psi'
=-r\zeta',
\qquad
\zeta'=\nabla^2\psi',
\]

\[
U(y)=U_0\operatorname{sech}^2(y/L),
\]

at the fixed point

\[
\beta=1.6\times10^{-11}\ {\rm m^{-1}s^{-1}},
\quad U_0=20\ {\rm m\,s^{-1}},
\quad L=1000\ {\rm km},
\quad r=(10\ {\rm d})^{-1},
\]

\[
L_x=20000\ {\rm km},
\qquad L_y=10000\ {\rm km},
\qquad
\tau_{\rm ref}=L/U_0=50000\ {\rm s}.
\]

The positive metric is perturbation kinetic energy. The poleward jet-translation tangent is `g(y)=-U'(y)`, and the signed channel is

\[
q_{\rm shift}(t)
=
\frac{\int g(y)[-\partial_y\overline{u'v'}]dy}
{\int g(y)^2dy}.
\]

Positive sign denotes forcing in the poleward-translation direction. The cumulative `J_shift` is only cumulative eddy forcing/impulse of the infinitesimal translation coordinate under frozen tangent dynamics; it is not realized nonlinear jet displacement.

The positive-zonal-Fourier / centered-sine Galerkin representation retains `k_x!=0` eddies, exact real-field conjugacy, Dirichlet walls, and both meridional parity sectors. `A_K` preserves parity whereas `Q_shift,K` couples opposite parity. The retained eddy state is admissible, so `B=I`, `R_in=M_K`.

### S5.2 Frozen protocol and pre-effect qualification

The nested ladder is

| role | `(M_x,N_y)` | complex dimension |
|---|---:|---:|
| structural smoke | `(8,16)` | 128 |
| coarse audit | `(12,24)` | 288 |
| primary | `(16,32)` | 512 |
| confirmation | `(20,40)` | 800 |
| high-resolution audit | `(24,48)` | 1152 |

The executed horizon ladder is `T/tau_ref={0.25,0.5,1,2,4,8}`.

Before finite-time execution, the 512-versus-1024 Gauss-Legendre assembly audit passed with worst relative discrepancy `2.92e-14`; `M_K` was positive definite; `Q_shift,K` was Hermitian and indefinite; parity-forbidden residuals were at roundoff; the predeclared `c_11=1,c_12=+/-i` sign witness reproduced the channel directly to about `1e-14` relative; and every frozen resolution was spectrally stable with `alpha(A_K)=-0.1 d^-1`.

### S5.3 Local finite-time gates passed

At primary, confirmation, and high audit, all local finite-time gates passed. Across the mandatory runs:

- worst raw Hermiticity residual: `5.49e-15`;
- worst Lyapunov-tail / independent block-exponential discrepancy: `1.06e-12`;
- worst extremal eigenpair residual: `2.57e-15`;
- worst normalization error: `8.89e-16`;
- worst Rayleigh residual: `2.28e-15`;
- worst direct terminal-energy reproduction error: `2.28e-15`;
- worst direct reconstructed Reynolds-stress cumulative-shift error: `9.68e-14`;
- minimum finite-time energy-operator eigenvalue: `1.0498e-2`.

Thus the eventual failure is not an algebraic, integration, eigensolver, PSD, or direct physical-reproduction failure.

### S5.4 Fixed-resolution observation, with required failure qualification

At every individual frozen truncation the same-resolution target-performance gap is `Delta_shift=1` to roundoff and optimizer angles are large. At several primary-resolution horizons the angle is 90 degrees; at the two shortest horizons it is approximately 78.34 and 77.45 degrees. This behavior has a clean parity explanation: the energy optimum remains in one preserved parity sector and hence has zero cumulative signed shift forcing, whereas the shift optimum mixes opposite parity sectors. **These are qualified fixed-truncation observations only and are rejected as robust Climate evidence because the mandatory refinement gates fail.**

The pre-specified cross-resolution protocol required, for both primary-to-confirmation and confirmation-to-high refinement,

\[
\epsilon_Y\le0.02,
\qquad
Y\in\{G_M,J_{\rm shift}^+,|J_{\rm shift}^-|\},
\]

together with common-space captured mass `mu_c>=0.95` and largest common-space principal angle no greater than 10 degrees for both objective optima.

### S5.5 Complete resolution failure

Zero of the six frozen horizons passes the full resolution protocol.

At `T/tau_ref=0.25`, the positive-shift objective changes by approximately 7.08% from primary to confirmation and 4.62% from confirmation to high audit, exceeding the 2% rule. Both optima also migrate from zonal mode `m=16` to `20` to `24`, producing zero captured common-space mass in the lower zonal subspace.

At `T/tau_ref=8`, where the optima are no longer pinned directly to the immediate cutoff, the failure persists. Primary-to-confirmation captured masses are `0.7281` for energy and `0.7513` for shift; confirmation-to-high masses are `0.7808` and `0.8337`. The positive signed objective changes by approximately 8.35% and 3.60% over the two refinement steps, again outside the 2% rule, and the common-space angle gates also fail.

| `T/tau_ref` | robust? | principal frozen failure features |
|---:|---|---|
| 0.25 | FAIL | signed-objective nonconvergence; zero captured mass from cutoff migration |
| 0.5 | FAIL | signed-objective nonconvergence; zero captured mass from cutoff migration |
| 1 | FAIL | objective-value failures and cutoff migration |
| 2 | FAIL | objective-value plus common-space mass/angle failures |
| 4 | FAIL | signed-objective plus common-space mass/angle failures |
| 8 | FAIL | objective nonconvergence; `mu_c<0.95`; principal-angle failures |

Hence

\[
\boxed{\text{0 of 6 frozen horizons resolution robust}}
\]

and the required two neighboring robust horizons do not exist.

Supplement Fig. S5 presents this result compactly; any displayed `Delta_shift=1` or large fixed-resolution angle appears only with the same-context refinement-failure qualification.

### S5.6 Frozen verdict and stop rule

The exact frozen verdict is

\[
\boxed{\text{CLIM-B-FAIL — resolution robustness failure}}.
\]

The large fixed-resolution angles, `Delta_shift=1`, and parity mechanism are retained only with this resolution-failure qualification. They may not be presented as a robust strong Climate result.

No Climate-B repair is part of this paper. The one-shot protocol forbids post-effect hyperdiffusion, scale-selective damping, extra resolution rungs, alternative `g=-U'`, masks, EOF restrictions, localization, changed horizons, or a third Climate candidate. Machine-readable frozen results are in `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv`.

## S6. Additional frozen-data tables and citation metadata notes

### S6.1 Supplement Table S1 — Operational rules and representative frozen outcomes

The study-specific strong rule is **operational, not a universal physical threshold**: both `theta >= 20 deg` and `Delta_Q >= 0.25` are required on at least two neighboring frozen horizons, together with the domain-specific numerical/structural and robustness gates. The Plasma benchmark retains its separately frozen `S0-S5` gate logic; common `theta`/`Delta_Q` values are listed only for cross-domain comparison.

| Case | Representative frozen horizon(s) | Geometry | Target-performance gap | Robustness / outcome |
|---|---|---|---|---|
| Plasma `P2-A` | `T=1` | `theta=53.396 deg` | `Delta_Gamma=0.504337` | strong primary anchor on tested `K=32,64,96` common resolved subspace |
| Neuro `NEURO-STRONG` | 112 ms; 224 ms | `46.824 deg`; `65.058 deg` | `0.529017`; `0.817841` | strong at neighboring frozen horizons; rank-two two-pulse geometry |
| Climate-A `CLIM-WEAK` | `T/tau_ref=8` | conservative subspace angle `90 deg` | `Delta_heat=0.0411846` | all six frozen horizons resolution robust; weak geometry/performance contrast |
| **Climate-B `CLIM-B-FAIL — resolution robustness`** | all six frozen horizons | large fixed-resolution angles may occur | `Delta_shift=1` at fixed truncation | **0/6 horizons pass full refinement; rejected as robust evidence** |

Climate-B attractive fixed-resolution quantities must never be quoted without the same-context failure qualification.

### S6.2 Frozen machine-readable sources

- Plasma: `research/d10_zf_pilot_0_2_execution_data.csv`
- Neuro: `research/neuro/neuro_pilot_0_1_execution_data.csv`
- Climate-A: `research/climate/climate_ocean_pilot_0_1_execution_data.csv`
- Climate-B: `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv`

No figure or table may instantiate model generators, solve new eigensystems, add horizons, interpolate or smooth scientific values, or rerun trajectories. If a desired display is unsupported by frozen stored values, it must be simplified or omitted.

### S6.3 Bibliography normalization status

Bibliographic metadata remain restricted to already approved positioning sources. `Ogino2026` remains an editorial metadata-verification item before submission; this does not authorize a new novelty search.

- **[Landreman2015]** Landreman, M., Plunk, G. G. & Dorland, W. (2015). “Generalized universal instability: transient linear amplification and subcritical turbulence.” *Journal of Plasma Physics* **81**, 905810501. DOI: `10.1017/S0022377815000495`.
- **[Foures2014]** Foures, D. P. G., Caulfield, C. P. & Schmid, P. J. (2014). “Optimal mixing in two-dimensional plane Poiseuille flow at finite Péclet number.” *Journal of Fluid Mechanics* **748**, 241–277. DOI: `10.1017/jfm.2014.182`.
- **[Hennequin2012]** Hennequin, G., Vogels, T. P. & Gerstner, W. (2012). “Non-normal amplification in random balanced neuronal networks.” *Physical Review E* **86**, 011909. DOI: `10.1103/PhysRevE.86.011909`.
- **[Bondanelli2020]** Bondanelli, G. & Ostojic, S. (2020). “Coding with transient trajectories in recurrent neural networks.” *PLoS Computational Biology* **16**(2), e1007655. DOI: `10.1371/journal.pcbi.1007655`.
- **[Friston2003]** Friston, K. J., Harrison, L. & Penny, W. (2003). “Dynamic causal modelling.” *NeuroImage* **19**(4), 1273–1302. DOI: `10.1016/S1053-8119(03)00202-7`.
- **[Daunizeau2011]** Daunizeau, J., Preuschoff, K., Friston, K. & Stephan, K. E. (2011). “Optimizing Experimental Design for Comparing Models of Brain Function.” *PLoS Computational Biology* **7**(11), e1002280. DOI: `10.1371/journal.pcbi.1002280`.
- **[Salfenmoser2022]** Salfenmoser, L. & Obermayer, K. (2022). “Nonlinear optimal control of a mean-field model of neural population dynamics.” *Frontiers in Computational Neuroscience* **16**, 931121. DOI: `10.3389/fncom.2022.931121`.
- **[Ogino2026]** Ogino, M. et al. (2026). “Designing optimal perturbation inputs for system identification in neuroscience.” *eLife reviewed preprint* 110030; reviewed-preprint v1 DOI `10.7554/eLife.110030.1`. **VERIFY FINAL PUBLICATION STATUS BEFORE SUBMISSION.**
- **[Farrell1982]** Farrell, B. F. (1982). “The Initial Growth of Disturbances in a Baroclinic Flow.” *Journal of the Atmospheric Sciences* **39**, 1663–1686.
- **[Farrell1985]** Farrell, B. F. (1985). “Transient Growth of Damped Baroclinic Waves.” *Journal of the Atmospheric Sciences* **42**, 2718–2727.
- **[FarrellIoannou1994]** Farrell, B. F. & Ioannou, P. J. (1994). “A Theory for the Statistical Equilibrium Energy Spectrum and Heat Flux Produced by Transient Baroclinic Waves.” *Journal of the Atmospheric Sciences* **51**(19), 2685–2698.
- **[KimMorgan2002]** Kim, H. M. & Morgan, M. C. (2002). “Dependence of Singular Vector Structure and Evolution on the Choice of Norm.” *Journal of the Atmospheric Sciences* **59**, 3099–3116.
- **[Kuang2004]** Kuang, Z. (2004). “The Norm Dependence of Singular Vectors.” *Journal of the Atmospheric Sciences* **61**, 2943–2949.
- **[Sevellec2008]** Sévellec, F., Huck, T., Ben Jelloul, M., Vialard, J. & Fedorov, A. V. (2008). “Optimal Surface Salinity Perturbations of the Meridional Overturning and Heat Transport in a Global Ocean General Circulation Model.” *Journal of Physical Oceanography* **38**(12). DOI: `10.1175/2008JPO3875.1`.

---

**Supplement boundary:** This companion file copies and reorganizes only frozen Supplement S1–S6 content from Draft 0.3 and integrates the already-produced Supplement Table S1 and Supplement Fig. S5 references. It introduces no new scientific calculation, parameter, horizon, value, model, objective, channel, admissible geometry, novelty claim, or robustness interpretation.
