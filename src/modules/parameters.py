# coding: UTF-8
import sys
from modules.constants import tpi, Atomtime, Hartree, Atomfield
import numpy as np
#Default values for options
cluster_mode = False
PC_option = True    #Predictor-corrector option
minimal_output = True #A flag to write-out minimal data or not
a = 1.0
Delta = 9.0/Hartree      #The Gap of the two-level system in a.u.
dt = 5.0e-1              #The size of the time-step
Nt = 4000               #The number of time steps
omegac = 1.55/Hartree    #Photon energy
phi_CEP = 0.0/tpi        #Carrier envelope phase
Tpulse = 40.0/Atomtime   #A parameter for pulse duration
nenvelope = 4            #Power for the sing envelope function
E0 = 1.0e0/Atomfield     #Field strength in a.u.

