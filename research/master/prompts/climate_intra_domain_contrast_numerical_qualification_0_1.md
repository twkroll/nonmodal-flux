# MASTER Prompt — Climate Intra-Domain Contrast Numerical Qualification 0.1

**Authority:** `research/climate/climate_intra_domain_contrast_candidate_freeze_0_1.md`, `research/master/climate_intra_domain_contrast_feasibility_gate_0_1.md`, and the shared prompt handoff protocol.

**Target chat:** existing Climate chat.

**Scope:** structural and spectral numerical qualification of the already frozen Climate-B candidate only. No finite-time CORE operator, no horizon selection, no optimizer, no angle, no performance gap, no parameter search, no retuning, no new channel, and no change to Climate-A.

## Frozen candidate

Use exactly the frozen equivalent-barotropic Bickley-jet candidate:

\[
U(y)=U_0\operatorname{sech}^2((y-y_0)/L),
\]

with

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

Use exactly the frozen Fourier/sine Galerkin representation, positive zonal Fourier modes with conjugate real-field reconstruction, `B=I`, `R_in=M_K`, the kinetic-energy matrix `M_K`, and the jet-translation forcing matrix `Q_shift,K` defined in the Candidate Freeze.

Frozen resolution roles:

- `(8,16)` structural smoke;
- `(12,24)` coarse audit;
- `(16,32)` primary;
- `(20,40)` confirmation;
- `(24,48)` high-resolution audit.

No rung may be added, removed, or reassigned.

## Required qualification tasks

For every frozen rung:

1. Assemble `A_K`, `M_K`, and `Q_shift,K` exactly from the Candidate Freeze using 512-point Gauss–Legendre quadrature for `U_N`, `C_N`, and `R_N`.
2. Perform the frozen 512-versus-1024 quadrature audit and require
   \[
   \|X_{1024}-X_{512}\|_F/\max(1,\|X_{1024}\|_F)\le10^{-12}
   \]
   for `X in {U_N,C_N,R_N}`.
3. Verify `M_K=M_K^\dagger\succ0` and report the minimum eigenvalue.
4. Verify `Q_shift,K=Q_shift,K^\dagger`, nontriviality, and signed indefiniteness by reporting at least one positive and one negative eigenvalue.
5. Verify the exact parity selection rules for `A_K` and `Q_shift,K` and report parity-forbidden residuals.
6. Reproduce the predeclared deterministic sign witness from Candidate Freeze §9.2 (`m=1`, `c_11=1`, `c_12=i`, all others zero) both by direct spatial Reynolds-stress/translation projection and by `x_K^\dagger Q_shift,K x_K`; replacing `i` by `-i` must reverse the sign while leaving kinetic energy unchanged.
7. Compute the complete spectrum of every modal `A_m` and the global spectral abscissa
   \[
   \alpha(A_K)=\max\Re\lambda(A_K).
   \]
8. Require `alpha(A_K)<0` at every frozen rung. If any rung is genuinely unstable, the qualification fails and Climate-B stops; no physical retuning is allowed.
9. Assess nested spectral convergence using common retained modal branches and the rightmost spectral boundary across the frozen ladder. Report whether the stability conclusion is robust under refinement.
10. Record conditioning of each Laplacian block `D_m` (or the worst case per rung) and normalized eigenpair residuals sufficient to exclude numerical eigensolver failure. Numerical residuals should be at or below ordinary double-precision scientific standards (`~1e-10` relative or better); if not, STOP rather than reinterpret the spectrum.

## Forbidden actions

Do **not** compute or inspect:

\[
K_M(T),\quad K_{\rm shift}(T),\quad G_M(T),\quad J_{\rm shift}^{\pm}(T),
\]

optimizer directions/subspaces, optimizer angles, `Delta_Q`, any horizon dependence, or any finite-time objective separation.

Do not select a horizon ladder in this task.

Do not change `U0`, `L`, `beta`, `r`, `Lx`, `Ly`, the Bickley profile, the translation tangent `g=-U'`, `B`, `R_in`, basis family, quadrature rule, or resolution roles.

Do not reopen or reinterpret Climate-A; it remains `CLIM-WEAK`.

## Verdict classes

End with exactly one of:

- `QUALIFIED` — all structural/channel checks pass, the complete frozen ladder is spectrally stable, and refinement supports a robust stability conclusion;
- `FAIL — STRUCTURAL/NUMERICAL` — a frozen representation/channel/assembly requirement fails;
- `FAIL — SPECTRAL STABILITY` — the frozen candidate is not robustly spectrally stable.

A FAIL is a valid one-shot Climate-B outcome. No third Climate candidate is authorized.

## Required canonical outputs

Create:

`research/climate/climate_intra_domain_contrast_numerical_qualification_0_1.md`

If useful for reproducibility, also create a machine-readable qualification table under:

`research/climate/climate_intra_domain_contrast_numerical_qualification_0_1_data.csv`

and a regression test under `tests/` that checks only the frozen qualification objects; it must not construct any finite-time CORE-effect operator.

Update:

`research/climate/STATUS.md`

The final result file must contain scope/forbidden actions, frozen model/representation, assembly checks, channel sign witness, spectral results for all rungs, convergence/conditioning diagnostics, PASS/FAIL verdict, allowed/forbidden interpretation, and a final STOP.

Commit all outputs and report the canonical paths, full commit hash, and CI status if available.

After completion, set Climate status to either:

`CLIMATE-B NUMERICAL QUALIFICATION COMPLETE — RETURN TO MASTER`

or the corresponding FAIL/STOP return state.

**STOP after returning to MASTER.**