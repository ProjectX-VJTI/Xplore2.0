import cv2
import numpy as np
height,width=500,500

image=np.ones((height,width,3),dtype=np.uint8)*255
image[:]=(230,215,170)

cv2.line(image,(0,500),(500,500),(32,46,126),30)

cv2.rectangle(image,(140,300),(354,500),(111,198,255),-1)

triangle= np.array([[140,300],[247,200],[354,300]],np.int32)
cv2.fillPoly(image,[triangle],(237,126,213))

cv2.rectangle(image,(230,380),(270,500),(248,173,232),-1)

cv2.rectangle(image,(165,340),(200,370),(172,245,255),-1)

cv2.rectangle(image,(294,340),(329,370),(172,245,255),-1)

cv2.circle(image,(420,70),30,(0,255,255),-1)

cv2.putText(image,"My House",(175,295),cv2.FONT_ITALIC,1,(0,0,0),2)

cv2.imshow("Task7",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

