# You have have been given an image with a white canvas containing few non white pixels. 
# The task is to use OpenCV to find the number of non white pixels and also return the positions of the pixels you have found.
import cv2 as cv 
import numpy as np
image = cv.imread('Task1.png')

def apply_gray(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return gray

_, thresh = cv.threshold(apply_gray(image), 254, 255, cv.THRESH_BINARY)

def count_nonw(image):
    nonw = []
    count = 0
    for y in range(thresh.shape[0]):
        for x in range(thresh.shape[1]):
            if thresh[y,x]!=255:
                count+=1
                nonw.append((x,y))
    print(f"Number of non white pixels are {count}")
    return nonw

nonw_pos = count_nonw(image)
print("Positions of non-white pixels:")
for pos in nonw_pos:
    print(pos)