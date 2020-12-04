from PIL import Image
import numpy as np
# im = Image.open('output.png')
im = Image.new('RGB', (60, 30), color = (0,0,0))

m = np.asarray(im)
p1 = np.array([40,0])
p2 = np.array([20,30])

m.tofile('zzz.ppm', sep=' ')
header = f'P6\n# some comments!\n{im.size[0]} {im.size[1]}\n255\n'
f = open('zzz.ppm', 'r+')
f.seek(0, 0)
f.writelines(header)
f.close()
# n=m.swapaxes(0,2)
px = im.load()
for i in range(im.size[0]):
    for j in range(im.size[1]):
        # if i < im.size[0]/2:
        #######################################
            
            im.putpixel((i,j), (255,0,0))

# print(px[-1,-1])
# print(m)
# print('***********************')
# print(m.swapaxes(0,2))
# a = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,20,30],[40,50,60],[70,80,90]]])
# # print(np.reshape(a, (3,2,3)))
# print(a[:,0,0])
# print('**********')
# print(a.swapaxes(0,2))

# im.save('New_PPM.ppm', 'PPM')

# print(im_array)
# np.savetxt('ccc.txt', im_array, delimiter=' ')

#     for data_slice in im:
#         np.savetxt(outfile, data_slice)
#         outfile.write('# New slice\n')
    
# t = Image.fromarray(m, mode='RGB')
# t.show()
im.show()

# np.savetxt('ccc.txt', (a, b, c), delimiter=' ')
'''
import numpy as np

# Image size
width = 640
height = 480
channels = 3

# Create an empty image
img = np.zeros((height, width, channels), dtype=np.uint8)

# Draw something (http://stackoverflow.com/a/10032271/562769)
xx, yy = np.mgrid[:height, :width]
circle = (xx - 100) ** 2 + (yy - 100) ** 2
print(circle)
# Set the RGB values
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        r, g, b = circle[y][x], circle[y][x], circle[y][x]
        img[y][x][0] = r
        img[y][x][1] = g
        img[y][x][2] = b

# Display the image
i = Image.fromarray(img)
i.show()
# Save the image
'''