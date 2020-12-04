import cv2
import numpy as np
from numpy.matrixlib.defmatrix import matrix


def minmax(v, mat):
    if v > mat: v = 255
    if v < mat: v = 0
    return v

def dithering_gray_order(inMat, samplingF):
    h = inMat.shape[0]
    w = inMat.shape[1]
    
    for y in range(0, h-1, 2):
        for x in range(1, w-1, 2):
            inMat[y, x] = minmax(inMat[y, x+1]/255, 0.25)
            inMat[y+1, x] = minmax(inMat[y+1, x-1], 0.75)
            inMat[y, x+1] = minmax(inMat[y+1, x], 1.0)
            inMat[y+1, x+1] = minmax(inMat[y+1, x+1], 0.5)
    return inMat

inMat = cv2.imread('order.jpg')
grayMat = cv2.cvtColor(inMat, cv2.COLOR_BGR2GRAY)
outMat_gray = dithering_gray_order(grayMat.copy(), 1)
cv2.imwrite('out_order.jpg', outMat_gray)