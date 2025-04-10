import cv2
import numpy as np

img = cv2.imread("C:/Users/adity/OneDrive/Documents/GitHub/Xplore2.0/Answers_AdityaPrasad/Task1.png", 0)
# wasn't able to get image by just its name so used the full path

kernel = np.ones((5, 5), np.uint8)
# got the kernel from chatgpt

closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


cv2.imshow("Task 1", closed)
cv2.waitKey(0)
cv2.destroyAllWindows()