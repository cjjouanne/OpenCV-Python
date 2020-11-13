import numpy as np
import cv2

# Instanciamos la camara
nCam = 0
cap = cv2.VideoCapture(nCam)

# Verificamos que la camara este inicializada o la inicializamos
if cap.isOpened():
	cap.open(nCam)

# Capturamos el video cuadro por cuadro
while(True):
	ret, frame = cap.read()
	cv2.imshow('frame1',frame)

	if cv2.waitKey(1) & 0xFF == 27:
		break

# Cerramos la camara y las Ventanas abiertas
cap.release()
cv2.destroyAllWindows()
