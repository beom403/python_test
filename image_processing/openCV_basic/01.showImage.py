# OpenCV (Open Computer Vision)
import cv2
import os

currentDir = os.path.dirname(os.path.realpath(__file__))
resourceDir = currentDir + "/../resource"
# read image file
ddong = cv2.imread(resourceDir + '/ddong.png')
print(ddong.shape) # height, width, channel
# ddong_color = cv2.imread(resourceDir + '/ddong.png', cv2.IMREAD_COLOR)
# ddong_gray = cv2.imread(resourceDir + '/ddong.png', cv2.IMREAD_GRAYSCALE)
# ddong_unchanged = cv2.imread(resourceDir + '/ddong.png', cv2.IMREAD_UNCHANGED)
# show image
cv2.imshow('img', ddong)
# cv2.imshow('img_color', ddong_color)
# cv2.imshow('img_gray', ddong_gray)
# cv2.imshow('img_unchanged', ddong_unchanged)
# wait key input (unit : ms)
cv2.waitKey(0)
# close all windows
cv2.destroyAllWindows()