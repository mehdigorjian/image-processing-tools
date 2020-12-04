from PIL import Image, ImageDraw
import numpy as np
import random
import math

class ShapeDraw:

    def __init__(self, w, h, inner_color=(25,150,0), outer_color=(10,255,10)):
        self.w = w
        self.h = h
        self.image = Image.new('RGB', (self.w, self.h), color = (0,0,0))
        self.cc = np.array([self.image.width/2, self.image.height/2])
        self.inner_color = inner_color
        self.outer_color = outer_color

    def line_draw(self):
        for i in range(self.image.width):
            for j in range(self.image.height):
                if i+j<(self.w+self.h)//2 + 2 and i+j>(self.w+self.h)//2 - 2:            
                    self.image.putpixel((i,j), self.inner_color)
                else:
                    self.image.putpixel((i,j), self.outer_color)
        return self.image

    def polygon_draw(self, r=30, div=6, angle_limit=360):
        for i in range(self.image.width):
            for j in range(self.image.height):
                num = 0
                for t in range(0,angle_limit,angle_limit//div):
                    xi = r * math.cos(t * 2 * math.pi / angle_limit) + self.image.size[0]/2
                    yi = r * math.sin(t * 2 * math.pi / angle_limit) + self.image.size[1]/2
                    if (i - xi) * math.cos(t * 2 * math.pi / angle_limit) + (j - yi) * math.sin(t * 2* math.pi / angle_limit) < 0:
                        num += 1    
                if num == div:
                    self.image.putpixel((i,j), self.inner_color)
                else:
                    self.image.putpixel((i,j), self.outer_color)
        return self.image

    def star_draw(self, r=20, div=6, angle_limit=360):
        for i in range(self.image.width):
            for j in range(self.image.height):
                num = 0
                for t in range(0,angle_limit,angle_limit//div):
                    xi = r * math.cos(t * 2 * math.pi / angle_limit) + self.image.size[0]/2
                    yi = r * math.sin(t * 2 * math.pi / angle_limit) + self.image.size[1]/2
                    if (i - xi) * math.cos(t * 2 * math.pi / angle_limit) + (j - yi) * math.sin(t * 2* math.pi / angle_limit) < 0:
                        num += 1    
                if num == div or num == div - 1:
                    self.image.putpixel((i,j), self.inner_color)
                else:
                    self.image.putpixel((i,j), self.outer_color)
        return self.image
    
    def draw_by_formula(self):
        ang = 12 * math.pi
        for t in np.arange(0, ang, .01):
            p = (math.exp(math.cos(t)) - 2 * math.cos(4 * t) - math.sin(t/12)**5)
            x = int(math.sin(t) * p * 25 + self.image.width/2)
            y = int(math.cos(t) * p * 25 + self.image.height/2)
            self.image.putpixel((x,y), self.outer_color)
        return self.image

    def jitter_sampling(self):
        for i in range(self.image.width):
            for j in range(self.image.height):
                cR, cG, cB = 0, 0, 0
                # cR, cG, cB = self.image.getpixel((i,j))
                for _ in range(8):
                    R1 = random.randrange(0,1)
                    R2 = random.randrange(0,1)
                    cR1, cG1, cB1 = self.image.getpixel((i+R1,j+R2))

                    cR += cR1
                    cG += cG1
                    cB += cB1
                self.image.putpixel((i,j), (int(cR/8), int(cG/8), int(cB/8)))
        return self.image

def main():
    # creating objects
    s1 = ShapeDraw(100,100, (235, 164, 52), (24, 96, 120))
    s2 = ShapeDraw(100,100, (120, 34, 24), (26, 23, 20))
    s3 = ShapeDraw(200,200, (41, 59, 39), (112, 161, 108))
    s4 = ShapeDraw(200,200, (41, 59, 39), (112, 161, 108))

    # drawing line
    im1 = s1.line_draw()
    im1_a = s1.jitter_sampling()
    im1.show()
    im1_a.show()
    im1.save('line_noSampling.png')
    im1_a.save('line_withSampling.png')
    
    # drawing star
    im2 = s2.star_draw()
    im2_a = s2.jitter_sampling()
    im2.show()
    im2_a.show()
    im2.save('circle_noSampling.png')
    im2_a.save('circle_withSampling.png')
    
    # drawing polygon
    im3 = s3.polygon_draw()
    im3_a = s3.jitter_sampling()
    im3.show()
    im3_a.show()
    im3.save('freeForm_noSampling.png')
    im3_a.save('freeForm_withSampling.png')
    
if __name__ == '__main__':
    main()