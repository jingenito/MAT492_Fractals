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
    
    def _get_bitMap(self, string_X : list, string_Y : list) :
        """ This method should not be called. """

        bitMap = []
        for y in range(self.resolution[ResolutionType.Height]) :
            if y in string_Y :
                bitMap.append([])
                for x in range(self.resolution[ResolutionType.Width]) :
                    bitMap[y].append(1 if x in string_X else 0)
            else:
                bitMap.append([0 for x in range(self.resolution[ResolutionType.Width])]) #add 0 for the entire row if y is not in the y cantor string

        return bitMap
                
    def _get_cantorStoneMap(self) :
        """ This method should not be called. """
        return self._get_bitMap(self._cantorSet_X.get_cantorString(), self._cantorSet_Y.get_cantorString()) 

    def get_cantorSetCrossString(self) :
        return self._get_bitMap(self._cantorSet_X.get_cantorSet(), self._cantorSet_Y.get_cantorString())
    
    def save_cantorSetCrossStringImage(self, filename : str) :
        bMap = self.get_cantorSetCrossString()
        self._save_bitMap(filename, bMap)

    def get_cantorStringCrossSet(self) :
        return self._get_bitMap(self._cantorSet_X.get_cantorString(), self._cantorSet_Y.get_cantorSet())
    
    def save_cantorStringCrossSetImage(self, filename : str) :
        bMap = self.get_cantorStringCrossSet()
        self._save_bitMap(filename, bMap)
    
    def get_boundary(self) :
        bnd1 = self.get_cantorSetCrossString()
        bnd2 = self.get_cantorStringCrossSet()

        for y in range(self.resolution[ResolutionType.Height]) :
            for x in range(self.resolution[ResolutionType.Width]) :
                bnd1[y][x] = 1 if bnd1[y][x] == 1 or bnd2[y][x] == 1 else 0
        
        return bnd1
    
    def save_boundaryImage(self, filename : str) :
        bMap = self.get_boundary()
        self._save_bitMap(filename,bMap)

    def save_image(self, filename : str) :
        self._save_bitMap(filename, self._cantorStoneBitMap)
    
    def _save_bitMap(self, filename : str, bitMap : list) :
        img = Image.new('RGB', self.resolution, (0,0,0)) 
        pixels = img.load() # Create the pixel map

        for y in range(self.resolution[ResolutionType.Height]) :
            for x in range(self.resolution[ResolutionType.Width]) :
                pixels[x,y] = (255,255,255) if bitMap[y][x] == 1 else (0,0,0)

        img.save(filename)


    

