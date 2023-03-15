import os
from PIL import Image, ImageOps

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def get_format():
    files = os.listdir('./uploads')
    return files[0].split('.')[1]


img_format = get_format()
inputFile = f'uploads/image_to_convert.{img_format}'
finalWidth = 100
finalHeight = 50


def fun_readFile(inputFile):
    try:
        wsad = Image.open(inputFile)
    except:
        print("This path is invalid")
    return wsad

def fun_size(wsad, finalWidth, finalHeight):
    size = wsad.resize((finalWidth, finalHeight))
    return size

def fun_greysc(size):
    greysc = ImageOps.grayscale(size)
    return greysc

def fun_char(greysc, finalWidth):
    pixels = greysc.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    pixelCount = len(characters)  
    asciiImage = "\n".join([characters[index:(index+finalWidth)] for index in range(0, pixelCount, finalWidth)])
    return asciiImage

def main():
    asciiImage = fun_char(fun_greysc(fun_size(fun_readFile(inputFile), finalWidth, finalHeight)), finalWidth)
    print(asciiImage)

main()