import os, sys
import numpy as np
from matplotlib import pyplot as plt

app_path = os.path.dirname(os.path.realpath('volumeCantorStringTestBench.py'))
sys.path.append(os.path.join(app_path,'src'))

import Util.CantorStringVolume as csv

D = np.log(2) / np.log(3)
alpha = D - 0.5
delEps = 10**-4

eCount = int(np.floor(0.01 / delEps))
epsSeq = np.linspace(delEps, 0.01, eCount)

volSeq = []
eAseq= []
eBseq = []

for e in epsSeq :
    vol = csv.Volume_Epsilon(e)
    eA = e**(1 - D)
    eB = e**(1 - alpha)

    volSeq.append(vol)
    eAseq.append(vol / eA)
    eBseq.append(vol / eB)

# plt.plot(epsSeq,volSeq,'g')
# plt.plot(epsSeq,eAseq,'r')
# plt.legend(['V(E)','V(E) / E**(1-D)'])
# plt.show()

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(epsSeq, volSeq, 'r')
ax1.plot(epsSeq, eAseq, 'b')
ax1.legend(['V(E)','V(E) / E**(1-D)'])
ax1.set(xlabel='E', ylabel='V(E)')
ax2.plot(epsSeq, volSeq, 'r')
ax2.plot(epsSeq, eBseq, 'b')
ax2.legend(['V(E)','V(E) / E**(1-a)'])
ax2.set(xlabel='E', ylabel='V(E)')
plt.show()