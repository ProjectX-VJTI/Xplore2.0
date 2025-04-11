import cv2

img = cv2.imread('Task2.png')


for i in range(img.shape[1]):
    if img[0][i][0] == 255:
        print(".", end="")
    elif img[0][i][0] == 0:
        print("-", end="")
    else: 
        print(" ", end="")
