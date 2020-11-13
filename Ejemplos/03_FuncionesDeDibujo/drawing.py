import numpy as np
import cv2

# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)

# Dibuja un circulo azul de radio 100px al centro de la imagen
img = cv2.circle(img, (260,260), 100, (255,0,0),-1)

# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "Example OpenCV", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)

cv2.imshow("dibujo", img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()

# Guarda el dibujo
cv2.imwrite('dibujo.jpg', img)
