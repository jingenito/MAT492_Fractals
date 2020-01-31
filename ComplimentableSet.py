import math

class ComplimentableSet:

    def __init__(self, interval, _set = []) :
        self.setNewSet(_set, interval)
    
    def getCompliment(self) :
        num_string = range(self.interval[0], self.interval[1] + 1)
        out_string = []
        for x in num_string :
            if not x in self.Set :
                out_string.append(x)
        return out_string

    def setNewSet(self, interval, _set = []) :
        self.Set = list(map(math.floor, _set))
        self.interval = interval
        self.compliment = self.getCompliment()