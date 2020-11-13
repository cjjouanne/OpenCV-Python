import numpy as np
import cv2

print (f"using OpenCV v{cv2.__version__}")

# Lee la imagen en su formato original
img = cv2.imread("../Recursos/imagen1.jpg", cv2.IMREAD_UNCHANGED)
# Lee la imagen en escala de grises
img2 = cv2.imread("../Recursos/imagen1.jpg", cv2.IMREAD_GRAYSCALE)

# Abre las ventanas con las imagenes, y las cierra al presionar Esc
cv2.imshow("original", img)
cv2.imshow("grayscaleImage", img2)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()

# Guarda la imagen en escala de grises
cv2.imwrite('grayscaleImage.jpg', img2)
