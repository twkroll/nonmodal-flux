import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy import linalg as la

BETA=0.8
R=0.05787037037037
LX=20.0
LY=10.0
GG=8.0*(np.tanh(5.0)**3/3.0-np.tanh(5.0)**5/5.0)

def coeff(ny):
    z,w=leggauss(512); y=5*z; w=5*w
    n=np.arange(1,ny+1)
    phi=np.sqrt(2/LY)*np.sin(np.outer(y+5,n*np.pi/LY))
    dphi=np.sqrt(2/LY)*np.cos(np.outer(y+5,n*np.pi/LY))*(n*np.pi/LY)
    s=1/np.cosh(y)**2
    un=phi.T@(w[:,None]*(s[:,None]*phi))
    upp=4*s-6*s*s
    cn=phi.T@(w[:,None]*((BETA-upp)[:,None]*phi))
    gp=6*s*s-4*s
    rn=phi.T@(w[:,None]*(gp[:,None]*dphi))
    return un,cn,rn

def modal(m,ny,un,cn,rn):
    k=2*np.pi*m/LX
    ell=np.arange(1,ny+1)*np.pi/LY
    kap=k*k+ell*ell
    D=-np.diag(kap)
    A=-R*np.eye(ny)-1j*k*np.diag(-1/kap)@(un@D+cn)
    M=2*LX*np.diag(kap)
    Q=1j*k/GG*(rn-rn.T)
    H=np.diag(1/np.sqrt(np.diag(M)))
    return A,M,Q,H

def finite(mx,ny,T):
    un,cn,rn=coeff(ny)
    KMs=[]; KQs=[]
    for m in range(1,mx+1):
        A,M,Q,H=modal(m,ny,un,cn,rn)
        E=la.expm(A*T)
        KM=H@E.conj().T@M@E@H
        X=la.solve_sylvester(A.conj().T,A,-Q)
        P=X-E.conj().T@X@E
        KQ=H@P@H
        KMs.append((KM+KM.conj().T)/2)
        KQs.append((KQ+KQ.conj().T)/2)
    def global_max(blocks):
        best=(-np.inf,None,None)
        for mi,K in enumerate(blocks,1):
            ev,v=la.eigh(K)
            if ev[-1]>best[0]:
                best=(float(ev[-1]),mi,v[:,-1])
        return best
    def global_min(blocks):
        best=(np.inf,None,None)
        for mi,K in enumerate(blocks,1):
            ev,v=la.eigh(K)
            if ev[0]<best[0]:
                best=(float(ev[0]),mi,v[:,0])
        return best
    return KMs,KQs,global_max(KMs),global_max(KQs),global_min(KQs)

def project_mass_and_angle(vh,mh,nyh,vl,ml,nyl,mxlow):
    if mh>mxlow:
        return 0.0, np.nan
    p=vh[:nyl]
    mu=float(np.vdot(p,p).real)
    if mu<1e-14:
        return mu,np.nan
    p=p/np.sqrt(mu)
    if mh!=ml:
        return mu,90.0
    ov=abs(np.vdot(vl,p))
    return mu,float(np.degrees(np.arccos(np.clip(ov,0,1))))

def test_primary_t8_canonical_values_and_gap():
    KMs,KQs,e,s,n=finite(16,32,8.0)
    assert np.isclose(e[0],13.327603789690187,rtol=1e-11)
    assert np.isclose(s[0],0.5269043077441947,rtol=1e-11)
    assert np.isclose(n[0],-0.5269043077441947,rtol=1e-11)
    assert e[1]==6
    assert s[1]==7
    w=e[2]
    val=np.vdot(w,KQs[e[1]-1]@w).real
    assert abs(val)<1e-12
    delta=(s[0]-val)/s[0]
    assert np.isclose(delta,1.0,rtol=0,atol=1e-11)

def test_t8_resolution_robustness_failure_is_canonical():
    _,_,eP,sP,_=finite(16,32,8.0)
    _,_,eC,sC,_=finite(20,40,8.0)
    _,_,eH,sH,_=finite(24,48,8.0)
    eps_pc_j=abs(sC[0]-sP[0])/max(abs(sC[0]),abs(sP[0]))
    eps_ch_j=abs(sH[0]-sC[0])/max(abs(sH[0]),abs(sC[0]))
    assert eps_pc_j>0.02
    assert eps_ch_j>0.02
    muE_pc,_=project_mass_and_angle(eC[2],eC[1],40,eP[2],eP[1],32,16)
    muQ_pc,_=project_mass_and_angle(sC[2],sC[1],40,sP[2],sP[1],32,16)
    muE_ch,_=project_mass_and_angle(eH[2],eH[1],48,eC[2],eC[1],40,20)
    muQ_ch,_=project_mass_and_angle(sH[2],sH[1],48,sC[2],sC[1],40,20)
    assert min(muE_pc,muQ_pc,muE_ch,muQ_ch)<0.95

def test_primary_t8_van_loan_crosscheck():
    ny=32; m=7; T=8.0
    un,cn,rn=coeff(ny)
    A,M,Q,H=modal(m,ny,un,cn,rn)
    E=la.expm(A*T)
    X=la.solve_sylvester(A.conj().T,A,-Q)
    P=X-E.conj().T@X@E
    V=np.block([[-A.conj().T,Q],[np.zeros_like(A),A]])
    EV=la.expm(V*T)
    Y=EV[:ny,ny:]
    PV=E.conj().T@Y
    rel=la.norm(P-PV,"fro")/max(1.0,la.norm(P,"fro"),la.norm(PV,"fro"))
    assert rel<=1e-10
