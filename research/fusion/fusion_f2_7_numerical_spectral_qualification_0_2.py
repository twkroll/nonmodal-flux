"""Fusion F2.7 0.2 spectral qualification driver.

Uses the frozen F2.6B source-level operator without modification.  The final
certification is based on the exact field-reduced dispersion relation for the
low-rank electrostatic coupling and a direct residual against op.apply_A.
No propagator or finite-time object is constructed.

Example:
  python research/fusion/fusion_f2_7_numerical_spectral_qualification_0_2.py \
      --level K2 --start-real 0.00621516 --start-imag 0.02731724 \
      --newton-iters 2 --workers 4
"""
from __future__ import annotations
import argparse, importlib.util, os, sys, time
from multiprocessing import get_context
from pathlib import Path
import numpy as np
from scipy import linalg, sparse
from scipy.sparse import linalg as spla

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

HERE = Path(__file__).resolve().parent
OP_PATH = HERE / "fusion_f2_6b_operator_0_1.py"
spec = importlib.util.spec_from_file_location("fusion_f2_6b_operator_0_1", OP_PATH)
mod = importlib.util.module_from_spec(spec); assert spec.loader is not None
sys.modules[spec.name] = mod; spec.loader.exec_module(mod)
build_operator = mod.build_operator
EPS,QSAF,KY,GPI,GTI,GPE,GTE = mod.EPS,mod.QSAF,mod.KY,mod.GPI,mod.GTI,mod.GPE,mod.GTE

class Reduced:
    def __init__(self, level: str):
        self.op=build_operator(level); op=self.op
        self.level=level; self.nt=len(op.theta); self.nu=len(op.u); self.nm=len(op.zeta)
        b=1/(1+EPS*np.cos(op.theta)); bp=EPS*np.sin(op.theta)*b*b
        ath=(b[:,None]/QSAF)*op.u[None,:]
        Du=op.metadata["Du"]
        Dtheta_u=sparse.kron(op.Dth,sparse.eye(self.nu),format="csr")
        Du_global=sparse.kron(sparse.eye(self.nt),sparse.csr_matrix(Du),format="csr")
        self.blocks=[]; self.Bbases=[]; self.Sbases=[]
        for m,z in enumerate(op.zeta):
            au=-(bp*b/QSAF)*z
            L=-sparse.diags(ath.ravel())@Dtheta_u - sparse.diags(np.repeat(au,self.nu))@Du_global
            d=op.Di[:,:,m].ravel(); sd=np.sqrt(d); isd=1/sd
            Lt=sparse.diags(sd)@L@sparse.diags(isd)
            Kt=0.5*(Lt-Lt.getH())-1j*sparse.diags(op.wd_i[:,:,m].ravel())
            self.blocks.append(Kt.tocsc())
            heat=op.energy_i[:,:,m]-2.5; J0m=op.J0[:,m]
            self.Bbases.append((sd.reshape(self.nt,self.nu),heat,J0m))
            self.Sbases.append(sd.reshape(self.nt,self.nu)*J0m[:,None])
        self.C=np.diag(op.Cdiag.astype(complex))

R_GLOBAL=None

def electron_contrib(R,lam,der=False):
    op=R.op; nwell,NE,Nlam=op.De.shape; norb=nwell*Nlam
    q=np.zeros(norb,dtype=complex); qp=np.zeros(norb,dtype=complex)
    wd=op.wd_e; heat=op.xE-2.5; c0=-1j*KY*(GPE+GTE*heat)
    for iw in range(nwell):
        for il in range(Nlam):
            den=-1j*wd[iw,:,il]-lam; c=c0-lam
            q[iw*Nlam+il]=-np.sum(op.De[iw,:,il]*c/den)
            if der: qp[iw*Nlam+il]=-np.sum(op.De[iw,:,il]*(c-den)/(den**2))
    H=(op.B_orb.T@sparse.diags(q)@op.B_orb).toarray()
    Hp=(op.B_orb.T@sparse.diags(qp)@op.B_orb).toarray() if der else None
    return H,Hp

def _ion_one(args):
    m,lam,der=args; R=R_GLOBAL; nt=R.nt; nu=R.nu
    A=R.blocks[m]-lam*sparse.eye(nt*nu,format="csc",dtype=complex)
    lu=spla.splu(A,permc_spec="COLAMD")
    sd2,heat,J0m=R.Bbases[m]
    coeff=(lam-1j*KY*(GPI+GTI*heat))*J0m[:,None]
    rows=np.arange(nt*nu); cols=np.repeat(np.arange(nt),nu)
    B=sparse.csc_matrix(((sd2*coeff).ravel(),(rows,cols)),shape=(nt*nu,nt)).toarray()
    Y=lu.solve(B)
    Sbase=R.Sbases[m]; H=np.einsum("tu,tuv->tv",Sbase,Y.reshape(nt,nu,nt),optimize=True)
    Hp=None
    if der:
        RB=sparse.csc_matrix(((sd2*J0m[:,None]*np.ones((1,nu))).ravel(),(rows,cols)),shape=(nt*nu,nt)).toarray()
        Z=lu.solve(Y+RB)
        Hp=np.einsum("tu,tuv->tv",Sbase,Z.reshape(nt,nu,nt),optimize=True)
    j=nt//2; rr=np.linalg.norm(A@Y[:,j]-B[:,j])/(np.linalg.norm(B[:,j])+1e-300)
    return m,H,Hp,float(rr)

class FullEvaluator:
    def __init__(self,R,workers=4):
        global R_GLOBAL; R_GLOBAL=R; self.R=R; self.ctx=get_context("fork"); self.pool=self.ctx.Pool(workers)
    def close(self): self.pool.close(); self.pool.join()
    def H(self,lam,der=False):
        R=self.R; H=R.C.copy(); Hp=np.zeros_like(H) if der else None
        he,hep=electron_contrib(R,lam,der); H+=he
        if der: Hp+=hep
        maxrr=0.0
        for m,h,hp,rr in self.pool.imap_unordered(_ion_one,[(m,lam,der) for m in range(R.nm)]):
            H+=h; maxrr=max(maxrr,rr)
            if der: Hp+=hp
        return H,Hp,maxrr

def svd_triplet(H):
    U,s,Vh=linalg.svd(H,full_matrices=False,lapack_driver="gesdd")
    return s[-1]/s[0],s[-1],s[0],U[:,-1],Vh.conj().T[:,-1]

def newton_step(H,Hp):
    ratio,smin,smax,u,v=svd_triplet(H)
    f=np.vdot(u,H@v); fp=np.vdot(u,Hp@v)
    return -f/fp,ratio,smin,smax,v

def reconstruct_state(R,lam,phi):
    op=R.op; nt=R.nt; nu=R.nu; yion=[]; maxrr=0.0
    for m in range(R.nm):
        A=R.blocks[m]-lam*sparse.eye(nt*nu,format="csc",dtype=complex); lu=spla.splu(A,permc_spec="COLAMD")
        sd2,heat,J0m=R.Bbases[m]; coeff=(lam-1j*KY*(GPI+GTI*heat))*J0m[:,None]
        rhs=(sd2*coeff*phi[:,None]).ravel(); y=-lu.solve(rhs)
        maxrr=max(maxrr,np.linalg.norm(A@y+rhs)/(np.linalg.norm(rhs)+1e-300)); yion.append(y.reshape(nt,nu))
    yi=np.stack(yion,axis=2)
    bo=(op.B_orb@phi).reshape(op.De.shape[0],op.De.shape[2])[:,None,:]
    den=-1j*op.wd_e-lam; c=-1j*KY*(GPE+GTE*(op.xE[None,:,None]-2.5))-lam
    ye=-np.sqrt(op.De)*c*np.broadcast_to(bo,op.De.shape)/den
    return op.join(yi/np.sqrt(op.Di),ye/np.sqrt(op.De)),float(maxrr)

def direct_residual(op,lam,x):
    Ax=op.apply_A(x); r=Ax-lam*x
    hi,he=op.split(r); ahi,ahe=op.split(Ax); xhi,xhe=op.split(x)
    rn=np.sqrt(np.sum(op.Di*np.abs(hi)**2)+np.sum(op.De*np.abs(he)**2))
    an=np.sqrt(np.sum(op.Di*np.abs(ahi)**2)+np.sum(op.De*np.abs(ahe)**2))
    xn=np.sqrt(np.sum(op.Di*np.abs(xhi)**2)+np.sum(op.De*np.abs(xhe)**2))
    F=op.apply_F(x); E=op.apply_E(x); rg=F-lam*E
    ghi,ghe=op.split(rg); Fhi,Fhe=op.split(F); Ehi,Ehe=op.split(E)
    gn=np.sqrt(np.sum(op.Di*np.abs(ghi)**2)+np.sum(op.De*np.abs(ghe)**2))
    fn=np.sqrt(np.sum(op.Di*np.abs(Fhi)**2)+np.sum(op.De*np.abs(Fhe)**2))
    en=np.sqrt(np.sum(op.Di*np.abs(Ehi)**2)+np.sum(op.De*np.abs(Ehe)**2))
    return {"rel_D":float(rn/(an+abs(lam)*xn)),"rel_generalized_D":float(gn/(fn+abs(lam)*en)),"abs_D":float(rn)}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--level",choices=["K0","K1","K2"],required=True)
    p.add_argument("--start-real",type=float,required=True); p.add_argument("--start-imag",type=float,required=True)
    p.add_argument("--newton-iters",type=int,default=3); p.add_argument("--workers",type=int,default=4)
    p.add_argument("--step-tol",type=float,default=1e-12); a=p.parse_args()
    R=Reduced(a.level); lam=complex(a.start_real,a.start_imag)
    print("level",a.level,"N",R.op.N,"start",repr(lam))
    for it in range(a.newton_iters):
        ev=FullEvaluator(R,a.workers)
        try: H,Hp,maxrr=ev.H(lam,der=True)
        finally: ev.close()
        step,ratio,smin,smax,v=newton_step(H,Hp)
        print("iter",it,"lam",repr(lam),"step",repr(step),"sv_ratio",ratio,"block_solve_max",maxrr)
        lam+=step
        if abs(step)<a.step_tol: break
    ev=FullEvaluator(R,a.workers)
    try: H,_,maxrr=ev.H(lam,der=False)
    finally: ev.close()
    ratio,smin,smax,u,v=svd_triplet(H); x,maxkin=reconstruct_state(R,lam,v); res=direct_residual(R.op,lam,x)
    print("final",repr(lam),"sv_ratio",ratio,"smin",smin,"smax",smax,"block_solve_max",maxrr,"kinetic_solve_max",maxkin,"residual",res)
if __name__=="__main__": main()
