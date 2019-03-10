import numpy as np
import cv2


img = cv2.imread('lion.jpg')


#centro = img.shape
#print(centro)

rotacao = cv2.getRotationMatrix2D( (300,300), 120, 1.0)
rotacionado = cv2.warpAffine(img, rotacao, (600,600))


cv2.imshow("Rotacionado 120 graus", rotacionado)
cv2.waitKey(0)
