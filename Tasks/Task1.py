# ## Task 1:

# You have have been given an image with a white canvas containing few non white pixels. The task is to use OpenCV to **find the number of non white pixels and also return the positions** of the pixels you have found.


# #### Link for the image: https://drive.google.com/file/d/1OTYYn3tJJ_iT4f0fUmPSnl71gYHjRphl/view?usp=drive_link
import cv2 
import numpy as np

img1 = cv2.imread("/home/rudrakshi/projectxopenCV/Xplore2.0/Tasks/Task1.png")
# print(img1.shape)
# pixel = img1[50,450]
# print(pixel)
# cv.imshow("img1" , img1)
# cv.waitKey(0)
# cv.destroyAllWindows()

white = [255,255,255]
count = 0 
for y in range (img1.shape[0]):
    for x in range (img1.shape[1]):
        if(img1[y,x] != [255,255,255]).all():
            print("coordinate are : (",y,x,")"
            )
            count=count+1


print("The total number of non-white pixels are ", count)
    



