import numpy as np
import cv2

img = cv2.imread('lion.jpg')
for i in range(0,200):
  pequena_parte = img[i:i+200, i:i+200]
  cv2.imshow('nome da janela', pequena_parte)
  tecla = cv2.waitKey(20)
  if tecla == ord('q'):
    break
