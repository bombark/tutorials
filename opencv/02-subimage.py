import numpy as np
import cv2


img = cv2.imread('lion.jpg')

pequena_parte = img[0:200, 0:200]

cv2.imshow('nome da janela', pequena_parte)
cv2.waitKey(0)
