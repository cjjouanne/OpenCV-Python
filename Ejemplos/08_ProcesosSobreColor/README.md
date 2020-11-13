# Procesos sobre Color

El archivo `seguimmientoObjetos.py` permite segmentar el color en el que se hace click, lo cual permite seguir a un objeto de un color particular. Para esto,
el _script_ utiliza

```python3
# In Range crea la máscara de color dejando solo los objetos que se encuentran en el rango
mask_color = cv2.inRange(hsv_frame, lower_color, upper_color)

# Unimos la máscara y la imagen original con bitwise AND
hsv_frame_mask = cv2.bitwise_and(frame,frame, mask= mask_color)
```
