import cv2 as cv
image = cv.imread('Task4.png')

def apply_gray(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return gray

_, thresh = cv.threshold(apply_gray(image), 254, 255, cv.THRESH_BINARY)

temp = 0
side = 0
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        if thresh[y,x] == 0:
            side = side+1
        if thresh[y,x] == 255:
            if side>temp:
                temp = side
            side = 0
print(temp)
            