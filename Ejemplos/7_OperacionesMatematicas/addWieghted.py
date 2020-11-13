import cv2
import numpy as np

img1 = cv2.imread('../Recursos/roi1.jpg')
img2 = cv2.imread('../Recursos/roi2.jpg')

shape1 = img1.shape
shape2 = img2.shape

print(f"shape Image 1: {shape1} \nshape Image 2: {shape2}")

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

new_image = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('addedImmage', new_image)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()

cv2.imwrite('addedWeightedImmage.jpg', new_image)
