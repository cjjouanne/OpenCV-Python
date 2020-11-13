import cv2
import numpy as np

# Esta funcion agrega un punto en el lugar donde se hace click
def setPoint(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x, y), 10, (255,0,0),-1)

# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Nombramos la ventana y asignamos el setMouseCallback
cv2.namedWindow('frame1')
cv2.setMouseCallback('frame1',setPoint)

while True:
    cv2.imshow('frame1',img)
    if cv2.waitKey(1) & 0xFF == 27:
      break

# Cerramos todas las ventanas
cv2.destroyAllWindows()
cv2.imwrite('mouseExample.jpg', img)
