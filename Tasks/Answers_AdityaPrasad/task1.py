import cv2
number_of_black_pixels = 0

img = cv2.imread('C:/Users/adity/OneDrive/Desktop/Task1.png')
size = img.shape
height = size[0]
width = size[1]

for i in range(height):
    for j in range(width):
        if img[i][j][0] != 255 and img[i][j][1] != 255 and img[i][j][2] != 255:
            number_of_black_pixels += 1
            print("Black pixel found at: ", i, j)

print("Total number of black pixels: ", number_of_black_pixels)