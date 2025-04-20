import cv2
import numpy as np

image = cv2.imread('D:/OPEN CV/OPEN CV Workshop/OPENCV TASKS/Answers_Avanish/OPENCV/Answers_Avanish/Task6.png')  

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 150, 150])
upper_red1 = np.array([8, 255, 255])
lower_red2 = np.array([170, 150, 150])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

redmask = cv2.bitwise_or(mask1, mask2)

red = cv2.bitwise_and(image, image, mask=redmask)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_again = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

inverse_mask = cv2.bitwise_not(redmask)

mask  = inverse_mask

gray_background = cv2.bitwise_and(gray_again, gray_again, mask)

output = cv2.add(red, gray_background)

cv2.imshow('ONLY RED', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
