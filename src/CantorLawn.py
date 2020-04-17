from PIL import Image
from CantorSet import CantorSet
from ResolutionType import ResolutionType
from Util import BinarySearch
import time

class CantorLawn:
    """ Class model that implements the 'Cantor String' of the CantorSet model in 2 dimensions at the specified resolution. """

    def __init__(self, resolution : tuple, tier : int) :
        self.resolution = resolution
        self.tier = tier
        self.build_cantorLawn()
    
    def get_cantorLawn(self) :
        """ Call this method to get an array of the current model. """
        return self._cantorLawnBitMap
    
    def get_cantorLawnImage(self) :
        """ Call this method to return the image of the current model. """
        return self._get_image(self._cantorLawnBitMap)

    def get_cantorString_X(self) :
        """ Call this method to get the Cantor String in the X axis for the current model. """
        return self._cantorString_X
    
    def get_cantorString_X(self) :
        """ Call this method to get the Cantor String in the Y axis for the current model. """
        return self._cantorString_Y
    
    def build_cantorLawn(self) :
        """ Call this method to rebuild the model after the resolution and tier is set. """
        _xInt = (0, self.resolution[ResolutionType.Width])
        _yInt = (0, self.resolution[ResolutionType.Height])

        self._cantorSet_X = CantorSet(_xInt, self.tier)
        self._cantorSet_Y = CantorSet(_yInt, self.tier)

        self._cantorLawnBitMap = self._get_cantorLawnMap()
    
    def _get_bitMap(self, string_X : list, string_Y : list) :
        """ This method should not be called. """

        bitMap = []
        for y in range(self.resolution[ResolutionType.Height]) :
            if BinarySearch(string_Y, y) != -1 :
                bitMap.append([])
                for x in range(self.resolution[ResolutionType.Width]) :
                    bitMap[y].append(1 if BinarySearch(string_X, x) != -1 else 0)
            else:
                bitMap.append([0 for x in range(self.resolution[ResolutionType.Width])]) #add 0 for the entire row if y is not in the y cantor string

        return bitMap
                
    def _get_cantorLawnMap(self) :
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
        self._save_bitMap(filename, self._cantorLawnBitMap)
    
    def _save_bitMap(self, filename : str, bitMap : list) :
        img = self._get_image(bitMap)
        img.save(filename)

    def _get_image(self, bitMap : list) -> Image :
        img = Image.new('RGB', self.resolution, (0,0,0)) 
        pixels = img.load() # Create the pixel map

        for y in range(self.resolution[ResolutionType.Height]) :
            for x in range(self.resolution[ResolutionType.Width]) :
                pixels[x,y] = (255,255,255) if bitMap[y][x] == 1 else (0,0,0)
        
        return img


    

