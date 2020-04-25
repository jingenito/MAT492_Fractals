from PIL import Image

import os, sys

app_path = os.path.dirname(os.path.realpath('main.py'))
sys.path.append(os.path.join(app_path,'src'))

from ResolutionType import ResolutionType

def BitMapToImage(bitMap : list) -> Image :
    """ Call this method to convert a bitmap to a PIL Image. """
    _resolution = (len(bitMap[0]), len(bitMap))
    img = Image.new('RGB', (len(bitMap[0]), len(bitMap)), (0,0,0)) 
    pixels = img.load() # Create the pixel map

    for y in range(_resolution[ResolutionType.Height]) :
        for x in range(_resolution[ResolutionType.Width]) :
            pixels[x,y] = (255,255,255) if bitMap[y][x] == 1 else (0,0,0)

    return img