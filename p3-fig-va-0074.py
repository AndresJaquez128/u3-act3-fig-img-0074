import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
#Jaquez Andres Nc 0074
print("Jaquez Andres NC 0074")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro")
mi_imagen = cv2.imread('GatoH.jpg')
plt.imshow(mi_imagen)
plt.title('Gato H y Jaquez Andres 0074')
plt.show()
print("+-+-+- Puntos en la imagen +-+-+-+")
plt.imshow(mi_imagen)
x = [100,100,300,176]
y = [100,400,500,152]
plt.scatter(x, y, s=20, c='red')
plt.show()
print("\n +-+-+- Cuadro en la imagen +-+-+-+-")
mi_imagen = cv2.imread("GatoH.jpg")
plt.imshow(mi_imagen)
#x = [100,100,500,500,100]
#y = [500,100,100,500,500]
x = [100,100,350,350,100]
y = [300,50,50,300,300]
plt.plot(x, y, c='blue')
plt.show()

print("+-+-+- Circulo verde en la imagen +-+-+-")
mi_imagen = cv2.imread('GatoH.jpg')
plt.imshow(mi_imagen)
N = 30 # lados del óligono
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc,yc) = (210,190)
r = 150 # radio
for i in range(N+1):
    t  = 2*np.pi/N*i
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)
plt.plot(x, y, c='green')
plt.show()