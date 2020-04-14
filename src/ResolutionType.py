from enum import Enum

class ResolutionType(int, Enum):
    """ Indeces for all resolution - tuples """
    Width = 0
    Height = 1
    Depth = 2