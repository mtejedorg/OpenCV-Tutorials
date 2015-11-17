#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# David Pascual Hernandez, 2015

import numpy as np
import cv2

# Decidimos si queremos una ventana de tamaño variable
print('Resizable? y/n')
a = raw_input()
if a == "y":
	cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# Leemos la imagen (en blanco y negro) y la mostramos
img = cv2.imread('hendrix.jpg', 0)
cv2.imshow('image', img)

# Esperamos indefinidamente una tecla
k = cv2.waitKey(0)
if k == 27:         # esperamos ESC para cerrar la ventana
    cv2.destroyAllWindows()
elif k == ord('s'): # esperamos 's' para guardar la imagen
    cv2.imwrite('hendrixgray.png', img)
    cv2.destroyAllWindows()