from PIL import Image
import numpy as np
import random
import math


class ShapeDraw:

    def __init__(self, w, h, inner_color=(255,0,0),outer_color=(10,255,10)):
        self.w = w
        self.h = h
        self.image = Image.new('RGB', (self.w, self.h), color = (0,0,0))
        self.cc = np.array([self.image.size[0]/2, self.image.size[1]/2])
        self.inner_color = inner_color
        self.outer_color = outer_color


    def line_draw(self):
        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
                if i+j<(self.w+self.h)//2:            
                    self.image.putpixel((i,j), self.inner_color)
                else:
                    self.image.putpixel((i,j), self.outer_color)
        return self.image


    def circle_draw(self, radius=20):
        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
                area = np.sqrt((i - self.cc[0])**2 + (j - self.cc[1])**2)
                if area<radius:            
                    self.image.putpixel((i,j), self.inner_color)
                else:
                    self.image.putpixel((i,j), self.outer_color)
        return self.image
    
    
    def polygon_draw(self, r=30, div=6, angle_limit=360):
        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
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
    

    def freeForm_draw(self, r=60, div=90, angle_limit=360,tolerance_factor=20):
        points = []
        count = 0
        while count < div:
            points.append(random.randrange(-1*tolerance_factor,tolerance_factor))
            count +=1

        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
                num = 0
                pt_count = 0
                for t in range(0,angle_limit,angle_limit//div):
                    r_new = r + points[pt_count]
                    xi = r_new * math.cos(t * 2 * math.pi / angle_limit) + self.image.size[0]/2
                    yi = r_new * math.sin(t * 2 * math.pi / angle_limit) + self.image.size[1]/2
                    if (i - xi) * math.cos(t * 2 * math.pi / angle_limit) + (j - yi) * math.sin(t * 2* math.pi / angle_limit) < 0:
                        num += 1
                    pt_count +=1
                if num == div:
                    self.image.putpixel((i,j), self.inner_color)
                else:
                    self.image.putpixel((i,j), self.outer_color)
        return self.image


    def jitter_sampling(self):
        for i in range(self.image.size[0]):
            for j in range(self.image.size[1]):
                cR, cG, cB = 0, 0, 0
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
    s1 = ShapeDraw(100,100, (235, 164, 52), (26, 23, 20))
    s2 = ShapeDraw(100,100, (120, 34, 24), (24, 96, 120))
    # s3 = ShapeDraw(100,100)
    s4 = ShapeDraw(200,200, (45, 58, 168), (184, 161, 35))

    # drawing line
    im1 = s1.line_draw()
    im1_a = s1.jitter_sampling()
    im1.show()
    im1_a.show()
    im1.save('line_noSampling.png')
    im1_a.save('line_withSampling.png')
    
    # drawing circle
    im2 = s2.circle_draw(radius=30)
    im2_a = s2.jitter_sampling()
    im2.show()
    im2_a.show()
    im2.save('circle_noSampling.png')
    im2_a.save('circle_withSampling.png')
    '''
    # drawing polygon
    im3 = s3.polygon_draw()
    im3_a = s3.jitter_sampling()
    im3.show()
    im3_a.show()
    im3.save('freeForm_noSampling.png')
    im3_a.save('freeForm_withSampling.png')
    '''
    # drawing free form
    im4 = s4.freeForm_draw()
    im4_a = s4.jitter_sampling()
    im4.show()
    im4_a.show()
    im4.save('freeForm_noSampling.png')
    im4_a.save('freeForm_withSampling.png')
    
if __name__ == '__main__':
    main()
