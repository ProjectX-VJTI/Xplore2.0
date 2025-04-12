import cv2 as cv
import numpy as np

#Just to get the dimensions
img = cv.imread(r'H:\Engineering 2024\Coding\ProjectX\Tasks to be done\OpenCV-Clone\Answers_Nathan\task7.png')
print(img.shape)

height = img.shape[0]*3
width = img.shape[1]*3

img = np.ones((height, width, 3), dtype=np.uint8) * 255
img[:] = (255, 200, 173) 

#ground
cv.rectangle(img, (0, height), (width, height-20), (0, 100, 0), -1)
#house
cv.rectangle(img, (width//3, height-21), (2*width//3, height-200), (0, 75, 128), -1)
#door
cv.rectangle(img, (width//2-30, height-21), (width//2+30, height-100), (230, 255, 255), -1)
#window
cv.rectangle(img, (width//3+10, height-150), (width//3+60, height-100), (230, 255, 255), -1)  
cv.rectangle(img, (2*width//3-60, height-150), (2*width//3-10, height-100), (230, 255, 255), -1)

#roof
pt1 = (2*width//3+30, height-200)
pt2 = (width//3-30, height-200)
pt3 = (width//2, height-280)
cv.circle(img, pt1, 0, (0,255,255), -1)
cv.circle(img, pt2, 0, (0,255,255), -1)
cv.circle(img, pt3, 0, (0,255,255), -1)
triangle_cnt = np.array( [pt1, pt2, pt3] )
cv.drawContours(img, [triangle_cnt], 0, (10,75,225), -1)

#text
cv.putText(img, 'My House Eh', (width//3, height//2), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv.LINE_AA)
#Sun
cv.circle(img, (width-70, 100), 30, (0,245,245), -1)

cv.imwrite('Task7_Nathan.png', img)
cv.waitKey(0)