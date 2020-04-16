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
from modules.parameters import *
from modules.functions import E_hOD, psih_Ene

if (not cluster_mode):
    import matplotlib.pyplot as plt
    from matplotlib import cm #To include color map

hD = np.zeros([2,2],dtype=np.complex128)
hD[0,0] = 0.5*Delta
hD[1,1] = -0.5*Delta
hOD = np.zeros([2,2],dtype=np.complex128)
hOD = E_hOD(0.0)
h = hD + hOD

psi = np.zeros([2],dtype=np.complex128)
psi[1] = 1.0  #Lower level is initailly fully occupied

#Hamiltonian and initial wavefunction set ups are done

Ene = psih_Ene(psi,h)
print('System energy at initial',Ene)
#sys.exit()

#############################RT calculation##############################

t = np.zeros([Nt],dtype=np.float64)
E = np.zeros([Nt],dtype=np.float64)
for it in range(Nt):
    t[it] = dt*it
    if (t[it] < Tpulse):
        E[it] = E0*(np.sin(pi*t[it]/Tpulse))**nenvelope*np.sin(omegac*(t[it] - 0.5*Tpulse) + phi_CEP)
if (np.amax(t) < Tpulse):
    print('# Warning: max(t) is shorter than Tpulse')
        
if (not cluster_mode):
    plt.xlabel('Time [fs]')
    plt.ylabel('Field strength [V/nm]')
    plt.xlim(0.0,np.amax(t)*Atomtime)
    plt.plot(t*Atomtime,E*Atomfield)
    plt.grid()
    plt.show()


tt = time.time()
print('# Elapse time for preparation: ', tt - ts, ' [sec]')
print('# Preparaiton is done')
#Time-propagation

te = time.time()
print('# Elapse time for RT: ', te - tt, ' [sec] = ', (te - tt)/60.0, ' [min] = ', (te - tt)/3600, ' [hour]')
print('# RT time per an iteration: ', (te - tt)/float(Nt), ' [sec] = ', (te - tt)/float(Nt)/60.0, ' [min]')
print('# Total elapse time: ', te - ts, ' [sec] = ', (te - ts)/60.0, ' [min] = ', (te - ts)/3600, ' [hour]')

if (minimal_output):
    print(' ')
else:
    print(' ')
    
print('# ===========================')
print(time.strftime("# Ended at %a, %d %b %Y %H:%M:%S %z %Z",time.localtime()))
sys.exit()

