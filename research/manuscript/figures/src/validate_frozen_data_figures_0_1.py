#!/usr/bin/env python3
"""Validation for Frozen-Data Figure Production Package 0.1.

Checks frozen horizon/role selections and canonical witness values directly from stored CSVs,
then checks rendered SVG guardrails. No scientific solver is invoked.
"""
from __future__ import annotations
import csv
from pathlib import Path

H=(0.25,0.5,1.0,2.0,4.0,8.0)
N=(7.0,14.0,28.0,56.0,112.0,224.0)

def rows(p):
    with p.open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
def f(r,k): return float(r[k])
def close(a,b,tol=1e-9): assert abs(a-b)<=tol,(a,b)

def main(root:Path):
    plasma=rows(root/'research/d10_zf_pilot_0_2_execution_data.csv')
    assert sorted({int(r['K']) for r in plasma})==[32,64,96]
    p32=[r for r in plasma if int(r['K'])==32]; assert tuple(f(r,'T') for r in p32)==H
    p1=next(r for r in p32 if f(r,'T')==1); close(f(p1,'theta_deg'),53.3959703434); close(f(p1,'delta'),0.504337166854,1e-12)

    neuro=rows(root/'research/neuro/neuro_pilot_0_1_execution_data.csv'); assert tuple(f(r,'T_ms') for r in neuro)==N
    n112=next(r for r in neuro if f(r,'T_ms')==112); n224=next(r for r in neuro if f(r,'T_ms')==224)
    close(f(n112,'theta_deg'),46.82427052368796); close(f(n112,'Delta_Q'),0.5290171344769217,1e-12)
    close(f(n112,'wQ_h1'),0.9924098526364102,1e-12); close(f(n112,'wQ_h2'),-0.1229743241094608,1e-12)
    close(f(n224,'theta_deg'),65.05825610409036); close(f(n224,'Delta_Q'),0.8178408750718505,1e-12)

    ca=rows(root/'research/climate/climate_ocean_pilot_0_1_execution_data.csv')
    cp=[r for r in ca if r['resolution_role']=='primary']; assert tuple(f(r,'T_over_tau_ref') for r in cp)==H
    c8=next(r for r in cp if f(r,'T_over_tau_ref')==8); close(f(c8,'angle_deg_conservative'),90,1e-12); close(f(c8,'Delta_heat_conservative'),0.0411845533755,1e-12)
    assert (int(c8['energy_opt_abs_m']),int(c8['energy_opt_n']))==(3,2); assert (int(c8['heat_opt_abs_m']),int(c8['heat_opt_n']))==(4,2)

    cb=rows(root/'research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv')
    bp=[r for r in cb if r['role']=='primary']; bc=[r for r in cb if r['role']=='confirmation']
    assert tuple(f(r,'T_over_tau') for r in bp)==H and tuple(f(r,'T_over_tau') for r in bc)==H
    assert sum(r['resolution_robust_for_verdict'].strip().lower()=='true' for r in bp)==0
    close(f(bp[-1],'mu_M_to_next'),0.728056084924855,1e-12); close(f(bp[-1],'mu_shift_to_next'),0.7513127890738873,1e-12)
    close(f(bc[-1],'mu_M_to_next'),0.7808402944455248,1e-12); close(f(bc[-1],'mu_shift_to_next'),0.8337269694786571,1e-12)

    figs=root/'research/manuscript/figures'
    required=[figs/'main/fig1_common_workflow.svg',figs/'main/fig2_plasma_strong_anchor.svg',figs/'main/fig3_neuro_two_pulse.svg',figs/'main/fig4_climate_a_weak_contrast.svg',figs/'main/fig5_cross_domain_summary.svg',figs/'supplement/figS5_climate_b_robustness_rejection.svg']
    for p in required: assert p.exists() and p.stat().st_size>500,p
    f5=(figs/'main/fig5_cross_domain_summary.svg').read_text(encoding='utf-8')
    assert 'Climate-B excluded' in f5 and 'Delta_shift' not in f5
    f3=(figs/'main/fig3_neuro_two_pulse.svg').read_text(encoding='utf-8'); assert 'Reachable cumulative negative branch: not depicted' in f3
    f4=(figs/'main/fig4_climate_a_weak_contrast.svg').read_text(encoding='utf-8'); assert '95.88% retained' in f4 and '90°' in f4
    s5=(figs/'supplement/figS5_climate_b_robustness_rejection.svg').read_text(encoding='utf-8'); assert 'CLIM-B-FAIL' in s5 and '0/6' in s5 and 'Delta_shift=1' in s5

    gen=(figs/'src/generate_frozen_data_figures_0_1.py').read_text(encoding='utf-8').lower()
    forbidden=('scipy','numpy.linalg.eig','expm(','solve_lyapunov','interp1d','polyfit','curve_fit','minimize(','svd(')
    for token in forbidden: assert token not in gen,token
    print('PASS — frozen-data values, selections, guardrails, and solver prohibitions verified.')

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument('--repo-root',type=Path,default=Path(__file__).resolve().parents[4]); a=ap.parse_args(); main(a.repo_root)
