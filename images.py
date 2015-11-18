#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# David Pascual Hernandez, 2015

import numpy as np
import cv2
import sys

if len(sys.argv) != 2:
    print "usage : python images.py <image_file>"
    sys.exit(1)
else:
    # Leemos la imagen (en escala de grises)
    img = cv2.imread(sys.argv[1], 0) # tambien ('img', cv2.IMREAD_GRAYSCALE)
    if img == None:
        print sys.argv[1], "not found"
        sys.exit(1)
		
# Decidimos si queremos una ventana de tamaño variable
print "Resizable -> y\r\nAny other key to continue the execution"
a = raw_input()
if a == "y":
	cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# Mostramos la imagen
cv2.imshow('image', img)

# Esperamos indefinidamente una tecla
while(True):
	k = cv2.waitKey(0)
	if k == 27:         # esperamos ESC para cerrar la ventana
		cv2.destroyAllWindows()
		break
	elif k == ord('s'): # esperamos 's' para guardar la imagen
		cv2.imwrite('hendrixgray.png', img)
		cv2.destroyAllWindows()
		break