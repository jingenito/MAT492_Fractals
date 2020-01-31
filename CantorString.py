from ComplimentableSet import ComplimentableSet
import json

class CantorString(ComplimentableSet):
    """ Wrapper class for CantorSetList - calling individual methods are only useful for the result, buildCantorString sets to intended use. """

    def __init__(self, interval, tier) :
        ComplimentableSet.__init__(self, interval, [interval[0], interval[1]])

        self.tier = tier
        self.buildCantorString()

    def getCantorSet(self) :
        return self.Set
    
    def getCantorString(self) : 
        return self.compliment
    
    """ Call this method after setting properties to desired values to build the Cantor String model. """
    def buildCantorString(self) :
        self.cantorLevels = [] 

        level = [self.interval[0], self.interval[1]]
        self.cantorLevels.append(level)
        self.setNewSet(self.interval, self.get_cantorSet(level, self.tier))

    def get_cantorSet(self, level, tier) :
        if tier <= 0 :
            self.cantorLevels.append(level)
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

            # must be re-sorted at every tier
            cSet.sort()
            self.cantorLevels.append(cSet) # displaying each level in a json file

            return self.get_cantorSet(cSet, tier - 1) # recursive step