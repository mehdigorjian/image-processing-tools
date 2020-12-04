from PIL import Image
import numpy as np
maxVal = 255

def image_ppm_writer(image_file_name):
    im = Image.open(image_file_name)
    im_rgb = im.convert('RGB')
    im_array = np.array(im)
    im_array.tofile('zzz.txt', sep=' ')
    
    m = im_array.reshape((im_array.shape[0],im_array.shape[1], -1))
    # print(m)
    # print(im_array.shape)
    # print(m.shape)
    # print(im_array)
    # print(im_array.shape)
    # print(im_rgb.getpixel((0,0)))
    # for m in range(im_array.shape[0]):
    #     for n in range(im_array.shape[1]):

    #         r = im_array[m, n, 0]
    #         g = im_array[m, n, 1]
    #         b = im_array[m, n, 2]

    #         print(r, g, b)

    pixels_color_list = np.ndarray.tolist(im_array)
    # print(pixels_color_list)
    # print(pixels_color_list[-1])
    # print(pixels_color_list[0])

    header = f'P6\n# some comments!\n{im.size[0]} {im.size[1]}\n{maxVal}\n'

    with open('ppmImage.ppm', 'w') as pFile:
        
        pFile.write(header)
        for element in pixels_color_list:
            # print(element)
            # print('***************************************')
            # print(len(element))
            # print('***************************************')
            line = ''
            for item in element:
                item_str = ''
                for k in item:
                    item_str += str(k) + ' '
                line += item_str


            pFile.write(line+'\n')
            


    # print(pixels_color_list)
# im1 = Image.open('tr.jpg')
# t = im1.resize((300,200))
# t.show()
# t.save('t.jpg')
image_ppm_writer('output.png')
