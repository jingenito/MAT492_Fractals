from PIL import Image
from JSONSerializer import JSONSerializer
from CantorString import CantorString
import math

_resolution = (1920,1080)
# tested 6 levels works best for 1080p
cString = CantorString((0, _resolution[0]), 6)

#for debugging
j = JSONSerializer("bin/cantorString.json")
j.SerializeJSON(cString.getCantorString())

j = JSONSerializer("bin/cantorSet.json")
j.SerializeJSON(cString.CantorSet)

j = JSONSerializer("bin/cantorLevels.json")
j.SerializeJSON(cString.cantorLevels)
##########################################

# Constants
_rowHeight = 150

_filename = "bin/cantorString.png"
_mode = 'RGB'
_color = (0,0,0)

img = Image.new(_mode, _resolution, _color) 
pixels = img.load() # Create the pixel map

for y in range(img.height):    # For every pixel:
    imgRow = int(math.floor(y / _rowHeight))
    #grab the floor of every value in this tier because we need to compare integers
    cLevel = cString.getCantorLevelString(imgRow)

    for x in range(img.width):
        if y % _rowHeight >= 25 and y % _rowHeight <= 125 :
            #draw white if in the cantor set, otherwise draw black
            if x in cLevel :
                pixels[x,y] = (255,255,255) 
            else:
                pixels[x,y] = (0,0,0) 
        else:
            #draw black inbetween tiers
            pixels[x,y] = (0,0,0) 
            

img.show()
