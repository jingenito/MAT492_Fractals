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
    print("9: Cantor Lawn Volume Just Voume")
    print("10: Cantor Strings 1 - x")
    print("11: Cantor Lawns 1 - x")
   
    inp = input("Choose an image to create: ")
    if inp.isnumeric() :
        mode = int(inp)

    if mode == 1 :
        FractalImages.CreateCantorStringImage((1000, 100), (40, 60), 1, "images/CantorString_1.png")
    elif mode == 2 :
        FractalImages.CreateCantorLawnImage((1000,1000), 6, "images/CantorLawn_6.png")
    elif mode == 3 :
        FractalImages.CreateCantorStringGIF((1000,1000), (475,525), 6, "images/CantorStringGIF_6.gif")
    elif mode == 4 :
        FractalImages.CreateCantorLawnGIF((1000,1000), 6, "images/CantorLawnGIF_6.gif")
    elif mode == 5 :
        FractalImages.CreatCantorStringVolumeImage((1000, 100), (40, 60), 4, 0.0125, "images/CantorStringVolume_4.png")
    elif mode == 6 :
        FractalImages.CreatCantorLawnVolumeImage((1000,1000), 6, 0.0125, "images/CantorLawnVolume_6.png")
    elif mode == 7 :
        FractalImages.CreateCantorStringVolumeGIF((1000,1000), (475,525), 6, 0.0125, "images/CantorStringVolumeGIF_6.gif")
    elif mode == 8 :
        FractalImages.CreateCantorLawnVolumeGIF((1000,1000), 6, 0.0125, "images/CantorLawnVolumeGIF_6.gif")
    elif mode == 9 :
        FractalImages.CreateCantorLawnVolumeJustVolume((1000,1000), 6, 0.0125, "images/CantorLawnVolumeJustVolume_6.png")
    elif mode == 10 :
        inp = input("Choose a stopping tier x: ")
        if inp.isnumeric() :
            for i in range(1, int(inp) + 1) :
                filename = "images/CantorString_" + str(i) + ".png"
                FractalImages.CreateCantorStringImage((1000, 100), (40, 60), i, filename)
    elif mode == 11 :
        inp = input("Choose a stopping tier x: ")
        if inp.isnumeric() :
            for i in range(1, int(inp) + 1) :
                filename = "images/CantorLawn_" + str(i) + ".png"
                FractalImages.CreateCantorLawnImage((1000, 1000), i, filename)
    else:
        print("Invalid input.")

    print("Done!")

