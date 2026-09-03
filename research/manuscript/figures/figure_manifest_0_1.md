# Figure Manifest 0.1

**Package:** Frozen-Data Figure Production Package 0.1  
**Primary target:** Physical Review E — Regular Article  
**Scientific authority:** `research/manuscript/figure_source_map_0_2.md`  
**Initial figure-production handoff base:** `bbe894289bb8f95d09397f9828e27cae38711106`  
**Rule:** frozen stored data only; no new scientific calculation, interpolation, smoothing, fit, added horizon/resolution, or Climate-B repair.

## Frozen numeric inputs

| Input | Git blob SHA |
|---|---|
| `research/d10_zf_pilot_0_2_execution_data.csv` | `51c454d5e0425036f2eafd69e2e3292953b272ac` |
| `research/neuro/neuro_pilot_0_1_execution_data.csv` | `31209401b3991bb0331f380dd10650d326c566da` |
| `research/climate/climate_ocean_pilot_0_1_execution_data.csv` | `abb458223a2630f8a7c75a9da1deee833c6b2986` |
| `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv` | `fa475bb87c7a0b8751ce4a546b885d7632caaa32` |

Definition/wording authority is additionally taken from the specification/result files authorized by `figure_source_map_0_2.md`; those files are never executed by the plotting script.

## Main figure assets

Each main figure has an SVG vector asset and a PNG inspection preview. PNGs are presentation previews only; SVG is the publication-oriented vector master.

| Figure | SVG SHA-256 | PNG Git blob SHA | PNG bytes |
|---|---|---|---:|
| Fig. 1 `fig1_common_workflow` | `33e81669b4b9fd0b3555b782aa91172ee20a48d9db649c074a26760f56116306` | `35f12b7174abbdfac0d2b80c406bdeadbded7c76` | 2584 |
| Fig. 2 `fig2_plasma_strong_anchor` | `920fca939bc141024d2660b77bee49e6aba73ca0a590da7b22582fce8b6b6b9c` | `a4ed328d6780c68db4433d777711fc9381d09089` | 2564 |
| Fig. 3 `fig3_neuro_two_pulse` | `d8b81e352681039c5dc164d42983e6517b232948150313c7edad0df57fcffc0c` | `b8b3b55b0611bebc0d5d9f9450328b9b01c6e283` | 2817 |
| Fig. 4 `fig4_climate_a_weak_contrast` | `1296b6eca744afa2bf00dff82d437b0984310da9d23e6e69e4da2575e810a720` | `7d35c7299adbaf73ca46927728195b1809f8ba9a` | 2478 |
| Fig. 5 `fig5_cross_domain_summary` | `ed23a39c714cd4ac6ab7f3f8aca4c5656c819f837795e600c450f18e24108bf8` | `4d751b4afebdbef7dbccd1472de98358761099b3` | 1999 |

## Supplement figure asset

| Figure | SVG SHA-256 | PNG Git blob SHA | PNG bytes |
|---|---|---|---:|
| Fig. S5 `figS5_climate_b_robustness_rejection` | `3f56306ab4bbfe6396b57eeb756873d2c5dd7d7508053ee2bcd9935f12d3d6b2` | `41a0383b422c66c9892f2c56ccec956b41052b17` | 3230 |

## Tables and source files

| File | SHA-256 |
|---|---|
| `research/manuscript/figures/captions_0_1.md` | `79acca57773173620a4eb22962973eb1cc4211559ea9d9cc56faab3fac48abee` |
| `research/manuscript/figures/src/generate_frozen_data_figures_0_1.py` | `54a879ef9117460986612fabbf844c454b59e68cf2305819a777fad5347e222d` |
| `research/manuscript/figures/src/validate_frozen_data_figures_0_1.py` | `deb212242a8bd842900f0c23ed6c86e17eb24c3d071b083baaf2eedaf06b427c` |
| `research/manuscript/figures/tables/main_table_1.md` | `33e5abf430d1dd4cdfcef3f6b9b8f2f56010726aefe3bce32ad1fca5131d9745` |
| `research/manuscript/figures/tables/main_table_1.tex` | `b10208e8414a1568de00c04f442418b950888541d75e4b2852027180d1b59bf3` |
| `research/manuscript/figures/tables/supplement_table_s1_operational_rules_outcomes.md` | `e465c888a13fad2a181288b6805f988a045b38221d2bf32bac713ac6c972fee2` |
| `research/manuscript/figures/tables/supplement_table_s1_operational_rules_outcomes.tex` | `b29bfcecf3363669fba74597587544a7ac3f5672b677f6dc9757f477660ef1e2` |

## Reproduction command

From repository root:

```bash
python research/manuscript/figures/src/generate_frozen_data_figures_0_1.py --repo-root .
python research/manuscript/figures/src/validate_frozen_data_figures_0_1.py --repo-root .
```

The generator performs only row selection, assertion, plotting-coordinate scaling, labeling, and SVG/PNG rendering.
