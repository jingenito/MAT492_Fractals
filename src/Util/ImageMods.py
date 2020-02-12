from PIL import Image
import PIL.ImageOps    

def ReverseImage(originalFileName : str, newFileName : str) :
    print('Opening image...')
    image = Image.open(originalFileName)

    print('Inverting image...')
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save(newFileName)

    print('Saved Image!')