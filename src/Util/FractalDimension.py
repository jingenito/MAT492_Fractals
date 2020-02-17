import numpy as np
from PIL import Image

def _checkBoxForValue(F: list, p0 : tuple, p1: tuple, p2 : tuple, p3 : tuple) -> bool :
    """ p0 and p1 are the top two end points, left and right respectively. """
    #loop over the box endpoints
    for y in range(int(p0[1]), int(p2[1])) :
        for x in range(int(p0[0]), int(p1[0])) :
            if F[y][x] == 1 :
                return True
    return False

def _calculateBoxCount(F : list, delta : float) -> int :
    #calculate resolution
    res_h = len(F)
    res_w = len(F[0])
    #calculate step size
    step_x = (delta / np.sqrt(2))*res_w
    step_y = (delta / np.sqrt(2))*res_h 
    #calculate the x and y vectors from the step size
    xVec = np.arange(0, res_w, step_x)
    yVec = np.arange(0, res_h, step_y)
    #when rounding images - going to make x floor and y ceiling - i feel like if one is floor and the other is ceiling
    #the error should cancel out - we shall see
    xVec = np.floor(xVec)
    yVec = np.ceil(yVec)

    _boxCount = 0
    #loop over F with the calculated step size
    for y in range(1, len(yVec) - 1) :
        for x in range(1, len(xVec) - 1) :
            p0 = (xVec[x-1], yVec[y-1])
            p1 = (xVec[x], yVec[y-1])
            p2 = (xVec[x-1], yVec[y])
            p3 = (xVec[x], yVec[y])

            if _checkBoxForValue(F, p0, p1, p2, p3) :
                _boxCount = _boxCount + 1
    return _boxCount

def BoxCountingDimension(filename : str, tol : float) -> float :
    """ Compute the box counting dimension of set F with delta approaching zero within some tolerance. """

    img = Image.open(filename)
    pixels = img.load() # this is not a list

    F = []
    res_w, res_h = img.size
    for y in range(res_h) :
        F.append([])
        for x in range(res_w) :
            F[y].append(0 if pixels[x,y] == (255,255,255) else 1) 

    delta = 0.5
    while delta > tol :
        N_del = _calculateBoxCount(F, delta)
        dim = float(np.log(N_del) / (-1 * np.log(delta)))
        
        print('Delta:', delta, '  Dimension:', dim)
        delta = delta / 2 # decreasing delta by factors of 10