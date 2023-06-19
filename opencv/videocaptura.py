import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    
    if ret == True:
        
        imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        min = np.array([0, 50, 50], np.uint8)
        max = np.array([25, 255, 255], np.uint8)
        mask = cv2.inRange(imghsv, min, max)
        
        contour,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i in contour:
            area = cv2.contourArea(i)
            if area > 100:
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 213), 2) # type: ignore
                cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 0, 213), 2) # type: ignore
        
        cv2.imshow('Video de entrada', img)
        cv2.imshow('Video de máscara', mask)
                
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()