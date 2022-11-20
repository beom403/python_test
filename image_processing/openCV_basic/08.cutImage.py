import cv2 as cv
import os
import numpy

currentDir = os.path.dirname(os.path.realpath(__file__))
resourceDir = currentDir + '/../resource'
imageFile = resourceDir + '/ddong.png'
# read image file
img = cv.imread(imageFile)
# org image : 900 x 900
crop = img[100:500, 200:400]
img[100:500, 400:600] = crop

cv.imshow('org', img)
cv.imshow('cropped', crop)

# wait key input (unit : ms)
cv.waitKey(0)
img.release()
crop.release()
cv.destroyAllWindows()