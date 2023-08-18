import cv2
import numpy as np
import os
import shutil

img = cv2.imread('fotos/foto.jpg')
imgGray = cv2.imread('fotos/foto.jpg',0)
width, height, channel = img.shape
print(f'width: {width}\nheight: {height}\nchannel: {channel}')

img1 = cv2.resize(img,(600, 600))
img2 = cv2.resize(imgGray,(600, 600))

imghsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

low_intenaity = np.array([140, 50, 50], np.uint8)
high_intenaity = np.array([170, 255, 255], np.uint8)


dir = 'C:/Users/spas2/Desktop/projects/programacion/simulador_motor/fotos'
contenido = os.listdir(dir)
print(contenido)
print(contenido[1])
resultados = []

for c in contenido:
    
    image = cv2.imread(f'fotos/{c}')
    image = cv2.resize(image,(600, 600))
    imghsv1 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    low_intenaity1 = np.array([140, 50, 50], np.uint8)
    high_intenaity1 = np.array([190, 255, 255], np.uint8)
    mask = cv2.inRange(imghsv1, low_intenaity1, high_intenaity1)

    contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    h = 0
    for i in contours:
        areas = cv2.contourArea(i)
        if areas > 50:
            x1, y1, w1, h1 = cv2.boundingRect(i)
            cv2.rectangle(image, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 213), 2) # type: ignore
            h +=1
            
    if h > 0:
        shutil.move(f'fotos/{c}','fotos2')
    
    
    cv2.imshow('Image Input',image)
    cv2.imshow('Image Output',mask)
    cv2.waitKey(0)
    
"""         resultados.append({
                                'imagen': image,
                                'mask': mask,
                                'contours': contours,
                                'areas': areas,
                                'x1': x1,
                                'y1': y1,
                                'w1': w1,
                                'h1': h1
                                })
    
    for resultado in resultados:
        cv2.imshow('Image RGB', resultado['imagen'])
        cv2.imshow('Image Mask', resultado['mask'])"""


dir2 = 'C:/Users/spas2/Desktop/projects/programacion/simulador_motor/fotos2'
contenido2 = os.listdir(dir2)
print(contenido2)
cv2.destroyAllWindows()