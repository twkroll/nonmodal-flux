# Fusion bridge — gyrokinetic observable dictionary

**Date:** 1 September 2026  
**Status:** exploratory bridge note; no model convention frozen  
**Purpose:** identify which fusion-relevant gyrokinetic observables can be represented in the `nonmodal-flux` framework without replacing physical fluxes by ad-hoc state norms.

## Working rule

The positive metric and the transport observables remain distinct:

\[
W[x]=x^\dagger Mx,\qquad M\succ0,
\]

\[
\mathcal F_\alpha[x]=x^\dagger Q_\alpha x,\qquad Q_\alpha=Q_\alpha^\dagger,
\]

with each \(Q_\alpha\) derived from a physical gyrokinetic diagnostic or balance term. A weighted sum of moments is not accepted as a transport observable unless the physical balance itself fixes that combination.

## Literature anchors

1. Bañón Navarro et al. (2011), *Free Energy Balance in Gyrokinetic Turbulence*, Physics of Plasmas 18, 092303. Uses the GENE formalism and derives/analyzes the gyrokinetic free-energy balance, including gradient drive, dissipation and internal transfer channels.
2. Bañón Navarro et al. (2011), *Free Energy Cascade in Gyrokinetic Turbulence*, PRL 106, 055001. Shows conservative nonlinear redistribution of free energy across perpendicular scales in ITG turbulence.
3. Helander & Plunk (2022), *Energetic bounds on gyrokinetic instabilities. Part 1*. Gives explicit species-resolved particle- and heat-flux expressions and relates them to the free-energy production budget.
4. Plunk & Helander (2022), *Part 2. Modes of optimal growth*. Optimizes instantaneous free-energy growth, not finite-horizon signed transport.
5. GENE documentation/publications: GENE computes transport coefficients from gyrokinetic fluctuations and provides particle, heat and momentum-flux diagnostics.

All exact prefactors, normalization choices, field variables and electromagnetic terms remain convention-dependent and must be re-derived from the specific model chosen later.

## Observable dictionary

| Observable | Physical role | Schematic gyrokinetic form | Quadratic/bilinear in linear perturbations? | `nonmodal-flux` role | Readiness |
|---|---|---|---|---|---|
| Free energy \(W\) | positive disturbance size / turbulence intensity | entropy-like distribution-function term plus field-energy terms | **Yes** | physical metric \(M\) | **High** |
| Species particle flux \(\Gamma_a\) | radial particle transport | \(\mathrm{Re}\langle\int \delta F_a(\delta\dot{\mathbf R}_a^*\!\cdot\nabla\psi)\,d^3v\rangle\) | **Yes**, after linear field/distribution representation | signed \(Q_{\Gamma_a}\) | **High** |
| Species heat flux \(q_a\) | radial thermal transport | \(\mathrm{Re}\langle\int \delta F_a( m_av^2/2-5T_a/2)(\delta\dot{\mathbf R}_a^*\!\cdot\nabla\psi)\,d^3v\rangle\) | **Yes** | signed \(Q_{q_a}\) | **High** |
| Ion/electron heat fluxes \(q_i,q_e\) | channel-resolved confinement loss | species-specific heat-flux forms | **Yes** | separate objectives, never merged by default | **High** |
| Radial momentum flux \(\Pi\) | rotation / momentum transport | velocity moment of \(\delta f\) times radial drift | **Typically yes** | signed \(Q_\Pi\) | **Medium** |
| Gradient-drive power | free-energy injection from equilibrium gradients | thermodynamic-force combinations of \(\Gamma_a,q_a,\ldots\) | **Yes**, but it is a balance combination | diagnostic / bound, not a primitive flux | **High** |
| Collisional dissipation \(D\) | sink of free energy | quadratic dissipative form | **Yes** | \(R\succeq0\) in balance bounds | **High** |
| Entropy ↔ field-energy internal transfer | redistribution between components of free energy | curvature/parallel-field transfer terms | Often bilinear/quadratic | possible internal-transfer observable | **Medium** |
| Spectral free-energy transfer \(\Pi_K\) | nonlinear cascade across a wavenumber cut | triadic nonlinear transfer | **Not generally quadratic in the full nonlinear state** | not in present linear \(Q\)-framework | **Low / later** |
| Turbulence → zonal/mean-flow transfer | saturation / flow generation | nonlinear energy-transfer term | not generally a fixed quadratic state form | later tangent-linear or higher-order extension | **Low / later** |

## 1. Free energy: natural positive metric

Gyrokinetic free energy is the natural candidate for \(M\), not a Euclidean norm of code variables. In simplified electrostatic settings it contains an entropy-like quadratic contribution of the perturbed distribution function together with field terms. Schematically,

\[
W = W_f + W_{\rm field},
\]

with

\[
W_f \sim \sum_a \int d\Lambda\,\frac{T_a}{2F_{0a}}|\delta f_a|^2,
\]

plus convention-dependent electrostatic/electromagnetic terms.

**Project consequence:** when a reduced gyrofluid or discretized gyrokinetic model is chosen, \(M\) must be obtained by discretizing the actual free-energy functional. It must not be replaced by an identity matrix simply because the state has been numerically normalized.

## 2. Particle flux: high-priority signed observable

Helander & Plunk give the species particle flux per perpendicular Fourier mode as

\[
\Gamma_a(\mathbf k,t)=
\mathrm{Re}\left\langle
\int \delta F_{a,\mathbf k}
\left(\delta\dot{\mathbf R}_{a,\mathbf k}^*\cdot\nabla\psi\right)
\,d^3v
\right\rangle.
\]

The radial drift fluctuation is itself linear in the fluctuating electromagnetic fields. Hence, after choosing a linear state vector containing the distribution-function and field degrees of freedom, \(\Gamma_a\) is bilinear in fluctuation amplitudes and can be represented as a Hermitian signed form

\[
\Gamma_a = x^\dagger Q_{\Gamma_a}x.
\]

This is attractive because it is directly a transport diagnostic, is signed, depends on a cross-phase, is physically distinct from free energy, and can remain species-resolved.

**Caveat:** for some reduced models/conventions particle flux may vanish identically under additional assumptions. Helander & Plunk show such a case for adiabatic electrons in a particular setting. The pilot model must therefore have a genuinely active particle-flux channel.

## 3. Heat flux: strongest fusion-facing target

The species heat flux is given in the same reference by

\[
q_a(\mathbf k,t)=
\mathrm{Re}\left\langle
\int \delta F_{a,\mathbf k}
\left(\frac{m_av^2}{2}-\frac{5T_a}{2}\right)
\left(\delta\dot{\mathbf R}_{a,\mathbf k}^*\cdot\nabla\psi\right)
\,d^3v
\right\rangle.
\]

This is also bilinear in linear fluctuations and is therefore a natural signed quadratic observable after discretization:

\[
q_a=x^\dagger Q_{q_a}x.
\]

For magnetic-confinement fusion, turbulent heat loss is directly tied to confinement performance. GENE is explicitly designed to calculate fluctuation-driven transport coefficients, so this gives a direct route from a reduced proof-of-concept to a realistic fusion diagnostic.

The theory should keep

\[
Q_{q_i},\qquad Q_{q_e},\qquad Q_{\Gamma_i},\qquad Q_{\Gamma_e}
\]

as independent observables. A later central question can be whether the free-energy optimal and the different species-resolved transport optimals are distinct under the same initial free-energy budget.

## 4. Gradient-drive terms: balance structure, not a replacement for fluxes

The gyrokinetic free-energy budget links equilibrium thermodynamic gradients to transport. Schematically,

\[
\frac{dW}{dt}
=\sum_a \left(g_{n,a}\Gamma_a+g_{T,a}q_a+\cdots\right)-D,
\]

where exact signs and coefficients depend on coordinates and normalization.

This structure is valuable for balance-based theorems, but the weighted combination on the right is **not** a substitute for the individual flux observables. It constrains the channels; it does not erase their identities.

## 5. Momentum flux: plausible second-generation observable

GENE diagnostics include momentum-flux quantities, and gyrokinetic momentum transport is important for toroidal rotation and flow shear. In a linear perturbation representation, the radial momentum flux has the same broad structure as other turbulent fluxes: a velocity-space moment of \(\delta f\) correlated with a fluctuating radial drift. Thus one expects

\[
\Pi=x^\dagger Q_\Pi x
\]

for a suitable discretized state. Toroidal geometry, rotation conventions and electromagnetic contributions make this more convention-sensitive than particle or heat flux, so it should not be the first fusion observable implemented.

## 6. Spectral free-energy cascade: related, but outside the present quadratic-output core

Bañón Navarro et al. show that the gyrokinetic nonlinearity conservatively redistributes free energy between perpendicular scales and produces a forward, strongly local cascade in the studied ITG case.

The associated scale-to-scale transfer is generated by the nonlinear term and is generally triadic. Therefore a spectral flux such as

\[
\Pi_K = \text{free-energy transfer across a cutoff }K
\]

is not, in general, a fixed quadratic form \(x^\dagger Q_Kx\) of the full nonlinear state.

**Project decision:** do not force \(\Pi_K\) into the current `nonmodal-flux` framework. Possible later routes are tangent-linearization around a turbulent trajectory, a higher-order output theory for cubic/triadic observables, or a separate statistical cascade branch such as Friedrich--Peinke / Markov-in-scale.

## Recommended fusion hierarchy

### Stage F0 — reduced analytical model

Use a two- or three-field drift model to verify the mathematics and construction procedure. Required outputs \(M\), \(Q_\Gamma\), and \(Q_q\) must each be derived from the model's actual energy and flux expressions.

### Stage F1 — reduced kinetic / gyrofluid model

Choose a model that retains a proper free-energy invariant/balance and at least two active transport channels. This is probably the most informative place to test a multichannel transport geometry.

### Stage F2 — linear GENE-facing formulation

For a fixed local gyrokinetic equilibrium, regard the discretized linearized gyrokinetic system as

\[
\dot x=Ax,
\]

and construct

\[
M_{\rm GK},\quad Q_{q_i},\quad Q_{q_e},\quad Q_{\Gamma_i},\quad Q_{\Gamma_e}
\]

from the same discretization/diagnostics used by the gyrokinetic model. Then compare finite-horizon free-energy and species-resolved transport optimals. This is the most direct route to a Jenko/GENE connection.

## Suitability ranking

**Tier 1 — core fusion observables:** free energy \(W\), ion heat flux \(q_i\), electron heat flux \(q_e\) when kinetic electrons are retained, and particle flux \(\Gamma_a\) when nonzero in the chosen model.

**Tier 2 — later:** momentum flux \(\Pi\), internal entropy/field-energy transfer terms.

**Tier 3 — parked extensions:** spectral cascade flux \(\Pi_K\), turbulence-to-zonal-flow nonlinear transfer, and Friedrich--Peinke scale-process analysis.

## Immediate implication for model choice

The simplest Hasegawa--Wakatani system remains useful for validating particle-flux ideas, but it cannot demonstrate the full fusion-facing value of the framework. A stronger second model should have:

1. an explicit positive free-energy functional;
2. at least one genuine heat-flux observable;
3. preferably two independently meaningful transport channels;
4. a linear operator small enough for analytic or semi-analytic work;
5. a transparent relation to ITG/gyrokinetic physics.

This suggests that after the HW benchmark, model selection should favor a free-energy-consistent ITG/gyrofluid or reduced gyrokinetic system rather than adding arbitrary extra state variables to HW.

## Questions left open before GENE implementation

- Which exact local gyrokinetic convention and state variable should define \(M_{\rm GK}\)?
- Which electrostatic/electromagnetic terms must be retained in each flux form?
- How should field constraints/quasineutrality be eliminated without spoiling coordinate invariance?
- What admissible input map \(B\) corresponds to a physically meaningful transport-neutral gyrokinetic perturbation?
- Can a useful finite-dimensional reduced basis preserve both the free-energy metric and all target flux forms?
- Does finite-horizon heat-flux optimization produce information genuinely different from existing free-energy optimal-mode theory?

These questions are deliberately left open. They require a later model-selection decision, not an ad-hoc choice here.

## Outcome of B1

**Conclusion:** the fusion bridge is viable at the level needed for the project. Free energy, particle flux and heat flux fit the mathematical architecture naturally and physically. Heat flux is probably the strongest eventual fusion-facing observable; the nonlinear spectral cascade is related but should remain outside the present quadratic-output core.

**No user decision is required yet.** The next step can be performed directly: a focused model audit comparing 2--4 reduced ITG/gyrofluid/gyrokinetic candidates against the five model-selection criteria above.
