import Util.FractalImages as FractalImages

if __name__ == "__main__":
    print("1: Cantor String")
    print("2: Cantor Lawn")
    print("3: Cantor String GIF")
    print("4: Cantor Lawn GIF")
    print("5: Cantor String Volume")
    print("6: Cantor Lawn Volume")
    print("7: Cantor String Volume GIF")
    print("8: Cantor Lawn Volume GIF")
   
    inp = input("Choose an image to create:\n")
    if inp.isnumeric() :
        mode = int(inp)

    if mode == 1 :
        FractalImages.CreateCantorStringImage((1000,1000), (475,525), 6, "images/CantorString.png")
    elif mode == 2 :
        FractalImages.CreateCantorLawnImage((1000,1000), 6, "images/CantorLawn.png")
    elif mode == 3 :
        FractalImages.CreateCantorStringGIF((1000,1000), (475,525), 6, "images/CantorStringGIF.gif")
    elif mode == 4 :
        FractalImages.CreateCantorLawnGIF((1000,1000), 6, "images/CantorLawnGIF.gif")
    elif mode == 5 :
        FractalImages.CreatCantorStringVolumeImage((1000,1000), (475,525), 6, 0.0125, "images/CantorStringVolume.png")
    elif mode == 6 :
        FractalImages.CreatCantorLawnVolumeImage((1000,1000), 6, 0.0125, "images/CantorLawnVolume.png")
    elif mode == 7 :
        FractalImages.CreateCantorStringVolumeGIF((1000,1000), (475,525), 6, 0.0125, "images/CantorStringVolumeGIF.gif")
    elif mode == 8 :
        FractalImages.CreateCantorLawnVolumeGIF((1000,1000), 6, 0.0125, "images/CantorLawnVolumeGIF.gif")
    else:
        print("Invalid input.")

    print("Done!")

