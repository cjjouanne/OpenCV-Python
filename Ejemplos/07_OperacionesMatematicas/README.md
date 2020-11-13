# 7 - Operaciones Matematicas

## add
El archivo `add.py` contiene una implementacion simple de la función `cv2.add`, la cual necesita que ambas imagenes sean del mismo tamaño. para eso, seleccionamos
una región de cada imagen, obteniendo imagenes del mismo porte.
```python3
roi1 = img1[0:683, 160:775]
roi2 = img2[0:683, 160:775]

shape1 = roi1.shape
shape2 = roi2.shape

print(f"shape ROI 1: {shape1} \nshape ROI 2: {shape2}")
```
Con este _script_ deberiamos obtener que ambas imagenes tienen las mismas propiedades.
Al utilizar `cv2.add()` obtenemos este resultado:

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/07_OperacionesMatematicas/addedImmage.jpg)

## addWeighted

Este archivo funciona parecido al anterior, con la diferencia que en este se importan imagenes del mismo tamaño, por lo que no es necesario seleccionar 
alguna región. Al aplicar los pesos **0.7** y **0.3** a cada imagen, se obtiene el siguiente resultado:

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/07_OperacionesMatematicas/addedWeightedImmage.jpg)

## bitwise AND, OR, XOR, & NOT

En este _script_ se aplican las diferentes operaciones `bitwise` a dos imagenes del mismo tamaño. se obtienen los siguienes resultados:

### AND
![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/07_OperacionesMatematicas/bitwiseAND.jpg)

### OR
![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/07_OperacionesMatematicas/bitwiseOR.jpg)

### XOR
![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/07_OperacionesMatematicas/bitwiseXOR.jpg)

### NOT
![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/07_OperacionesMatematicas/bitwiseNOT.jpg)
