# OpenCV-Python:computer: :eyes:

Si quieres aprender a usar **OpenCV** con **Python** en español, creo que este es un buen lugar lara empezar. Solo necesitas tener conocimientos básicos de Python3, y tener instalado `Python 3`,`NumPy` y `OpenCV`.
###### Ejemplos y contenidos absolutamente basados en [este sitio](https://opencv-python-tutroals.readthedocs.io/en/latest/index.html)
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

# Lee la imagen en escala de grises
img = cv2.image("image.jpg", cv2.IMREAD_GRAYSCALE)
```
### Mostrar una imagen
Ahora que ya tenemos la imagen cargada, queremos poder mostrarla en pantalla. Para eso, utilizamos el comando `cv2.imshow()`, el cual tambien recibe dos parámetros. El primero es un string con el nombre de la ventana, y el segundo es la imagen ya cargada con `cv2.imread()`. Siguiendo con el código anterior, nuestro ejemplo se vería de la siguiente forma:
```python3
# Abre la ventana con la imagen
cv2.imshow("frame1", img)
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

# Lee la imagen en escala de grises
img = cv2.image("image.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen, y la cierra al presionar una tecla
cv2.imshow("frame1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guarda la imagen en escala de grises
cv2.imwrite('grayscaleImage.jpg', img)
```
###### Si quieres leer más sobre esto, haz click [aquí](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html)

## Videos
OpenCV provee una interfaz muy simple a la hora de trabajar con videos desde Python, por lo que una implementación para capturar tu propio video, o trabajar con un archivo existente, no es muy compleja.

### Captura de Videos con tu cámara
Para capturar video desde una cámara, OpenCV provee la clase `cv2.VideoCapture()`, la cual recibe un parámetro único, ques es un `int` que indica a cuál cámara debe conectarse. La cámara por *default* del equipo (si es que tiene una) tiene asignado el número 0, y las siguientes opciones continuan con 1, 2, 3, etc. Los objetos pertenecientes a esta clase tienen el método `read()`, el cual no recibe parámteros, y retorna a lo que nos referiremos como `ret` y `frame`, donde `ret` es `True` si la cámara captó algo o `False` si no captó nada, y `frame` es la imagen capturada por la cámara.

Con esto, y lo visto en la [sección anterior](#Imagenes), ya podemos capturar nuestro propio video:
```python3
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
```
### Abre un video de tu librería
Para abrir un video guardado en la librería, el codigo es bastante similar. Solo debes cambiar el parámetro que recibe `cv2.VideoCature()`, entregando el nombre 
del archivo, o el path que lleva a este.
```python3
import numpy as np
import cv2

# Instanciamos el video
cap = cv2.VideoCapture('videoExample.mp4')

# Verificamos que el video este inicializado o lo inicializamos
if cap.isOpened():
	cap.open(nCam)

# Capturamos el video cuadro por cuadro
while(cap.isOpened()):
	ret, frame = cap.read()
	cv2.imshow('frame1',frame)
	
	if cv2.waitKey(1) & 0xFF == 27:
		break

# Cerramos el video y las Ventanas abiertas
cap.release()
cv2.destroyAllWindows()
```
### Guarda los videos
A difrencia de la captura de imagenes, la implementación de la captura de video puede ser un poco más compleja. En primer lugar, es necesario instanciar un objeto
`cv2.VideoWriter()` el cual recibe cuatro parámetros. El primero es el nombre del archivo que se creará (ej: `prueba.mp4`). El segundo parámetro corresponde al 
codec de video en formato `FourCC`(Four Character Code), para lo cual podemos instanciar un objeto de la clase `cv2.VideoWriter_fourcc()` que recibe el FourCC en 
formato string(Los codecs disponibles varían según la plataforma, ej `*'MJPG'` para .mp4). En tercer parámetro es la cantidad de cuadros por segundo o **fps** por 
sus siglas en inglés. Luego se agrega el tamaño de los cuadros, y por último, como parametro opcional, esta el flag **isColor** el cual indica si el video es 
color(`True`) o en escala de grises(`False`). Una implementación del código se vería así:
```python3
import numpy as np
import cv2

# Instanciamos la camara
nCam = 0
cap = cv2.VideoCapture(nCam)

# Verificamos que la camara este inicializada o la inicializamos
if cap.isOpened():
	cap.open(nCam)

# Definimos el codec y creamos el VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('newVideo.mp4',fourcc, 20.0, (640,480), True)

while(True):
    ret, frame = cap.read()
    if ret==True:
        # guardamos cada cuadro
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break

# Terminamos todas las instancias y objetos
cap.release()
out.release()
cv2.destroyAllWindows()
```
