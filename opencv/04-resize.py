import numpy as np
import cv2


img = cv2.imread('lion.jpg')
small1 = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
small2 = cv2.resize(image, (100, 50))

cv2.imshow('nome da janela', small1)
cv2.waitKey(0)
