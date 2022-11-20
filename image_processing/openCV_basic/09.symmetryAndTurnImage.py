import cv2 as cv
import os
import numpy

currentDir = os.path.dirname(os.path.realpath(__file__))
resourceDir = currentDir + '/../resource'
imageFile = resourceDir + '/ddong.png'
# read image file
img = cv.imread(imageFile)
# org image : 900 x 900
# flip_horizontal = cv.flip(img, 1)
# flip_vertical = cv.flip(img, 0)
# flip_both = cv.flip(img, -1)
rotate_90 = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

cv.imshow('org', img)
# cv.imshow('flipped_v', flip_vertical)
# cv.imshow('flipped_h', flip_horizontal)
# cv.imshow('flipped_b', flip_both)
cv.imshow('rotate_90', rotate_90)

# wait key input (unit : ms)
cv.waitKey(0)
img.release()
crop.release()
cv.destroyAllWindows()