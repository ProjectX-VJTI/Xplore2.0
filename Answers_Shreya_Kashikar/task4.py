import numpy as np
import cv2 as cv
img=cv.imread('Task4.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print("Error: Image not found or unable to load.")
    exit()

ret, thresh = cv.threshold(img, 180, 255, cv.THRESH_BINARY)
contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
area_max=0
for cnt in contours:
    epsilon = 0.02 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)
    if len(approx) == 4:
        x, y, w, h = cv.boundingRect(approx)
        ratio = float(w) / h
        area = cv.contourArea(approx)
        if area<50000 and 0.95 <= ratio <= 1.05:
                area_max = max(area_max, area)
print(area_max)