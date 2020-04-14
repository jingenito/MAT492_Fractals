from matplotlib import pyplot as plt
import numpy as np
from PIL import Image, ImageOps

def _checkBoxForValue(F: list, xyInt : tuple) -> bool :
    """ p0 and p1 are the top two end points, left and right respectively. """
    #calculate resolution
    res = len(F)

    # get x loop start and end points
    xy_0 = int(np.ceil(xyInt[0]))
    xy_n = int(np.floor(xyInt[1]))
    xy_n = ( xy_n if xy_n < res else res - 1 )

    #loop over the box endpoints
    for y in range(xy_0, xy_n + 1) :
        for x in range(xy_0, xy_n + 1) :
            if F[y][x] == 1 :
                return True
    return False

def _calculateBoxCount(F : list, delta : float) -> int :
    #calculate resolution
    res = len(F)
    #calculate the x and y vectors from the required amount of points
    num_xy = int(np.floor(1 / delta)) + 1
    xyVec = np.linspace(0, res, num_xy, True)

    _boxCount = 0
    #loop over delta-sized boxes 
    for y in range(1, len(xyVec)) :
        for x in range(1, len(xyVec)) :
            xyInt = (xyVec[x-1], xyVec[x])

            if _checkBoxForValue(F, xyInt) :
                _boxCount = _boxCount + 1

    return _boxCount

def BoxCountingDimension(filename : str, tol : float) -> float :
    """ Compute the box counting dimension of set F with delta approaching zero within some tolerance. """

    img = Image.open(filename)
    res_w, res_h = img.size
    dim = max(res_w, res_h) 
    img = img.resize((dim, dim))   

    pixels = ImageOps.grayscale(img).load()
    threshold = 0.5 * 255

    F = []
    for y in range(dim) :
        F.append([])
        for x in range(dim) :
            F[y].append(0 if pixels[x,y] >= threshold else 1) 

    delta = 0.5 #init to get in the loop
    N_Seq = []
    delta_Seq = []
    while delta > tol :
        N_del = _calculateBoxCount(F, delta)

        delta_Seq.append(delta)
        N_Seq.append(N_del)

        delta = delta / 2

    #calculate the loglog data points
    xs = -1 * np.log(delta_Seq)
    ys = np.log(N_Seq)

    #plot the N sequence
    A = np.vstack([xs, np.ones(len(xs))]).T
    m,b = np.linalg.lstsq(A, ys, None)[0]
    plt.plot(xs,ys,'ro')

    print('Dimension:', m)

    #plot the regression line on top of the sequence
    def line(x) : return m*x+b
    ys = line(xs)
    plt.plot(xs,ys)

    #label the plot axes
    plt.xlabel('delta sequence')
    plt.ylabel('N_delta Sequence')

    plt.show()
    
