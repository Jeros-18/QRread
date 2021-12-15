import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode
# import sys
#
# type = sys.getfilesystemencoding()

with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()  # 读取被授权名单
# print(myDataList)

img = cv.imread('10.png')
code = decode(img)
print(code)

for barcode in code:
    myData = barcode.data.decode('utf-8')
    print(myData)
    if myData in myDataList:  # 根据名单判断是否授权,同时切换输出的文本和边界框颜色
        myOutput = 'Authorized'
        myColor = (0, 255, 0)
    else:
        myOutput = 'Un-Authorized'
        myColor = (0, 0, 255)
    print('myOutput')

    # 用多边形画出二维码的边界框。因为当画面出现旋转时，矩形可能无法画出相应的区域    #
    pts = np.array([barcode.polygon], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv.polylines(img, [pts], True, myColor, 5)

    pts2 = barcode.rect  # 使用矩形左上方的点作为文本初始点
    cv.putText(img, myData + myOutput, (pts2[0], pts2[1] - 25), cv.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)

cv.imshow('Result', img)
cv.waitKey(0)
