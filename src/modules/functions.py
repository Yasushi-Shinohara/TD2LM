# coding: UTF-8
#Relevant functions are written
# This is created 2020/04/17 by Y. Shinohara
# This is lastly modified 2020/05/20 by Y. Shinohara
import os
import math
import numpy as np
from modules.constants import *
#
def get_hD(param):
    hD = np.zeros([2,2],dtype=np.complex128)
    hD[0,0] = 0.5*param.Delta
    hD[1,1] = -0.5*param.Delta
    return hD
#
def get_hD_IntPict(param):
    hD = np.zeros([2,2],dtype=np.complex128)
    return hD
#
def ES_hOD(param,E,S): #The action S is not used for this function.
    hOD = np.zeros([2,2],dtype=np.complex128)
    hOD[0,1] = -param.a*E                     #The negative sign is from elementary charge of electron
    hOD[1,0] = np.conj(hOD[0,1])
    return hOD
#
def ES_hOD_IntPict(param,E,S):
    hOD = np.zeros([2,2],dtype=np.complex128)
    hOD[0,1] = -np.exp(+zI*S)*param.a*E                     #The negative sign is from elementary charge of electron
    hOD[1,0] = np.conj(hOD[0,1])
    return hOD
#
def psih_Ene(param,psi,h): #The class param is not used for this function.
    Ene = np.vdot(psi,np.dot(h,psi))
    return np.real(Ene)
#
def psih_Ene_IntPict(param,psi,h):
    h[0,0] = 0.5*param.Delta
    h[1,1] = -0.5*param.Delta
    Ene = np.vdot(psi,np.dot(h,psi))
    return np.real(Ene)
#
def h_U(param,h):
    w, v = np.linalg.eigh(h)
    #U = np.exp(-zI*w[0]*param.dt)*np.outer(v[0,:],np.conj(v[0,:])) + np.exp(-zI*w[1]*param.dt)*np.outer(v[1,:],np.conj(v[1,:])) #This must be bug
    U = np.exp(-zI*w[0]*param.dt)*np.outer(v[:,0],np.conj(v[:,0])) + np.exp(-zI*w[1]*param.dt)*np.outer(v[:,1],np.conj(v[:,1]))
    return U
#
def psih2psi_exp(param,psi,h):
    U = h_U(param,h)
    psi = np.dot(U, psi)
    return psi
#
def psih_hpsi(param,psi,h):
    hpsi = np.dot(h, psi)
    return hpsi
#
def psih2psi_RK4(param,psi,h):
    k1 = psih_hpsi(param, psi, h)/zI
    k2 = psih_hpsi(param, psi + 0.5*param.dt*k1, h)/zI
    k3 = psih_hpsi(param, psi + 0.5*param.dt*k2, h)/zI
    k4 = psih_hpsi(param, psi + param.dt*k3, h)/zI
    psi = psi + (k1 + 2.0*k2 + 2.0*k3 + k4)*param.dt/6.0
    return psi
#
def Make_Efield(param):
    t = np.zeros([param.Nt],dtype=np.float64)
#    E = np.zeros([param.Nt],dtype=np.float64)
    E = np.zeros([param.Nt,param.Ncolor],dtype=np.float64)
    for it in range(param.Nt):
        t[it] = param.dt*it
    if (param.Ncolor == 1):
        icolor = 0
        for it in range(param.Nt):
            if (t[it] < param.Tpulse):
                E[it,icolor] = param.E0*(np.sin(pi*t[it]/param.Tpulse))**param.nenvelope*np.sin(param.omegac*(t[it] - 0.5*param.Tpulse) + param.phi_CEP)
    elif (param.Ncolor > 1):
        for icolor in range(param.Ncolor):
            for it in range(param.Nt):
                if (t[it] < param.Tpulse[icolor]):
                    E[it,icolor] = param.E0[icolor]*(np.sin(pi*t[it]/param.Tpulse[icolor]))**param.nenvelope[icolor]*np.sin(param.omegac[icolor]*(t[it] - 0.5*param.Tpulse[icolor]) + param.phi_CEP[icolor])
        E = np.sum(E,axis=1)
    else :
        print('ERROR: The parameter '+str(param.Ncolor)+' is improper.')
        sys.exit()
    return t, E
