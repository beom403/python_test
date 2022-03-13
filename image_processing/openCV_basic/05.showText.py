import cv2 as cv
import numpy as np

# create sketchbook
img = np.zeros((720, 1280, 3), dtype = np.uint8)
# init all cells by color
# Blue, Green, Red
# img[:] = (255, 255, 255)
# print(img)

# init some cells by color (vertical, horizontal)
# img[100:200, 200:300] = (100, 255, 1)

# text fonts by open CV
# cv.FONT_HERSHEY_SIMPLEX
# cv.FONT_HERSHEY_COMPLEX
# cv.FONT_HERSHEY_PLAIN
# cv.FONT_HERSHEY_DUPLEX
# cv.FONT_HERSHEY_SCRIPT_SIMPLEX
# cv.FONT_HERSHEY_TRIPLEX
# cv.FONT_ITALIC

COLOR = (255, 255, 255)
THICKNESS = 1
SCALE = 1
x_pos = 100
y_pos = 50

def get_y_pos():
    global y_pos
    org = y_pos
    y_pos += 50
    return org

cv.putText(img, 'FONT_HERSHEY_SIMPLEX', (x_pos, get_y_pos()), cv.FONT_HERSHEY_SIMPLEX, SCALE, COLOR)
cv.putText(img, 'FONT_HERSHEY_COMPLEX', (x_pos, get_y_pos()), cv.FONT_HERSHEY_COMPLEX, SCALE, COLOR)
cv.putText(img, 'FONT_HERSHEY_PLAIN', (x_pos, get_y_pos()), cv.FONT_HERSHEY_PLAIN, SCALE, COLOR)
cv.putText(img, 'FONT_HERSHEY_DUPLEX', (x_pos, get_y_pos()), cv.FONT_HERSHEY_DUPLEX, SCALE, COLOR)
cv.putText(img, 'FONT_HERSHEY_SCRIPT_SIMPLEX', (x_pos, get_y_pos()), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR)
cv.putText(img, 'FONT_HERSHEY_TRIPLEX', (x_pos, get_y_pos()), cv.FONT_HERSHEY_TRIPLEX, SCALE, COLOR)
cv.putText(img, 'FONT_HERSHEY_TRIPLEX | FONT_ITALIC', (x_pos, get_y_pos()), cv.FONT_HERSHEY_TRIPLEX | cv.FONT_ITALIC, SCALE, COLOR)

# openCV doesn't support korean
cv.putText(img, "openCV doesn't support korean - 한글", (x_pos, get_y_pos()), cv.FONT_HERSHEY_SIMPLEX, SCALE, COLOR)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
