import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

#Jaquez Andres Nc 0074
print("Jaquez Andres NC 0074")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro")
mi_imagen = cv2.imread('imagen.jpg')
plt.imshow(mi_imagen)
plt.title('Gato H y Jaquez Andres 0074')
plt.show()
print("+-+-+- Puntos en la imagen +-+-+-+")
plt.imshow(mi_imagen)
x = [100,100,300,176]
y = [100,400,500,152]
plt.scatter(x, y, s=20, c='red')
plt.show()