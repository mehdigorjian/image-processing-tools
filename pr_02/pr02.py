from PIL import Image, ImageDraw
import numpy as np
import random
im = Image.new('RGB', (100, 60), color = (0,0,0))
p1 = np.array([70,0])
p2 = np.array([30,60])
cc = np.array([im.size[0]/2, im.size[1]/2])

def line_draw1(_image):
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            temp_point = np.array([i,j])
            pp1 = np.subtract(temp_point, p1)
            pp2 = np.subtract(temp_point, p2)
            cross = np.cross(pp1, pp2)

            if cross<0:            
                im.putpixel((i,j), (255,0,0))
            else:
                im.putpixel((i,j), (0,255,0))

def line_draw2(_image):
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if i+j<80:            
                im.putpixel((i,j), (255,0,0))
            else:
                im.putpixel((i,j), (0,255,0))

def circle_draw(_image):
    for i in range(im.size[0]):
            for j in range(im.size[1]):
                area = np.sqrt((i - cc[0])**2 + (j - cc[1])**2)
                if area<20:            
                    im.putpixel((i,j), (255,0,0))
                else:
                    im.putpixel((i,j), (0,255,0))
# def free_draw(_image):
#     for i in range(360):
#         # x = int((10+amplitude * np.sin(n*ang)) * np.sin(n*ang)+ n*ang)
#         # y = int((10+amplitude * np.cos(n*ang)) * np.cos(n*ang)+ n*ang)
#         x = int(cc[0]/2 + 10 * np.sin(i))
#         y = int(cc[0]/2 + 10 * np.cos(i))
#             # if np.sqrt((i - cc[0])**2 + (j - cc[1])**2) <= 20:
#         # if np.sqrt((x - im.size[0])**2 + (y - im.size[1])**2) <= 10:
#         print(x, ' ', y)
#         im.putpixel((x,y), (255,0,0))
            # else:
                # im.putpixel((i,j), (0,255,0))
'''
def free_draw(_image, r=10, angle=120):
    p_i_list = []
    for t in range(0,360,angle):
        # dp_i = np.array([r * np.cos(t * 2* np.pi / 360), r * np.sin(t * 2* np.pi / 360)])
        xi = r * np.cos(t * 2* np.pi / 360) + im.size[0]/2
        yi = r * np.sin(t * 2* np.pi / 360) + im.size[1]/2
        n_i = np.array([np.cos(t * 2* np.pi / 360), np.sin(t * 2* np.pi / 360)])
        p_i = np.array([xi,yi])
        p_i_list.append([p_i, n_i])
        # p_i_list.append(p_i)

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            temp_pt = np.subtract(np.array([i,j]), cc)
            # dir_list = []
            num = 0
            for pt in p_i_list:
                diff = np.subtract(pt[0], temp_pt)
                dot = np.dot(pt[1], diff)
                if dot<0:
                    num += 1
                    # print(dot)
            if num == 360//angle:
                im.putpixel((i,j), (255,0,0))
            else:
                im.putpixel((i,j), (0,255,0))
            
            
            # if np.product(dir_list)<0:
            #     im.putpixel((i,j), (255,0,0))
            # else:
            #     im.putpixel((i,j), (0,255,0))
'''
    # print(p_i_list)
    # draw = ImageDraw.Draw(im)
    # for k in range(len(p_i_list)):
    #     if k < len(p_i_list)-1:
    #         draw.line((p_i_list[k][0],p_i_list[k][1], \\
    #         p_i_list[k+1][0],p_i_list[k+1][1]), width=3, fill=(0,255,0))
    #     else:
    #         draw.line((p_i_list[k][0],p_i_list[k][1], \\
    #         p_i_list[0][0],p_i_list[0][1]), width=3, fill=(0,255,0))

    
    # im.putpixel(p_i, (255,0,0))
            


import math
def free_draw(_image, r=10, div=30, angle_limit=360):
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            num = 0
            r_new = r + random.random() # change this line
            for t in range(0,angle_limit,angle_limit//div):
                xi = r_new * math.cos(t * 2* math.pi / angle_limit) + im.size[0]/2
                yi = r_new * math.sin(t * 2* math.pi / angle_limit) + im.size[1]/2
                if (i - xi) * math.cos(t * 2* math.pi / angle_limit) + (j - yi) * math.sin(t * 2* math.pi / angle_limit) < 0:
                    num += 1    
            if num == div:
                im.putpixel((i,j), (255,0,0))
            else:
                im.putpixel((i,j), (0,255,0))


free_draw(im)
im.show()
