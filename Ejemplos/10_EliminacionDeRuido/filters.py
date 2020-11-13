import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../Recursos/roi1.jpg', 0)

blur = cv2.blur(img,(15,15))
median = cv2.medianBlur(img,15)
gaussian = cv2.GaussianBlur(img,(15,15),0)
bilateral = cv2.bilateralFilter(img,9,75,75)

titles = ['Blur', 'Median Blur',
            'GaussianBlur', 'Bilateral Blur']
images = [blur, median, gaussian, bilateral]

for i in range(0, 4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
