import Util.FractalImages as FractalImages

if __name__ == "__main__":
    print("1: Cantor String")
    print("2: Cantor Lawn")
    print("3: Cantor String GIF")
    print("4: Cantor Lawn GIF")

    inp = input("Choose an image to create:\n")
    if inp.isnumeric() :
        mode = int(inp)

    if mode == 1 :
        FractalImages.CreateCantorStringImage((2560,1440), (670, 770), 6, "images/CantorString_Tier6.png")
    elif mode == 2 :
        FractalImages.CreateCantorLawnImage((2560,1440), 6, "images/CantorLawn_Tier6.png")
    elif mode == 3 :
        FractalImages.CreateCantorStringGIF((2560,1440), (670, 770), 9, "images/CantorStringGIF.gif")
    elif mode == 4 :
        FractalImages.CreateCantorLawnGIF((2560,1440), 9, "images/CantorLawnGIF.gif")
    else:
        print("Invalid input.")

    print("Done!")

