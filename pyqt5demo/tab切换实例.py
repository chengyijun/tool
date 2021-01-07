# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: stacked切换实例.py
@time: 2021/1/7 9:01
@desc:
"""
import sys

from PyQt5.QtCore import QMetaObject
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QLabel


class Demo(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super(Demo, self).__init__(parent, *args, **kwargs)
        # 整体垂直盒子布局
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)

        self.tab = QTabWidget()
        self.vbox.addWidget(self.tab)

        self.lab1 = QLabel('页面1')
        self.lab2 = QLabel('页面2')
        self.lab3 = QLabel('页面3')

        self.tab.addTab(self.lab1, '页面1')
        self.tab.addTab(self.lab2, '页面2')
        self.tab.addTab(self.lab3, '页面3')

        QMetaObject.connectSlotsByName(self)


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
