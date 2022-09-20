import numpy as np
import cv2 as cv

cap = cv.VideoCapture('videos/personas.mp4')
count = 0

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    count = count + 1
    print(count)
    if cv.waitKey(1) == ord('d'):
        break

cap.release()
cv.destroyAllWindows()