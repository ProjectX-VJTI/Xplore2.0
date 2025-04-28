import cv2 as cv
image_path = r"c:\Users\Dhruv\OneDrive\Desktop\Xplore2.0\Answers_DhruvLad\Task1\1.png"

img =cv.imread(image_path)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
treshold=254
result=[]
count=0
for y in range(gray.shape[0]):
    for x in range(gray.shape[1]):
        p=gray[y,x]
        if p<treshold:
            result.append((y,x))
            count=count+1

print(f"Total non white pixels = {count}")
print("Positions:")
for i in result:
    print(i)