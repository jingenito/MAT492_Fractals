from CantorSet import CantorSet
from CantorStone import CantorStone
from ResolutionType import ResolutionType
from PIL import Image, ImageDraw

resolutionLookupTable = { (1920,1080) : 6,
                          (2560,1440) : 7
                        }
_Tiers = 6

def CreateCantorStringImage(resolution, rowRange, filename) :
    print("Create Cantor String Image started.")
    cSet = CantorSet((0, resolution[ResolutionType.Width]), _Tiers)
    print("Created the Cantor Set.")

    cSet.save_cantorStringImage(resolution, rowRange, filename)
    print("Saved Cantor String image.")

def CreateCantorLawnImage(resolution, filename) :
    print("Create Cantor Lawn Image started.")
    cStone = CantorStone(resolution, _Tiers)
    print("Created the Cantor Lawn.")

    cStone.save_image(filename)
    print("Saved the Cantor Lawn image.")

def CreateCantorLawnGIF(resolution, tier, filename) :
    print("Create Cantor Lawn GIF tier:", tier, "started.")
    images = []
    
    for i in range(1, tier + 1) :
        c = CantorStone(resolution, i)
        img = c.get_cantorStoneImage()
        images.append(img)
        print(float(i / tier) * 100, "%")

    print("Created images, saving the GIF.")
    images[0].save(filename, save_all=True, append_images=images[1:], optimize=False, duration=200, loop=0)
    print("Created the GIF!")

if __name__ == "__main__":
    print("1: Cantor String")
    print("2: Cantor Lawn")
    print("3: Cantor Lawn GIF")

    inp = input("Choose an image to create:\n")
    if inp.isnumeric() :
        mode = int(inp)

    if mode == 1 :
        CreateCantorStringImage((2560,1440), (670, 770), "images/CantorString.png")
    elif mode == 2 :
        CreateCantorLawnImage((2560,1440), "images/CantorLawn_Tier6.png")
    elif mode == 3 :
        CreateCantorLawnGIF((2560,1440), 15, "images/CantorLawnGIF.gif")
    else:
        print("Invalid input.")

    print("Done!")

