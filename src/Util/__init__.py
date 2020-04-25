#making the Util directory a module

from bisect import bisect_left 
  
def BinarySearch(a : list, x) -> int : 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1