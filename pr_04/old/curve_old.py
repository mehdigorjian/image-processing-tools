from PIL import Image, ImageDraw
import numpy as np
import math
from pixel import Pixel

class Curve:

    def __init__(self, image):
        self.image = image
        self.im_width = self.image.size[0]
        self.im_height = self.image.size[1]
        self.curve_pixs = []
            
    def curve_pix_by_index(self, index):
        return self.curve_pixs[index]

    def draw_line(self, param=10, p0=(0,0), p1=(100,100), line_width=1):
        x0, y0 = p0
        x1, y1 = p1
        dx, dy = x1 - x0, y1 - y0
        i = 0
        while i <= 1:
            x, y = x0 + dx * i, y0 + dy * i
            draw = ImageDraw.Draw(self.image)
            draw.line((x0,y0,x,y), fill=(100,100,100), width=line_width)
            px = int(x + 0.5)
            py = int(y + 0.5)
            self.curve_pixs.append((px,py))
            x0, y0 = x, y
            i += 1/param 


    # color_to_change = (0, 0, 255)
    # threshold = 220

    # # Load image:
    # input_image = Image.open("input.png")
    # input_pixels = input_image.load()

    # # Create output image
    # output_image = Image.new("RGB", input_image.size)
    # draw = ImageDraw.Draw(output_image)

    # # Generate image
    # for x in range(output_image.width):
    #     for y in range(output_image.height):
    #         r, g, b = input_pixels[x, y]
    #         if distance2(color_to_change, input_pixels[x, y]) < threshold ** 2:
    #             r = int(r * .5)
    #             g = int(g * 1.25)
    #             b = int(b * .5)
    #         draw.point((x, y), (r, g, b))

    # output_image.save("output.png")

def main():
    im = Image.new('RGB', (100,100), color=(0, 0, 0))
    c = Curve(im)
    c.draw_line()
    print(c.curve_pixs)
    print(c.curve_pix_by_index(0))
    im.show()






if __name__ == '__main__':
    main()