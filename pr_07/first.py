from PIL import Image, ImageDraw
from math import sin, cos, tan, radians, floor
import numpy as np

def rotate(ang, im='img.jpeg'):
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
    output_image.save("output_rotate.png")

def scale(new_WIDTH, new_HEIGHT, im='img.jpeg'):
    input_image = Image.open(im)
    input_pixels = input_image.load()
    output_image = Image.new("RGB", (new_WIDTH,new_HEIGHT))
    draw = ImageDraw.Draw(output_image)
    x_scale = input_image.width / output_image.width
    y_scale = input_image.height / output_image.height
    for x in range(output_image.width):
        for y in range(output_image.height):
            xp, yp = floor(x * x_scale), floor(y * y_scale)
            draw.point((x, y), input_pixels[xp, yp])
    output_image.show()
    output_image.save("output_scale.png")

def mirror(im='img.jpeg'):
    input_image = Image.open(im)
    input_pixels = input_image.load()
    output_image = Image.new("RGB", input_image.size)
    draw = ImageDraw.Draw(output_image)
    for x in range(output_image.width):
        for y in range(output_image.height):
            xp = input_image.width - x - 1
            draw.point((x, y), input_pixels[xp, y])
    output_image.show()
    output_image.save("output_mirror.png")

def shear(im='img.jpeg'):
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
    new_centre_width= round(((new_width+1)/2)-1)          
    for i in range(height):
        for j in range(width):
            y = image.shape[0]-1-i-original_centre_height                   
            x = image.shape[1]-1-j-original_centre_width 
            new_x, new_y = round(x-y*tan(angle/2)), y
            new_x, new_y = new_centre_width-new_x, new_centre_height-new_y
            output[new_y,new_x,:]=image[i,j,:]                          
    pil_img=Image.fromarray((output).astype(np.uint8))
    pil_img.show()                   
    pil_img.save("output_shear.png")         

shear(im='img1.jpg')
mirror()
scale(100,100)
rotate(30)