from PIL import Image, ImageDraw
import numpy as np
import math

im = Image.new('RGB', (100,100), color=(0, 0, 0))

def line(_image, param=10, start_point=(0,0), end_point=(100,100),\
    start_color=(155,20,0), end_color=(20,10,55), line_width=5):

    r0, g0, b0 = start_color
    r1, g1, b1 = end_color
    dr, dg, db = r1 - r0, g1 - g0, b1 - b0
    x0, y0 = start_point
    x1, y1 = end_point
    dx, dy = x1 - x0, y1 - y0
    i = 0

    while i <= 1:
        x, y = x0 + dx * i, y0 + dy * i
        # print(f'x: {x} | y: {y}')
        r, g, b = int(r0 + dr * i), int(g0 + dg * i), int(b0 + db * i)
        draw = ImageDraw.Draw(im)
        # draw.point((x, y), fill=(255,0,0))
        draw.line((x0,y0,x,y), fill=(r,g,b), width=line_width)
        x0, y0 = x, y
        r0, g0, b0 = r, g, b
        i += 1/param

# Square distance between 2 colors
def distance2(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

color_to_change = (0, 0, 255)
threshold = 220

# Load image:
input_image = Image.open("input.png")
input_pixels = input_image.load()

# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Generate image
for x in range(output_image.width):
    for y in range(output_image.height):
        r, g, b = input_pixels[x, y]
        if distance2(color_to_change, input_pixels[x, y]) < threshold ** 2:
            r = int(r * .5)
            g = int(g * 1.25)
            b = int(b * .5)
        draw.point((x, y), (r, g, b))

output_image.save("output.png")

line(im)
im.show()