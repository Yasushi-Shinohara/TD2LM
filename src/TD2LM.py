#!/usr/bin/python
# coding: UTF-8
import time
ts = time.time()
print(time.strftime("# Started at %a, %d %b %Y %H:%M:%S %z %Z",time.localtime()))
print('# ===========================')
import sys
print('# Python version: ',sys.version.replace('\n',' '))
print('# API version: ',sys.api_version)
print('# Platform: ',sys.platform)
#print('Flags: ',sys.flags)
#print('Copyright: ',sys.copyright)
print('# ===========================')
import numpy as np
import math
import ctypes as ct
from modules.constants import *
from modules.parameters import parameter_class
param = parameter_class()
param.read_parameters()
from modules.functions import E_hOD, psih_Ene

if (not param.cluster_mode):
    import matplotlib.pyplot as plt
    from matplotlib import cm #To include color map

hD = np.zeros([2,2],dtype=np.complex128)
hD[0,0] = 0.5*param.Delta
hD[1,1] = -0.5*param.Delta
hOD = np.zeros([2,2],dtype=np.complex128)
hOD = E_hOD(param,0.0)
h = hD + hOD

psi = np.zeros([2],dtype=np.complex128)
psi[1] = 1.0  #Lower level is initailly fully occupied

#Hamiltonian and initial wavefunction set ups are done

Ene = psih_Ene(psi,h)
print('# System energy at initial:',Ene, '[a.u.] =',Ene*Hartree, ' [eV]')
#sys.exit()

#############################Prep. for RT################################
t = np.zeros([param.Nt],dtype=np.float64)
E = np.zeros([param.Nt],dtype=np.float64)
nv = np.zeros([param.Nt],dtype=np.float64)
nc = np.zeros([param.Nt],dtype=np.float64)
Ene = np.zeros([param.Nt],dtype=np.float64)
for it in range(param.Nt):
    t[it] = param.dt*it
    if (t[it] < param.Tpulse):
        E[it] = param.E0*(np.sin(pi*t[it]/param.Tpulse))**param.nenvelope*np.sin(param.omegac*(t[it] - 0.5*param.Tpulse) + param.phi_CEP)
if (param.PC_option):
    Eave = 0.0*E
    for it in range(param.Nt-1):
        Eave[it] = 0.5*(E[it] + E[it+1])
    Eave[param.Nt - 1] = 1.0*Eave[param.Nt - 2]

if (np.amax(t) < param.Tpulse):
    print('# Warning: max(t) is shorter than Tpulse')
        
if (not param.cluster_mode):
    plt.xlabel('Time [fs]')
    plt.ylabel('Field strength [V/nm]')
    plt.xlim(0.0,np.amax(t)*Atomtime)
    plt.plot(t*Atomtime,E*Atomfield)
    plt.grid()
    plt.show()

#############################RT calculation##############################


tt = time.time()
print('# Elapse time for preparation: ', tt - ts, ' [sec]')
print('# Preparaiton is done')
#Time-propagation
for it in range(param.Nt):
    if (param.PC_option):
        hOD = E_hOD(param,Eave[it])
    else:
        hOD = E_hOD(param,E[it])
    h = hD + hOD
    w, v = np.linalg.eigh(h)
    U = np.exp(-zI*w[0]*param.dt)*np.outer(v[0,:],np.conj(v[0,:])) + np.exp(-zI*w[1]*param.dt)*np.outer(v[1,:],np.conj(v[1,:]))
    psi = np.dot(U, psi)
    nv[it] = (np.abs(psi[0]))**2
    nc[it] = (np.abs(psi[1]))**2
    norm = np.linalg.norm(psi)
    Ene[it] = psih_Ene(psi,h)
    if (it%1000 == 0):
        print('# ',it, Ene[it], norm)

if (not param.cluster_mode):
    plt.figure()
    plt.xlabel('Time [fs]')
    plt.ylabel('Populations')
    plt.xlim(0.0,np.amax(t)*Atomtime)
    plt.plot(t*Atomtime,nv,label='nv')
    plt.plot(t*Atomtime,nc,label='nc')
    plt.legend()
    plt.grid()
    plt.show()
    plt.figure()
    plt.yscale('log')
    plt.xlabel('Time [fs]')
    plt.ylabel('Populations')
    plt.xlim(0.0,np.amax(t)*Atomtime)
    plt.plot(t*Atomtime,nv,label='nv')
    plt.legend()
    plt.grid()
    plt.show()
    plt.figure()
    plt.xlabel('Time [fs]')
    plt.ylabel('Energy [eV]')
    plt.xlim(0.0,np.amax(t)*Atomtime)
    plt.plot(t*Atomtime,Ene*Hartree)
    plt.grid()
    plt.show()

te = time.time()
print('# Elapse time for RT: ', te - tt, ' [sec] = ', (te - tt)/60.0, ' [min] = ', (te - tt)/3600, ' [hour]')
print('# RT time per an iteration: ', (te - tt)/float(param.Nt), ' [sec] = ', (te - tt)/float(param.Nt)/60.0, ' [min]')
print('# Total elapse time: ', te - ts, ' [sec] = ', (te - ts)/60.0, ' [min] = ', (te - ts)/3600, ' [hour]')

if (param.minimal_output):
    print(' ')
else:
    print(' ')
    
print('# ===========================')
print(time.strftime("# Ended at %a, %d %b %Y %H:%M:%S %z %Z",time.localtime()))
sys.exit()

