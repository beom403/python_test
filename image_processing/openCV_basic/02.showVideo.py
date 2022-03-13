import cv2 as cv
import os
import numpy

currentDir = os.path.dirname(os.path.realpath(__file__))
resourceDir = currentDir + '/../resource'
videoFile = resourceDir + '/cat_video.mp4'
# read image file
cap = cv.VideoCapture(videoFile)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('no more frame')
        break

    cv.imshow('video', frame)

    if cv.waitKey(1) == ord('q'):
        print('quit by q button')
        break

cap.release()
cv.destroyAllWindows()