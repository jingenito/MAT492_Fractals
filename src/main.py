import Util.FractalImages as FractalImages

if __name__ == "__main__":
    print("1: Cantor String")
    print("2: Cantor Lawn")
    print("3: Cantor String GIF")
    print("4: Cantor Lawn GIF")
    print("5: Cantor String Volume")
    print("6: Cantor Lawn Volume")

    inp = input("Choose an image to create:\n")
    if inp.isnumeric() :
        mode = int(inp)

    if mode == 1 :
        FractalImages.CreateCantorStringImage((1000,1000), (450,550), 5, "images/CantorString.png")
    elif mode == 2 :
        FractalImages.CreateCantorLawnImage((1000,1000), 5, "images/CantorLawn.png")
    elif mode == 3 :
        FractalImages.CreateCantorStringGIF((1000,1000), (450,550), 7, "images/CantorStringGIF.gif")
    elif mode == 4 :
        FractalImages.CreateCantorLawnGIF((1000,1000), 7, "images/CantorLawnGIF.gif")
    elif mode == 5 :
        FractalImages.CreatCantorStringVolumeImage((1000,1000), (450,550), 5, 0.05, "images/CantorStringVolume.png")
    elif mode == 6 :
        FractalImages.CreatCantorLawnVolumeImage((1000,1000), 5, 0.02, "images/CantorLawnVolume.png")
    else:
        print("Invalid input.")

    print("Done!")

