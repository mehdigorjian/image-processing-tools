import numpy as np
'''
a = np.array([[1,5,6],\
              [4,6,8],\
              [0,9,1],\
              [3,2,1],\
              [8,5,7],\
              [4,4,0]])

b = np.array([[1,1,False],\
              [1,1,False],\
              [False,False,1],\
              [1,False,1],\
              [1,1,False],\
              [1,1,False]])

print(a[b].reshape(3,3,6))
print(a[b].shape)
'''

from PIL import Image
img = Image.open('img.png')
pix = img.convert('RGBA')
aimg = img.copy()
aimg = aimg.resize((100, 100))
new = Image.new(size=(100,100), mode='RGBA')

# print(pix.getpixel((10,10)))
for i in range(aimg.width):
    for j in range(aimg.height//2):
        # aimg.putalpha(50)
        # aa = aimg.getpixel((i,j))
        rgba = (255, 255, 255, 50)
        new.putpixel((i,j), rgba)
new.show()
# aimg.save('aimg.jpg')