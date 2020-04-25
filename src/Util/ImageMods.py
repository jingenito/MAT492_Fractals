from PIL import Image, ImageOps 

def ReverseImage(originalFileName : str, newFileName : str) :
    print('Opening image...')
    image = Image.open(originalFileName)

    print('Inverting image...')
    inverted_image = ImageOps.invert(image)
    inverted_image.save(newFileName)

    print('Saved Image!')

def BlendImages(image1 : Image, image2 : Image, steps : int) -> list :
    """ Call this method to blend the 2 images with the specified step size """
    newList = []
    newList.append(image1)
    #blend over the images with the specified step size
    for x in range(steps) :
        scale = (x + 1) / steps
        img = Image.blend(image1, image2, scale)
        newList.append(img)
    newList.append(image2)
    return newList
