import numpy as np
import Util.CantorStringVolume as csv

def Volume_Epsilon(eps : float) -> float :
    """ Return the volume formula for the given epsilon. """
    if eps > csv.UPPER_LIMIT : return 0
    
    cStr_Volume = csv.Volume_Epsilon(eps)
    return 2 * cStr_Volume - cStr_Volume**2
