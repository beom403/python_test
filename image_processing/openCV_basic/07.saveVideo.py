import cv2 as cv
import os
import numpy

currentDir = os.path.dirname(os.path.realpath(__file__))
resourceDir = currentDir + '/../resource'
videoFile = resourceDir + '/cat_video.mp4'
# read image file
cap = cv.VideoCapture(videoFile)

# define codec
fourcc = cv.VideoWriter_fourcc(*'DIVX')
# print('DIVX')
# print(*'DIVX')
width = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = round(cap.get(cv.CAP_PROP_FPS))

out = cv.VideoWriter('output.mp4', fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('no more frame')
        break

    out.write(frame)
    cv.imshow('video', frame)

    if cv.waitKey(1) == ord('q'):
        print('quit by q button')
        break

out.release()
cap.release()
cv.destroyAllWindows()