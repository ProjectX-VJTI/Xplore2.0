# Each pixel value corresponds to
#   - 255 -> (.)
#   - 0 -> (-)
#   - 120-220 -> separator (space)
# The code should return the correct morse code represented by the image.
import cv2 as cv
import numpy as np
image = cv.imread('Task2.png')

def apply_gray(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return gray

image = apply_gray(image)

def morse(img):
    morse = ""
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if img[y,x] == 255:
                morse+="."
            elif img[y,x] == 0:
                morse+="-"
            elif 120<=img[y,x] and img[y,x]<=220:
                morse+=" "
    return morse

print(morse(image))