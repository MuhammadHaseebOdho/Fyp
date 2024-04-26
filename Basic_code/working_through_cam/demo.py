import cv2 as cv
import numpy as np

cap = cv.VideoCapture(1)
while True:
    ret,frame = cap.read()

    cv.imshow('frame',frame)

    if cv.waitKey(0) & 0xFF == ord('q'):
          break

cap.release()

cv.destroyAllWindows()

