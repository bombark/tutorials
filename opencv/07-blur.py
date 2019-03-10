import numpy as np
import cv2

img = cv2.imread('lion.jpg')
borrada = cv2.blur(img,(5,5))

cv2.imshow('nome da janela', borrada)
cv2.waitKey(0)
