import importlib.util
from pathlib import Path
import sys
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"research/fusion/fusion_f2_6b_operator_0_1.py"
spec=importlib.util.spec_from_file_location("fusion_f2_6b_operator_0_1",SRC)
opm=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=opm
spec.loader.exec_module(opm)

def rv(K,seed):
    rng=np.random.default_rng(seed)
    x=rng.standard_normal(K.N)+1j*rng.standard_normal(K.N)
    return x/np.linalg.norm(x)

def test_f2_6b_matrix_free_interfaces_and_balance():
    for name in ("K0","K1","K2"):
        K=opm.build_operator(name)
        x=rv(K,20260907); y=rv(K,20261907)
        assert np.linalg.norm(opm.solve_E(K,opm.apply_E(K,x))-x)/np.linalg.norm(x) < 1e-12
        phi=K.P_apply(x); sx=K.S_apply(x)
        assert np.linalg.norm(K.Cdiag*phi-sx)/(np.linalg.norm(sx)+1e-300) < 1e-12
        assert K.direct_positive_energy(x) > 0
        Mx=K.apply_M(x); My=K.apply_M(y)
        herr=abs(np.vdot(x,My)-np.vdot(Mx,y))/(abs(np.vdot(x,My))+abs(np.vdot(Mx,y))+1e-300)
        assert herr < 1e-11
        for sp,heat in (("i",False),("e",False),("i",True),("e",True)):
            qquad=float(np.vdot(x,K.apply_Q(x,sp,heat)).real)
            assert abs(qquad-K.channel_value(x,sp,heat)) < 1e-12
        assert abs(K.channel_value(x,"i")-K.channel_value(x,"e")) < 1e-15
        Ax=K.apply_A(x); Ay=K.apply_A(y)
        lhs=np.vdot(x,K.apply_M(Ay))+np.vdot(Ax,K.apply_M(y))
        QG=0.5*(K.apply_Q(y,"i")+K.apply_Q(y,"e"))
        rhs=2*((opm.GPI+opm.GPE)*np.vdot(x,QG)
               +opm.GTI*np.vdot(x,K.apply_Q(y,"i",True))
               +opm.GTE*np.vdot(x,K.apply_Q(y,"e",True)))
        rel=abs(lhs-rhs)/(abs(lhs)+abs(rhs)+1e-300)
        assert rel < 1e-9
