import math

class ComplimentableSet:
    """ Provides a class for a list that represents a Mathematical Set of integers to obtain the compliment easily. If the set is non integral
        the floor of each value will be entered by default.
    """

    def __init__(self, _interval : tuple, _set : list) :
        self.set_newSet(_interval, _set)
    
    def _get_compliment(self) :
        """ This method should not be called. """
        num_string = range(self._interval[0], self._interval[1] + 1)
        out_string = []
        for x in num_string :
            if not x in self._set :
                out_string.append(x)
        return out_string
    
    def get_compliment(self) :
        """ Call this method to return the compliment of the inner set. """
        return self._compliment

    def set_newSet(self, _interval : tuple, _set : list) :
        """ Call this method to set a new _set. """
        self._set = list(map(ComplimentableSet.intFloor, _set))
        self._interval = (int(_interval[0]), int(_interval[1]))
        self._compliment = self._get_compliment()
    
    def inner_set(self) :
        """ Call this method to get the current inner set. """
        return self._set
    
    @staticmethod
    def intFloor(flt : float) :
        return int(math.floor(flt))