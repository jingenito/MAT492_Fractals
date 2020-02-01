import math

class ComplimentableSet:
    """ Provides a class for a list that represents a Mathematical Set of integers to obtain the compliment easily. If the set is non integral
        the floor of each value will be entered by default.
    """

    def __init__(self, _interval, _set) :
        self.set_newSet(_interval, _set)
    
    def get_compliment(self) :
        num_string = range(self._interval[0], self._interval[1] + 1)
        out_string = []
        for x in num_string :
            if not x in self._set :
                out_string.append(x)
        return out_string

    def set_newSet(self, _interval, _set) :
        self._set = list(map(ComplimentableSet.intFloor, _set))
        self._length = len(_set) #cache length for later use
        self._interval = (int(_interval[0]), int(_interval[1]))
        self._compliment = self.get_compliment()
    
    def inner_set(self) :
        return self._set
    
    def __len__(self) :
        return len(self._set)
    
    @staticmethod
    def intFloor(flt) :
        return int(math.floor(flt))