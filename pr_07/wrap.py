from PIL import Image, ImageDraw
from math import sqrt, atan2, pi, sin, cos
import numpy as np

def swirl(swirlRadius, swirlFactor, im='img1.jpg'):
    input_image = Image.open(im)
    input_pixels = input_image.load()
    output_image = Image.new("RGB", input_image.size)
    draw = ImageDraw.Draw(output_image)
    swirlX = input_image.width//2
    swirlY = input_image.height//2
    for x in range(input_image.width):
        for y in range(input_image.height):
            pixX = x - swirlX
            pixY = y - swirlY
            pixDist = sqrt((pixX*pixX) + (pixY*pixY))
            pixAng = atan2(pixX, pixY)
            sAmount = abs(1.0 - pixDist/swirlRadius)
            twistAng = swirlFactor * sAmount * pi * 2
            pixAng += twistAng
            pixX = int(cos(pixAng) * pixDist)
            pixY = int(sin(pixAng) * pixDist)
            draw.point((x, y), input_pixels[pixX, pixY])
    output_image.show()
    output_image.save("output_swirl11.png")

swirl(20, .025, im='img1.jpg')