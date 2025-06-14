import cv2

image = cv2.imread("D:/OPEN CV/OPEN CV Workshop/OPENCV TASKS/Answers_Avanish/OPENCV/Answers_Avanish/Task3.png")
gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY )


#after learning cascades , came to know all are are not inbuilt , so we need to download for nose and eye ones, only some of them are inbuilt

face =  cv2.CascadeClassifier( cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

nose = cv2.CascadeClassifier('D:/OPEN CV/OPEN CV Workshop/OPENCV TASKS/Answers_Avanish/OPENCV/Answers_Avanish/nose.xml')

mouth = cv2.CascadeClassifier('D:/OPEN CV/OPEN CV Workshop/OPENCV TASKS/Answers_Avanish/OPENCV/Answers_Avanish/mouth.xml')


faces = face.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=15)

for (x, y, w, h) in faces:
    interest_gray = gray[y:y+h, x:x+w]
    interest_color = image[y:y+h, x:x+w]
    
    #scale factor ke values apply kar kar ke dekhe hai , it forms multiple rectagles for that

    eyes = eye.detectMultiScale(interest_gray, scaleFactor=1.3, minNeighbors=15)
    for (mx, my, mw, mh) in eyes:
        cv2.rectangle(interest_color, (mx, my), (mx+mw, my+mh), (0 , 0 , 255), 5)
    cv2.imshow("Eye", image[y+my:y+my+mh, x+mx:x+mx+mw])

        

    nose = nose.detectMultiScale(interest_gray, scaleFactor=1.5, minNeighbors=15)
    for (mx, my, mw, mh) in nose:
        cv2.rectangle(interest_color, (mx, my), (mx+mw, my+mh), (0, 0, 255), 5)
        break 
    cv2.imshow("Nose", image[y+my:y+my+mh, x+mx:x+mx+mw])


    mouths = mouth.detectMultiScale(interest_gray, scaleFactor=1.5, minNeighbors=15)
    for (mx, my, mw, mh) in mouths:
        cv2.rectangle(interest_color, (mx, my), (mx+mw, my+mh), (0, 0, 255), 5)
        break  
    cv2.imshow("Mouth", image[y+my:y+my+mh, x+mx:x+mx+mw])
    cv2.imshow("ALL IN ONE", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
