import cv2

img= cv2.imread('Task1.png')

no=0

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        pixel=img[y,x]
        if (pixel != [255, 255, 255]).all():
            print(pixel)
            print(f"Coordinates are: y-coordinate:{y} x-coordinate:{x}")
            no+=1

print(f"Number of non white pixels is: {no}" )