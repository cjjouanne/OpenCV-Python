# 3 - Funciones de Dibujo 🎨

El _script_ `drawing.py` crea una imagen cuadrada de _512x512_ pixeles
```python3
img = np.zeros((512,512,3), np.uint8)
```
Le agrega una diagonal blanca de 3 pixeles de ancho desde una esquina a la otra
```python3
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)
```
Dibuja un circulo azul de radio de 100 pixeles al centro de la imagen
```python3
img = cv2.circle(img, (260,260), 100, (255,0,0),-1)
```
Añade a la imagen el texto "Example OpenCV" en color blanco
```python3
img = cv2.putText(img, "Example OpenCV", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)
```
y despues lo muestra en pantalla, obteniendo el siguiente resultado

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/03_FuncionesDeDibujo/dibujo.jpg)
