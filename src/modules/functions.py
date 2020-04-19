# coding: UTF-8
#Relevant functions are written
import os
import math
import numpy as np
#from modules.parameters import a
#
def E_hOD(param,E):
    hOD = np.zeros([2,2],dtype=np.complex128)
    hOD[0,1] = -param.a*E                     #The negative sign is from elementary charge of electron
    hOD[1,0] = np.conj(hOD[0,1])
    return hOD
#
def psih_Ene(psi,h):
    Ene = np.vdot(psi,np.dot(h,psi))
    return np.real(Ene)
#
