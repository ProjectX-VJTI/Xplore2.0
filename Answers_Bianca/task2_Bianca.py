import cv2

img= cv2.imread('Task2.png')

morse=""

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        pixel=img[y,x]
        if (pixel == [255, 255, 255]).all():
            morse+="."
        elif (pixel == [0, 0, 0]).all():
            morse+="-"
        else:
            morse+=" "

print(morse)
            