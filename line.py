import cv2
import numpy as np

img = np.ones ((600,800,3), dtype=np.uint8)*255
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.line(img, (0,0), (800,600), (0,0),10)
cv2.imshow("image",img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.line(img, (0,599), (799,0), (255,0,0), 10)
cv2.imshow("image",img)
cv2.waitKey()
cv2.waitKey()

cv2.destroyAllWindows()