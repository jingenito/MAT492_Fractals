import os, sys
import numpy as np
from matplotlib import pyplot as plt

app_path = os.path.dirname(os.path.realpath('volumeCantorLawnTestBench.py'))
sys.path.append(os.path.join(app_path,'src'))

import Util.CantorLawnVolume as clv

D = (np.log(4) / np.log(3)) - 0.001
delEps = 10**-4

eCount = int(np.floor(0.01 / delEps))
epsSeq = np.linspace(delEps, 0.01, eCount)

bSeq = []
volSeq = []
epsAlpha = []

for e in epsSeq :
    vol = clv.Volume_Epsilon(e)
    eA = e**(2-D)

    volSeq.append(vol)
    bSeq.append(vol / eA)
    epsAlpha.append(eA)

plt.plot(epsSeq,bSeq,'r')
plt.plot(epsSeq,volSeq,'g')
plt.plot(epsSeq,epsAlpha,'b')
plt.legend(['V / E**(2-D)','Vols','E**(2-D)'])
plt.show()


