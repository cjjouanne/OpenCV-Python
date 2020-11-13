import numpy as np
import cv2

def _mouseEvent(event, x, y, flags, param):
	global lower_color, upper_color
	if event == cv2.EVENT_LBUTTONDOWN:
		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		color_hsv = hsv_frame[y,x]
		lower_color = np.array([color_hsv[0]-10,color_hsv[1]-35,color_hsv[2]-35])
		upper_color = np.array([color_hsv[0]+10,color_hsv[1]+35,color_hsv[2]+35])
		print("aaaaa")

nCam = 0
cap = cv2.VideoCapture(nCam)

if cap.isOpened():
	cap.open(nCam)

cv2.namedWindow('frame1')
cv2.moveWindow('frame1', 30, 100)

lower_color = np.array([0,0,0]) #
upper_color = np.array([255,255,255]) #

cv2.setMouseCallback('frame1',_mouseEvent)

while(True):
	ret, frame = cap.read()
	# Convertimos la imagen de BGR a HSV
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# Creamos una mascara que deja en BLANCO los pixeles en ese rango, y en NEGRO lo demas.
	mask_color = cv2.inRange(hsv_frame, lower_color, upper_color)
	# Unimos la máscara y la imagen original
	hsv_frame_mask = cv2.bitwise_and(frame,frame, mask= mask_color)

	cv2.imshow('frame1',hsv_frame_mask)

	if cv2.waitKey(1) & 0xFF == 27:
		break


cap.release()
cv2.destroyAllWindows()
