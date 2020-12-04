import sys, os
import numpy as np
from imageio import imread, imwrite
from scipy.ndimage.filters import convolve
from PIL import Image

def calc_energy(img):
    filter_du = np.array([
        [1.0, 2.0, 1.0],
        [0.0, 0.0, 0.0],
        [-1.0, -2.0, -1.0],
    ])
    filter_du = np.stack([filter_du] * 3, axis=2)

    filter_dv = np.array([
        [1.0, 0.0, -1.0],
        [2.0, 0.0, -2.0],
        [1.0, 0.0, -1.0],
    ])
    filter_dv = np.stack([filter_dv] * 3, axis=2)
    img = img.astype('float32')
    convolved = np.absolute(convolve(img, filter_du)) + np.absolute(convolve(img, filter_dv))

    energy_map = convolved.sum(axis=2)
    return energy_map

def minimum_seam(img):
    r, c, _ = img.shape
    energy_map = calc_energy(img)
    M = energy_map.copy()
    backtrack = np.zeros_like(M, dtype=np.int)

    for i in range(1, r):
        for j in range(0, c):
            if j == 0:
                idx = np.argmin(M[i - 1, j:j + 2])
                backtrack[i, j] = idx + j
                min_energy = M[i - 1, idx + j]
            else:
                idx = np.argmin(M[i - 1, j - 1:j + 2])
                backtrack[i, j] = idx + j - 1
                min_energy = M[i - 1, idx + j - 1]
            M[i, j] += min_energy
    return M, backtrack

def left_column(img, base_img):
    img_read = imread(img)
    r, c, _ = img_read.shape
    M, backtrack = minimum_seam(img_read)
    mask = np.ones((r, c), dtype=np.bool)
    j = np.argmin(M[-1])
    for i in reversed(range(r)):
        mask[i, j] = False
        j = backtrack[i, j]

    mask = np.transpose(mask)
    base_img_size = Image.open(base_img)
    img_ = Image.open(img)
    img1 = img_.copy()
    img1 = img1.convert('RGBA')

    # img1 = img1.resize((img_.width,img_.height))
    new_img = Image.new(size=(base_img_size.width, base_img_size.height), mode='RGBA')
    back_img = new_img.copy()
    back_img.paste(img1, (0, 0), img1)
    back_img.save('temp_.png')
    img1 = Image.open('temp_.png')

    
    for i in range(img_.width):
        for j in range(img_.height):
            if mask[i,j] == False:
                # new_img.putpixel((i,j),(255,0,0,255))
                for k in range(i):
                    rgba = img1.getpixel((k,j))
                    new_img.putpixel((k,j),rgba)
    new_img.show()
    os.remove('temp_.png')
    return new_img


def right_column(img, base_img):
    img_read = imread(img)
    r, c, _ = img_read.shape
    M, backtrack = minimum_seam(img_read)
    mask = np.ones((r, c), dtype=np.bool)
    j = np.argmin(M[-1])
    for i in reversed(range(r)):
        mask[i, j] = False
        j = backtrack[i, j]

    mask = np.transpose(mask)
    base_img_size = Image.open(base_img)
    img_ = Image.open(img)
    img1 = img_.copy()
    img1 = img1.convert('RGBA')

    # img1 = img1.resize((img_.width,img_.height))
    new_img = Image.new(size=(base_img_size.width, base_img_size.height), mode='RGBA')
    back_img = new_img.copy()
    back_img.paste(img1, (back_img.width-img1.width, 0), img1)
    back_img.save('temp_.png')
    img1 = Image.open('temp_.png')

    for i in range(img_.width):
        for j in range(img_.height):
            if mask[i,j] == False:
                # new_img.putpixel((i,j),(255,0,0,255))
                for k in range(i,img_.width):
                    rgba = img1.getpixel((k,j))
                    new_img.putpixel((k,j),rgba)
    new_img.show()
    os.remove('temp_.png')
    return new_img

def main():
    out_left = left_column('img_left.png', 'img.png')
    out_right = right_column('img_right.png', 'img.png')
    imwrite('final_stitch_left.png', out_left)
    imwrite('final_stitch_right.png', out_right)
    img = Image.open('final_stitch_left.png')
    background = Image.open('stitch_right.png')
    background.paste(img, (0, 0), img)
    background.save('final_stitch_overlap.png','PNG')   
if __name__ == '__main__':
    main()
