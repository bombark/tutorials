

import numpy as np
import cv2

img = cv2.imread('lena.png')
borrada = cv2.medianBlur(img,5)

cv2.imshow('nome da janela', borrada)
cv2.waitKey(0)
