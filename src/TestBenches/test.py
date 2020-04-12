import os, sys, time

app_path = os.path.dirname(os.path.realpath('cantorSetTestBench.py'))
sys.path.append(os.path.join(app_path,'src'))

from Util import BinarySearch
from CantorSet import CantorSet

cSet = CantorSet((0, 2560), 6) 
cString = cSet.get_cantorString()

print("Start loop")
start = time.time()

for y in range(1440) :
    for x in range(2560) :
        if BinarySearch(cString, x) != -1 :
            z = 1

finish = time.time()
print("Time: ", finish - start)
