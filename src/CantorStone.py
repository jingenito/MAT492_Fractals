from PIL import Image
from CantorSet import CantorSet
from ResolutionType import ResolutionType

class CantorStone:
    """ Class model that implements the 'Cantor String' of the CantorSet model in 2 dimensions at the specified resolution. """

    def __init__(self, resolution : tuple, tier : int) :
        self.resolution = resolution
        self.tier = tier
        self.build_cantorStone()
    
    def get_cantorStone(self) :
        """ Call this method to get an array of the current model. """
        return self._cantorStoneBitMap

    def get_cantorString_X(self) :
        """ Call this method to get the Cantor String in the X axis for the current model. """
        return self._cantorString_X
    
    def get_cantorString_X(self) :
        """ Call this method to get the Cantor String in the Y axis for the current model. """
        return self._cantorString_Y
    
    def build_cantorStone(self) :
        """ Call this method to rebuild the model after the resolution and tier is set. """
        _xInt = (0, self.resolution[ResolutionType.Width])
        _yInt = (0, self.resolution[ResolutionType.Height])

        self._cantorSet_X = CantorSet(_xInt, self.tier)
        self._cantorSet_Y = CantorSet(_yInt, self.tier)

        self._cantorStoneBitMap = self._get_cantorStoneMap()
                
    def _get_cantorStoneMap(self) :
        """ This method should not be called. """
        xCantorString = self._cantorSet_X.get_cantorString()
        yCantorString = self._cantorSet_Y.get_cantorString()

        bitMap = []
        for y in range(self.resolution[ResolutionType.Height]) :
            if y in yCantorString :
                bitMap.append([])
                for x in range(self.resolution[ResolutionType.Width]) :
                    bitMap[y].append(1 if x in xCantorString else 0)
            else:
                bitMap.append([0 for x in range(self.resolution[ResolutionType.Width])]) #add 0 for the entire row if y is not in the y cantor string

        return bitMap
    
    def save_image(self, filename : str) :
        img = Image.new('RGB', self.resolution, (0,0,0)) 
        pixels = img.load() # Create the pixel map

        for y in range(self._yInt[1]) :
            for x in range(self._xInt[1]) :
                pixels[x,y] = (255,255,255) if self._cantorStoneBitMap[y][x] == 1 else (0,0,0)

        img.save(filename)


    

