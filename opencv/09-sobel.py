import cv2
import numpy as np


img = cv2.imread('lion.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)


laplacian = np.uint8( np.absolute(laplacian) )
cv2.imshow('janela',laplacian)
cv2.waitKey(0)

sobelx = np.uint8( np.absolute(sobelx) )
cv2.imshow('janela',sobelx)
cv2.waitKey(0)

sobely = np.uint8( np.absolute(sobely) )
cv2.imshow('janela',sobely)
cv2.waitKey(0)
