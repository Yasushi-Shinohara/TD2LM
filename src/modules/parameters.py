# coding: UTF-8
import sys
from modules.constants import tpi, Atomtime, Hartree, Atomfield
import numpy as np

class parameter_class:
    def __init__(self):
        #Default values for the parameters
        self.cluster_mode = False
        self.PC_option = True    #Predictor-corrector option
        self.minimal_output = True #A flag to write-out minimal data or not
        self.a = 10.0
        self.Delta = 9.0/Hartree      #The Gap of the two-level system in a.u.
        self.dt = 5.0e-1              #The size of the time-step
        self.Nt = 4000               #The number of time steps
        self.omegac = 1.55/Hartree    #Photon energy
        self.phi_CEP = 0.0/tpi        #Carrier envelope phase
        self.Tpulse = 40.0/Atomtime   #A parameter for pulse duration
        self.nenvelope = 4            #Power for the sing envelope function
        self.E0 = 1.0e0/Atomfield     #Field strength in a.u.

    def read_parameters(self):
        argv = sys.argv
        argc = len(argv)
        #Reading data from the standard input
        if (argc == 1):
            print('# The default parameters are chosen.')
        elif (argc == 2):
            print('# Name of input file is "'+argv[1]+'".')
            f = open(argv[1],'r')
            lines = f.readlines()
            f.close
            Nlen = len(lines)
            text = [0]*Nlen
            for i in range(Nlen):
                text[i] = lines[i].strip()
            for i in range(Nlen):
                if (str(text[i]) == 'cluster_mode'):
                    if (str(text[i+1]) == 'True'):
                        self.cluster_mode = True
                    else:
                        self.cluster_mode = False
                if (str(text[i]) == 'PC_option'):
                    if (str(text[i+1]) == 'True'):
                        self.PC_option = True
                    else:
                        self.PC_option = False
                if (str(text[i]) == 'minimal_output'):
                    if (str(text[i+1]) == 'True'):
                        self.minimal_output = True
                    else:
                        self.minimal_output = False
                if (str(text[i]) == 'a'):
                    self.a = float(str(text[i+1]))
                if (str(text[i]) == 'Delta'):
                    self.Delta = float(str(text[i+1]))
                if (str(text[i]) == 'dt'):
                    self.dt = float(str(text[i+1]))
                if (str(text[i]) == 'Nt'):
                    self.Nt = int(str(text[i+1]))
                if (str(text[i]) == 'Tpulse'):
                    self.Tpulse = float(str(text[i+1]))
                if (str(text[i]) == 'omegac'):
                    self.omegac = float(str(text[i+1]))
                if (str(text[i]) == 'phi_CEP'):
                    self.phi_CEP = float(str(text[i+1]))
                if (str(text[i]) == 'nenvelope'):
                    self.nenvelope = int(str(text[i+1]))
                if (str(text[i]) == 'E0'):
                    self.E0 = float(str(text[i+1]))
        else:
            print('Error: Number of argmeunt is wrong.')
            sys.exit()
        
        print('#=====Print the parmeters')
        print('# cluster_mode =', self.cluster_mode)
        print('# PC_option =', self.PC_option)
        print('# minimal_output =', self.minimal_output)
        print('# a =', self.a)
        print('# Delta =', self.Delta) 
        print('# dt =', self.dt) 
        print('# Nt =', self.Nt) 
        print('# Tpulse =', self.Tpulse) 
        print('# nenvelope =', self.nenvelope) 
        print('# omegac =', self.omegac) 
        print('# phi_CEP =', self.phi_CEP, ' [2 pi]')
        self.phi_CEP = tpi*self.phi_CEP
        print('# E0 =', self.E0) 
        print('# a*E0 =', self.a*self.E0) 

