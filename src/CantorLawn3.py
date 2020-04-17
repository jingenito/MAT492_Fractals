from CantorSet import CantorSet
from CantorLawn import CantorLawn
from ResolutionType import ResolutionType
from Util import BinarySearch

class CantorLawn3:
    """ Class model that implements the 'Cantor Lawn 3D' of the CantorString model in 3 dimensions at the specified resolution. """

    def __init__(self, resolution : tuple, tier : int) :
        self.resolution = resolution
        self.tier = tier
        self.build_cantorLawn()

    def get_cantorLawn3(self) :
        """ Call this method to get a bit map of the current Cantor Lawn model. """
        return self._cantorLawnBitMap

    def build_cantorLawn(self) :
        """ Call this method to rebuild the model after the resolution and tier is set. """
        _zInt = (0, self.resolution[ResolutionType.Depth])
        _xyResolution = (self.resolution[ResolutionType.Width], self.resolution[ResolutionType.Height])

        self._cantorSet_Z = CantorSet(_zInt, self.tier)
        self._cantorLawn_XY = CantorLawn(_xyResolution, self.tier) #only need to make once since the dimension of the bitmap will never change at any z height

        self._cantorLawnBitMap = self._get_bitMap(self._cantorSet_Z.getCantorString(), self._cantorLawn_XY)

    def _get_bitMap(self, string_Z : list, cantorLawn_XY : CantorLawn) :
        """ This method should not be called. """

        bitMap = []
        
        for z in range(self.reslution[ResolutionType.Depth]) :
            if BinarySearch(string_Z, z) != -1 :
                #append a cantor lawn to the current z value
                bitMap.append(cantorLawn_XY.get_cantorLawn())
            else:
                #append a 2d map of 0s
                bitMap.append([0 for x in range(self.resolution[ResolutionType.Width])] for y in range(self.resolution[ResolutionType.Height]))

        return bitMap