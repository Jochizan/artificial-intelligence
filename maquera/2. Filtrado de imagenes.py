# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 09:42:17 2022

@author: Usuario
"""
#Configurar como directorio de trabajo D:/Universidad/UNCP/Innovacion de TI/Practicas"
# Tools -> Preferences / Working Directory
# Tools -> Run / Working Directory

import cv2
import numpy as np

bananos=cv2.imread('C:/Users/jochi/.spyder-py3/bananos.jpg')

# Crear imagen original
cv2.imshow('original',bananos)

# Crear filtro 3x3. Creacion de matriz de 3 x 3 de 1s
kernel_3x3=np.ones((3,3))/(3*3)

output3x3=cv2.filter2D(bananos,-1,kernel_3x3)

cv2.imshow('Filtro 3x3', output3x3)

# Crear filtro 11x11. Creacion de matriz de 11 x 11 de 1s
kernel_11x11=np.ones((11,11))/(11*11)

output11x11=cv2.filter2D(bananos,-1,kernel_11x11)

cv2.imshow('Filtro 11x11', output11x11)

# Crear filtro 31x31. Creacion de matriz de 31 x 31 de 1s
kernel_31x31=np.ones((31,11))/(31*11)

output31x31=cv2.filter2D(bananos,-1,kernel_31x31)

cv2.imshow('Filtro 31x31', output31x31)