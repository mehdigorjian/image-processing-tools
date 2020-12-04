import cv2
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

inMat = cv2.imread('floyd.jpg')
grayMat = cv2.cvtColor(inMat, cv2.COLOR_BGR2GRAY)
outMat_gray = dithering_gray(grayMat.copy(), 1)
cv2.imwrite('out_floyd.jpg', outMat_gray)