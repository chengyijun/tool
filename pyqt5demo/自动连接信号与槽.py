# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 自动连接信号与槽.py
@time: 2021/1/5 15:38
@desc:
"""
import sys

from PyQt5.QtCore import QMetaObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextBrowser


class Demo2(QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.mylayout = QVBoxLayout()
        self.setLayout(self.mylayout)

        btn1 = QPushButton('点我')
        btn1.setObjectName('btn1')
        browser = QTextBrowser()

        self.mylayout.addWidget(btn1)
        self.mylayout.addWidget(browser)
        QMetaObject.connectSlotsByName(self)

    @pyqtSlot()
    def on_btn1_clicked(self):
        print(111)


def main():
    app = QApplication(sys.argv)
    demo = Demo2()
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
