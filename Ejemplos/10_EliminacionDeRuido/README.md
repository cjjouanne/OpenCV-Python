# 10 - Eliminacio de Ruido

## Convolucion 2D

Aplica un filtro de convolucion utilizando `cv2.filter2D` para convolicionar una imagen con un kernel. Se obtiene una imagen con menos ruido, pero a su vez es más
borrosa:

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/10_EliminacionDeRuido/convolution.jpg)

## Filtros

El archivo `filters.py` aplica cuatro tipos de filtro sobre una imagen, obtiendo diferentes resultados. Los filtros aplicados son `cv2.blur()`, `cv2.medianBlur()`,
`cv2.GaussianBlur()` y `cv2.bilateralFilter()`.

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/10_EliminacionDeRuido/filters.png)
