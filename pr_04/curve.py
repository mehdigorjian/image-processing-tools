from PIL import Image, ImageDraw
import math
from pixel import Pixel
class Curve:
    def __init__(self, image):
        self.curve_pixs = []
        self.image = image
            
    def curve_pix_by_index(self, index):
        return self.curve_pixs[index]

    def curve_draw(self, p0, p1, pt_list, line_width=3):
        # pt_list.remove(pt_list[0])
        # pt_list.remove(pt_list[-1])
        xList = []
        yList = []
        param = len(pt_list)
        pdt = p0 - p1
        p = Pixel(0,0)
        draw = ImageDraw.Draw(self.image)
        for i in range(param):
            temp_pt = Pixel(pt_list[i][0], pt_list[i][1])
            p.x = p0.x + pdt.x * temp_pt.x
            p.y = temp_pt.y
            xList.append(p.x)
            yList.append(p.y)
            # if i < param + 1:
            #     draw.line((p0.x,p0.y,p.x,p.y), fill=(255,0,0), width=line_width)
            #     self.curve_pixs.append(Pixel(int(p.x + 0.5), int(p.y + 0.5)))
            #     p0.x, p0.y = p.x, p.y
            # else:
            #     draw.line((p.x,p.y,p1.x,p1.y), fill=(255,0,0), width=line_width)
            #     self.curve_pixs.append(Pixel(int(p.x + 0.5), int(p.y + 0.5)))
        m = 100000 # of steps
        for p in range(m):
            x = (self.image.size[0] - 1) * p / (m - 1)
            y = 0.0
            for j in range(param):
                Lx = 1.0
                for k in range(param):
                    if k != j:
                        Lx = Lx * (x - xList[k]) / (xList[j] - xList[k])
                y = y + yList[j] * Lx
            if y >= 0 and y <= self.image.size[1] - 1:
                self.image.putpixel((int(x), int(y)), (255, 255, 255))
        # show the points used
        cr = 3 # circle radius
        for i in range(param):
            cx = int(xList[i])
            cy = int(yList[i])
            draw.ellipse((cx - cr, cy - cr, cx + cr, cy + cr))
        self.image.save('Polynomial_Interpolation.png', 'PNG')
        return list(zip(xList, yList))

    def calc_parabola_vertex(self, x1, y1, x2, y2, x3, y3):
        denom =(x1-x2)*(x1-x3)*(x2-x3)
        A = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom
        B = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom
        C = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1) * y2+x1 * x2 * (x1-x2) * y3) / denom
        return A,B,C
    # Ax**2 + Bx + C
    def color_map(self, a, b, c):
        for i in range(self.image.width):
            for j in range(self.image.height):
                px_color_r, px_color_g, px_color_b = self.image.getpixel((i,j))
                mapped_color_r = int(a * px_color_r**2 + b * px_color_r + c)
                mapped_color_g = int(a * px_color_g**2 + b * px_color_g + c)
                mapped_color_b = int(a * px_color_b**2 + b * px_color_b + c)
                if mapped_color_r > 255: mapped_color_r = 255
                if mapped_color_g > 255: mapped_color_g = 255
                if mapped_color_b > 255: mapped_color_b = 255
                self.image.putpixel((i,j), (mapped_color_r, mapped_color_g, mapped_color_b))
        self.image.save('Color_Interpolated_Mapped.png', 'PNG')




