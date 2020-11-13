import cv2
import numpy as np
from matplotlib import pyplot as plt

# Binarizacion de Otsu
img = cv2.imread('../Recursos/roi1.jpg',0)
# Con filtro Gaussiano:
blur = cv2.GaussianBlur(img,(5,5),0)

# Binarizacion Global
ret1,thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Binarizacion de Otsu
ret2,thr2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Binarizacion de Otsu con filtro Gaussiano
ret3,thr3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, thr1,
          img, 0, thr2,
          blur, 0, thr3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(0, 3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()
