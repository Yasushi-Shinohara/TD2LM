# coding: UTF-8
import sys
import numpy as np
from modules.constants import tpi, Atomtime, Hartree, Atomfield
from modules.parameters import cluster_mode, PC_option, minimal_output, a, Delta, dt, Nt, omegac, phi_CEP, Tpulse, nenvelope, E0

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
                cluster_mode = True
            else:
                cluster_mode = False
        if (str(text[i]) == 'PC_option'):
            if (str(text[i+1]) == 'True'):
                PC_option = True
            else:
                PC_option = False
        if (str(text[i]) == 'minimal_output'):
            if (str(text[i+1]) == 'True'):
                minimal_output = True
            else:
                minimal_output = False
        if (str(text[i]) == 'a'):
            a = float(str(text[i+1]))
        if (str(text[i]) == 'Delta'):
            Delta = float(str(text[i+1]))
        if (str(text[i]) == 'dt'):
            dt = float(str(text[i+1]))
        if (str(text[i]) == 'Nt'):
            Nt = int(str(text[i+1]))
        if (str(text[i]) == 'Tpulse'):
            Tpulse = float(str(text[i+1]))
        if (str(text[i]) == 'omegac'):
            omegac = float(str(text[i+1]))
        if (str(text[i]) == 'phi_CEP'):
            phi_CEP = float(str(text[i+1]))
        if (str(text[i]) == 'nenvelope'):
            nenvelope = int(str(text[i+1]))
        if (str(text[i]) == 'E0'):
            E0 = float(str(text[i+1]))
else:
    print('Error: Number of argmeunt is wrong.')
    sys.exit()

print('#=====Print the parmeters')
print('# cluster_mode =', cluster_mode)
print('# PC_option =', PC_option)
print('# minimal_output =', minimal_output)
print('# a =', a)
print('# Delta =', Delta) 
print('# dt =', dt) 
print('# Nt =', Nt) 
print('# Tpulse =', Tpulse) 
print('# nenvelope =', nenvelope) 
print('# omegac =', omegac) 
print('# phi_CEP =', phi_CEP, ' [2 pi]')
phi_CEP = tpi*phi_CEP
print('# E0 =', E0) 
print('# a*E0 =', a*E0) 

