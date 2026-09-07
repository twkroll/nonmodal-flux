from __future__ import annotations
import hashlib, importlib.util, json
from pathlib import Path
import numpy as np
from scipy import special

HERE=Path(__file__).resolve().parent
SRC=HERE/"fusion_f2_6b_operator_0_1.py"
spec=importlib.util.spec_from_file_location("fusion_f2_6b_operator_0_1", SRC)
opm=importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name]=opm
spec.loader.exec_module(opm)

SEEDS=[20260907,20260908,20260909]
TOL=dict(
    flr_rel=1e-9,
    qn=1e-12,
    solve_E=1e-12,
    metric_hermiticity=1e-11,
    metric_factorization=1e-11,
    skew=1e-11,
    channel_hermiticity=1e-11,
    channel_direct=1e-12,
    ambipolarity_abs=1e-15,
    balance_rel=1e-9,
)

def randvec(K,seed):
    rng=np.random.default_rng(seed)
    x=rng.standard_normal(K.N)+1j*rng.standard_normal(K.N)
    return x/np.linalg.norm(x)

def sha_array(a):
    a=np.ascontiguousarray(a)
    return hashlib.sha256(a.view(np.uint8)).hexdigest()

def flr_envelope(name):
    cfg=opm.LEVELS[name]; W=cfg["W"]; ne=4*W+2
    left=-(2*W+1)*np.pi
    z,wz=special.roots_laguerre(cfg["Nmu"])
    maxabs=maxrel=0.0; worst_theta=worst_b=None
    for e in range(ne):
        j=np.arange(257)
        xc=np.cos(np.pi*j/256)
        th=left+e*np.pi+(xc+1)*np.pi/2
        b=1/(1+opm.EPS*np.cos(th))
        Lam=opm.SHAT*th
        kpr=opm.KY*np.sqrt(1+Lam**2)
        bi=kpr**2/b**2
        exact=special.i0e(bi)
        arg=kpr[:,None]*np.sqrt(2*z[None,:]/b[:,None])
        quad=np.sum(b[:,None]*wz[None,:]*np.exp(-(b[:,None]-1)*z[None,:])*special.j0(arg)**2,axis=1)
        ad=np.abs(quad-exact); rd=ad/np.maximum(exact,1e-300)
        if ad.max()>maxabs: maxabs=float(ad.max())
        ir=int(np.argmax(rd))
        if rd[ir]>maxrel:
            maxrel=float(rd[ir]); worst_theta=float(th[ir]); worst_b=float(bi[ir])
    return dict(points=ne*257,max_abs=maxabs,max_rel=maxrel,worst_theta=worst_theta,worst_b=worst_b)

def bounce_check(Nb):
    def calc(n):
        x,w=special.roots_legendre(n); chi=x*np.pi/2; w=w*np.pi/2
        la=1.0; tb=np.arccos((la-1)/opm.EPS); sb=np.sin(tb/2)
        d=2*np.arcsin(sb*np.sin(chi))
        dth=2*sb*np.cos(chi)/np.sqrt(1-(sb*np.sin(chi))**2)
        b=1/(1+opm.EPS*np.cos(d))
        wt=(opm.QSAF/b)/np.sqrt(np.maximum(1-la*b,1e-300))*dth*w
        wn=wt/wt.sum()
        return np.array([wn.sum(),np.sum(wn*np.cos(d)),np.sum(wn*b)])
    got=calc(Nb); ref=calc(512)
    return dict(one_abs=float(abs(got[0]-ref[0])),cos_abs=float(abs(got[1]-ref[1])),B_abs=float(abs(got[2]-ref[2])))

def manufactured(K):
    th=K.theta[:,None,None]; u=K.u[None,:,None]; z=K.zeta[None,None,:]
    b=1/(1+opm.EPS*np.cos(K.theta))[:,None,None]
    hi=np.exp(-(th/2.5)**2)*(1+0.08*u+0.04*(u*u/2+z*b-1.5))*np.exp(1j*0.15*th)
    wells=np.array(K.metadata["wells"])[:,None,None]
    E=K.xE[None,:,None]; la=K.lam[None,None,:]
    he=np.exp(-(2*np.pi*wells/4.0)**2)*(1+0.05*(E-1.5)+0.08*(la-1))*np.exp(1j*0.1*(2*np.pi*wells))
    return K.join(hi,he)

def qualify_level(name):
    K=opm.build_operator(name)
    active_abs=float(np.max(np.abs(K.gamma_quad-K.gamma_exact)))
    active_rel=float(np.max(np.abs(K.gamma_quad-K.gamma_exact)/K.gamma_exact))
    env=flr_envelope(name)
    vel=K.Di/K.mV[:,None,None]
    den=vel.sum(axis=(1,2))
    Eavg=np.sum(vel*K.energy_i,axis=(1,2))
    Havg=np.sum(vel*(K.energy_i-2.5),axis=(1,2))
    moments=dict(
        density=float(np.max(abs(den-1))),
        energy=float(np.max(abs(Eavg-1.5))),
        heat_weight=float(np.max(abs(Havg+1))),
    )
    cn=np.sqrt(K.Cdiag)
    Hn=(K.Hschur/cn[:,None])/cn[None,:]
    Hfn=(K.Hfield/cn[:,None])/cn[None,:]
    cond=dict(
        Cdiag=float(K.Cdiag.max()/K.Cdiag.min()),
        normalized_E_schur=float(np.linalg.cond(Hn)),
        normalized_positive_field=float(np.linalg.cond(Hfn)),
        E_schur_cholesky_min_diag=float(np.min(np.diag(K.Hchol[0]))),
        positive_field_cholesky_min_diag=float(np.min(np.diag(K.Hfield_chol[0]))),
    )
    maxima=dict(qn=0.0,solve_E=0.0,metric_hermiticity=0.0,metric_factorization=0.0,
                stream_mirror_skew=0.0,full_conservative_skew=0.0,channel_hermiticity=0.0,
                channel_direct=0.0,ambipolarity_abs=0.0,ambipolarity_rel=0.0,
                balance_abs=0.0,balance_rel=0.0)
    for seed in SEEDS:
        x=randvec(K,seed); y=randvec(K,seed+1000)
        sx=K.S_apply(x); phi=K.P_apply(x)
        maxima["qn"]=max(maxima["qn"],float(np.linalg.norm(K.Cdiag*phi-sx)/(np.linalg.norm(sx)+1e-300)))
        maxima["solve_E"]=max(maxima["solve_E"],float(np.linalg.norm(K.solve_E(K.apply_E(x))-x)/np.linalg.norm(x)))
        Mx=K.apply_M(x); My=K.apply_M(y)
        maxima["metric_hermiticity"]=max(maxima["metric_hermiticity"],float(abs(np.vdot(x,My)-np.vdot(Mx,y))/(abs(np.vdot(x,My))+abs(np.vdot(Mx,y))+1e-300)))
        direct=K.direct_positive_energy(x); factor=float(np.vdot(x,Mx).real)
        maxima["metric_factorization"]=max(maxima["metric_factorization"],abs(direct-factor)/(abs(direct)+1e-300))
        xi,xe=K.split(x); yi,ye=K.split(y)
        aix=K.cons_i(xi)+1j*K.wd_i*xi; aiy=K.cons_i(yi)+1j*K.wd_i*yi
        ns=np.vdot(xi,K.Di*aiy)+np.vdot(aix,K.Di*yi)
        ds=abs(np.vdot(xi,K.Di*aiy))+abs(np.vdot(aix,K.Di*yi))+1e-300
        maxima["stream_mirror_skew"]=max(maxima["stream_mirror_skew"],float(abs(ns)/ds))
        cix=K.cons_i(xi); ciy=K.cons_i(yi); cex=K.cons_e(xe); cey=K.cons_e(ye)
        nc=np.vdot(xi,K.Di*ciy)+np.vdot(cix,K.Di*yi)+np.vdot(xe,K.De*cey)+np.vdot(cex,K.De*ye)
        dc=abs(np.vdot(xi,K.Di*ciy))+abs(np.vdot(cix,K.Di*yi))+abs(np.vdot(xe,K.De*cey))+abs(np.vdot(cex,K.De*ye))+1e-300
        maxima["full_conservative_skew"]=max(maxima["full_conservative_skew"],float(abs(nc)/dc))
        for sp,heat in [("i",False),("e",False),("i",True),("e",True)]:
            Qx=K.apply_Q(x,sp,heat); Qy=K.apply_Q(y,sp,heat)
            hh=abs(np.vdot(x,Qy)-np.vdot(Qx,y))/(abs(np.vdot(x,Qy))+abs(np.vdot(Qx,y))+1e-300)
            maxima["channel_hermiticity"]=max(maxima["channel_hermiticity"],float(hh))
            qdirect=K.channel_value(x,sp,heat); qquad=float(np.vdot(x,Qx).real)
            maxima["channel_direct"]=max(maxima["channel_direct"],abs(qdirect-qquad))
        gi=K.channel_value(x,"i"); ge=K.channel_value(x,"e")
        aa=abs(gi-ge); ar=aa/(abs(gi)+abs(ge)+1e-300)
        maxima["ambipolarity_abs"]=max(maxima["ambipolarity_abs"],float(aa))
        maxima["ambipolarity_rel"]=max(maxima["ambipolarity_rel"],float(ar))
        Ax=K.apply_A(x); Ay=K.apply_A(y)
        lhs=np.vdot(x,K.apply_M(Ay))+np.vdot(Ax,K.apply_M(y))
        QG=0.5*(K.apply_Q(y,"i")+K.apply_Q(y,"e"))
        rhs=2*((opm.GPI+opm.GPE)*np.vdot(x,QG)+opm.GTI*np.vdot(x,K.apply_Q(y,"i",True))+opm.GTE*np.vdot(x,K.apply_Q(y,"e",True)))
        ba=abs(lhs-rhs); br=ba/(abs(lhs)+abs(rhs)+1e-300)
        maxima["balance_abs"]=max(maxima["balance_abs"],float(ba))
        maxima["balance_rel"]=max(maxima["balance_rel"],float(br))
    hashes=dict(
        theta=sha_array(K.theta),
        Di=sha_array(K.Di),
        De=sha_array(K.De),
        J0=sha_array(K.J0),
        B_orb_data=sha_array(K.B_orb.data),
        B_orb_indices=sha_array(K.B_orb.indices),
        B_orb_indptr=sha_array(K.B_orb.indptr),
        Hschur=sha_array(K.Hschur),
    )
    criteria=dict(
        flr=active_rel<TOL["flr_rel"] and env["max_rel"]<TOL["flr_rel"],
        weights=(K.Di.min()>0 and K.De.min()>0),
        qn=maxima["qn"]<TOL["qn"],
        solve_E=maxima["solve_E"]<TOL["solve_E"],
        metric=maxima["metric_hermiticity"]<TOL["metric_hermiticity"] and maxima["metric_factorization"]<TOL["metric_factorization"],
        skew=max(maxima["stream_mirror_skew"],maxima["full_conservative_skew"])<TOL["skew"],
        channels=maxima["channel_hermiticity"]<TOL["channel_hermiticity"] and maxima["channel_direct"]<TOL["channel_direct"],
        ambipolarity=maxima["ambipolarity_abs"]<TOL["ambipolarity_abs"],
        balance=maxima["balance_rel"]<TOL["balance_rel"],
    )
    return dict(
        dimensions=K.dims,
        state_layout={"ion":"theta,u,zeta / C-order","electron":"well,energy,lambda / C-order","block_order":["ion","trapped_electron"]},
        flr={"active":{"max_abs":active_abs,"max_rel":active_rel},"envelope":env},
        moments=moments,
        min_positive_weight={"ion":float(K.Di.min()),"electron":float(K.De.min())},
        bounce=bounce_check(K.dims["Nb"]),
        conditioning=cond,
        residuals=maxima,
        hashes=hashes,
        manufactured_free_energy=float(np.vdot(manufactured(K),K.apply_M(manufactured(K))).real),
        criteria=criteria,
        verdict="PASS" if all(criteria.values()) else "FAIL",
    )

def run():
    out={
      "gate":"Fusion F2.6B — Source-Level Matrix-Free Operator Implementation Freeze / Algebraic Requalification Gate 0.1",
      "implementation_version":"fusion_f2_6b_operator_0_1",
      "historical_identity_claim":False,
      "source_path":"research/fusion/fusion_f2_6b_operator_0_1.py",
      "interfaces":["build_operator","apply_E","apply_F","solve_E"],
      "probe_seeds":SEEDS,
      "tolerances":TOL,
      "no_spectral_work":True,
      "no_finite_time_work":True,
      "levels":{},
    }
    for name in ["K0","K1","K2"]:
        out["levels"][name]=qualify_level(name)
    mf=[out["levels"][n]["manufactured_free_energy"] for n in ["K0","K1","K2"]]
    out["structural_convergence"]={
        "manufactured_free_energy":mf,
        "successive_relative_changes":[abs(mf[1]-mf[0])/abs(mf[0]),abs(mf[2]-mf[1])/abs(mf[1])]
    }
    out["source_git_blob_sha"]="ab2ecd18a53ddf8a3a4b4c4826a876054de15dd9"
    out["verdict"]="PASS" if all(out["levels"][n]["verdict"]=="PASS" for n in out["levels"]) else "FAIL"
    return out

if __name__=="__main__":
    out=run()
    print(json.dumps(out,indent=2,sort_keys=True,default=lambda o:o.item() if hasattr(o,'item') else str(o)))
