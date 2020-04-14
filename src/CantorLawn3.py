from CantorSet import CantorSet
from CantorStone import CantorStone
from ResolutionType import ResolutionType
from Util import BinarySearch

class CantorLawn3:
    """ Class model that implements the 'Cantor Lawn 3D' of the CantorString model in 3 dimensions at the specified resolution. """

    def __init__(self, resolution : tuple, tier : int) :
        self.resolution = resolution
        self.tier = tier
        self.build_cantorLawn()

    def build_cantorLawn(self) :
        """ Call this method to rebuild the model after the resolution and tier is set. """
        _zInt = (0, self.resolution[ResolutionType.Depth])
        _xyResolution = (self.resolution[ResolutionType.Width], self.resolution[ResolutionType.Height])

        self._cantorSet_Z = CantorSet(_zInt, self.tier)
        self._cantorStone_XY = CantorStone(_xyResolution, self.tier)

        self.cantorLawnBitMap = self._get_bitMap(self._cantorSet_Z.getCantorString(), self._cantorStone_XY)

    def _get_bitMap(self, string_Z : list, cantorLawn_XY : CantorStone) :
        """ This method should not be called. """

        bitMap = []
        
        return bitMap