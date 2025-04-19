import cv2
image=cv2.imread("Task1.png")
img =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
count=0
positions=[]
for y in range (img.shape[0]):
    for x in range (img.shape[1]):
        if img[y][x]!=255:
            count+=1
            positions.append((y,x))
print(count)
print(positions)
        