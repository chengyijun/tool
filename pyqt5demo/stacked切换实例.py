# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: stacked切换实例.py
@time: 2021/1/7 9:01
@desc:
"""
import sys

from PyQt5.QtCore import QMetaObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel


class Demo(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super(Demo, self).__init__(parent, *args, **kwargs)
        # 整体水平盒子布局
        self.hbox = QHBoxLayout()
        self.setLayout(self.hbox)

        self.vbox = QVBoxLayout()
        self.stacked = QStackedWidget()

        self.hbox.addLayout(self.vbox)
        self.hbox.addWidget(self.stacked)

        self.btn1 = QPushButton('btn1')
        self.btn2 = QPushButton('btn2')
        self.btn3 = QPushButton('btn3')
        self.btn1.setObjectName('btn1')
        self.btn2.setObjectName('btn2')
        self.btn3.setObjectName('btn3')

        self.vbox.addWidget(self.btn1)
        self.vbox.addWidget(self.btn2)
        self.vbox.addWidget(self.btn3)

        self.lab1 = QLabel('页面1')
        self.lab2 = QLabel('页面2')
        self.lab3 = QLabel('页面3')
        self.stacked.insertWidget(0, self.lab1)
        self.stacked.insertWidget(1, self.lab2)
        self.stacked.insertWidget(2, self.lab3)

        QMetaObject.connectSlotsByName(self)

    @pyqtSlot()
    def on_btn1_clicked(self):
        self.stacked.setCurrentIndex(0)

    @pyqtSlot()
    def on_btn2_clicked(self):
        self.stacked.setCurrentIndex(1)

    @pyqtSlot()
    def on_btn3_clicked(self):
        self.stacked.setCurrentIndex(2)


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
