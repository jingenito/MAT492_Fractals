from PIL import Image
from JSONSerializer import JSONSerializer
from CantorSet import CantorSet
from CantorStone import CantorStone

def CreatCantorStringImage(resolution, rowRange, filename) :
    cSet = CantorSet((0, resolution[0]), 6)
    cString = cSet.get_cantorString()

    #build Cantor String Image
    img = Image.new('RGB', resolution, _Global_Black_) 
    pixels = img.load() # Create the pixel map

    for y in range(img.height):    # For every pixel:
        for x in range(img.width):
            if y >= rowRange[0] and y <= rowRange[1] :
                #draw white if in the cantor string, otherwise draw black
                if x in cString :
                    pixels[x,y] = _Global_White_ 
                else:
                    pixels[x,y] = _Global_Black_
            else:
                #draw black inbetween tiers
                pixels[x,y] = _Global_Black_
            
    img.save(filename)


if __name__ == "__main__":
    # Constants
    _Global_Black_ = (0,0,0)
    _Global_White_ = (255,255,255)

    #CreatCantorStringImage((1920,1080), (490, 590), "bin/cantorString.png")
    cStone = CantorStone((1920,1080), 6)
    print("Created the Cantor Stone.")

    cStone.save_image("bin/cantorStone.png")
    print("Saved the image.")

    print("Done!")

