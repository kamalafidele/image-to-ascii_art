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


def read_img(inputFile):
    try:
        img_data = Image.open(inputFile)
    except:
        print("This path is invalid")
    return img_data

def resize_img(img_data, finalWidth, finalHeight):
    size = img_data.resize((finalWidth, finalHeight))
    return size

def generate_grayscale(size):
    greysc = ImageOps.grayscale(size)
    return greysc

def convert_pixel_to_ascii(greysc, finalWidth):
    pixels = greysc.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    pixelCount = len(characters)  
    asciiImage = "\n".join([characters[index:(index+finalWidth)] for index in range(0, pixelCount, finalWidth)])
    return asciiImage

def main():
    asciiImage = convert_pixel_to_ascii(generate_grayscale(resize_img(read_img(inputFile), finalWidth, finalHeight)), finalWidth)
    print(asciiImage)

main()