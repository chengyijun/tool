# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: test1.py
@time: 2021/1/5 14:04
@desc:
"""
import sys
from time import sleep

from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow

from pyqt5demo.demoui import Ui_MainWindow


class Demo(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)

        self.setupUi(self)
        self.worker = MyTask()
        # 连接信号与槽
        self.worker.mySignal.connect(self.handle_mysignal)

    def handle_mysignal(self, value):
        print('我被调用了')
        print(value)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.worker.start()


class MyTask(QThread):
    # 自定义一个信号
    mySignal = pyqtSignal(int)
    counter = 0

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def task(self):
        self.counter += 1
        # 发射信号
        self.mySignal.emit(self.counter)

    def run(self) -> None:

        while True:
            self.task()
            sleep(1)
            if self.counter == 10:
                break


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
