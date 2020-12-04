import sys
import numpy as np
from imageio import imread, imwrite
from scipy.ndimage.filters import convolve
from PIL import Image
# tqdm is not strictly necessary, but it gives us a pretty progress bar
# to visualize progress.
from tqdm import trange

def calc_energy(img):
    filter_du = np.array([
        [1.0, 2.0, 1.0],
        [0.0, 0.0, 0.0],
        [-1.0, -2.0, -1.0],
    ])
    # This converts it from a 2D filter to a 3D filter, replicating the same
    # filter for each channel: R, G, B
    filter_du = np.stack([filter_du] * 3, axis=2)

    filter_dv = np.array([
        [1.0, 0.0, -1.0],
        [2.0, 0.0, -2.0],
        [1.0, 0.0, -1.0],
    ])
    # This converts it from a 2D filter to a 3D filter, replicating the same
    # filter for each channel: R, G, B
    filter_dv = np.stack([filter_dv] * 3, axis=2)

    img = img.astype('float32')
    convolved = np.absolute(convolve(img, filter_du)) + np.absolute(convolve(img, filter_dv))

    # We sum the energies in the red, green, and blue channels
    energy_map = convolved.sum(axis=2)

    return energy_map

def minimum_seam(img):
    r, c, _ = img.shape
    energy_map = calc_energy(img)
    M = energy_map.copy()
    backtrack = np.zeros_like(M, dtype=np.int)
    for i in range(1, r):
        for j in range(0, c):
            # Handle the left edge of the image, to ensure we don't index -1
            if j == 0:
                idx = np.argmin(M[i - 1, j:j + 2])
                backtrack[i, j] = idx + j
                min_energy = M[i - 1, idx + j]
            else:
                idx = np.argmin(M[i - 1, j - 1:j + 2])
                backtrack[i, j] = idx + j - 1
                min_energy = M[i - 1, idx + j - 1]
            M[i, j] += min_energy
    # print('Mshape: ', M.shape, 'bshape: ', backtrack.shape, 'M: ', M, 'backtrack: ', backtrack)
    return M, backtrack

def left_column(img):
    img_read = imread(img)
    r, c, _ = img_read.shape
    M, backtrack = minimum_seam(img_read)
    mask = np.ones((r, c), dtype=np.bool)
    j = np.argmin(M[-1])
    for i in reversed(range(r)):
        mask[i, j] = False
        j = backtrack[i, j]

    mask = np.transpose(mask)
    img_ = Image.open(img)
    img1 = img_.copy()
    img1 = img1.resize((img_.width,img_.height))
    img1 = img1.convert('RGBA')
    new_img = Image.new(size=(img_.width, img_.height), mode='RGBA')
    for i in range(img_.width):
        for j in range(img_.height):
            if mask[i,j] == False:
                # new_img.putpixel((i,j),(255,0,0,255))
                for k in range(i):
                    rgba = img1.getpixel((k,j))
                    new_img.putpixel((k,j),rgba)
    new_img.show()
    return new_img


def right_column(img):
    img_read = imread(img)
    r, c, _ = img_read.shape
    M, backtrack = minimum_seam(img_read)
    mask = np.ones((r, c), dtype=np.bool)
    j = np.argmin(M[-1])
    for i in reversed(range(r)):
        mask[i, j] = False
        j = backtrack[i, j]

    mask = np.transpose(mask)
    img_ = Image.open(img)
    img1 = img_.copy()
    img1 = img1.resize((img_.width,img_.height))
    img1 = img1.convert('RGBA')
    new_img = Image.new(size=(img_.width, img_.height), mode='RGBA')
    for i in range(img_.width):
        for j in range(img_.height):
            if mask[i,j] == False:
                # new_img.putpixel((i,j),(255,0,0,255))
                for k in range(i,img_.width):
                    rgba = img1.getpixel((k,j))
                    new_img.putpixel((k,j),rgba)
    new_img.show()
    return new_img

def main():
    out_left = left_column('img.png')
    out_right = right_column('img.png')
    imwrite('stitch_left.png', out_left)
    imwrite('stitch_right.png', out_right)
    img = Image.open('stitch_left.png')
    background = Image.open('stitch_right.png')
    background.paste(img, (0, 0), img)
    background.save('stitch_overlap.png','PNG')   
if __name__ == '__main__':
    main()
