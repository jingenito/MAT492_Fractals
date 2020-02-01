from PIL import Image
from JSONSerializer import JSONSerializer
from CantorSet import CantorSet
from ComplimentableSet import ComplimentableSet
import math

# Constants
_black = (0,0,0)
_white = (255,255,255)

def CreatCantorStringImage(resolution, rowRange, filename) :
    cSet = CantorSet((0, resolution[0]), 6)
    cString = cSet.get_cantorString()

    #build Cantor String Image
    img = Image.new('RGB', resolution, _black) 
    pixels = img.load() # Create the pixel map

    for y in range(img.height):    # For every pixel:
        for x in range(img.width):
            if y >= rowRange[0] and y <= rowRange[1] :
                #draw white if in the cantor set, otherwise draw black
                if x in cString :
                    pixels[x,y] = _white 
                else:
                    pixels[x,y] = _black
            else:
                #draw black inbetween tiers
                pixels[x,y] = _black
            
    img.save(filename)


CreatCantorStringImage((1920,1080), (490, 590), "bin/cantorString.png")
print("Done!")