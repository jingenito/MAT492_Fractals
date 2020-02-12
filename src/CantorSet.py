from PIL import Image
from ComplimentableSet import ComplimentableSet
import math

class CantorSet:

    def __init__(self, interval : tuple, tier : int) :
        self.interval = interval
        self.tier = tier
        self.build_cantorSet()
    
    def build_cantorSet(self) :
        """ Call this method after setting interval and tier to desired values to rebuild the CantorSet model. """

        self._cantorFloatLevels = [] #hold the float values during calculations for accuracy - storing for later reference - set to None later if memory is an issue

        firstLevel = [self.interval[0], self.interval[1]]
        self._cantorFloatLevels.append(firstLevel)
        #calling _get_cantorSet will add the rest of the levels
        self._cantorFloatSet = self._get_cantorSet(firstLevel, self.tier) #storing for later reference - set to None later if memory is an issue 

        self._cantorSet = ComplimentableSet(self.interval, self._cantorFloatSet)
        self._cantorLevels = { self.tier : self._cantorSet }

    #this method will fill in the cantor level
    def _draw_CantorLevel(self, level : list) :
        """ Should not call this method """
        #if efficiency is becoming an issue, the use of this result really doesnt really 'need' to be sorted per se
        #but its nice to have it sorted for human readability when debugging
        c = []
        for x in range(len(level)) :
            if x % 2 == 1 :
                c.extend(range(level[x - 1], level[x]))
        c.sort()
        return c

    #this method will not do any rounding, and will only give float values
    def _get_cantorSet(self, level : list, tier : int) :
        """ Should not call this method, for intended use set interval and tier, then call build_cantorSet """

        if tier <= 0 :
            self._cantorFloatLevels.append(level)
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
            self._cantorFloatLevels.append(cSet) 
            return self._get_cantorSet(cSet, tier - 1) # recursive step
    
    def save_cantorStringImage(self, resolution : tuple, rowRange : tuple, filename : str) :
        """ Call this method to save the current model to the specified filename. Resolution and rowRange will dictate how the 1D image
            is mapped onto a 2D plane.
        """
        img = Image.new('RGB', resolution, (0,0,0)) 
        pixels = img.load() # Create the pixel map
        cString = self.get_cantorString() #cache value for the process

        for y in range(img.height):    # For every pixel:
            for x in range(img.width):
                if y >= rowRange[0] and y <= rowRange[1] :
                    #draw white if in the cantor string, otherwise draw black
                    if x in cString :
                        pixels[x,y] = (255,255,255)
                    else:
                        pixels[x,y] = (0,0,0)
                else:
                    #draw black inbetween tiers
                    pixels[x,y] = (0,0,0)
            
        img.save(filename)

    def get_cantorSet(self) -> list :
        """ Call this method to get the current CantorSet model. """
        return self._cantorSet.inner_set()

    def get_cantorSetLevel(self, index : int) -> list :
        """ Call this method to get the CantorSet model at the specified index. """
        return self._cantorFloatLevels[index]

    def get_cantorString(self) -> list : 
        """ Call this method to return the 'Cantor String' associated with the current CantorSet model. """
        return self._cantorSet.get_compliment()

    def _get_cantorLevelString(self, index : int) -> list :
        """ This method should not be called. """
        lvl = self._cantorLevels.get(index, None) #only querying the dictionary once
        cLvlStr = None
        if lvl == None :
            lvl = self._draw_CantorLevel(list(map(math.floor, self._cantorFloatLevels[index])))

            cLvl = ComplimentableSet(self.interval, self._draw_CantorLevel(lvl))
            self._cantorLevels[index] = cLvl #cache the level in the dictionary
            cLvlStr = cLvl.get_compliment()
        else: cLvlStr = lvl.get_compliment()
        return cLvlStr
    def get_cantorLevelstring(self, index : int) -> list :
        """ Call this method to return the 'Cantor String' associated with the current CantorSet model as a list. """
        return self._get_cantorLevelString(index)
    
    def get_maxRepeatedFloorValues(self) -> tuple :
        """ For debugging, useful for configuring the tiers to the resolution. - Returns a tuple... (maxCount, repeatCount) """
        maxCount = 0 #count of max repeated values
        repeatCount = 0 #amount of all repeated values
        count = 0
        array = map(math.floor, self._cantorFloatSet)

        prevX = None
        for x in array :
            if x == prevX :
                count += 1
                repeatCount += 1
            else:
                maxCount = count
                count = 0
            prevX = x
        return (maxCount, repeatCount)