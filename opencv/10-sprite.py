import cv2
import numpy as np


tela = np.zeros((800,600,3), np.uint8)
frame = cv2.imread('lion.jpg')
tela[100:300,100:300] = frame[0:200,0:200]

cv2.imshow("janela",tela)
cv2.waitKey(0)
