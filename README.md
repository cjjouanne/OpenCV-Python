# OpenCV-Python:computer: :eyes:
> Por [Carlos Jouanne G.](https://github.com/cjjouanne)

Si quieres aprender a usar **OpenCV** con **Python** en español, creo que este es un buen lugar para empezar con lo **basico**. Solo necesitas tener conocimientos básicos de Python 3, y tener instalado `Python 3`,`NumPy`, `matplotlib` y `OpenCV`. Ante cualquier duda puedes revisar la carpeta de [ejemplos](https://github.com/cjjouanne/OpenCV-Python/tree/main/Ejemplos), la cual contiene diferentes scripts testeados utilizando los contenidos de este artículo.

> Ejemplos y contenidos absolutamente basados en [este sitio](https://opencv-python-tutroals.readthedocs.io/en/latest/index.html)
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
  * [Thresholding](#Thresholding)
  * [Eliminación de Ruido](#Eliminacion-de-Ruido)

## OpenCV
OpenCV es una librería de visión por computadora, la se inició en Intel el año 1999 por Gary Bradsky, y su primera versión salió el año 2000. En este momento, OpenCV admite muchos algoritmos relacionados con la visión por computadora y el aprendizaje automático y se está expandiendo día a día. Actualmente, OpenCV admite una amplia variedad de lenguajes de programación como `C++`, `Python`, `Java`, etc. y está disponible en diferentes plataformas, incluidas **Windows**, **Linux**, **OS X**, **Android**, **iOS**, etc. Además, las interfaces basadas en `CUDA` y `OpenCL` también están en desarrollo activo para operaciones de alta velocidad de la GPU.

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
img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
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
img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

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
img = cv2.putText(img, "Example Text", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)
```
### Otros
Se pueden añadir más figuras como [rectángulos](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html#drawing-rectangle), [polígonos](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html#drawing-polygon) y [elipses](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_drawing_functions/py_drawing_functions.html#drawing-ellipse) pero las funciones son todas bastante
similares, por lo que no vale la pena mencionarlas todas. Si necesitas alguna en específico, puedes consultar la documentación de OpenCV.
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
Una herramienta que nos será de gran utilidad a la hora de manejar parámetros y variables mientras ejecutamos nuestro programa son los **trackbars** ya que OpenCV no cuenta con ningún otro tipo de botón. Para insertar un trackbar en nuestro código, debemos llamar a la funcion `cv2.createTrackbar()` la cual recibe cinco parámetros. El primero es un string con el nombre del trackbar (ej: `'Trackbar1'`), el segundo corresponde al nombre de la ventana en la cual se quieren insertar, el tercero y cuarto corresponden al valor mínimo y máximo respectivamente, y el quinto corresponde a la función que se llamará cada vez que este cambie de valor, función a la cual se le entrega en nuevo valor del trackbar. Además, para obtener el valor de un trackbar, podemos utilizar `cv2.getTrackbarPos()` que recibe el nombre del trackbar y el de la ventana en la cual este se encuentra, y retorna su valor actual.
```python3
import cv2
import numpy as np

def on_trackbar(val):
  print(val)

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
En esta sección no se ven contenidos demasiado relevantes, y yo personalmente jámas los he usado, pero creo que pueden serle de utilidad a alguien.
### Modificar Pixeles
Para modificar un pixel en una imagen podemos hacerlo de varias formas. La primera es hacerlos directamente:
```python3
import cv2
import numpy as np

img = cv2.imread('testImage.jpg')

# Podemos acceder al contenido de un pixel asi
px = img[100,100]

# Podemos acceder solo al canal B (BGR son 0,1,2 respectivamente) de ese pixel
blue = img[100,100,0]

# Podemos asignarle un valor BGR a un determinado pixel
img[100,100] = [255,255,255]
```
Pero una manera más eficiente para acceder y modificar al contenido de un pixel es a través de `NumPy`, ya que este módulo está optimizado para operaciones matriciales:
```python3
# Acceder al canal R con array.item()
red = img.item(10,10,2)

# O modificar el canal R, con array.itemset()
img.itemset((10,10,2),100)
```
### Acceder a las Propiedades de la Imagen
Es posible acceder a las propiedades de una imagen a través de comandos muy simples, y es posible que queramos usarlos:
```python3
# .shape nos retorna la cantidad de filas, columnas, y canales en un arreglo
shape = img.shape
# >> (400, 600, 3)

# .size nos retorna la cantidad de pixeles (la multiplicación de los parametros de shape)
size = img.size
# >> 720000

# Con .dtype obtenemos el tipo de datos de la imagen
dtype = img.dtype
# >> uint8
```
### ROI
Muchas veces vamos a querer modificar una región de la imagen en particular. Esto se usa en algoritmos de reconocimiento, como por ejemplo, para buscar los ojos, primero se buscan las caras, y luego en cada cara se buscan los ojos. Para hacer operaciones en la Región de Interés, o Region Of Interst (ROI), una vez que ya la tenemos identificada, lo hacemos a través del módulo `NumPy`
```python3
# Seleccionamos el contenido de la region de interes
roi = img[280:340, 330:390]

# Modificamos otra region, igualandola a nuestra roi
img[273:333, 100:160] = roi
```
### Separar y Unir canales de una Imagen
Una de las muchas posibilidades que nos ofrece OpenCV conciste es separar y unir los canales **BGR** de una imagen cualquiera. Esto nos permite trabajar con cada canal por separado, y despues volver a unirlos una sola imagen. Para esto usamos las funciones `cv2.split()` y `cv2.merge()`, las cuales separan y unen los canales respectivamente.
```python3
# Almacena en las variable b,g,r los respectivos canales de la imagen
b,g,r = cv2.split(img)

# Une los canales b,g,r en una sola imagen
img = cv2.merge((b,g,r))

# Otra forma de obtener alguncanl de una imagen es con Numpy
# Ej: obtener el canal B
b = img[:,:,0]

# Tambien podemos hacer operaciones sobre un canal
# Como transformar todo el canal R a 0
img[:,:,2] = 0
```
> Se puede agregar bordes a una imagen(_Padding_), pero no me pareció relevante incluirlo. De todas formas puedes aprender sobre esto [aquí](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#making-borders-for-images-padding)
## Operaciones Matemáticas

### cv2.add()
Uno de los comandos para _sumar_ dos imágenes es `cv2.add` el cual recibe dos imágenes como parámetros, las cuales deben ser del mismo tamaño y estar en el mismo formato. Un ejemplo de esto sería así:
```python3
img1 = cv2.imread('image1.png')
img2 = cv2.imread('image2.jpg')

# Esta operación es necesaria si las imágenes son de tamaños distintos
img1 = cv2.resize(img1, (480, 480))
img2 = cv2.resize(img2, (480, 480))

# Sumamos las imagenes
new_image = cv2.add(img1, img2)

cv2.imshow('new image',new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

### cv2.addWeighted()
Este comando tambien nos sirve para _sumar_ imágenes, pero nos permite asignarle diferentes pesos a cada imagen, lo que otorga una sensación de transparencia.
```python3
img1 = cv2.imread('image1.png')
img2 = cv2.imread('image2.jpg')

# Esta operación es necesaria si las imágenes son de tamaños distintos
img1 = cv2.resize(img1, (480, 480))
img2 = cv2.resize(img2, (480, 480))

# Sumamos las imagenes con peso 0.7 y .0.3
new_image = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('new image',new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### cv2.bitwise()
Hay cuatro tipos de operaciones **_bitwise_**: **AND**, **OR**, **NOT** y **XOR**. Las operaciones `cv2.bitwise_and()`,`cv2.bitwise_or()`,`cv2.bitwise_xor()` reciben 4 parametros. Los primeros dos corresponden a las imágenes sobre las cuales se realiza la operación. El tercer parámetro `dest` viene con un valor default que no vamos a modificar por ahora. El cuarto parámetro `mask` corresponde a la máscara que se aplica en la operación, a la cual le podemos asignaner el valor `None`. Es difícil describir que hace cad una, por lo que recomiendo jugar con el codigo un rato.
```python3
img1 = cv2.imread('image1.jpg')  
img2 = cv2.imread('image2.jpg')

bitwise_and = cv2.bitwise_and(img2, img1, mask = None)

cv2.imshow('bitwise and',bitwise_and)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
El el caso de `cv2.bitwise_not()`, esta operación recibe tres parámetros. El primero corresponde a la imagen sobre la cual se realiza la operación, el segundo parámetro, `dest`, viene con un valor default que no vamos a modificar por ahora. El tercer parámetro, `mask`, corresponde a la máscara que se aplica en la operación, a la cual le podemos asignaner el valor `None`.
```python3
img1 = cv2.imread('image1.jpg')

bitwise_not = cv2.bitwise_not(img1, mask = None)

cv2.imshow('bitwise not',bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
## Procesos sobre Color

### Transformaciones de Color
OpenCV nos permite transformar los colores de una imagen **_BGR_** a **_Escala de Grises_** o a **_HSV_**. Si bie existen muchas más transformaciones, y muchas otras maneras de hacerlo, la forma más comñun es a través de la función `cv2.cvtColor()` la cual recibe como primer parámetro una imagen en **_BGR_**, y como segungo parámetro un flag, el cual es `cv2.COLOR_BGR2GRAY` para transformar una imagen **_BGR_** a **_Escala deGrises_**, y es `cv2.COLOR_BGR2HSV` para tranformar una imagen de **_BGR_** a **_HSV_**.
```python3
img1 = cv2.imread('image1.jpg')

hsv_frame = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
grey_frame = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

cv2.imshow('HSV',hsv_frame)
cv2.imshow('GREY SCALE',grey_frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
Para obtener todos los flags de OpenCV, ejecuta el siguiente _script_:
```python3
import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags
```
### Seguimiento de objetos
Una técnica para hacer seguimiento de objetos muy utilizada es seguir el color del objeto, los cual es bastante facíl ahora que podemos trabajar la imagen es **_HSV_**. Para esto, capturamos cada cuadro, lo convertimos a _HSV_, aplicamos un filtro, y luego podemos hacer lo que uieramos con esa imagen.
```python3
import numpy as np
import cv2

nCam = 0
cap = cv2.VideoCapture(nCam)

if cap.isOpened():
	cap.open(nCam)

cv2.namedWindow('frame1')
cv2.moveWindow('frame1', 30, 100)

cv2.namedWindow('frame2')
cv2.moveWindow('frame2', 700, 100)

cv2.namedWindow('frame3')
cv2.moveWindow('frame3', 365, 150)

lower_color = np.array([155,80,80]) #
upper_color = np.array([175,255,255]) #

while(True):
	ret, frame = cap.read()

	# Convertimos la imagen de BGR a HSV
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Creamos una mascara que deja en BLANCO los pixeles en ese rango, y en NEGRO lo demas.
	mask_color = cv2.inRange(hsv_frame, lower_color, upper_color)

	# Unimos la máscara y la imagen original
	hsv_frame_mask = cv2.bitwise_and(frame,frame, mask= mask_color)

	cv2.imshow('frame1',frame)
	cv2.imshow('frame2',hsv_frame_mask)
	cv2.imshow('frame3',mask_color)

	if cv2.waitKey(1) & 0xFF == 27:
		break


cap.release()
cv2.destroyAllWindows()
```
## Thresholding

### Thresholding Simple
El **_thresholding_** es un grupo de algoritmos que nos permite separar un conjunto de elementos, y para esto se utiliza el método del umbral. En el caso de las imágenes, donde a los valores de un pixel que están por sobre el umbral se les asigna un nuevo valor (que puede ser Blanco), y a los pixeles cuyos valores se encuentran por debajo del umbral se les asigna un valor diferente (que puede ser negro). Para hacer esto en OpenCV, se utiliza la función `cv2.threshold()` la cual recibe cuatro argumentos, el primero es la imagen (preferiblemente en Escala de Grises), el segundo parámetro corresponde al valor del umbral, el cual debe ser superado, el tercer parámetro es el valor que se le asigna a aquellos pixeles que superan el umbral, y el cuarto es un flag que define el tipo de _threshold_ que se quiere realizar. Algunos tipos son:

* cv2.THRESH_BINARY
* cv2.THRESH_BINARY_INV
* cv2.THRESH_TRUNC
* cv2.THRESH_TOZERO
* cv2.THRESH_TOZREO_INV

> Puedes ver ejemplos de lo que hace cada tipo de threshold haciendo click [aquí](https://github.com/cjjouanne/OpenCV-Python/tree/main/Ejemplos/09_Thresholding).

Esta función retorna dos valores definidos como **_retval_** y la imagen obtenida del _thresholding_.

```python3
import cv2
import numpy as np

img = cv2.imread('image1.png',0)

ret,thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thr2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thr3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thr4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thr5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('BINARY',thr1)
cv2.imshow('BINARY_INV',thr2)
cv2.imshow('TRUNC',thr3)
cv2.imshow('TOZERO',thr4)
cv2.imshow('TOZERO_INV',thr5)


cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Adaptive Thresholding

La mayoría de las veces un umbral global para toda la imagen no nos dará los resultados que estamos buscando, por lo que existe `cv2.adaptiveThreshold()`. Esta función calcula el _threshold_ en areas más pequeñas de la imagen, lo cual nos da mejores resultados. Puede llevar los parámetros `cv2.ADAPTIVE_THRESH_MEAN_C` o `cv2.ADAPTIVE_THRESH_GAUSSIAN_C` los cuales proporcionan diferentes formas de obtener el _threshold_.
```python3
import cv2
import numpy as np

img = cv2.imread('image1.jpg',0)
img = cv2.medianBlur(img,5)

ret,thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

thr2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
thr3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow('BINARY',thr1)
cv2.imshow('ADAPTIVE_THRESH_MEAN',thr2)
cv2.imshow('ADAPTIVE_THRESH_GAUSSIAN',thr3)

cv2.waitKey(0)
cv2.destroyAllWindows()
```
> Esta función solo retorna un valor. Para ver más de esto haz click [aqui](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#adaptive-thresholding)

### Binarización de Otsu
Cuando utilizamos un umbral global con `cv2.threshold()` se suele poner un valor arbitrario, y para ver si es bueno, se utiliza el _ensayo y error_, sin embrago, cuando una imagen es **bimodal** (con dos picos en el histograma), se puede tomar como valor del umbral el valor medio entre estos dos picos, y esto es lo que hace el método de Otsu. Para utilizar la Binarización de Otsu en OpenCV, simplemente hay que pasarlo como parámetro extra en `cv2.threshold()`, asignándole `0` al valor del umbral. Si es que no se usa el umbral de Otsu, el parámetro _retval_ corresponde al umbral que se utilizó.
```python3
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Al usar 0 como segundo parametro se abre en escala de grises
img = cv2.imread('image1.png',0)

# Global thresholding
ret1, thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Thresholding con Binarización de Otsu
ret2, thr2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Thresholding con Binarización de Otsu tras filtro Gaussiano.
blur = cv2.GaussianBlur(img,(5,5),0)
ret3, thr3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Imprime todas las imagenes y sus histogramas
images = [img, 0, thr1,
          img, 0, thr2,
          blur, 0, thr3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]

for i in range(0, 3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()
```

## Eliminacion de Ruido

Al trabajar en ambientes de poca luz, o con cámaras de mala calidad, nos encontramos con mucho ruido en las imágenes. OpenCV nos ofrece diferentes maneras de _suavizar_ el ruido, difuminando un poco la imagen.
### Convolucion 2D
Al igual que cuando se trabaja con señales unidimensionales, con las imágenes se pueden utilizar **_filtros de paso bajo_** y **_filtros de paso alto_** (LPF y HPS por sus siglas en inglés). Un LPF ayuda a eliminar el ruido, y un HPF ayuda a encontrar los bordes. OpenCV ofrece la función `cv2.filter2D()` la cual nos permite convolucionar un _kernel_ con una imagen. En el siguiente ejemplo se utiliza un kernel de filtro de promedio de _5x5_:
```python3
import cv2
import numpy as np

img = cv2.imread('image1.png')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

cv2.imshow('frame1',img)
cv2.imshow('frame2',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Difuminado de Imagen
Hay varios tipos de difuminado de imagen:
#### Difuminación
En este ejemplo se utiliza un kernel de _5x5_
```python3
import cv2
import numpy as np

img = cv2.imread('image1.png')

blur = cv2.blur(img,(5,5))

cv2.imshow('frame1',img)
cv2.imshow('frame2',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
#### Filtro de Mediana
```python3
import cv2
import numpy as np

img = cv2.imread('image1.png')

median = cv2.medianBlur(img,5)

cv2.imshow('frame1',img)
cv2.imshow('frame2',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
#### Difuminación Gaussiana
Hay que especificar el alto y ancho del kernel, el cual debe se un entero impar positivo.
```python3
import cv2
import numpy as np

img = cv2.imread('image1.png')

blur = cv2.GaussianBlur(img,(5,5),0)

cv2.imshow('frame1',img)
cv2.imshow('frame2',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

#### Filtro Bilateral

Este filtro se caracteriza por su efectividad para eliminar el ruido y conservar los bordes, sin embargo, es considerablemente más lento, y por lo tanto, su uso tiene más limitaciones en comparación a los otros métodos.
```python3
import cv2
import numpy as np

img = cv2.imread('image1.png')

blur = cv2.bilateralFilter(img,9,75,75)

cv2.imshow('frame1',img)
cv2.imshow('frame2',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
