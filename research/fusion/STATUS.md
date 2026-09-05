# Fusion Branch Status

**Last updated:** 2026-09-05  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and the submission track remains parked.

B5.5, F1.2, F1.3 and F1.4 are complete and MASTER-integrated. The targeted R1 structural-redundancy / fidelity-breaking literature audit is also complete and MASTER-integrated.

## Frozen R1 status

The anisotropic-ZLR four-moment R1 minimal-curvature candidate remains a frozen structural/conservative control. Its exact collisionless one-channel balance and the frozen `B=I_4`, `R_in=M_k` geometry imply

\[
2\frac{R_0}{L_T}K_q(T)=\mathcal E_M(T)-I,
\]

so cumulative ion-heat and final free-energy optimization are affinely equivalent at every horizon. The R1 objective-separation pilot remains blocked.

No damping, retuning or FLR-only rescue is permitted.

## Integrated literature guidance

Canonical audit:

`research/literature/fusion_r1_structural_redundancy_fidelity_breaking_literature_audit_0_1.md`

MASTER integration freeze:

`research/master/fusion_r1_structural_redundancy_literature_integration_freeze_0_1.md`

The audit positions the R1 no-go as an explicit optimal-control consequence of a standard one-channel gyrokinetic free-energy-balance limit, not as a new free-energy theorem. No `SAME` source was found; absence is not novelty evidence.

Physics-first conclusions carried forward:

- H-theorem-compatible physical collisions can add a positive free-energy sink;
- nonadiabatic electrons can add an independent electron free-energy drive;
- conservative FLR alone does not generically add an independent source/sink;
- collisionless phase mixing is redistribution in the fully resolved kinetic system; reduced sinks require explicit balance/sign verification.

## Active instruction

**Status:** `FUSION F2.1 TWO-SPECIES LOCAL-GK CANDIDATE / BALANCE SPECIFICATION READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_f2_1_two_species_local_gyrokinetic_balance_specification_gate_0_1.md`

On a bare `GO`, first read this STATUS and execute only that committed instruction.

## F2.1 scope

Specify one balance-complete two-species local-gyrokinetic higher-fidelity lineage using physical/source criteria only. The leading reduced architecture is finite-ion-FLR gyrokinetic ions plus nonadiabatic bounce-averaged/trapped electrons, with fully kinetic two-species local gyrokinetics retained as the higher-fidelity reference if the exact balance closes consistently.

F2.1 must derive the positive free-energy functional, physical species particle/heat transport channels, collision treatment and exact source/dissipation balance, and determine only whether the R1 affine redundancy is no longer structurally forced.

## Forbidden until F2.1 returns

Do not discretize velocity space for optimization, scan parameters or model variants, run GENE, construct finite-time propagators/Gramians/objective operators, compute optimizers/angles/gaps, or choose fidelity by expected effect size. Do not open MODES/CONT/CASCADE, Power Grid/Photonics work, or modify the frozen first paper.

## Expected return state

One of:

- `F2.1 PASS — TWO-SPECIES GK CANDIDATE/BALANCE SPECIFIED — RETURN TO MASTER`;
- `F2.1 HOLD — SPECIFIC MODEL/BALANCE DECISION REQUIRED — RETURN TO MASTER`;
- `F2.1 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Governance authority

- `research/master/fusion_f1_4_marginal_structural_integration_freeze_0_1.md`
- `research/literature/fusion_r1_structural_redundancy_fidelity_breaking_literature_audit_0_1.md`
- `research/master/fusion_r1_structural_redundancy_literature_integration_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / AWAIT GO.**
