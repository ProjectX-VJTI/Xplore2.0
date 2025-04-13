import cv2

image=cv2.imread("Task2.png")
image =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

morse_code=""
for y in range(image.shape[0]):
   for x in range(image.shape[1]):
      if image[y][x]==0:
         morse_code+="-"
      elif image[y][x]==255:
         morse_code+="."
      elif image[y][x] in range(120,220):
         morse_code+=" "

print(morse_code)
         
         