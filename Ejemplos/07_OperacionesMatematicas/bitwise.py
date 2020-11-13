import cv2
import numpy as np

img1 = cv2.imread('../Recursos/roi1.jpg')
img2 = cv2.imread('../Recursos/imagen3.jpg')

shape1 = img1.shape
shape2 = img2.shape

print(f"shape Image 1: {shape1} \nshape Image 2: {shape2}")

bitwise_and = cv2.bitwise_and(img2, img1, mask = None)
bitwise_or = cv2.bitwise_or(img2, img1, mask = None)
bitwise_xor = cv2.bitwise_xor(img2, img1, mask = None)
bitwise_not = cv2.bitwise_not(img2, mask = None)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('bitwise AND',bitwise_and)
cv2.imshow('bitwise OR',bitwise_or)
cv2.imshow('bitwise XOR',bitwise_xor)
cv2.imshow('bitwise NOT',bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('bitwiseAND.jpg',bitwise_and)
cv2.imwrite('bitwiseOR.jpg',bitwise_or)
cv2.imwrite('bitwiseXOR.jpg',bitwise_xor)
cv2.imwrite('bitwiseNOT.jpg',bitwise_not)
