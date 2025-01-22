# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:43:44 2022

@author: Usuario
"""

import cv2
import numpy as np

bananos=cv2.imread('1. Procesamiento de imagenes/bananos.jpg')

# Escala de grises
gray=cv2.cvtColor(bananos,cv2.COLOR_BGRA2GRAY)

# Componentes Gx Gy, kernel tamaño 5
gx=cv2.Sobel(gray, cv2.CV_64F,1,0,5)
gy=cv2.Sobel(gray, cv2.CV_64F,0,1,5)

# Magnitud base. Suma de cuadrados
mag,_=cv2.cartToPolar(gx,gy)

# Magnitud de mag. Ejecutar en la consola
# np.max(mag)
# np.min(mag)

# Escalando valores en mag
mag=np.uint8(255*mag/np.max(mag))

cv2.imshow('',mag)