# MASTER Prompt — Climate Intra-Domain Contrast Candidate Freeze 0.1

**Authority:** `research/master/climate_intra_domain_contrast_feasibility_gate_0_1.md`.

**Target chat:** `70 – CLIMATE – Klima/Ozean & gerichteter Transport`.

**Scope:** candidate freeze only. No CORE optimization, no finite-time objective comparison, no parameter/effect search, no retuning of Climate-A, no manuscript revision.

## Task

Freeze exactly one Climate-B candidate from the passed feasibility gate:

\[
\boxed{\text{equivalent-barotropic midlatitude Bickley jet}}
\]

with positive objective = perturbation kinetic energy and signed channel = eddy-induced forcing of the infinitesimal poleward jet-translation coordinate.

Preserve the existing Climate-A result exactly as `CLIM-WEAK`; do not reopen it.

## Required physical freeze

Freeze and document explicitly:

1. dimensional PDE
   \[
   \partial_t\zeta'+U\partial_x\zeta'+(\beta-U'')\partial_x\psi'=-r\zeta',
   \qquad \zeta'=\nabla^2\psi';
   \]
2. base jet
   \[
   U(y)=U_0\operatorname{sech}^2((y-y_0)/L);
   \]
3. nominal physical point from the feasibility gate, without alteration:
   \[
   \beta=1.6\times10^{-11}\,\mathrm{m^{-1}s^{-1}},\quad
   U_0=20\,\mathrm{m\,s^{-1}},\quad
   L=1000\,\mathrm{km},\quad
   r=(10\,\mathrm d)^{-1},
   \]
   with `Lx=20000 km`, `Ly=10000 km`, jet centered in the meridional channel;
4. periodic `x`, `psi'=0` at meridional walls, and `kx != 0` eddy-state restriction;
5. positive metric
   \[
   E'=\frac12\int|\nabla\psi'|^2dA=\frac12x^\dagger Mx;
   \]
6. jet-translation tangent
   \[
   g(y)=-U'(y);
   \]
7. signed channel
   \[
   q_{\rm shift}(t)=
   \frac{\int g(y)[-\partial_y\overline{u'v'}]dy}{\int g^2dy},
   \]
   positive for projection onto a poleward jet translation;
8. cumulative future observable
   \[
   J_{\rm shift}(T)=\int_0^Tq_{\rm shift}(t)dt;
   \]
9. physical admissibility of `B=I`, `R_in=M` on the retained eddy space;
10. a time normalization chosen from the already frozen physical scales, not from any objective result.

## Structural checks allowed before effect inspection

Candidate Freeze may analytically establish:

- `M=M^dagger > 0` on the retained space;
- existence of a Hermitian quadratic representation `Q_shift`;
- nontriviality and signed/indefinite character of `Q_shift` using symmetry/cross-phase arguments;
- Rayleigh-Kuo pre-effect stability condition at the nominated physical point;
- whether the provisional channel/domain/boundary specification is mathematically consistent.

Do **not** compute any finite-time `K_M`, `K_shift`, optimizer, angle, performance gap, or objective-separation metric.

## Discretization handoff

Specify the exact structure-preserving numerical representation to be used in the next `Numerical Qualification` step, including:

- basis family in `x` and `y`;
- state ordering;
- treatment of real-field conjugacy and parity;
- nested resolution ladder with roles chosen before effect inspection;
- how `A_K`, `M_K`, and `Q_shift,K` will be assembled;
- numerical stability/Hermiticity/indefiniteness/flux-reproduction checks for qualification.

The Candidate Freeze must not choose resolution or zonal wavenumber by inspecting CORE separation.

## Governance

- Climate-B is one-shot.
- No alternative physical parameter point may be tried.
- No new weight/mask/EOF may replace `g=-U'`.
- If a purely representational inconsistency exists, report it to MASTER; do not silently change the physical problem.
- If Candidate Freeze fails, STOP and return to MASTER; the project returns to `Manuscript Structure Freeze 0.2`.

## Required outputs

Create:

`research/climate/climate_intra_domain_contrast_candidate_freeze_0_1.md`

Update:

`research/climate/STATUS.md`

After success set Climate status to:

`CLIMATE-B CANDIDATE FROZEN — RETURN TO MASTER FOR NUMERICAL QUALIFICATION`

Report canonical path and full commit hash, then STOP.
