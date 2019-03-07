import numpy as np
import cv2


frame = cv2.imread('moedas.png')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow("Deteccao 1", gray)
cv2.waitKey(0)

###

gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
cv2.imshow("Deteccao 2", gray_blur)
cv2.waitKey(0)

###

thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=4)
cont_img = closing.copy()
cv2.imshow("Deteccao 3", closing)
cv2.waitKey(0)

####

contours, hierarchy = cv2.findContours(cont_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 2000 or area > 4000:
        continue
    if len(cnt) < 5:
        continue
    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(frame, ellipse, (0,255,0), 2)
cv2.imshow("Deteccao 4", frame)
cv2.waitKey(0)
