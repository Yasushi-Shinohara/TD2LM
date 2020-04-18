# coding: UTF-8
#Relevant functions are written
import os
import math
import numpy as np
from modules.parameters import Delta, a
#
def E_hOD(E):
    hOD = np.zeros([2,2],dtype=np.complex128)
    hOD[0,1] = a*E
    hOD[1,0] = np.conj(hOD[0,1])
    return hOD
#
def psih_Ene(psi,h):
    Ene = np.vdot(psi,np.dot(h,psi))
    return np.real(Ene)
#
