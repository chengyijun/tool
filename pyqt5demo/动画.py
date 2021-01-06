# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 动画.py
@time: 2021/1/6 15:49
@desc:
"""

import sys

from PyQt5.QtCore import QPropertyAnimation, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.btn = QPushButton('Bigger', self)
        self.btn.resize(100, 100)

        self.animation = QPropertyAnimation(self)  # 1
        # 指定动画作用的对象
        self.animation.setTargetObject(self.btn)
        # b'size' 改变大小  b'pos' 改变位置
        self.animation.setPropertyName(b'size')
        self.animation.setDuration(6000)  # 2
        self.animation.setStartValue(QSize(100, 100))  # 3
        self.animation.setEndValue(QSize(600, 600))  # 4
        self.animation.start()  # 5


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
