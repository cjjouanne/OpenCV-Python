import cv2
import numpy as np

img = cv2.imread('../Recursos/imagen1.jpg')

# Separa la imagen en los canales BGR
b,g,r = cv2.split(img)

# Modifica el canal R a 0
img[:,:,2] = 0

cv2.imshow("R", r)
# cv2.imshow("G", g)
# cv2.imshow("B", b)

cv2.imshow("BG", img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()

cv2.imwrite('channelsBG.jpg', img)
cv2.imwrite('channelR.jpg', r)
