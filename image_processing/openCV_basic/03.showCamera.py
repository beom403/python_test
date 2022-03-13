import cv2 as cv

# load camera 0
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv.imshow('camera', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()