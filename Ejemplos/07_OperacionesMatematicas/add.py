import cv2
import numpy as np

img1 = cv2.imread('../Recursos/imagen1.jpg')
img2 = cv2.imread('../Recursos/imagen2.jpg')

shape1 = img1.shape
shape2 = img2.shape

print(f"shape Image 1: {shape1} \nshape Image 2: {shape2}")

roi1 = img1[0:683, 160:775]
roi2 = img2[0:683, 160:775]

shape1 = roi1.shape
shape2 = roi2.shape

print(f"shape ROI 1: {shape1} \nshape ROI 2: {shape2}")

cv2.imshow("roi1", roi1)
cv2.imshow("roi2", roi2)

new_image = cv2.add(roi1, roi2)

cv2.imshow('addedImmage', new_image)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()

cv2.imwrite('../Recursos/roi1.jpg', roi1)
cv2.imwrite('../Recursos/roi2.jpg', roi2)
cv2.imwrite('addedImmage.jpg', new_image)
