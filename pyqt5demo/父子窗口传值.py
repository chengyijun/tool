# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 父子窗口传值.py
@time: 2021/1/6 8:33
@desc:
"""
import sys

from PyQt5.QtCore import QMetaObject, pyqtSlot
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton, QWidget, QDialog, QTextEdit


class ParentWin(QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.resize(500, 500)

        self.vbox = QVBoxLayout()
        self.lab1 = QLabel("姓名")
        self.lab2 = QLabel("年龄")
        self.btn1 = QPushButton("打开")
        self.btn1.setObjectName('btn1')
        self.vbox.addWidget(self.lab1)
        self.vbox.addWidget(self.lab2)
        self.vbox.addWidget(self.btn1)
        self.setLayout(self.vbox)

        # 关键点在于 让子窗口持有父窗口对象的引用
        self.childwin = ChildWin(parent=self)
        QMetaObject.connectSlotsByName(self)

    @pyqtSlot()
    def on_btn1_clicked(self):
        print(111)
        self.childwin.exec()


class ChildWin(QDialog):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.parent = parent
        self.vbox = QVBoxLayout()
        self.te1 = QTextEdit()
        self.te2 = QTextEdit()
        self.te1.setPlaceholderText('姓名')
        self.te2.setPlaceholderText('年龄')
        self.btn1 = QPushButton("提交")
        self.btn1.setObjectName('btn1')
        self.vbox.addWidget(self.te1)
        self.vbox.addWidget(self.te2)
        self.vbox.addWidget(self.btn1)
        self.setLayout(self.vbox)
        QMetaObject.connectSlotsByName(self)

    @pyqtSlot()
    def on_btn1_clicked(self):
        print(222)
        self.parent.lab1.setText(self.te1.toPlainText())
        self.parent.lab2.setText(self.te2.toPlainText())
        self.close()


def main():
    app = QApplication(sys.argv)
    parentwin = ParentWin()
    parentwin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
