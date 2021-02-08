import cv2   # импорт модуля  из библиотеки Opencv
import numpy as np # модуль обработки массивов
import sys  # системный модуль
import time  


# Первый блок проверяет условие, передан ли скрипту в командной строке дополнительный аргумент в виде картинки **QR кода**. Если первое условие ложно, то считывается указанная нами картинка.

if len(sys.argv)>1:
    inputImage = cv2.imread(sys.argv[1])  
else:
    inputImage = cv2.imread("myrusakov_out.jpg") #  стандартный метод opencv для считывания изображения



#  Создание функции выводящей в отдельном окне изображение QR с синим обрамлением.
def display(im, bbox):

    n = len(bbox)

    for j in range(n):

        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)
 
    # Display results
    cv2.imshow("Results", im)



# В Opencv имеется  встроенный метод детектор QR

qrDecoder = cv2.QRCodeDetector() # создание объекта детектора

 

# Нахождение и декодирование нашего кода. Метод **detectAndDecode** возвращает  кортеж из трех  значений которыми кодируется QR, где первый аргумент data содержит декодированную строку, bbox - координаты вершин нашего изображения и rectifiedImage,  содержит **QR** изображение в виде массива пикселей.

data, bbox, rectifiedImage = qrDecoder.detectAndDecode(inputImage)

if len(data)>0:

    print("Decoded Data : {}".format(data)) # вывод декодированной строки

    display(inputImage, bbox)

    #rectifiedImage = np.uint8(rectifiedImage);

    #cv2.imshow("Rectified QRCode", rectifiedImage);

else:

    print("QR Code not detected")  

    cv2.imshow("Results", inputImage)



cv2.waitKey(0)

cv2.destroyAllWindows()