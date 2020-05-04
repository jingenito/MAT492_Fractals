import os, sys
import numpy as np
from matplotlib import pyplot as plt

app_path = os.path.dirname(os.path.realpath('volumeCantorLawnTestBench.py'))
sys.path.append(os.path.join(app_path,'src'))

import Util.CantorLawnVolume as clv

D = 1 + (np.log(2) / np.log(3)) 
start_eps = 10**-6
stop_eps = 10**-3

epsSeq = np.linspace(start_eps, stop_eps, 1000)

bSeq = []
volSeq = []
epsAlpha = []

for e in epsSeq.copy() :
    vol = clv.Volume_Epsilon(e)
    eA = e**(2-D)

    volSeq.append(vol)
    bSeq.append(vol / eA)
    epsAlpha.append(eA)

plt.plot(epsSeq,bSeq,'r')
plt.plot(epsSeq,volSeq,'g')
plt.plot(epsSeq,epsAlpha,'b')
plt.legend(['V(E) / E**(2-D)','V(E)','E**(2-D)'])
plt.show()


