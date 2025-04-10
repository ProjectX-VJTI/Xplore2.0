import cv2

img = cv2.imread("C:/Users/adity/OneDrive/Desktop/Task1.png")
count = 0 

size = img.shape
height = size[0]
width = size[1]

for i in range(height):
    for j in range(width):
        if img[i][j][0] != 255 and img[i][j][1] != 255 and img[i][j][2] != 255:
            print(f"Pixel at {i} , {j} is not white")
            count += 1
            

print("The number of non white pixels in the image is: ", count)
    