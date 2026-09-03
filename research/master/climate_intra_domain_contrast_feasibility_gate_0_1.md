# Climate Intra-Domain Contrast Feasibility Gate 0.1

**Status:** PASS — ONE-SHOT CLIMATE-B CANDIDATE AUTHORIZED FOR CANDIDATE FREEZE  
**Date:** 2026-09-03  
**Authority:** MASTER, with the existing `CLIM-WEAK` result and Manuscript Structural Revision 0.2 retained unchanged.  
**Scope:** feasibility and physical candidate selection only. No CORE optimization, no energy-vs-channel separation, no parameter/effect search, no replacement or retuning of the existing Climate/Ocean pilot.

## 0. Executive verdict

A second, physically distinct Climate/Atmospheric-dynamics demonstrator is scientifically justified **only as one additional pre-specified attempt** designed to test intra-domain selectivity of the framework.

The existing two-layer Phillips-QG heat-transport pilot remains

\[
\boxed{\text{Climate-A}=\text{CLIM-WEAK}}
\]

and is not reopened.

The most defensible second candidate is

\[
\boxed{\text{Climate-B: equivalent-barotropic midlatitude jet, perturbation energy vs. signed eddy-induced jet-shift forcing}.}
\]

The candidate uses a stable beta-plane Bickley-type jet, a positive perturbation kinetic-energy metric, and a signed quadratic channel formed from the projection of eddy momentum-flux convergence onto the infinitesimal jet-translation direction. This is a physically independent question from the existing poleward heat-transport channel and is not chosen from any inspected CORE effect.

Therefore

\[
\boxed{\text{Climate Intra-Domain Contrast Feasibility Gate 0.1 = PASS}.}
\]

The next authorized action is **Candidate Freeze only**. No finite-time energy/channel operator or optimizer may be evaluated before that freeze and subsequent numerical qualification.

---

## 1. Scientific purpose

The purpose is not to obtain a second positive example by searching parameter space. The purpose is to ask whether the same workflow can distinguish, within geophysical/climate dynamics, between two physically different channel questions:

1. **Climate-A, already frozen:** QG perturbation energy versus cumulative poleward eddy heat transport, which returned `CLIM-WEAK`;
2. **Climate-B, proposed here:** perturbation energy versus the cumulative signed eddy forcing of a jet-translation coordinate.

If Climate-B later returns a strong result, the manuscript can make a sharper intra-domain statement: the usefulness of an energy-optimal perturbation as a proxy can vary substantially even within one broad discipline, depending on the physical channel. If Climate-B returns weak/null or fails qualification, that outcome is retained and the project returns immediately to `Manuscript Structure Freeze 0.2`. No third Climate search is authorized.

---

## 2. Nominated physical model class

Use the linearized equivalent-barotropic vorticity equation on a midlatitude beta-plane channel about a prescribed eastward zonal jet

\[
U(y)=U_0\,\operatorname{sech}^2\!\left(\frac{y-y_0}{L}\right).
\]

For perturbation streamfunction `psi'`,

\[
\zeta'=\nabla^2\psi',
\]

and the frozen model class is

\[
\boxed{
\partial_t\zeta'
+U(y)\,\partial_x\zeta'
+\bigl[\beta-U''(y)\bigr]\partial_x\psi'
=-r\zeta'.
}
\]

The base jet is externally maintained and is not evolved during the tangent calculation. The Rayleigh drag acts on perturbation vorticity.

Boundary structure for the candidate freeze:

- periodic in `x`;
- channel walls in `y` with `psi'=0`;
- exclude `k_x=0` from the eddy perturbation space;
- retain both meridional-parity sectors, because the signed jet-shift channel couples them.

A structure-preserving Fourier-in-`x` / Galerkin-in-`y` discretization is admissible. Exact basis and resolution ladder belong to Numerical Qualification, not this gate.

---

## 3. Positive metric `M`

The positive objective is the standard barotropic perturbation kinetic energy

\[
\boxed{
E'(t)=\frac12\int_\Omega |\nabla\psi'(x,y,t)|^2\,dA
=\frac12 x^\dagger Mx,
\qquad M=M^\dagger\succ0
}
\]

on the `k_x\ne0` retained eddy space.

This is a genuine physical energy metric and requires no ad hoc weighting.

For full physically admissible retained eddy initial conditions,

\[
\boxed{B=I,\qquad R_{\rm in}=M}
\]

is the natural candidate geometry/cost, subject to structural verification in the Candidate Freeze / Numerical Qualification.

---

## 4. Signed physical channel: eddy-induced jet-shift forcing

Let the meridional coordinate increase poleward and define the infinitesimal translation tangent of the base jet by

\[
\boxed{g(y)=-U'(y)}.
\]

Indeed,

\[
U(y-\delta Y)=U(y)+\delta Y\,g(y)+O(\delta Y^2),
\]

so positive amplitude along `g` represents a poleward translation of the jet.

For a real eddy field, define the zonal-mean Reynolds stress

\[
F_M(y,t)=\overline{u'v'}(y,t),
\qquad
u'=-\partial_y\psi',\quad v'=\partial_x\psi'.
\]

The eddy-induced zonal-mean acceleration is

\[
\mathcal A(y,t)=-\partial_y F_M(y,t).
\]

The proposed signed channel is the normalized projection of this acceleration onto the jet-translation tangent:

\[
\boxed{
q_{\rm shift}(t)
=
\frac{\int g(y)\,[-\partial_y\overline{u'v'}]\,dy}
{\int g(y)^2\,dy}.
}
\]

With vanishing boundary momentum flux this is equivalently

\[
q_{\rm shift}(t)
=
\frac{\int g'(y)\,\overline{u'v'}(y,t)\,dy}
{\int g(y)^2\,dy}.
\]

The sign convention is frozen conceptually as

\[
\boxed{q_{\rm shift}>0\;\Longleftrightarrow\;\text{eddy forcing projects onto a poleward jet translation}.}
\]

The cumulative channel would later be

\[
J_{\rm shift}(T)=\int_0^T q_{\rm shift}(t)\,dt.
\]

For any fixed Galerkin representation this real quadratic functional has a Hermitian matrix representation

\[
q_{\rm shift}=x^\dagger Q_{\rm shift}x.
\]

It is signed rather than positive: reversal of the relevant cross-phase between opposite meridional-parity components reverses the Reynolds-stress projection while leaving perturbation energy unchanged. Numerical Qualification must explicitly verify `Q_shift=Q_shift^dagger` and indefiniteness/nontriviality.

### Why this is not merely the perturbation-energy balance

Global barotropic energy exchange weights `u'v'` by the base shear `U'`. The proposed jet-translation forcing instead projects **momentum-flux convergence** onto `g=-U'`, equivalently weighting `u'v'` by `g'=-U''` after integration by parts. It is therefore a different physical quadratic functional and is not algebraically identical to terminal perturbation energy or the global Reynolds-stress energy-conversion term.

### Interpretation restriction

`J_shift` is a cumulative **eddy impulse/forcing of the jet-translation coordinate under frozen tangent dynamics**. It is not, by itself, the realized displacement of a fully coupled nonlinear jet. The manuscript may later call it jet-shift forcing or translation-mode forcing, not a predicted climate-change jet displacement.

---

## 5. Single a-priori nominal point for Candidate Freeze

To prevent effect-guided parameter choice, nominate exactly one dimensional point for the next freeze:

\[
\boxed{
\beta=1.6\times10^{-11}\;\mathrm{m^{-1}s^{-1}},\quad
U_0=20\;\mathrm{m\,s^{-1}},\quad
L=1000\;\mathrm{km},\quad
r=(10\;\mathrm d)^{-1}.
}
\]

Use a symmetric channel centered on the jet with provisional physical extents

\[
\boxed{L_y=10{,}000\;\mathrm{km},\qquad L_x=20{,}000\;\mathrm{km}}
\]

unless the Candidate Freeze identifies a purely representational inconsistency before any objective calculation. These values are selected from standard midlatitude scales and domain accommodation, not from CORE separation.

For the Bickley profile,

\[
\max_y U''(y)=\frac{2}{3}\frac{U_0}{L^2}.
\]

At the nominated point,

\[
\frac{2}{3}\frac{U_0}{L^2}=1.333\times10^{-11}\;\mathrm{m^{-1}s^{-1}}<\beta,
\]

so

\[
\beta-U''(y)>0
\]

throughout the ideal profile. The Rayleigh-Kuo sign-change necessary condition for inviscid barotropic instability is therefore not met. With the fixed positive Rayleigh drag, the point is a strong **pre-effect stability candidate**. Exact finite-dimensional `alpha(A_K)<0` still must be verified blindly in Numerical Qualification; it is not assumed from this gate.

No alternative `U0`, `L`, `beta`, `r`, domain size, or jet profile may be tried after objective separation is inspected.

---

## 6. Literature-positioning feasibility

Targeted literature inspection shows dense prior art around all individual ingredients:

- barotropic beta-plane optimal excitation and finite-time energy growth of neutral/stable Rossby waves;
- the central role of eddy momentum-flux convergence in maintaining and shifting midlatitude eddy-driven jets;
- linearized barotropic models that diagnose the space-time structure of eddy momentum fluxes and poleward/equatorward jet responses;
- sensitivity/optimization of turbulent-jet variance and heat/momentum fluxes with respect to changes in the mean jet.

This prior art **demotes any broad novelty claim** for barotropic nonmodal growth, eddy momentum fluxes, jet-shift dynamics, or optimization of atmospheric fluxes.

However, the targeted search did not identify a `SAME` result that directly compares, for one fixed stable barotropic jet and one fixed admissible initial-condition space,

\[
\text{terminal perturbation-energy optimum}
\quad\text{vs.}\quad
\text{positive cumulative jet-translation-forcing optimum}
\]

with signed extrema, optimizer/subspace geometry, target-performance gap, pre-effect freezing, and no-retuning discipline. Absence of a `SAME` hit is **not proof of novelty**; it only means the candidate is sufficiently distinct for a controlled feasibility branch.

Mandatory prior-art anchors for any later write-up include at least:

- Farrell (1988), *Optimal Excitation of Neutral Rossby Waves*, Journal of the Atmospheric Sciences 45, 163–172;
- Lorenz (2014), *Understanding Midlatitude Jet Variability and Change Using Rossby Wave Chromatography: Poleward-Shifted Jets in Response to External Forcing*, JAS 71, 2370–2389, DOI `10.1175/JAS-D-13-0200.1`;
- Lorenz (2015), *Understanding Midlatitude Jet Variability and Change Using Rossby Wave Chromatography: Methodology*, JAS 72, 369–388, DOI `10.1175/JAS-D-13-0199.1`;
- Lorenz (2022), *The Role of Barotropic versus Baroclinic Feedbacks on the Eddy Response to Annular Mode Zonal Wind Anomalies*, JAS 79, 2529–2547, DOI `10.1175/JAS-D-22-0061.1`;
- Farrell & Ioannou (2004), *Sensitivity of Perturbation Variance and Fluxes in Turbulent Jets to Changes in the Mean Jet*, JAS 61;
- the broader eddy-driven-jet / momentum-flux-convergence literature relevant to the final chosen framing.

---

## 7. Feasibility criteria

| Criterion | Result | Reason |
|---|---|---|
| autonomous stable-candidate linear `A` exists | PASS | equivalent-barotropic tangent dynamics; Kuo-stable nominal profile plus fixed drag |
| natural positive `M` exists | PASS | perturbation kinetic energy |
| independent signed quadratic channel exists | PASS | projection of eddy momentum-flux convergence onto jet-translation tangent |
| channel is not just the energy objective in disguise | PASS | `U''`-weighted translation forcing differs from `U'`-weighted global energy conversion |
| physical `B` with rank > 1 exists | PASS | full retained eddy state, `B=I`, `R_in=M` |
| numerically tractable structure exists | PASS | 2-D linear barotropic PDE with Fourier/Galerkin representation |
| branch is literature-positionable without broad novelty claims | PASS WITH RESTRICTION | dense related prior art, no targeted `SAME` hit for full dual-objective comparison |
| anti-cherry-picking governance can be enforced | PASS | one nominated candidate, one attempt, no replacement of `CLIM-WEAK` |

---

## 8. Hard governance restrictions

1. **Climate-A remains frozen as `CLIM-WEAK`.** It may not be retuned, replaced, or relabeled.
2. Climate-B is exactly one additional attempt. If it fails Candidate Freeze/Numerical Qualification or later returns weak/null, retain the outcome and STOP the Climate search.
3. No third Climate candidate is authorized before the first manuscript.
4. No `K_M`, `K_shift`, optimizer, angle, gap, or objective-separation quantity may be computed before Candidate Freeze and Numerical Qualification are complete.
5. No parameter scan over `U0`, `L`, `beta`, `r`, domain size, zonal wavenumber, horizon, or channel weight is allowed to search for a stronger effect.
6. The translation tangent `g=-U'` is physically fixed by the base jet. It may not be replaced post hoc by an EOF, mask, or weight chosen to enlarge separation.
7. If the finite-dimensional stability qualification fails because of a genuine structural inconsistency, MASTER may either STOP Climate-B or permit one **pre-effect** representational correction only if it does not change the physical point. No physical retuning is permitted.
8. `Manuscript Structure Freeze 0.2` is placed on **HOLD**, not canceled. It is the mandatory return point after Climate-B resolves.

---

## 9. Allowed future claim if the branch succeeds

Only if a later frozen execution actually supports it, a cross-domain/intra-domain statement may be considered along the lines of:

> Within geophysical fluid dynamics, the same energy-based proxy can be nearly adequate for one signed channel yet substantially nonredundant for another, so the value of a conventional positive objective is channel- and admissible-geometry-dependent even within one discipline.

This sentence is **not currently an empirical result**. It is only the motivation for the one-shot Climate-B test.

---

## 10. Verdict

\[
\boxed{\text{PASS — Climate-B Candidate Freeze authorized}.}
\]

Nominated candidate:

\[
\boxed{
\text{stable equivalent-barotropic Bickley jet}
+\text{perturbation energy}
+\text{signed cumulative jet-translation forcing}.
}
\]

Next task: `Climate Intra-Domain Contrast Candidate Freeze 0.1`.

**STOP — no CORE-effect quantity has been evaluated in this gate.**