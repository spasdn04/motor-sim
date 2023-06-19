import cv2
import numpy as np

img = cv2.imread('foto.jpg')
imgGray = cv2.imread('foto.jpg',0)
width, height, channel = img.shape
print(f'width: {width}\nheight: {height}\nchannel: {channel}')

img1 = cv2.resize(img,(600, 600))
img2 = cv2.resize(imgGray,(600, 600))

imghsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

low_intenaity = np.array([140, 50, 50], np.uint8)
high_intenaity = np.array([170, 255, 255], np.uint8)
mask2 = cv2.inRange(imghsv, low_intenaity, high_intenaity)

contour,_ = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for i in contour:
    area = cv2.contourArea(i)
    if area > 100:
        x, y, w, h = cv2.boundingRect(i)
        cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 213), 2) # type: ignore

cv2.imshow('Image RGB',img1)
cv2.imshow('Image Gray', img2)
cv2.imshow('Image rosa', mask2)


cv2.waitKey(0)
cv2.destroyAllWindows()