from JSONSerializer import JSONSerializer
from CantorSet import CantorSet
from CantorStone import CantorStone
from ResolutionType import ResolutionType

_Tiers = 6

def CreateCantorStringImage(resolution, rowRange, filename) :
    cSet = CantorSet((0, resolution[ResolutionType.Width]), _Tiers)
    print("Created the Cantor Set.")

    cSet.save_cantorStringImage(resolution, rowRange, filename)
    print("Saved Cantor String image.")

def CreateCantorStoneImage(resolution, filename) :
    cStone = CantorStone(resolution, _Tiers)
    print("Created the Cantor Stone.")

    cStone.save_image(filename)
    print("Saved the Cantor Stone image.")


if __name__ == "__main__":
    CreateCantorStringImage((1920,1080), (490, 590), "bin/CantorString.png")
    CreateCantorStoneImage((1920,1080), "bin/CantorSone.png")
    print("Done!")

