# Frozen-Data Figure Validation 0.1

**Status:** PASS  
**Scope:** presentation validation only; no scientific recomputation.

## Automated checks

`validate_frozen_data_figures_0_1.py` passed after generation and verifies:

1. Plasma stored resolutions are exactly `K={32,64,96}` and the `K=32` display horizon set is exactly `{0.25,0.5,1,2,4,8}`;
2. Plasma `T=1` reproduces stored `theta=53.3959703434 deg` and `Delta_Gamma=0.504337166854`;
3. Neuro horizons are exactly `{7,14,28,56,112,224} ms`, including the stored signed pulse coordinates and 112/224-ms witnesses;
4. Climate-A primary horizons are exactly `{0.25,0.5,1,2,4,8}`, with stored longest-horizon `(3,2)` versus `(4,2)`, `90 deg`, and `Delta_heat=0.0411845533755`;
5. Climate-B primary/confirmation horizon sets are exactly frozen; `0/6` primary horizons are robust, and the stored longest-horizon common-space masses are checked;
6. Main Fig. 5 explicitly excludes Climate-B and contains no Climate-B fixed-resolution `Delta_shift` point;
7. Neuro figure explicitly preserves the reachable-sign restriction;
8. Climate-A figure pairs the `90 deg` geometry with `95.88%` retained target performance;
9. Supplement Fig. S5 contains `CLIM-B-FAIL`, `0/6`, and any `Delta_shift=1` mention in the same failure-qualified visual;
10. the generator contains no calls/imports corresponding to scientific eigensolvers, matrix exponentials, Lyapunov solves, interpolation routines, polynomial/curve fitting, numerical optimization, or SVD.

Python syntax compilation of both source scripts also passed.

## Visual checks

All six SVG assets were raster-rendered solely for inspection. Review found:

- no clipped panel titles or axes;
- no overlapping table-like text blocks after final layout adjustment;
- readable monochrome line/marker distinctions without relying on color;
- Neuro pulse-coordinate signs retained;
- Climate-A `90 deg` / `Delta_heat≈0.0412` contrast visible together;
- Main Fig. 5 presented as aligned diagnostic strips with no trend line, decision region, phase-diagram framing, threshold boundary, fit, or regression;
- Supplement Fig. S5 visually separates local PASS gates from cross-resolution FAIL gates and prominently states `CLIM-B-FAIL — resolution robustness failure; 0/6 frozen horizons robust`.

## Omitted / simplified panels

- Plasma Fourier-mode weight and full trajectory panels were omitted because the required main message is already directly supported by stored horizon quantities and the package avoids reconstructing any scientific time series.
- Neuro uses the directly stored two-pulse coordinates rather than a state-space trajectory depiction.
- Climate-A uses stored modal-support/BT-fraction summaries and stored cumulative values, not reconstructed fields or trajectories.
- Climate-B principal-angle details are omitted from the compact figure because stored objective-value convergence plus common-space mass already demonstrates the frozen rejection; the full frozen execution table remains canonical.

## Output-format check

SVG is used as the vector publication master for each figure, with PNG previews already present for inspection. Tables are supplied in Markdown and LaTeX-compatible form. No font files are included.

**Verdict:** PASS — figure/table assets satisfy Frozen-Data Figure Production Package 0.1 without opening new science.
