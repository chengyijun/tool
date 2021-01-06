# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 动画.py
@time: 2021/1/6 15:49
@desc:
"""

import sys

from PyQt5.QtCore import QPropertyAnimation, QPoint, QMetaObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.btn = QPushButton('Bigger', self)
        self.btn.setObjectName('btn')
        self.btn.resize(100, 100)

        self.animation = QPropertyAnimation(self)
        # 指定动画作用的对象
        self.animation.setTargetObject(self.btn)
        # b'size' 改变大小  b'pos' 改变位置
        self.animation.setPropertyName(b'pos')
        # 设置动画持续时长
        self.animation.setDuration(1000)
        # 设置位置关键帧
        self.animation.setKeyValueAt(0, self.btn.pos() + QPoint(0, 0))
        self.animation.setKeyValueAt(0.2, self.btn.pos() + QPoint(0, 15))
        self.animation.setKeyValueAt(0.4, self.btn.pos() + QPoint(0, 0))
        self.animation.setKeyValueAt(0.6, self.btn.pos() + QPoint(0, -15))
        self.animation.setKeyValueAt(0.8, self.btn.pos() + QPoint(0, 0))
        # self.animation.setKeyValueAt(1, self.btn.pos() + QPoint(0, 0))  
        self.animation.setLoopCount(3)

        QMetaObject.connectSlotsByName(self)

    @pyqtSlot()
    def on_btn_clicked(self):
        # 启动动画
        self.animation.start()


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
