import cv2 
import numpy as np

img = cv2.imread("duba.jpg")

hsv_img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

lower_orange= np.array([0, 164, 0])
upper_orange = np.array([179, 255, 255])

mask = cv2.inRange(hsv_img,lower_orange,upper_orange)

contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

centers = []

for contour in contours:
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        centers.append((cX, cY))
        
        cv2.circle(img, (cX, cY), 5, (255, 0, 0), -1)

for i in range(len(centers) - 1):
    cv2.line(img, centers[i], centers[i + 1], (255, 255, 255), 2)


cv2.imshow("img",img)

cv2.waitKey(0)