import cv2 as cv
import numpy as np
import os

# create sketchbook
img = np.zeros((720, 1280, 3), dtype = np.uint8)

currentDir = os.path.dirname(os.path.realpath(__file__))
resourceDir = currentDir + "/../resource"
# read image file
ddong = cv.imread(resourceDir + '/ddong.png')
print(ddong.shape) # height, width, channel
ddong_color = cv.imread(resourceDir + '/ddong.png', cv.IMREAD_COLOR)
ddong_gray = cv.imread(resourceDir + '/ddong.png', cv.IMREAD_GRAYSCALE)
ddong_unchanged = cv.imread(resourceDir + '/ddong.png', cv.IMREAD_UNCHANGED)
# save image
result = cv.imwrite('img_save.jpg', ddong_unchanged)
print(result)
