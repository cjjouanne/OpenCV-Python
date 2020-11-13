import numpy as np
import cv2

# Instanciamos el video
cap = cv2.VideoCapture('../Recursos/video1.mp4')

# Capturamos el video cuadro por cuadro
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Video 1',frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break

# Cerramos el video y las Ventanas abiertas
cap.release()
cv2.destroyAllWindows()
