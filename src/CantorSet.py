from PIL import Image
from ComplimentableSet import ComplimentableSet
import math

class CantorSet:

    def __init__(self, interval, tier) :
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

        #if non integer values are supported later on than this section will just need to be by passed, and methods for getting the floats Levels/Sets
        #will need to be added
        self._cantorLevels = [] #initialize the cantor levels of complimentable sets (floor values)
        for c in self._cantorFloatLevels :
            cLevel = ComplimentableSet(self.interval, c) #floor values beyond here
            self._cantorLevels.append(self._draw_CantorLevel(cLevel.inner_set())) 

        self._cantorSet = self._cantorLevels[len(self._cantorLevels) - 1] #the current CantorSet model is the last level - will already be a complimentable set

    #this method will fill in the cantor level
    def _draw_CantorLevel(self, level) :
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
    def _get_cantorSet(self, level, tier) :
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
    
    def save_cantorStringImage(self, resolution, rowRange, filename) :
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

    def get_cantorSet(self) :
        """ Call this method to get the current CantorSet model as a ComplimentableSet. """
        return self._cantorSet

    def get_cantorSetLevel(self, index) :
        """ Call this method to get the CantorSet model at the specified index as a ComplimentableSet. """
        return self._cantorLevels[index]

    def get_cantorString(self) : 
        """ Call this method to return the 'Cantor String' associated with the current CantorSet model as a list. """
        return ComplimentableSet(self.interval, self._cantorSet).get_compliment()

    def get_cantorLevelstring(self, index) :
        """ Call this method to return the 'Cantor String' associated with the current CantorSet model as a list. """
        return ComplimentableSet(self.interval, self._cantorLevels[index]).get_compliment()
    
    def get_maxRepeatedFloorValues(self) :
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