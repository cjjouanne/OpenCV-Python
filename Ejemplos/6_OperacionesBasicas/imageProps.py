import cv2
import numpy as np

img = cv2.imread('../Recursos/imagen2.jpg')

# .shape nos retorna la cantidad de filas, columnas, y canales en un arreglo
shape = img.shape

# .size nos retorna la cantidad de pixeles (la multiplicación de los parametros de shape)
size = img.size

# Con .dtype obtenemos el tipo de datos de la imagen
dtype = img.dtype

print(f"shape: {shape} \nsize: {size}\ndtype: {dtype}")

cv2.imshow("frame", img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
