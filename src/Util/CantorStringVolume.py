import numpy as np

UPPER_LIMIT = 1 / 2

def intFLoor(flt : float) -> int : 
    """ Return the numpy floor function already as an integer. """
    return int(np.floor(flt))

def FractionalPart(flt: float) -> float :
    """ Return the fractional part of a float. ie... flt - Floor(flt) """
    return flt - np.floor(flt)

def Volume_Epsilon(eps : float) -> float :
    """ Return the volume formula for the given epsilon. """
    if eps > UPPER_LIMIT : return 0
    D = np.log(2) / np.log(3) 
    twoEps = 2*eps
    fPart = FractionalPart(np.log(twoEps) / np.log(3))

    return (twoEps)**(1-D) * ( (0.5)**(-fPart) + (3/2)**(-fPart) ) - twoEps