import numpy as np
from PIL import Image

def _checkBoxForValue(F: list, xInt : tuple, yInt : tuple) -> bool :
    """ p0 and p1 are the top two end points, left and right respectively. """
    #calculate resolution
    res_h = len(F)
    res_w = len(F[0])

    # get x loop start and end points
    x_0 = int(np.ceil(xInt[0]))
    x_n = int(np.floor(xInt[1]))
    x_n = ( x_n if x_n < res_h else res_h )

    # get y loop start and end points
    y_0 = int(np.ceil(yInt[0]))
    y_n = int(np.floor(yInt[1]))
    y_n = ( y_n if y_n < res_w else res_w )

    print(x_0, x_n)
    print(y_0, y_n)

    #loop over the box endpoints
    for y in range(y_0, y_n + 1) :
        for x in range(x_0, x_n + 1) :
            if F[y][x] == 1 :
                return True
    return False

def _calculateBoxCount(F : list, delta : float) -> int :
    #calculate resolution
    res_h = len(F)
    res_w = len(F[0])
    #calculate the x and y vectors from the step size
    xVec = np.arange(0, res_w, delta * res_w)
    yVec = np.arange(0, res_h, delta * res_h)

    _boxCount = 0
    #loop over F with the calculated step size
    for y in range(1, len(yVec) - 1) :
        for x in range(1, len(xVec) - 1) :
            xInt = (xVec[x-1], xVec[x])
            yInt = (yVec[y-1], yVec[y])

            if _checkBoxForValue(F, xInt, yInt) :
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

    delta = 1 #init to get in the loop
    N_Seq = []
    delta_Seq = []
    while delta > tol :
        N_del = _calculateBoxCount(F, delta)

        delta_Seq.append(delta)
        N_Seq.append(N_del)

        print(delta)
        print(N_del)

        delta = delta / 2

    # xs = np.log(delta_Seq)
    # ys = np.log(N_Seq)

    # A = np.vstack([xs, np.ones(len(xs))]).T
    # m,b = np.linalg.lstsq(A, ys)[0]

    # print('deltas:', delta_Seq)
    # print('N:', N_Seq)
    # print('Dimension:', m)
    
