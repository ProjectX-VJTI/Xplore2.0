import cv2
import numpy as np

cap = cv2.VideoCapture("D:/OPEN CV/OPEN CV Workshop/OPENCV TASKS/Answers_Avanish/OPENCV/Answers_Avanish/task9.mp4") 

frame_count = 0
pixels_count_sideways = 0
last_frame = None

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    last_frame = frame
    

    frame_count += 1

    
    pixels_count_sideways = frame.shape[1]

# print("Total frames :" , frame_count)
# print("Number of pixel sideways :" , pixels_count_sideways)

# cap.release()

#just did this to check whether the program is working or not and checked the details with the properties of the video 

minimum_speed = (200*2*pixels_count_sideways)/(120*frame_count)

print("Minimum speed for PROJECT X to reach back to its position :", minimum_speed , "m/s")
#unit hoga kuch toh ofc m/s


#now i want to go with the last frame cause usse we can get the distance travelled so we can find the current speed and also the distance remaining

gray = cv2.cvtColor(last_frame , cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray , 200 , 255 , cv2.THRESH_BINARY_INV)

contours , _ = cv2.findContours(thresh , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

projectx = contours[0]

x , y , w, h = cv2.boundingRect(projectx)

remaining_distance = 200*x

print("remaining distance :", remaining_distance, " m ")

current_speed = (2*200*pixels_count_sideways - remaining_distance)/(frame_count*120)

print("Current speed of project X : " , current_speed , "m/s")

print("BUT THE ACTUAL SPEED OF PROJECT X IS MUCH GREATER THAN IT SEEMS IN THE VIDEO")
