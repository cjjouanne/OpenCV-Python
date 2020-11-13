import cv2
import numpy as np

img = cv2.imread('../Recursos/roi1.jpg')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

cv2.imshow('frame1',img)
cv2.imshow('frame2',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('convolution.jpg', dst)
