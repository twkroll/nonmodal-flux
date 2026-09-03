#!/usr/bin/env python3
"""Frozen-data manuscript figure generator.

Reads only committed frozen CSVs. Operations are selection, assertions, labeling,
coordinate plotting and rendering. No model, eigensolve, matrix exponential, trajectory,
interpolation, smoothing, fit, optimization or parameter search is performed.
"""
from pathlib import Path
import argparse, csv
import matplotlib.pyplot as plt

H=(.25,.5,1.,2.,4.,8.); N=(7.,14.,28.,56.,112.,224.)

def read(p):
    with p.open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
def F(r,k):return float(r[k])
def save(fig,p):
    p.parent.mkdir(parents=True,exist_ok=True); fig.savefig(p,format='svg',bbox_inches='tight'); fig.savefig(p.with_suffix('.png'),dpi=140,bbox_inches='tight'); plt.close(fig)
def pairs(ax,x,a,b,la,lb,xlab):
    ax.plot(x,a,'o-',label=la); ax.plot(x,b,'s--',label=lb); ax.set_ylim(0,1); ax.set_xlabel(xlab); ax.legend(frameon=False); ax.grid(axis='y',alpha=.25)

def main(root:Path):
    P=read(root/'research/d10_zf_pilot_0_2_execution_data.csv'); R=[r for r in P if int(r['K'])==32]
    assert sorted({int(r['K']) for r in P})==[32,64,96] and tuple(F(r,'T') for r in R)==H
    Ndat=read(root/'research/neuro/neuro_pilot_0_1_execution_data.csv'); assert tuple(F(r,'T_ms') for r in Ndat)==N
    C=read(root/'research/climate/climate_ocean_pilot_0_1_execution_data.csv'); Cp=[r for r in C if r['resolution_role']=='primary']; assert tuple(F(r,'T_over_tau_ref') for r in Cp)==H
    B=read(root/'research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv'); Bp=[r for r in B if r['role']=='primary']; Bc=[r for r in B if r['role']=='confirmation']; assert tuple(F(r,'T_over_tau') for r in Bp)==H==tuple(F(r,'T_over_tau') for r in Bc)
    out=root/'research/manuscript/figures'

    fig,ax=plt.subplots(figsize=(7.0,3.5)); ax.axis('off'); ax.set_title('Figure 1. Common frozen-data workflow',loc='left')
    boxes=[('1  Freeze tuple','A, M, Q, B, R_in'),('2  Build objectives','positive metric vs signed channel'),('3  Compare diagnostics','geometry vs target performance'),('4  Gate robustness','direct checks + refinement')]
    for i,(h,t) in enumerate(boxes):
        x=.02+i*.245; ax.text(x+.105,.73,h,ha='center',weight='bold',transform=ax.transAxes); ax.text(x+.105,.63,t,ha='center',transform=ax.transAxes,fontsize=8); ax.add_patch(plt.Rectangle((x,.56),.21,.27,fill=False,transform=ax.transAxes));
        if i<3: ax.text(x+.225,.68,'→',transform=ax.transAxes)
    ax.text(.02,.43,'Plasma: free energy  ↔  particle transport',transform=ax.transAxes); ax.text(.02,.31,'Neuro: synaptic-filter storage  ↔  V1-SP → V4-SS contribution',transform=ax.transAxes); ax.text(.02,.19,'Climate-A: QG energy  ↔  poleward eddy heat transport',transform=ax.transAxes); ax.text(.02,.04,'Climate-B is Supplement robustness-rejection evidence, not a fourth robust domain.',transform=ax.transAxes,fontsize=8)
    save(fig,out/'main/fig1_common_workflow.svg')

    t=[F(r,'T') for r in R]; th=[F(r,'theta_deg')/90 for r in R]; d=[F(r,'delta') for r in R]; qp=[F(r,'qplus') for r in R]; qm=[F(r,'qminus') for r in R]
    r1=next(r for r in R if F(r,'T')==1); assert abs(F(r1,'delta')-.504337166854)<1e-12
    fig,(a,b)=plt.subplots(1,2,figsize=(7,3.5)); fig.suptitle('Figure 2. Plasma strong anchor (P2-A)'); pairs(a,t,th,d,'theta/90','Delta_Gamma','T'); b.plot(t,qp,'o-',label='J_Gamma+'); b.plot(t,qm,'s--',label='J_Gamma−'); b.axhline(0,lw=.8); b.set_xlabel('T'); b.legend(frameon=False); b.text(.03,.95,'T=1: theta=53.40°, Delta=0.5043',transform=b.transAxes,va='top',fontsize=8); save(fig,out/'main/fig2_plasma_strong_anchor.svg')

    tm=[F(r,'T_ms') for r in Ndat]; th=[F(r,'theta_deg')/90 for r in Ndat]; d=[F(r,'Delta_Q') for r in Ndat]
    n112=next(r for r in Ndat if F(r,'T_ms')==112); n224=next(r for r in Ndat if F(r,'T_ms')==224)
    fig,axs=plt.subplots(1,3,figsize=(7.2,3.5)); fig.suptitle('Figure 3. Neuro constrained two-pulse result'); pairs(axs[0],tm,th,d,'theta/90','Delta_Q','T [ms]')
    for ax,r,title in [(axs[1],n112,'112 ms'),(axs[2],n224,'224 ms')]:
        ax.axhline(0,lw=.5); ax.axvline(0,lw=.5); ax.quiver(0,0,F(r,'wM_h1'),F(r,'wM_h2'),angles='xy',scale_units='xy',scale=1,label='w_M'); ax.quiver(0,0,F(r,'wQ_h1'),F(r,'wQ_h2'),angles='xy',scale_units='xy',scale=1,label='w_Q'); ax.set_xlim(-1.1,1.1); ax.set_ylim(-1.1,1.1); ax.set_aspect('equal'); ax.set_title(title); ax.set_xlabel('pulse 1'); ax.set_ylabel('pulse 2'); ax.legend(frameon=False,fontsize=7)
    fig.text(.5,.01,'Fixed 1-ms preparations; V1-SP → V4-SS channel. No reachable negative cumulative branch is depicted.',ha='center',fontsize=8); save(fig,out/'main/fig3_neuro_two_pulse.svg')

    th=[F(r,'angle_deg_conservative')/90 for r in Cp]; d=[F(r,'Delta_heat_conservative') for r in Cp]; c8=next(r for r in Cp if F(r,'T_over_tau_ref')==8)
    assert (int(c8['energy_opt_abs_m']),int(c8['energy_opt_n']))==(3,2) and (int(c8['heat_opt_abs_m']),int(c8['heat_opt_n']))==(4,2)
    fig,(a,b)=plt.subplots(1,2,figsize=(7.2,3.5)); fig.suptitle('Figure 4. Climate-A robust weak contrast (CLIM-WEAK)'); pairs(a,H,th,d,'theta_sub/90','Delta_heat','T/tau_ref'); b.axis('off'); b.text(.02,.88,'T/tau_ref=8',weight='bold'); b.text(.02,.72,'Energy optimum: (|m|,n)=(3,2), BT=0.3373'); b.text(.02,.60,'Heat optimum: (|m|,n)=(4,2), BT=0.1762'); b.text(.02,.44,'Subspace angle = 90°',weight='bold'); b.text(.02,.31,'Delta_heat = 0.04118'); b.text(.02,.19,'Energy optimum retains 95.88% of J_heat+',weight='bold'); b.text(.02,.06,'All six frozen horizons pass refinement.',fontsize=8); save(fig,out/'main/fig4_climate_a_weak_contrast.svg')

    p=next(r for r in R if F(r,'T')==1); n1=n112; n2=n224; c=c8
    labs=['Plasma T=1','Neuro 112 ms','Neuro 224 ms','Climate-A T/tau=8']; ang=[F(p,'theta_deg'),F(n1,'theta_deg'),F(n2,'theta_deg'),F(c,'angle_deg_conservative')]; gap=[F(p,'delta'),F(n1,'Delta_Q'),F(n2,'Delta_Q'),F(c,'Delta_heat_conservative')]
    fig,(a,b)=plt.subplots(2,1,figsize=(7,3.7)); fig.suptitle('Figure 5. Robust-domain geometry/performance summary'); y=range(4); a.scatter(ang,y,facecolors='none',edgecolors='black'); a.set_xlim(0,90); a.set_yticks(y,labs); a.set_xlabel('optimizer / subspace angle [deg]'); b.scatter(gap,y,facecolors='none',edgecolors='black'); b.set_xlim(0,1); b.set_yticks(y,labs); b.set_xlabel('target-performance gap Delta_Q'); fig.text(.5,.01,'Non-inferential; Climate-B excluded (see Supplement S5).',ha='center',fontsize=8); save(fig,out/'main/fig5_cross_domain_summary.svg')

    eps1=[F(r,'eps_Jplus_to_next') for r in Bp]; eps2=[F(r,'eps_Jplus_to_next') for r in Bc]; muM1=[F(r,'mu_M_to_next') for r in Bp]; muQ1=[F(r,'mu_shift_to_next') for r in Bp]; muM2=[F(r,'mu_M_to_next') for r in Bc]; muQ2=[F(r,'mu_shift_to_next') for r in Bc]
    assert all(r['resolution_robust_for_verdict'].lower()=='false' for r in Bp) and abs(F(Bp[-1],'Delta_shift')-1)<1e-10
    fig,(a,b)=plt.subplots(1,2,figsize=(7.5,3.8)); fig.suptitle('Supplement Fig. S5. CLIM-B-FAIL — resolution robustness failure; 0/6 robust'); a.plot(H,eps1,'o-',label='primary→confirmation'); a.plot(H,eps2,'s--',label='confirmation→high'); a.axhline(.02,ls=':',label='frozen limit 0.02'); a.set_xlabel('T/tau_ref'); a.set_ylabel('epsilon_J+'); a.legend(frameon=False,fontsize=7); b.plot(H,muM1,'o-',label='M P→C'); b.plot(H,muQ1,'s--',label='Shift P→C'); b.plot(H,muM2,'^-',label='M C→H'); b.plot(H,muQ2,'v--',label='Shift C→H'); b.axhline(.95,ls=':',label='frozen minimum 0.95'); b.set_ylim(0,1); b.set_xlabel('T/tau_ref'); b.set_ylabel('captured common-space mass'); b.legend(frameon=False,fontsize=7); fig.text(.5,.01,'Local algebraic/direct gates PASS; fixed-truncation Delta_shift=1 is rejected by failed refinement.',ha='center',fontsize=8); save(fig,out/'supplement/figS5_climate_b_robustness_rejection.svg')

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--repo-root',type=Path,default=Path(__file__).resolve().parents[4]); a=ap.parse_args(); main(a.repo_root)
