# 4 - Utilizando el Mouse 🖱

En el archivo `mouseDrawing.py` se encuentra la funcion
```python3
def setPoint(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x, y), 10, (255,0,0),-1)
```

La cual dibuja un circulo azul de radio 10 en cada lugar donde se hace click. Un ejemplo de mi gran talento artístico es puede ver en esta imagen:

![](https://github.com/cjjouanne/OpenCV-Python/blob/main/Ejemplos/04_Mouse/mouseExample.jpg)
