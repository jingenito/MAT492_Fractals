from CantorSet import CantorSet
from CantorStone import CantorStone
from ResolutionType import ResolutionType

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

def CreateCantorStoneImage(resolution, filename) :
    print("Create Cantor Lawn Image started.")
    cStone = CantorStone(resolution, _Tiers)
    print("Created the Cantor Lawn.")

    cStone.save_image(filename)
    print("Saved the Cantor Lawn image.")


if __name__ == "__main__":
    print("1: Cantor String")
    print("2: Cantor Lawn")

    inp = input("Choose an image to create:\n")
    if inp.isnumeric() :
        mode = int(inp)

    if mode == 1 :
        CreateCantorStringImage((2560,1440), (670, 770), "images/CantorString.png")
    elif mode == 2 :
        CreateCantorStoneImage((2560,1440), "images/CantorLawn_Tier6.png")
    else:
        print("Invalid input.")

    print("Done!")

