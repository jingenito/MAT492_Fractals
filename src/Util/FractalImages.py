import os, sys

app_path = os.path.dirname(os.path.realpath('main.py'))
sys.path.append(os.path.join(app_path,'src'))

from CantorSet import CantorSet
from CantorLawn import CantorLawn
from ResolutionType import ResolutionType
import Util.ImageMods as ImageMods

from PIL import Image

# this is more of a lookup table to remember my work than of actual impotortance
# resolutionLookupTable = { (1920,1080) : 6,
#                           (2560,1440) : 7
#                         }
# _Tiers = 6

def CreateCantorStringImage(resolution : tuple, rowRange : tuple, _Tiers : int, filename : str) :
    print("Create Cantor String Image started.")
    cSet = CantorSet((0, resolution[ResolutionType.Width]), _Tiers)
    print("Created the Cantor Set.")

    cSet.save_cantorStringImage(resolution, rowRange, filename)
    print("Saved Cantor String image.")

def CreateCantorLawnImage(resolution : tuple, _Tiers : int, filename : str) :
    print("Create Cantor Lawn Image started.")
    cLawn = CantorLawn(resolution, _Tiers)
    print("Created the Cantor Lawn.")

    cLawn.save_image(filename)
    print("Saved the Cantor Lawn image.")

def CreateCantorLawnGIF(resolution : tuple, tier : int, filename : str) :
    print("Create Cantor Lawn GIF tier:", tier, "started.")
    images = []
    
    #initialize variables
    c = CantorLawn(resolution, 0)
    prevImg = c.get_cantorLawnImage()

    #repeat 0 a few times to slow down the beginning
    for i in range(4) :
        images.append(prevImg)
        
    for i in range(1, tier + 1) :
        c = CantorLawn(resolution, i)
        currImg = c.get_cantorLawnImage()

        #this is to get a smoother transition between tiers
        imgList = ImageMods.BlendImages(prevImg, currImg, 10)
        images.extend(imgList)

        print(float(i / tier) * 100, "%")
        prevImg = currImg

    print("Created images, saving the GIF...")
    images[0].save(filename, save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
    print("Saved the GIF!")

def CreateCantorStringGIF(resolution : tuple, rowRange : tuple, tier : int, filename : str) :
    print("Create Cantor String GIF tier:", tier, "started.")
    images = []

    #initialize variables
    _xInt = (0, resolution[ResolutionType.Width])
    cSet = CantorSet(_xInt, 0)
 
    prevImg = cSet.get_cantorStringImage(resolution, rowRange)

    #repeat 0 a few times to slow down the beginning
    for i in range(3) :
        images.append(prevImg)

    for i in range(1, tier + 1) :
        cSet = CantorSet(_xInt, i)
        currImg = cSet.get_cantorStringImage(resolution, rowRange)

        #this is to get a smoother transition between tiers
        imgList = ImageMods.BlendImages(prevImg, currImg, 10)
        images.extend(imgList)

        print(float(i / tier) * 100, "%")
        prevImg = currImg

    print("Created images, saving the GIF...")
    images[0].save(filename, save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
    print("Saved the GIF!")

def CreatCantorStringVolumeImage(resolution : tuple, rowRange : tuple, tier : int, epsilon : float, filename : str) :
    print("Create Cantor String Volume Image epsilon:", epsilon,"and tier:", tier, "started.")
    cSet = CantorSet((0, resolution[ResolutionType.Width]), tier)
    print("Created the Cantor Set.")

    print("Creating the Volume Image.")
    cSet.save_cantorStringVolumeImage(resolution, rowRange, epsilon, filename)
    print("Saved Cantor String Volume image.")

def CreatCantorLawnVolumeImage(resolution : tuple, tier : int, epsilon : float, filename : str) :
    print("Create Cantor Lawn Volume Image epsilon:", epsilon,"and tier:", tier, "started.")
    cLawn = CantorLawn(resolution, tier)
    print("Created the Cantor Lawn.")

    print("Creating the Volume Image.")
    cLawn.save_cantorLawnVolumeImage(epsilon, filename)
    print("Saved Cantor Lawn Volume image.")

def CreateCantorStringVolumeGIF(resolution : tuple, rowRange : tuple, tier : int, epsilon : float, filename : str) -> list :
    print("Create Cantor String Volume GIF Image epsilon:", epsilon,"and tier:", tier, "started.")
    images = []

    #initialize variables
    _xInt = (0, resolution[ResolutionType.Width])
    c = CantorSet(_xInt, tier)
    completed_img = c.get_cantorStringImage(resolution, rowRange)
    prevImg = completed_img

    #repeat 0 a few times to slow down the beginning
    for i in range(3) :
        images.append(completed_img)

    for i in range(1, tier + 1) :
        cSet = CantorSet(_xInt, i)
        currImg = cSet.get_cantorStringVolumeImage(resolution, rowRange, epsilon, completed_img.copy())

        #this is to get a smoother transition between tiers
        imgList = ImageMods.BlendImages(prevImg, currImg, 10)
        images.extend(imgList)
        images.append(currImg)

        print(float(i / tier) * 100, "%")
        prevImg = currImg
        
    print("Created images, saving the GIF...")
    images[0].save(filename, save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
    print("Saved the GIF!")
    return images

def CreateCantorLawnVolumeGIF(resolution : tuple, tier : int, epsilon : float, filename : str) :
    print("Create Cantor Lawn Volume GIF tier:", tier, "started.")
    images = []
    
    #initialize variables
    c = CantorLawn(resolution, tier)
    completed_img = c.get_cantorLawnImage()
    prevImg = completed_img

    #repeat 0 a few times to slow down the beginning
    for i in range(4) :
        images.append(prevImg)
        
    for i in range(1, tier + 1) :
        c = CantorLawn(resolution, i)
        currImg = c.get_cantorLawnVolumeImage(epsilon, completed_img.copy())

        #this is to get a smoother transition between tiers
        imgList = ImageMods.BlendImages(prevImg, currImg, 10)
        images.extend(imgList)
        images.append(currImg)

        print(float(i / tier) * 100, "%")
        prevImg = currImg

    print("Created images, saving the GIF...")
    images[0].save(filename, save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
    print("Saved the GIF!")

def CreateCantorLawnVolumeJustVolume(resolution : tuple, tier : int, epsilon : float, filename : str) :
    print("Create Cantor Lawn Volume Image epsilon:", epsilon,"and tier:", tier, "started.")
    cLawn = CantorLawn(resolution, tier)
    print("Created the Cantor Lawn.")

    print("Creating the Volume Image with just the Volume.")
    cLawn.save_cantorLawnVolumeJustVolumeImage(epsilon, filename)
    print("Saved Cantor Lawn Volume image.")