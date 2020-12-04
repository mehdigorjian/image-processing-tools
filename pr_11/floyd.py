import cv2, os
import numpy as np


def minmax(v):
    if v > 255: v = 255
    if v < 0: v = 0
    return v

def dithering_gray(inMat, samplingF):
    h = inMat.shape[0]
    w = inMat.shape[1]
    
    for y in range(0, h-1):
        for x in range(1, w-1):
            old_p = inMat[y, x]
            new_p = np.round(samplingF * old_p/255.0) * (255/samplingF)
            inMat[y, x] = new_p
            quant_error_p = old_p - new_p
            
            inMat[y, x+1] = minmax(inMat[y, x+1] + quant_error_p * 7 / 16.0)
            inMat[y+1, x-1] = minmax(inMat[y+1, x-1] + quant_error_p * 3 / 16.0)
            inMat[y+1, x] = minmax(inMat[y+1, x] + quant_error_p * 5 / 16.0)
            inMat[y+1, x+1] = minmax(inMat[y+1, x+1] + quant_error_p * 1 / 16.0)
    return inMat

images = [img for img in os.listdir('folderName') if img.endswith('.jpg') or img.endswith('.png')]
for im in images:
    im_path = os.path.join('folderName', im)

    inMat = cv2.imread(im_path)
    grayMat = cv2.cvtColor(inMat, cv2.COLOR_BGR2GRAY)
    outMat_gray = dithering_gray(grayMat.copy(), 1)
    im_name = os.path.join('IMG_floyd', im)
    cv2.imwrite(im_name, outMat_gray)