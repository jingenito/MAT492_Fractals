from PIL import Image, ImageOps 

def ReverseImage(originalFileName : str, newFileName : str) :
    print('Opening image...')
    image = Image.open(originalFileName)

    print('Inverting image...')
    inverted_image = ImageOps.invert(image)
    inverted_image.save(newFileName)

    print('Saved Image!')