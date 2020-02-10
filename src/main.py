from JSONSerializer import JSONSerializer
from CantorSet import CantorSet
from CantorStone import CantorStone
from ResolutionType import ResolutionType

_Tiers = 7

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
    CreateCantorStringImage((2560,1440), (670, 770), "bin/CantorString.png")
    CreateCantorStoneImage((2560,1440), "bin/CantorSone.png")

    print("Done!")

