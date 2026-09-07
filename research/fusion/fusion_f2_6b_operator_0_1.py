"""Fusion F2.6B source-level matrix-free operator implementation 0.1.

This is a NEW reproducible realization of the frozen F2-R model; it does not
claim source identity with historical F2.6 0_3. No spectral or finite-time
operations are implemented here.

State layout (NumPy C order):
  ion:     h_i[theta, u, zeta]
  electron:h_e[well, energy, lambda]
with the ion block followed by the trapped-electron block.

The continuous LGL spectral-element derivative is assembled by mass projection
of elementwise LGL derivatives. The physical ion streaming+mirror raw
characteristic action is converted to the exact discrete split/skew form
0.5*(L - D_i^{-1} L^dagger D_i). Magnetic drifts are real diagonal
frequencies and therefore enter as -1j*omega_d.

Quasineutrality uses S=R^dagger D and C from the two-species electrostatic
susceptibility in the frozen volume measure. The generalized mass operator is
E=I-R C^{-1}S and solve_E uses the exact Woodbury/Schur identity.
"""

from __future__ import annotations
from dataclasses import dataclass
import hashlib, json
import numpy as np
from scipy import special, sparse, linalg

EPS = 0.18
QSAF = 1.4
SHAT = 0.8
KY = 0.3
GN = 0.8
GTI = 2.49
GTE = 2.49
GPI = GN + GTI
GPE = GN + GTE

LEVELS = {
    "K0": dict(W=1,p=12,Nu=16,Nmu=16,NE=12,Nlam=12,Nb=24),
    "K1": dict(W=2,p=16,Nu=24,Nmu=24,NE=18,Nlam=18,Nb=36),
    "K2": dict(W=3,p=20,Nu=32,Nmu=40,NE=24,Nlam=24,Nb=48),
}

def lgl(p):
    if p < 1: raise ValueError
    if p == 1:
        x=np.array([-1.,1.])
    else:
        xi,_=special.roots_jacobi(p-1,1,1)
        x=np.r_[-1.,xi,1.]
    Pp=special.eval_legendre(p,x)
    w=2.0/(p*(p+1)*Pp**2)
    n=p+1
    bw=np.ones(n)
    for j in range(n):
        bw[j]=1.0/np.prod(x[j]-np.delete(x,j))
    D=np.empty((n,n))
    for i in range(n):
        for j in range(n):
            if i!=j: D[i,j]=bw[j]/bw[i]/(x[i]-x[j])
        D[i,i]=-np.sum(np.delete(D[i],i))
    return x,w,D

def lagrange_eval(nodes, xp):
    nodes=np.asarray(nodes)
    n=len(nodes)
    bw=np.ones(n)
    for j in range(n):
        bw[j]=1.0/np.prod(nodes[j]-np.delete(nodes,j))
    diff=xp-nodes
    k=np.argmin(np.abs(diff))
    if abs(diff[k]) < 1e-14:
        out=np.zeros(n); out[k]=1.; return out
    q=bw/diff
    return q/q.sum()

@dataclass
class Level:
    name:str
    theta:np.ndarray
    mbase:np.ndarray
    mV:np.ndarray
    Dth:sparse.csr_matrix
    u:np.ndarray
    wu:np.ndarray
    zeta:np.ndarray
    wz:np.ndarray
    Di:np.ndarray
    J0:np.ndarray
    energy_i:np.ndarray
    wd_i:np.ndarray
    B_orb:sparse.csr_matrix
    De:np.ndarray
    xE:np.ndarray
    lam:np.ndarray
    wd_e:np.ndarray
    Cdiag:np.ndarray
    Hschur:np.ndarray
    Hchol:tuple
    Hfield:np.ndarray
    Hfield_chol:tuple
    gamma_exact:np.ndarray
    gamma_quad:np.ndarray
    Delta:np.ndarray
    dims:dict
    metadata:dict

    @property
    def Ni(self): return int(np.prod(self.Di.shape))
    @property
    def Ne(self): return int(np.prod(self.De.shape))
    @property
    def N(self): return self.Ni+self.Ne

    def split(self,x):
        x=np.asarray(x)
        hi=x[:self.Ni].reshape(self.Di.shape)
        he=x[self.Ni:].reshape(self.De.shape)
        return hi,he
    def join(self,hi,he):
        return np.concatenate([np.asarray(hi).ravel(),np.asarray(he).ravel()])

    def R_apply(self,phi):
        ri=self.J0[:,None,:]*phi[:,None,None]
        borb=self.B_orb@phi
        nwell,NE,Nlam=self.De.shape
        be=borb.reshape(nwell,Nlam)[:,None,:]
        re=-np.broadcast_to(be,(nwell,NE,Nlam))
        return ri,re

    def S_apply(self,x):
        hi,he=self.split(x)
        si=np.sum(self.Di*self.J0[:,None,:]*hi,axis=(1,2))
        tmp=np.sum(self.De*he,axis=1).reshape(-1)
        se=-(self.B_orb.T@tmp)
        return si+se

    def P_apply(self,x):
        return self.S_apply(x)/self.Cdiag

    def apply_E(self,x):
        phi=self.P_apply(x)
        ri,re=self.R_apply(phi)
        hi,he=self.split(x)
        return self.join(hi-ri,he-re)

    def solve_E(self,y):
        sy=self.S_apply(y)
        z=linalg.cho_solve(self.Hchol,sy,check_finite=False)
        ri,re=self.R_apply(z)
        yi,ye=self.split(y)
        return self.join(yi+ri,ye+re)

    def raw_adv_i(self,h):
        b=1/(1+EPS*np.cos(self.theta))
        bp=EPS*np.sin(self.theta)*b*b
        dhth=np.empty_like(h)
        for iu in range(len(self.u)):
            for im in range(len(self.zeta)):
                dhth[:,iu,im]=self.Dth@h[:,iu,im]
        Du=self.metadata["Du"]
        dhu=np.einsum("ab,tbm->tam",Du,h,optimize=True)
        ath=(b[:,None,None]/QSAF)*self.u[None,:,None]
        au=-(bp[:,None,None]*b[:,None,None]/QSAF)*self.zeta[None,None,:]
        return -(ath*dhth + au*dhu)

    def raw_adv_i_adj(self,y):
        b=1/(1+EPS*np.cos(self.theta))
        bp=EPS*np.sin(self.theta)*b*b
        ath=(b[:,None,None]/QSAF)*self.u[None,:,None]
        au=-(bp[:,None,None]*b[:,None,None]/QSAF)*self.zeta[None,None,:]
        out=np.empty_like(y)
        for iu in range(len(self.u)):
            for im in range(len(self.zeta)):
                out[:,iu,im]=-(self.Dth.T@(ath[:,iu,0]*y[:,iu,im]))
        Du=self.metadata["Du"]
        out += -np.einsum("ba,tbm->tam",Du,au*y,optimize=True)
        return out

    def cons_i(self,h):
        raw=self.raw_adv_i(h)
        adj=self.raw_adv_i_adj(self.Di*h)/self.Di
        adv=0.5*(raw-adj)
        return adv - 1j*self.wd_i*h

    def cons_e(self,h):
        return -1j*self.wd_e*h

    def apply_F(self,x):
        hi,he=self.split(x)
        fi=self.cons_i(hi)
        fe=self.cons_e(he)
        phi=self.P_apply(x)
        B_i=self.J0[:,None,:]*phi[:,None,None]
        borb=(self.B_orb@phi).reshape(self.De.shape[0],self.De.shape[2])[:,None,:]
        B_e=np.broadcast_to(borb,self.De.shape)
        heat_i=self.energy_i-2.5
        heat_e=self.xE[None,:,None]-2.5
        fi += -1j*KY*(GPI+GTI*heat_i)*B_i
        fe += -1j*KY*(GPE+GTE*heat_e)*B_e
        return self.join(fi,fe)

    def apply_A(self,x):
        return self.solve_E(self.apply_F(x))

    def apply_Mg(self,x):
        ex=self.apply_E(x)
        hi,he=self.split(ex)
        return self.join(self.Di*hi,self.De*he)

    def apply_M(self,x):
        mg=self.apply_Mg(x)
        phi=self.P_apply(x)
        v=(self.Delta/self.Cdiag)*phi
        ri,re=self.R_apply(v)
        corr=self.join(self.Di*ri,self.De*re)
        return mg+corr

    def direct_positive_energy(self,x):
        phi=self.P_apply(x)
        ri,re=self.R_apply(phi)
        hi,he=self.split(x)
        kin=np.vdot(hi-ri,self.Di*(hi-ri)).real + np.vdot(he-re,self.De*(he-re)).real
        fld=np.vdot(phi,self.Hfield@phi).real
        return kin+fld

    def channel_T_apply(self,x,species,heat=False):
        hi,he=self.split(x)
        phi=self.P_apply(x)
        yi=np.zeros_like(hi); ye=np.zeros_like(he)
        if species=="i":
            H=(self.energy_i-2.5) if heat else 1.0
            yi=(-1j*KY)*self.Di*H*(self.J0[:,None,:]*phi[:,None,None])
        else:
            H=(self.xE[None,:,None]-2.5) if heat else 1.0
            borb=(self.B_orb@phi).reshape(self.De.shape[0],self.De.shape[2])[:,None,:]
            ye=(-1j*KY)*self.De*H*np.broadcast_to(borb,self.De.shape)
        return self.join(yi,ye)

    def channel_T_adj_apply(self,x,species,heat=False):
        hi,he=self.split(x)
        if species=="i":
            H=(self.energy_i-2.5) if heat else 1.0
            field=np.sum(self.J0[:,None,:]*self.Di*H*hi,axis=(1,2))
        else:
            H=(self.xE[None,:,None]-2.5) if heat else 1.0
            tmp=np.sum(self.De*H*he,axis=1).reshape(-1)
            field=self.B_orb.T@tmp
        v=field/self.Cdiag
        ri,re=self.R_apply(v)
        return (1j*KY)*self.join(self.Di*ri,self.De*re)

    def apply_Q(self,x,species,heat=False):
        return 0.5*(self.channel_T_apply(x,species,heat)+self.channel_T_adj_apply(x,species,heat))

    def channel_value(self,x,species,heat=False):
        hi,he=self.split(x)
        phi=self.P_apply(x)
        if species=="i":
            H=(self.energy_i-2.5) if heat else 1.0
            z=np.vdot(hi,self.Di*H*(self.J0[:,None,:]*phi[:,None,None]))
        else:
            H=(self.xE[None,:,None]-2.5) if heat else 1.0
            borb=(self.B_orb@phi).reshape(self.De.shape[0],self.De.shape[2])[:,None,:]
            z=np.vdot(he,self.De*H*np.broadcast_to(borb,self.De.shape))
        return float(np.real(-1j*KY*z))

def build_level(name):
    cfg=LEVELS[name]; W=cfg["W"]; p=cfg["p"]
    ne=4*W+2
    left=-(2*W+1)*np.pi
    xl,wl,Dl=lgl(p)
    nfull=ne*p+1
    theta_full=np.empty(nfull); mbase_full=np.zeros(nfull)
    Me=(np.pi/2)*wl
    for e in range(ne):
        a=left+e*np.pi
        idx=np.arange(e*p,e*p+p+1)
        th=a+(xl+1)*np.pi/2
        theta_full[idx]=th
        mbase_full[idx]+=Me
    Mglob=mbase_full.copy()
    Ag=sparse.lil_matrix((nfull,nfull),dtype=float)
    for e in range(ne):
        idx=np.arange(e*p,e*p+p+1)
        block=np.diag(Me)@((2/np.pi)*Dl)
        Ag[np.ix_(idx,idx)] += block
    Dg=sparse.diags(1/Mglob)@Ag.tocsr()
    keep=np.arange(1,nfull-1)
    theta=theta_full[keep]
    mbase=mbase_full[keep]
    Dth=Dg[keep][:,keep].tocsr()

    b=1/(1+EPS*np.cos(theta))
    Jl=QSAF/b
    mV=mbase*Jl/b

    u,wu=special.roots_hermitenorm(cfg["Nu"])
    z,wz=special.roots_laguerre(cfg["Nmu"])
    n=len(u); bw=np.ones(n)
    for j in range(n):
        bw[j]=1.0/np.prod(u[j]-np.delete(u,j))
    Du=np.empty((n,n))
    for i in range(n):
        for j in range(n):
            if i!=j: Du[i,j]=bw[j]/bw[i]/(u[i]-u[j])
        Du[i,i]=-np.sum(np.delete(Du[i],i))

    vel=(b[:,None,None]/np.sqrt(2*np.pi))*wu[None,:,None]*wz[None,None,:]*np.exp(-(b[:,None,None]-1)*z[None,None,:])
    Di=mV[:,None,None]*vel

    lamgeo=SHAT*theta
    Dgeo=np.cos(theta)+lamgeo*np.sin(theta)
    kpr=KY*np.sqrt(1+lamgeo**2)
    arg=kpr[:,None]*np.sqrt(2*z[None,:]/b[:,None])
    J0=special.j0(arg)
    energy_i=u[None,:,None]**2/2 + z[None,None,:]*b[:,None,None]
    wd_i=KY*Dgeo[:,None,None]*(u[None,:,None]**2/b[:,None,None] + z[None,None,:])

    gamma_quad=np.sum(vel*J0[:,None,:]**2,axis=(1,2))
    bi=(kpr**2)/(b**2)
    gamma_exact=special.i0e(bi)
    Delta=mV*(gamma_quad-gamma_exact)

    xE,wE=special.roots_genlaguerre(cfg["NE"],0.5)
    yg,wyg=special.roots_legendre(cfg["Nlam"])
    lam=1+EPS*yg
    wlam=EPS*wyg
    chi,wchi=special.roots_legendre(cfg["Nb"])
    chi=chi*np.pi/2
    wchi=wchi*np.pi/2
    xloc=xl
    row=[]; col=[]; data=[]
    orb_measure=[]
    orb_wd_geom=[]
    wells=np.arange(-W,W+1)
    for iw,w in enumerate(wells):
        center=2*np.pi*w
        for il,la in enumerate(lam):
            tb=np.arccos((la-1)/EPS)
            sb=np.sin(tb/2)
            delta=2*np.arcsin(sb*np.sin(chi))
            thq=center+delta
            dth=2*sb*np.cos(chi)/np.sqrt(1-(sb*np.sin(chi))**2)
            bq=1/(1+EPS*np.cos(thq))
            wt=(QSAF/bq)/np.sqrt(np.maximum(1-la*bq,1e-300))*dth*wchi
            den=wt.sum()
            wn=wt/den
            accum={}
            for tq,wq in zip(thq,wn):
                e=int(np.floor((tq-left)/np.pi))
                e=max(0,min(ne-1,e))
                a=left+e*np.pi
                xi=2*(tq-a)/np.pi-1
                Lv=lagrange_eval(xloc,xi)
                idx=np.arange(e*p,e*p+p+1)
                for jj,vv in zip(idx,Lv*wq):
                    if jj==0 or jj==nfull-1: continue
                    kk=jj-1
                    accum[kk]=accum.get(kk,0.0)+vv
            r=iw*cfg["Nlam"]+il
            for kk,vv in accum.items():
                row.append(r); col.append(kk); data.append(vv)
            orb_measure.append(den)
            Dgq=np.cos(thq)+(SHAT*thq)*np.sin(thq)
            orb_wd_geom.append(np.sum(wn*(2/bq-la)*Dgq))
    B_orb=sparse.csr_matrix((data,(row,col)),shape=(len(wells)*cfg["Nlam"],len(theta)))
    orb_measure=np.array(orb_measure).reshape(len(wells),cfg["Nlam"])
    orb_wd_geom=np.array(orb_wd_geom).reshape(len(wells),cfg["Nlam"])
    De=(1/np.sqrt(np.pi))*orb_measure[:,None,:]*wE[None,:,None]*wlam[None,None,:]
    wd_e=-KY*xE[None,:,None]*orb_wd_geom[:,None,:]

    Cdiag=2*mV
    ionresp=mV*gamma_quad
    dorb=np.sum(De,axis=1).reshape(-1)
    He=(B_orb.T@sparse.diags(dorb)@B_orb).toarray()
    Hschur=np.diag(Cdiag-ionresp)-He
    Hschur=(Hschur+Hschur.T)/2
    Hchol=linalg.cho_factor(Hschur,lower=True,check_finite=False)
    Hfield=np.diag(Cdiag-mV*gamma_exact)-He
    Hfield=(Hfield+Hfield.T)/2
    Hfield_chol=linalg.cho_factor(Hfield,lower=True,check_finite=False)

    dims=dict(Ntheta=len(theta),Ni=int(Di.size),Ne=int(De.size),N=int(Di.size+De.size),
              W=W,p=p,Nu=cfg["Nu"],Nmu=cfg["Nmu"],NE=cfg["NE"],Nlam=cfg["Nlam"],Nb=cfg["Nb"])
    meta=dict(Du=Du,wells=wells.tolist(),left=float(left),ne=ne)
    return Level(name,theta,mbase,mV,Dth,u,wu,z,wz,Di,J0,energy_i,wd_i,B_orb,De,xE,lam,wd_e,
                 Cdiag,Hschur,Hchol,Hfield,Hfield_chol,gamma_exact,gamma_quad,Delta,dims,meta)


def build_operator(level: str) -> Level:
    return build_level(level)

def apply_E(op: Level, x):
    return op.apply_E(x)

def apply_F(op: Level, x):
    return op.apply_F(x)

def solve_E(op: Level, x):
    return op.solve_E(x)

def source_sha256(path=__file__):
    with open(path,"rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
