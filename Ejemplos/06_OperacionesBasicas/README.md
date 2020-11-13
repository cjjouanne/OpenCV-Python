# 6 - Operaciones Basicas

## Image Props

El archivo `imageProps.py` obtiene e imprime por consola diferentes parametros de la imagen que recibe

```
shape: (688, 1600, 3) 
size: 3302400
dtype: uint8
```

y despues muestra una visualización simple de la imagen con `cv2.imshow()`

## Image ROI

El archivo `imageROI.py` selecciona una region de interés de esta imagen

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/Recursos/imagen2.jpg)

la cual resulta en esto.

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/06_OperacionesBasicas/roi.jpg)

y modifica la misma imagen, agregando la region de interés en otra sección de la misma.

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/06_OperacionesBasicas/newImage.jpg)

> Está claro que una Jennifer Lawrence no es suficiente para este mundo, por eso pusimos dos.

## Channels

En el archivo `channels.py` se separan los canales de la imagen, y se muestra el canal **R** el cual al ser un solo canal, se lee como imagen en escala de grises.

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/06_OperacionesBasicas/channelR.jpg)

Despues, se modifica la imagen, y al canal **R** se le asigna el valor `0` mostrando esta imagen, la cual contiene solo los canales **B** y **G**

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/06_OperacionesBasicas/channelsBG.jpg)
