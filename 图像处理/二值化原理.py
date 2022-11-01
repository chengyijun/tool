import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Administrator\Desktop\white.jpg',
                 cv2.IMREAD_GRAYSCALE)  #灰度图像
x, y = img.shape
print(img.shape)

#遍历灰度图，阈值大于150的全变白
for i in range(x):
    for j in range(y):
        if img[i, j] > 150:
            img[i, j] = 255
        else:
            img[i, j] = 0
black = 0
white = 0
#遍历二值图，为0则black+1，否则white+1
for i in range(x):
    for j in range(y):
        if img[i, j] == 0:
            black += 1
        else:
            white += 1
print("白色个数:", white)
print("黑色个数:", black)
rate1 = white / (x * y)
rate2 = black / (x * y)
#round()第二个值为保留几位有效小数。
print("白色占比:", round(rate1 * 100, 2), '%')
print("黑色占比:", round(rate2 * 100, 2), '%')
