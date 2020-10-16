# OpenCV-Python:computer: :eyes:

Si quieres aprender a usar **OpenCV** con **Python** en español, creo que este es un buen lugar lara empezar. Solo necesitas tener conocimientos básicos de Python3, y tener instalado `Python 3`,`NumPy` y `OpenCV`.

## Contenidos
* [OpenCV](#OpenCv)
* [Empezemos](#Empezemos)
  * [Imágenes](#Imagenes)
  * [Videos](#Videos)

## OpenCV

OpenCV se inició en Intel en 1999 por Gary Bradsky y la primera versión salió en 2000. En este momento, OpenCV admite muchos algoritmos relacionados con la visión por computadora y el aprendizaje automático y se está expandiendo día a día. Actualmente, OpenCV admite una amplia variedad de lenguajes de programación como `C++`, `Python`, `Java`, etc. y está disponible en diferentes plataformas, incluidas **Windows**, **Linux**, **OS X**, **Android**, **iOS**, etc. Además, las interfaces basadas en `CUDA` y `OpenCL` también están en desarrollo activo para operaciones de alta velocidad de las la GPU.

**OpenCV-Python** es la API de Python de OpenCV. Combina las mejores cualidades de la API `OpenCV C++` y el lenguaje `Python`.

### Empezemos

## Imagenes

Para trabajar con imagenes en OpenCV, vamos a empezar con loc comandos más básicos: `cv2.imread()`,`cv2.imshow()`, y `cv2.imwrite()`. Con estos tres comandos podemos leer imagenes, mostrarlas en pantalla, y guardarlas como archivos.

### Leer una imagen
En primer lugar, tenemos la función `cv2.imread()`, la cual recibe dos argumentos, el primero es un string con el nombre de la imagen (ej: `"image.jpg"`) si la imagen se encuentra en el mismo directorio que nuestro archivo de Python, o bien el path hasta la imagen (`"dir/image.jpg"`). El segundo argumento pueden ser alguna de las siguientes opciones:
* `cv2.IMREAD_COLOR`: Carga la imagen a color (rellenando las transparencias por *defualt*)
* `cv2.IMREAD_GRAYSCALE`: Carga la imagen en escala de grises
* `cv2.IMREAD_UNCHANGED`: Carga la imagen como está definida (Incluyendo transaparencias o *canal alpha*)

Aunque estas opciones se pueden reemplazar por `1`,`0` o `-1` respectivamente, pero no es lo recomendable puesto que reduce la legibilidad del código. Entonces, tenemos que:
```python3
import numpy as np
import cv2

img = cv2.image("image.jpg", cv2.IMREAD_GRAYSCALE) # Lee la imagen en escala de grises
```
### Mostrar una imagen
Ahora que ya tenemos la imagen cargada, queremos poder mostrarla en pantalla. Para eso, utilizamos el comando `cv2.imshow()`, el cual tambien recibe dos parámetros. El primero es un string con el nombre de la ventana, y el segundo es la imagen ya cargada con `cv2.imread()`. Siguiendo con el código anterior, nuestro ejemplo se vería de la siguiente forma:
```python3
cv2.imshow("frame1", img) # Abre la ventana con la imagen
cv2.waitKey(0)
cv2.destroyAllWindows()
```
Donde `cv2.waitKey()` espera a que se presione alguna tecla (en esta caso puede ser cualquiera), y `cv2.destroyAllWindows()` cierra todas las ventanas abiertas por `OpenCV`.(Para destruir una ventana en específico usa el comando `cv2.destroyWindow("windowName")`)
### Guardar una imagen
Suponiendo que queramos guardar la imagen despues de trabajar con ella, podemos utilizar el comando `cv2.imwrite()`, cuyo primer argumento es un `string`
con el nombre con el cual queremos guardar nuestra imagen, y el segundo es la imagen que queremos guardar, lo cual nos lleva a terminar nuestro ejemplo de la siguiente forma:
```python3
cv2.imwrite('grayscaleImage.jpg', img)
```
Si juntamos todo lo anterior, tenemos lo siguiente:

```python3
import numpy as np
import cv2

img = cv2.image("image.jpg", cv2.IMREAD_GRAYSCALE) # Lee la imagen en escala de grises

cv2.imshow("frame1", img) # Abre la ventana con la imagen, y la cierra al presionar una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('grayscaleImage.jpg', img) # Guarda la imagen en escala de grises
```
###### Si quieres leer más sobre esto, haz click [aquí](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html)

## Videos
