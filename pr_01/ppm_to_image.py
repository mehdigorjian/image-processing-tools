#  READING A *.PPM FILE FORMAT AND SHOWING IT AS AN *.JPG IMAGE
import numpy as np
from PIL import Image
import cv2
'''
def ppm_to_image_array(func):
    
        input: body of the ppm file which could be gained from:
               getting_header(ppmFile)
        output: image as an array
    
    def wrapper(f):
                
        w, h, _, fullBody = func(f)
        body_array = np.empty((w,h))
        # print(w, h)

        # for n in range(len(fullBody)):
        #     if n%3 == 0: red_list.append(fullBody[n])
        #     if n%3 == 1: green_list.append(fullBody[n])
        #     if n%3 == 2: blue_list.append(fullBody[n])

        for l in fullBody:
            red_list = []
            green_list = []
            blue_list = []

            line_listing = l.split()
            line_int = [int(i) for i in (line_listing)]
            for n in range(len(line_int)):
                if n%3 == 0: red_list.append(line_int[n])
                if n%3 == 1: green_list.append(line_int[n])
                if n%3 == 2: blue_list.append(line_int[n])

            line_array_tuple = np.asarray(list(zip(red_list, green_list, blue_list)))/255.0
            # line_array_tuple.reshape((1,w,3))
            # np.append(body_array, line_array_tuple, axis=0)
        # print(body_array *255)
        return body_array.reshape((h, w, 3))
    return wrapper
'''

# @ppm_to_image_array
def getting_params(fileName):
    '''
        without decorator:
            input: *.ppm file format
            output: width:int, height:int, maxValue:int, body:list
    '''
    header_list = []
    body_list = []
    with open(fileName, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#') and len(line.split()) < 3:
                header_list.extend(line.rstrip('\n').split())
            else:
                if not line.startswith('#'):
                    body_list.append(line.rstrip('\n'))

    body_color_list = []
    for l in body_list:
            red_list = []
            green_list = []
            blue_list = []

            line_listing = l.split()
            line_int = [int(i) for i in (line_listing)]
            for n in range(len(line_int)):
                if n%3 == 0: red_list.append(line_int[n])
                if n%3 == 1: green_list.append(line_int[n])
                if n%3 == 2: blue_list.append(line_int[n])
    
            line_color_list = list(zip(red_list, green_list, blue_list))
            body_color_list.append(line_color_list)

    body_array = np.array(body_color_list)
    
    # print(body_array[-1,-1,:])
    print('->', body_array.shape)
    if header_list[0] != 'P6': raise Exception('Only P6 format is accepted!')
    header_list.pop(0)

    # return int(header_list[0]), int(header_list[1]), int(header_list[2]), body_array/255.0
    return body_array

image_as_array = getting_params('zzz.ppm')
print(image_as_array)


im = Image.fromarray(image_as_array, mode='RGB')
im.save('ppm_output.png')
# print(im.size)
im.show()

