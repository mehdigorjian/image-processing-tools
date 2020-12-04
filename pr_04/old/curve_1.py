from PIL import Image, ImageDraw
import math
from pixel import Pixel

class Curve:
    
    def __init__(self, image):
        self.curve_pixs = []
            
    def curve_pix_by_index(self, index):
        return self.curve_pixs[index]

    def curve_draw(self, image, p0, p1, param=10, line_width=3):
        pdt = p0 - p1        
        i = 0
        while i <= 1:
            p = p0 + pdt * i
            draw = ImageDraw.Draw(image)
            # print(p.x, ' | ', p.y)
            draw.line((p0.x,p0.y,p.x,p.y), fill=(255,0,0), width=line_width)
            self.curve_pixs.append(Pixel(int(p.x + 0.5), int(p.y + 0.5)))
            p0 = p
            i += 1/param
