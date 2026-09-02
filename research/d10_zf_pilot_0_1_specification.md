# D10-ZF Pilot 0.1 — canonical instantiation only

**Date:** 2026-09-02  
**Status:** parameter/specification freeze only; no pilot evaluation, optimization, parameter search, or new theory

## Scope

This note instantiates exactly one canonical parameter point of the already accepted D10-ZF prescribed-zonal-flow branch for the preregistered Pilot 0.1. The point is chosen only for simplicity, physical admissibility, and continuity with the existing D2-A/D10-ZF model. No attempt is made to maximize any CORE observable, gain, angle, nonnormality measure, spectral property, or transport effect.

No MODES/CONT/CASCADE extension is opened here, and no new plasma branch is introduced.

## 1. Frozen continuous model and normalization

Use the accepted D10-ZF linearization at one fixed nonzero poloidal wavenumber,

```math
\partial_t\Delta_k\hat\varphi
+i k_y U\,\Delta_k\hat\varphi
-i k_y U''\hat\varphi
=C(\hat\varphi-\hat\eta),
```

```math
\partial_t\hat\eta+i k_y U\hat\eta
=C(\hat\varphi-\hat\eta)-i\kappa k_y\hat\varphi,
```

with

```math
\Delta_k=\partial_x^2-k_y^2.
```

The zonal density background remains the D10-ZF choice

```math
N(x)=0.
```

The time variable is the existing nondimensional HW time. Define

```math
\tau=t/\tau_{\rm ref},
```

and for Pilot 0.1 choose the model unit

```math
\boxed{\tau_{\rm ref}=1}.
```

Thus all rates below are expressed per one existing nondimensional D10-ZF time unit. No conversion to dimensional seconds is asserted by this pilot specification.

## 2. Canonical parameter point

Freeze the simplest resolved nonuniform periodic zonal flow,

```math
\boxed{U(x)=\cos x}.
```

Equivalently, with the D10 Fourier convention,

```math
u_{+1}=u_{-1}=\frac12,
\qquad
u_q=0\quad(q\neq\pm1).
```

A compatible zonal potential is `Phi(x)=sin x` up to an irrelevant additive constant, since `U=Phi'`.

Choose

```math
\boxed{L_x=2\pi},
\qquad
\boxed{k_0=\frac{2\pi}{L_x}=1},
```

```math
\boxed{k_y=1},
\qquad
\boxed{C=1},
\qquad
\boxed{\kappa=1}.
```

These values retain the unit-order D2-A/D8 normalization already used in the repository while introducing only the single D10-ZF ingredient required to remove radial block independence: a nonuniform prescribed zonal flow.

### Damping

The existing D10-ZF production assembler contains no perpendicular damping law and intentionally does not inherit the earlier single-mode diagnostic damping. Therefore Pilot 0.1 freezes

```math
\boxed{\text{additional perpendicular damping}=0}.
```

The resistive HW coupling `C=1` remains part of the model and its physical sink is unchanged. No Laplacian or hyperdiffusive term is added in this specification.

## 3. Fourier-Galerkin truncation

Use the smallest centered symmetric radial Galerkin space that contains the base radial harmonic and the first sidebands produced by the `q_Z=1` profile:

```math
\boxed{m\in\{-1,0,1\}}.
```

Hence

```math
N_x=3,
\qquad
k_{x,m}=m,
```

and the state dimension is six.

The orthonormal radial basis is

```math
e_m(x)=L_x^{-1/2}e^{imx}.
```

The state ordering is frozen as

```math
\boxed{
z=
(\phi_{-1},\phi_0,\phi_{+1},\eta_{-1},\eta_0,\eta_{+1})^T.
}
```

This is a Galerkin projection: sidebands outside the retained set are projected out. No convergence statement is made here; convergence belongs to a later pilot-evaluation step and is explicitly outside this specification.

## 4. Concrete projected operators

For the retained radial modes,

```math
D_x=\operatorname{diag}(-i,0,i),
```

and

```math
\Delta
=D_x^2-k_y^2I
=\operatorname{diag}(-2,-1,-2).
```

Projected multiplication by `U(x)=cos x` is

```math
\mathsf U=
\begin{pmatrix}
0&\tfrac12&0\\
\tfrac12&0&\tfrac12\\
0&\tfrac12&0
\end{pmatrix},
```

with

```math
\mathsf U_{xx}=-\mathsf U.
```

The D10-ZF generator is the already derived block matrix

```math
A=
\begin{pmatrix}
A_{\phi\phi}&A_{\phi\eta}\\
A_{\eta\phi}&A_{\eta\eta}
\end{pmatrix},
```

where

```math
A_{\phi\phi}
=\Delta^{-1}
\left(-ik_y\mathsf U\Delta+ik_y\mathsf U_{xx}+CI\right),
```

```math
A_{\phi\eta}=-C\Delta^{-1},
```

```math
A_{\eta\phi}=(C-i\kappa k_y)I,
```

```math
A_{\eta\eta}=-CI-ik_y\mathsf U.
```

At the frozen Pilot-0.1 values this becomes

```math
\boxed{
A=
\begin{pmatrix}
-\tfrac12&0&0&\tfrac12&0&0\\
-\tfrac{i}{2}&-1&-\tfrac{i}{2}&0&1&0\\
0&0&-\tfrac12&0&0&\tfrac12\\
1-i&0&0&-1&-\tfrac{i}{2}&0\\
0&1-i&0&-\tfrac{i}{2}&-1&-\tfrac{i}{2}\\
0&0&1-i&0&-\tfrac{i}{2}&-1
\end{pmatrix}.
}
```

No spectral property of this matrix is evaluated in this note.

## 5. Physical energy metric

The accepted D10-ZF Galerkin energy is

```math
E_{\rm pert}=\frac12 z^\dagger M z,
```

with

```math
M=\begin{pmatrix}-\Delta&0\\0&I\end{pmatrix}.
```

Therefore for Pilot 0.1

```math
\boxed{
M=
\operatorname{diag}(2,1,2,1,1,1).
}
```

This is inherited directly from the continuous perturbation energy; no ad-hoc weighting is introduced.

## 6. Physical radial particle-flux form

The target observable remains the D2-A/D10-ZF outward radial particle flux

```math
\Gamma
=k_y\operatorname{Im}(\eta^\dagger\phi)
=z^\dagger Q_\Gamma z.
```

For the three-mode Galerkin state,

```math
Q_\Gamma
=\frac{k_y}{2}
\begin{pmatrix}
0&iI_3\\
-iI_3&0
\end{pmatrix}.
```

Thus at `k_y=1`,

```math
\boxed{
Q_\Gamma
=\frac12
\begin{pmatrix}
0&0&0&i&0&0\\
0&0&0&0&i&0\\
0&0&0&0&0&i\\
-i&0&0&0&0&0\\
0&-i&0&0&0&0\\
0&0&-i&0&0&0
\end{pmatrix}.
}
```

`Q_Gamma` is Hermitian and signed/indefinite; it is not a norm.

The separate mean-flow exchange operator `Q_U` and the resistive sink `D_C` remain those already derived in D10-ZF and are not merged into the target observable. They are not needed to define the Pilot-0.1 optimization tuple requested here.

## 7. Physical admissibility of `B=I`

For this fixed-`k_y` Galerkin representation, the retained coefficients of `phi` and `eta` are independent small perturbation amplitudes. The physical real field is obtained in the usual way by including the conjugate `-k_y` sector; this imposes no additional algebraic constraint among the six coefficients of the represented `+k_y` amplitude vector.

There is also no D10-ZF constraint that ties the initial density perturbation to the initial potential perturbation. Every vector in the retained six-dimensional Galerkin state has finite positive perturbation energy because `M>0`.

Therefore the full retained perturbation space is physically admissible for Pilot 0.1, and

```math
\boxed{B=I_6}
```

is accepted.

This choice is **not** a transport-neutral restriction: in general

```math
B^\dagger Q_\Gamma B=Q_\Gamma\neq0.
```

That is not a defect of physical admissibility; it only means that Pilot 0.1 does not impose initial particle-flux neutrality at the specification stage.

With the natural physical initial-energy cost,

```math
R_{\rm in}=B^\dagger M B,
```

so the frozen input metric is

```math
\boxed{R_{\rm in}=M
=\operatorname{diag}(2,1,2,1,1,1).}
```

## 8. Frozen Pilot 0.1 tuple

The canonical D10-ZF Pilot 0.1 specification is therefore

```text
U(x)                 = cos(x)
Phi(x)               = sin(x) + const.
N(x)                 = 0
L_x                  = 2*pi
k0                   = 1
k_y                  = 1
C                     = 1
kappa                 = 1
additional damping    = 0
radial modes          = (-1, 0, +1)
N_x                   = 3
state dimension       = 6
state ordering        = (phi_-1, phi_0, phi_+1, eta_-1, eta_0, eta_+1)
tau_ref               = 1 normalized D10-ZF time unit
B                     = I_6
R_in                  = M
```

The matrices `A`, `M`, and `Q_Gamma` are the explicit matrices displayed above.

## 9. Explicit stop boundary

This specification does **not** evaluate:

- eigenvalues or spectral stability;
- energy contraction or transient growth;
- nonnormality;
- terminal or cumulative transport gains;
- generation order;
- optimizer directions or energy/transport angles;
- parameter sensitivity;
- truncation convergence.

Those are later pilot-evaluation questions. This note ends after fixing the single canonical parameter point and checking the physical admissibility of `B=I`.
