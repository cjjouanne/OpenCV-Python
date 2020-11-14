# 9 - Tresholding

## Treshold

El archivo `threshold.py` aplica 5 variaciones de threshold a una misma imagen. Luego las imagenes son impresas con `matplotlib` obteniendo el siguiente resultado:

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/09_Thresholding/output1.png)

## Adaptive Threshold

El archivo `adaptiveThreshold.py` aplica threshold adaptativo a una imagen. Utiliza dos tipos de threshold adaptativo: `cv2.ADAPTIVE_THRESH_MEAN_C` 
y `cv2.ADAPTIVE_THRESH_GAUSSIAN_C`. Luego las imagenes son impresas con `matplotlib` obteniendo el siguiente resultado:

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/09_Thresholding/output2.png)

## Binarización de Otsu

Por ultimo, El archivo `otsuFilter.py` aplica un filtro de Otsu a una imagen. Primero lo hace sobre una imagen con ruido, y luego sobre la imagen tras aplicarle
un filtro Gaussiano. Luego las imagenes son impresas con `matplotlib` obteniendo el siguiente resultado:

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/09_Thresholding/output3.png)
