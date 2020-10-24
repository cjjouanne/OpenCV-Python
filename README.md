# OpenCV-Python:computer: :eyes:

Si quieres aprender a usar **OpenCV** con **Python** en español, creo que este es un buen lugar para empezar. Solo necesitas tener conocimientos básicos de 
Python 3, y tener instalado `Python 3`,`NumPy` y `OpenCV`.
###### Ejemplos y contenidos absolutamente basados en [este sitio](https://opencv-python-tutroals.readthedocs.io/en/latest/index.html)
## Contenidos
* [OpenCV](#OpenCv)
* [Empezemos](#Empezemos)
  * [Imágenes](#Imagenes)
  * [Videos](#Videos)
  * [Funciones de Dibujo](#Funciones-de-Dibujo)
  * [Utilizando el Mouse](#Utilizando-el-Mouse)
  * [Trackbars](#Trackbars)
* [Operaciones y Procesamiento de Imágenes](#Operaciones-y-Procesamiento-de-Imágenes)
  * [Operaciones Básicas](#Operaciones-Básicas)
  * [Operaciones Matemáticas](#Operaciones-Matemáticas)
  * [Procesos sobre Color](#Procesos-sobre-Color)

## OpenCV
OpenCV se inició en Intel en 1999 por Gary Bradsky y la primera versión salió en 2000. En este momento, OpenCV admite muchos algoritmos relacionados con la visión 
por computadora y el aprendizaje automático y se está expandiendo día a día. Actualmente, OpenCV admite una amplia variedad de lenguajes de programación como 
`C++`, `Python`, `Java`, etc. y está disponible en diferentes plataformas, incluidas **Windows**, **Linux**, **OS X**, **Android**, **iOS**, etc. Además, las 
interfaces basadas en `CUDA` y `OpenCL` también están en desarrollo activo para operaciones de alta velocidad de las la GPU.

**OpenCV-Python** es la API de Python de OpenCV. Combina las mejores cualidades de la API `OpenCV C++` y el lenguaje `Python`.

### Empezemos

## Imagenes

Para trabajar con imagenes en OpenCV, vamos a empezar con loc comandos más básicos: `cv2.imread()`,`cv2.imshow()`, y `cv2.imwrite()`. Con estos tres comandos 
podemos leer imagenes, mostrarlas en pantalla, y guardarlas como archivos.

### Leer una imagen
En primer lugar, tenemos la función `cv2.imread()`, la cual recibe dos argumentos, el primero es un string con el nombre de la imagen (ej: `"image.jpg"`) si la 
imagen se encuentra en el mismo directorio que nuestro archivo de Python, o bien el path hasta la imagen (`"dir/image.jpg"`). El segundo argumento pueden ser 
alguna de las siguientes opciones:
* `cv2.IMREAD_COLOR`: Carga la imagen a color (rellenando las transparencias por *defualt*)
* `cv2.IMREAD_GRAYSCALE`: Carga la imagen en escala de grises
* `cv2.IMREAD_UNCHANGED`: Carga la imagen como está definida (Incluyendo transaparencias o *canal alpha*)

Aunque estas opciones se pueden reemplazar por `1`,`0` o `-1` respectivamente, pero no es lo recomendable puesto que reduce la legibilidad del código. Entonces, 
tenemos que:
```python3
import numpy as np
import cv2

# Lee la imagen en escala de grises
img = cv2.image("image.jpg", cv2.IMREAD_GRAYSCALE)
```
### Mostrar una imagen
Ahora que ya tenemos la imagen cargada, queremos poder mostrarla en pantalla. Para eso, utilizamos el comando `cv2.imshow()`, el cual tambien recibe dos 
parámetros. El primero es un string con el nombre de la ventana, y el segundo es la imagen ya cargada con `cv2.imread()`. Siguiendo con el código anterior, nuestro 
ejemplo se vería de la siguiente forma:
```python3
# Abre la ventana con la imagen
cv2.imshow("frame1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
Donde `cv2.waitKey()` espera a que se presione alguna tecla (en esta caso puede ser cualquiera), y `cv2.destroyAllWindows()` cierra todas las ventanas abiertas por 
`OpenCV`.(Para destruir una ventana en específico usa el comando `cv2.destroyWindow("windowName")`)
### Guardar una imagen
Suponiendo que queramos guardar la imagen despues de trabajar con ella, podemos utilizar el comando `cv2.imwrite()`, cuyo primer argumento es un `string`
con el nombre con el cual queremos guardar nuestra imagen, y el segundo es la imagen que queremos guardar, lo cual nos lleva a terminar nuestro ejemplo de la 
siguiente forma:
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
OpenCV provee una interfaz muy simple a la hora de trabajar con videos desde Python, por lo que una implementación para capturar tu propio video, o trabajar con un 
archivo existente, no es muy compleja.

### Captura de Videos con tu cámara
Para capturar video desde una cámara, OpenCV provee la clase `cv2.VideoCapture()`, la cual recibe un parámetro único, ques es un `int` que indica a cuál cámara 
debe conectarse. La cámara por *default* del equipo (si es que tiene una) tiene asignado el número 0, y las siguientes opciones continuan con 1, 2, 3, etc. Los 
objetos pertenecientes a esta clase tienen el método `read()`, el cual no recibe parámteros, y retorna a lo que nos referiremos como `ret` y `frame`, donde `ret` 
es `True` si la cámara captó algo o `False` si no captó nada, y `frame` es la imagen capturada por la cámara.

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
## Funciones de Dibujo
OpenCv permite añadir en las imágenes o videos, figuras como círculos, rectangulos, lineas, y texto. Para esto, OpenCV provee una serie de funciones muy simples y 
bastante similares entre si.
### Lineas
Para añadir una linea tenemos la función `cv2.line()`, que recibe la imagen sobre la que dibuja, las coordenadas desde donde parte la linea, las cooredenadas donde 
la linea termina, el color de la linea en **BGR** y el grosor de la linea e pixeles.
```python3
import numpy as np
import cv2

# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)
```
### Círculos
En el caso de los círculos, tenemos `cv2.circle()`, que recibe la imagen sober la que se dibuja, las coordenadas del centro, el radio en pixeles, el color en **BGR**, y el grosor del borde en pixeles(en caso de ser `-1` se rellena el círculo con el color especificado).
```python3
# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260,260), 10, (255,0,0),-1)
```
### Texto
Para añadir texto, utilizamos `cv2.puText()`, que recibe como parámetros la imagen a la que se le añade el texto, un `string` con el texto que se quiere añadir, las coordenadas de la esquina superior izquierda del cuadro de texto, la tipografía del texto,la cual puede ser sacada de [aquí](https://docs.opencv.org/3.1.0/d0/de1/group__core.html#ga0f9314ea6e35f99bb23f29567fc16e11), la escala del texto, el color en **BGR**, y el grosor del texto.
```python3
# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "Example Text", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
```
### Otros
Se pueden añadir más figuras como [rectángulos](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html#drawing-rectangle), [polígonos](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html#drawing-polygon) y [elipses](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html#drawing-ellipse) pero las funciones son todas bastante 
similares, por lo que no vale la pena mencionarlas todas. Si necesitas alguna en específico, puedes consultar la documentación de OpneCV.
## Utilizando el Mouse
En muchos casos podemos necesitar acceder a información donde la manera más simple de hacerlo es con un **click** sobre lo que necesitamos. Para estos casos, OpenCV nos facilita la función `cv2.setMouseCallback()`, la cual recibe dos parámetros. El primero es un string con el nombre de la ventana sobre la cual definiremos el evento, y el segundo corresponde a la función que será llamada al hacer *click*. Se pueden agregar además parámetros extra para entregar más información a la función que se llama, pero por *default* `cv2.setMouseCallback()` entrega a su función un `event` de los cuales puedes aprender más [aquí](https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga927593befdddc7e7013602bca9b079b0), la coordenada `x` del click, la coordenada `y` del click, `flags` y 
`param`. Una implementación se vería así:
```python3
import cv2
import numpy as np

# Esta funcion agrega un punto en el lugar donde se hace click
def setPoint(event,x,y,flags,param):
  if event == cv2.EVENT_LBUTTONUP:
    cv2.circle(img, (x, y), 3, (255, 255, 255),-1)
    
# Crea una imagen negra
img = np.zeros((h,w,3)).astype(np.uint8) 

# Nombramos la ventana y asignamos el setMouseCallback
cv2.namedWindow('frame1')
cv2.setMouseCallback('frame1',setPoint)

while True:
  cv2.imshow('frame1',img)
  if cv2.waitKey(1) & 0xFF == 27:
    break
    
# Cerramos todas las ventanas
cv2.destroyAllWindows()
```
## Trackbars
Una herramienta que nos será de gran utilidad a la hora de manejar parámetros y variables mientras ejecutamos nuestro programa son los **trackbars** ya que OpenCV no cuenta con ningún otro tipo de botón. Para insertar un trackbar en nuestro código, debemos llamar a la funcion `cv2.createTrackbar()` la cual recibe cinco parámetros. El primero es un string con el nombre del trackbar (ej: `'Trackbar1'`), el segundo corresponde al nombre de la ventana en la cual se quieren insertar, el tercero y cuarto corresponden al valor mínimo y máximo respectivamente, y el quinto corresponde a la función que se llamará cada vez que este cambie de valor, función a la cual se le entrega en nuevo valor del trackbar. Además, para obtener el valor de un trackbar, podemos utilizar `cv2.getTrackbarPos()` que recibe el nombre y el nombre de la ventana en la cual se encuentra correspondientes a un trackbar, y retorna su valor actual.
```python3
import cv2
import numpy as np

def on_trackbar(val):
  print val:
  
# Crea a una imagen negra, y una ventana llamada 'frame'
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('frame')

# Crea tres trackbar en frame, llamados R,G,B, que van de 0 a 255 y llaman a on_trackbar()
cv2.createTrackbar('R','frame',0,255,on_trackbar)
cv2.createTrackbar('G','frame',0,255,on_trackbar)
cv2.createTrackbar('B','frame',0,255,on_trackbar)

while(True):
    cv2.imshow('frame',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Obtiene las posiciones de los trackbars
    r = cv2.getTrackbarPos('R','frame')
    g = cv2.getTrackbarPos('G','frame')
    b = cv2.getTrackbarPos('B','frame')

    img[:] = [b,g,r]

cv2.destroyAllWindows()
```
Este ejemplo nos permite manipular colores **RGB** en nuestra ventana e imprime el valor de la respectiva variable cada vez que esta cambia.
### Operaciones y Procesamiento de Imágenes
## Operaciones Básicas
...
## Operaciones Matemáticas
...
## Procesos sobre Color
...

