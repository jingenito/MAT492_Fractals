from PIL import Image
from os import path
import math
import json

cantorLevels = []

def getCantorSet(level, tier) :
    if tier <= 0 :
        return level
    else:
        cSet = []

        for x in range(len(level)) :
            if x % 2 == 1 :
                # only split at odd indeces
                offSet = (float)((level[x] - level[x-1]) / 3)
                c1 = level[x-1] + offSet
                c2 = level[x] - offSet

                cSet.insert(x,c1)
                cSet.insert(x+1,c2)
                cSet.insert(x+2,level[x])
            else:
                # add the even indeces to the set
                cSet.append(level[x])

        #must be re-sorted at every tier
        cSet.sort()

        cantorLevels.append(cSet) #displaying each level in a json file

        return getCantorSet(cSet, tier - 1) # recursive step

# get cantor set after five levels
level = [0,1]
c = getCantorSet(level, 5)
print(c)

# serialize the list containing each level to a json file
filename = "bin/cantorLevels.json"
mode = "w" if path.exists(filename) else "x"
f = open(filename,mode)
json.dump(cantorLevels, f)