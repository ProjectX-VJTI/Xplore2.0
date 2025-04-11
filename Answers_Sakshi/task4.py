import cv2 as cv

image =cv.imread('Task4.png')

image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

sumofpixel=0
noofpixel=0
norm=image.tolist()
noofpixel=image.shape[0]*image.shape[1]

for y in range(image.shape[0]):
   for x in range(image.shape[1]):
    sumofpixel=sumofpixel+norm[y][x]
thv=sumofpixel/noofpixel

count=0
max=0
for y in range(image.shape[0]):
   for x in range(image.shape[1]):
      if image[y][x]<thv:
        image[y][x]=0
      else:
        image[y][x]=255 

for y in range(image.shape[0]):
   for x in range(image.shape[1]):
     if image[y][x]==0:
       count+=1
     else:
      if(count>max):max=count
      count=0

print(max*max)
