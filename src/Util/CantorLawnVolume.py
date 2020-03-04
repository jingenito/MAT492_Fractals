import numpy as np

UPPER_LIMIT = 1 / 6

def intFLoor(flt : float) -> int : 
    """ Return the numpy floor function already as an integer. """
    return int(np.floor(flt))

#not the finalized formula
def Volume_Epsilon(eps : float) -> float :
    """ Return the volume formula for the given epsilon. """
    if eps > UPPER_LIMIT : return 0
    n = -intFLoor(np.log(2*eps) / np.log(3))

    sum = 0
    for k in range(3, n + 1) :
        c1 = 4**(k-1)
        c2 = 3**(-k)
        c3 = 4*eps**2

        #ugly terms 
        t1 = c1*(4*eps*c2 - c3)
        t2 = c1*(2*eps*c2 + 2*eps*3*c2 - c3)
        t3 = c1*(3*eps*( (1/3)**k ) * ( (1/2)**(k-1) ) + ( 2*eps*3*c2*( (4/3)*(3/2)**k - 3 ) ))
        t4 = c3*(1 - (1/2)**k-2)
        #remaining nice term
        t5 = ((2/3)**(n+1))*3 - (4/9)**n

        #I forgot to add the rest of the sum earlier -_-
        sum = sum + t1 + t2 + t3 + t4 + t5

    return sum