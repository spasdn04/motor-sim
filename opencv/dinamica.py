import cv2
import numpy as np

cap = cv2.VideoCapture(0)
i = 0
element_e = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
frequency = 4000
duration = 1

while cap.isOpened():
    ret, img = cap.read()
    
    if ret == True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if i == 20:
            bgGray = gray
        
        if i > 20:
            dif = cv2.absdiff(gray, bgGray) # type: ignore
            _, th = cv2.threshold(dif, 50, 255, cv2.THRESH_BINARY)
            cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            erosion = cv2.erode(th, element_e)
            cv2.imshow('Imagen con erosion', erosion)

            for c in cnts:
                area = cv2.contourArea(c)
                if area > 7000:
                    x, y, w, h = cv2.boundingRect(c)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 213), 2) # type: ignore
            
        cv2.imshow('Videcaptura: ', img)
        i += 1
        
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()