import math

class CantorString():
    """ Wrapper class for CantorSetList - calling individual methods are only useful for the result, buildCantorString sets to intended use. """

    def __init__(self, interval, tier) :
        self.setNewSet(interval, [interval[0], interval[1]])
        self.tier = tier
        self.buildCantorString()

    @staticmethod
    def intFloor(flt) :
        return int(math.floor(flt))
    
    def setNewSet(self, interval, _set) :
        self.CantorSet = list(map(CantorString.intFloor, _set))
        self.interval = (int(interval[0]), int(interval[1]))
    
    def getCantorString(self) : 
        return self.getCantorLevelString(len(self.cantorLevels) - 1)

    def getCantorLevelString(self, index) :
        c = self.cantorLevels[index]
        level = list(map(CantorString.intFloor, c))
        return self.drawCantorLevel(level)
    
    def drawCantorLevel(self, level) :
        c = []
        for x in range(len(level)) :
            if x % 2 == 1 :
                c.extend(range(level[x - 1], level[x]))
        c.sort()
        return c
    
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
                    offSet = float((level[x] - level[x-1]) / 3)
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
            self.cantorLevels.append(cSet) 

            return self.get_cantorSet(cSet, tier - 1) # recursive step