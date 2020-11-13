import cv2
import numpy as np
from matplotlib import pyplot as plt

# Thresholding
img = cv2.imread('../Recursos/roi1.jpg',0)

ret,thr1 = cv2.threshold(img,98,255,cv2.THRESH_BINARY)
ret,thr2 = cv2.threshold(img,98,255,cv2.THRESH_BINARY_INV)
ret,thr3 = cv2.threshold(img,98,255,cv2.THRESH_TRUNC)
ret,thr4 = cv2.threshold(img,98,255,cv2.THRESH_TOZERO)
ret,thr5 = cv2.threshold(img,98,255,cv2.THRESH_TOZERO_INV)


titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thr1, thr2, thr3, thr4, thr5]

for i in range(0, 6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
