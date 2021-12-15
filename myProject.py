import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('2.png')
# code=decode(img)
# print(img)
cap = cv2.VideoCapture(0) # 打开电脑摄像头
'''
参数：3：在视频流的帧的宽度
　　　480：高度的数值
功能：把视频流的帧(图片)的宽度调成480
'''
cap.set(3,640)
cap.set(4,480)

while True:
    success,img=cap.read()
    for barcode in decode(img):
        # print(barcode.data) # b'20211204'
        myData = barcode.data.decode('utf-8') # 20211204
        print(myData)

    cv2.imshow('result',img)
    cv2.waitKey(1)