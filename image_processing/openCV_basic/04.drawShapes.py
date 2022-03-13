import cv2 as cv
import numpy as np

# create sketchbook 640 * 480
img = np.zeros((480, 640, 3), dtype = np.uint8)
# init all cells by color
# Blue, Green, Red
# img[:] = (255, 255, 255)
# print(img)

# init some cells by color (vertical, horizontal)
# img[100:200, 200:300] = (100, 255, 1)

# straight line

# 4 direction
# cv.LINE_4
# 8 direction
# cv.LINE_8
# anti-aliasing
# cv.LINE_AA
COLOR = (0, 255, 255)
THICKNESS = 3

cv.line(img, (50, 100), (400, 50), COLOR, THICKNESS, cv.LINE_4)
cv.line(img, (70, 120), (410, 60), COLOR, THICKNESS, cv.LINE_8)
cv.line(img, (90, 140), (420, 70), COLOR, THICKNESS, cv.LINE_AA)

# circle
c_center = (100, 100)
c_radius = 50
# empty circle
cv.circle(img, c_center, c_radius, COLOR, thickness=THICKNESS, lineType=cv.LINE_AA)
# filled circle
cv.circle(img, (200, 200), c_radius, COLOR, thickness=cv.FILLED, lineType=cv.LINE_AA)

# rectangle
cv.rectangle(img, (300, 300), (400, 400), COLOR, thickness=THICKNESS)
cv.rectangle(img, (400, 400), (500, 500), COLOR, thickness=cv.FILLED)

# polylines
poly_points = np.array([[260, 160], [500, 260], [400, 70]])
poly_points2 = np.array([[460, 160], [300, 260], [200, 70]])
poly_points3 = np.array([[460, 260], [300, 360], [200, 170]])

cv.polylines(img, [poly_points, poly_points2], True, COLOR, thickness=3)
cv.fillPoly(img, [poly_points3], COLOR)


cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
