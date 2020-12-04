from PIL import Image, ImageDraw
from math import sin, cos, tan, radians, floor
import numpy as np

def translate(dx, dy, im='img.jpeg'):
    input_image = Image.open(im)
    input_pixels = input_image.load()
    output_image = Image.new("RGB", input_image.size)
    draw = ImageDraw.Draw(output_image)
    for x in range(input_image.width):
        for y in range(input_image.height):
            xp = x + dx
            yp = y + dy
            if 0 <= xp < input_image.width and 0 <= yp < input_image.height:
                draw.point((x, y), input_pixels[xp, yp])
    output_image.show()
    output_image.save("output_translate.png")

def persp(im):
    input_image = Image.open(im)
    output_image = Image.new("RGB", input_image.size)
    draw = ImageDraw.Draw(output_image)
    angle=radians(30)                              
    image = np.array(Image.open(im))             
    height=image.shape[0]                                  
    width=image.shape[1]                                    
    new_height  = round(abs(image.shape[0]*cos(angle))+abs(image.shape[1]*sin(angle)))+1
    new_width  = round(abs(image.shape[1]*cos(angle))+abs(image.shape[0]*sin(angle)))+1
    output=np.zeros((new_height,new_width,image.shape[2]))
    original_centre_height   = round(((image.shape[0]+1)/2)-1)    
    original_centre_width    = round(((image.shape[1]+1)/2)-1)    
    new_centre_height= round(((new_height+1)/2)-1)        
    # new_centre_width= round(((new_width+1)/2)-1)          
    for i in range(height):
        for j in range(width):
            y = image.shape[0]-1-i-original_centre_height                   
            x = image.shape[1]-1-j-original_centre_width 
            new_x, new_y = round(x-y*tan(angle/2)), y
            new_x, new_y = (new_width-new_x)//2, (new_centre_height-new_y)//2
            output[new_y,new_x,:]=image[i,j,:]                          
    pil_img=Image.fromarray((output).astype(np.uint8))
    input_pixels1 = pil_img.load()
    center_x = pil_img.width / 2
    center_y = pil_img.height / 2
    for x in range(pil_img.width):
        for y in range(pil_img.height):
            xp = int((x - center_x) * cos(angle) - (y - center_y) * sin(angle) + center_x)
            yp = int((x - center_x) * sin(angle) + (y - center_y) * cos(angle) + center_y)
            if 0 <= xp < pil_img.width and 0 <= yp < pil_img.height:
                draw.point((x, y), input_pixels1[xp, yp])
    output_image.show()
    output_image.save("output_perspective.png")


persp('img1.jpg')
translate(80,80)