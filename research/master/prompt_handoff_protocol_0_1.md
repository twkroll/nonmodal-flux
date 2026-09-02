# Shared Prompt Handoff Protocol 0.1

**Status:** ACTIVE GOVERNANCE  
**Date:** 2026-09-02

## Purpose

Eliminate manual copy/paste of long MASTER prompts between project chats while preserving exact scope, STOP conditions and reproducibility.

## Canonical rule

When MASTER decides that a branch requires more than a bare `GO`, MASTER writes the exact instruction to a committed Markdown file under

`research/master/prompts/`

and the relevant branch `STATUS.md` points to that file.

The committed prompt file, not a copied chat message, is the canonical handoff instruction.

## Branch-chat execution convention

When the user writes `GO` in an active branch chat, that chat should first read its branch status file

`research/<branch>/STATUS.md`

and then read the `Next instruction` path recorded there.

The branch chat executes only the scope in that committed prompt, produces the requested canonical result Markdown, updates its `STATUS.md`, commits both, and stops at the specified STOP point.

If `STATUS.md` says `WAIT`, `BLOCKED`, `RETURN TO MASTER`, or contains no active prompt path, `GO` must not silently open new work.

## File naming

Versioned canonical instructions use

`research/master/prompts/<branch>_<gate_or_task>_0_1.md`

The branch status file records the exact active path. Versioned prompt files are never overwritten after execution; a later instruction receives a new version/name.

## Result handoff

After a branch finishes, the user does not need to copy the result back to MASTER. A later `Status?`, integration command, or explicit MASTER gate reads the committed branch `STATUS.md` and canonical result file directly from the repository.

## Governance constraints

- MASTER remains the only place that opens a new branch, changes a freeze, or changes global success criteria.
- Branch chats may execute a committed instruction but may not infer a new uncommitted research program from `GO`.
- All Gate/Freeze/Audit/Pilot outputs must remain committed Markdown plus an updated branch `STATUS.md`.
- Numerical data/tests may be added as separate files where needed.
- A prompt handoff does not itself authorize calculations forbidden by an earlier freeze.

## Current adoption

The protocol becomes active with the post-Cross-Domain-Integration instructions for Neuro and Climate.

- Neuro next prompt: `research/master/prompts/neuro_pilot_specification_0_1.md`
- Climate next prompt: `research/master/prompts/climate_ocean_pilot_specification_0_1.md`

## Decision log

- **DEC-291:** Shared Prompt Handoff Protocol 0.1 adopted — STABLE.
- **DEC-292:** `GO` in an active branch means read `STATUS.md` plus the committed `Next instruction` before acting — STABLE.
- **DEC-293:** Manual copy/paste of MASTER prompts is no longer required when an active prompt file exists — STABLE.

