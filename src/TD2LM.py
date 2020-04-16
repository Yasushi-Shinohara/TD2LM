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
#from modules.functions import A_tkAGG, Make_vGG, Make_wmat 

h = np.zeros([2,2],dtype=np.complex128)
psi = np.zeros([2,2],dtype=np.complex128)


#Hamiltonian set up is done
#

#Set up initial condition
#sys.exit()

#############################RT calculation##############################

t = np.zeros([Nt],dtype=np.float64)
E = np.zeros([Nt],dtype=np.float64)

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

