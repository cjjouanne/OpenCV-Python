import cv2
import numpy as np

img = cv2.imread('../Recursos/imagen2.jpg')

# Seleccionamos el contenido de la region de interes
# 0:683 corresponde al rango en y, 160:775 corresponde al rango en x
roi = img[0:683, 160:775]

# Modificamos otra region, igualandola a nuestra roi
# 5:688 corresponde al rango en y, 740:1355 corresponde al rango en x
img[5:688, 740:1355] = roi

cv2.imshow("frame", img)
cv2.imshow("roi", roi)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()

cv2.imwrite('roi.jpg', roi)
cv2.imwrite('newImage.jpg', img)
