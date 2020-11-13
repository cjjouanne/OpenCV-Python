import cv2
import numpy as np
from matplotlib import pyplot as plt

# Adaptive Thresholding
img = cv2.imread('../Recursos/roi1.jpg',0)

img = cv2.medianBlur(img, 5)

ret, thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
thr2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
thr3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, thr1, thr2, thr3]

for i in range(0, 4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
