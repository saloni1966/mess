import numpy as no
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
# Capture frame-by-frame
    ret, frame = cap.read()
# if frame is read correctly ret is True

# Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
# Display the resulting frame
    cv.imshow('frame' , gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv. destroyAllwindows()