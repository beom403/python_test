import cv2 as cv
import numpy as np

# create sketchbook
img = np.zeros((720, 1280, 3), dtype = np.uint8)

# init some cells by color (vertical, horizontal)
# img[100:200, 200:300] = (100, 255, 1)


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

# openCV doesn't support korean
cv.putText(img, "openCV doesn't support korean - 한글", (x_pos, get_y_pos()), cv.FONT_HERSHEY_SIMPLEX, SCALE, COLOR)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
