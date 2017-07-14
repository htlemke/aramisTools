import numpy as np
from . import utilities
from scipy import constants

def hklRangeInfo(material,energy,
                 hRange=(-3,3),kRange=(-3,3),lRange=(-3,3),
                 hklInterval=(1,1,1),temperature=0):
    hRange = np.sort(hRange)
    kRange = np.sort(kRange)
    lRange = np.sort(lRange)
    hs = np.arange(*hRange,hklInterval[0])
    ks = np.arange(*kRange,hklInterval[1])
    ls = np.arange(*lRange,hklInterval[2])
    hkls = utilities.cartesian((hs,ks,ls))
    Qs = [material.Q(*hkl) for hkl in hkls]
    Fs = material.StructureFactorForQ(Qs,en0=energy,temp=temperature)
    FsSquared = np.real(Fs*Fs.conj())
    Qabs = np.linalg.norm(Qs,axis=1)
    return hkls,Qabs,FsSquared

def hklInfo(material,hkl,energy,temperature=0):
    Q = material.Q(*hkl)
    F = material.StructureFactor(Q,en=energy,temp=temperature)
    FSquared = np.real(F*F.conj())
    Qabs = np.linalg.norm(Q)
    return Q,Qabs,FSquared


def darwinWidth(material,hkl,energy,temperature=0):
    """ symmetric case formula from: http://www.esrf.eu/computing/scientific/people/srio/publications/SPIE04_MONO.pdf"""
    er = constants.physical_constants['classical electron radius']
    Q = material.Q(hkl)
    theta = utilities.QE2theta(np.linalg.norm(Q),energy)
    F = material.StructureFactor(Q,en=energy,temp=temperature)
    lam = utilities.E2lam(energy)
    V = material.lattice.UnitCellVolume()
    dw = (2*er[0]*1e10*lam**2*np.abs(F))/(np.pi*V*np.sin(2*theta))
    return dw,theta,dw/np.tan(theta)










