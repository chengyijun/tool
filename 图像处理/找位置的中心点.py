import numpy as np

import cv2

img = cv2.imread(r"C:\Users\Administrator\Desktop\678.png")
groundtruth = img[:, :, 0]
# print(groundtruth.shape)(768, 1024)
h1, w1 = groundtruth.shape
contours, cnt = cv2.findContours(groundtruth, cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)
image = np.zeros([h1, w1])
X_center = []
Y_center = []
for i in range(len(contours)):
    M = cv2.moments(contours[i])  # 计算第一条轮廓的各阶矩,字典形式
    center_x = int(M["m10"] / M["m00"])
    center_y = int(M["m01"] / M["m00"])
    X_center.append(center_x)
    Y_center.append(center_y)
    cv2.drawContours(image, contours, i, 255, -1)  # 绘制轮廓，填充
    m_image = cv2.circle(image, (center_x, center_y), 7, 128, -1)  # 绘制中心点
cv2.imwrite("e.png", image)