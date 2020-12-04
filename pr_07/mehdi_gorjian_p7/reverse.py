from PIL import Image, ImageDraw
from math import sin, cos, radians

def reverse_rotate(ang, im):
    input_image = Image.open(im)
    input_pixels = input_image.load()
    output_image = Image.new("RGB", input_image.size)
    draw = ImageDraw.Draw(output_image)
    angle = radians(ang)
    center_x = input_image.width / 2
    center_y = input_image.height / 2
    for x in range(input_image.width):
        for y in range(input_image.height):
            xp = int((x - center_x) * cos(angle) - (y - center_y) * sin(angle) + center_x)
            yp = int((x - center_x) * sin(angle) + (y - center_y) * cos(angle) + center_y)
            if 0 <= xp < input_image.width and 0 <= yp < input_image.height:
                draw.point((x, y), input_pixels[xp, yp])
    output_image.show()
    output_image.save("output_reverse_rotate.png")
reverse_rotate(-30, 'output_rotate.png')