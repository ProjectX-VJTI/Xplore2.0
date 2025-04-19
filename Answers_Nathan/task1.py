import cv2 as cv
import numpy as np

img = cv.imread('H:\Engineering 2024\Coding\ProjectX\Answers_Nathan\OpenCV-Clone\Answers_Nathan\Task1.png')

def apply_grayscale(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return gray 

img2 = apply_grayscale(img)

count = 0

for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        if img2[i][j] != 255:
            count += 1
            print(f"Pixel {count} at (", i, ",", j, ") is not white.")

print("The number of non-white pixels in the image is: ", count)