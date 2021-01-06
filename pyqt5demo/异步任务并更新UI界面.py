# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 自动连接信号与槽.py
@time: 2021/1/5 15:38
@desc:
"""
import sys
from time import sleep

from PyQt5.QtCore import QMetaObject, pyqtSlot, QThread, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextBrowser


class Demo2(QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.mylayout = QVBoxLayout()
        self.setLayout(self.mylayout)
        self.btn1 = QPushButton('点我')
        self.btn1.setObjectName('btn1')
        self.browser = QTextBrowser()
        self.mylayout.addWidget(self.btn1)
        self.mylayout.addWidget(self.browser)

        # 自动连接信号与槽
        QMetaObject.connectSlotsByName(self)
        # 创建异步任务并启监听
        self.worker = MyTask()
        self.worker.mySignal.connect(self.handle_mysignal)
        # 启一个定时器监听异步任务是否结束
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_timer)

    @pyqtSlot()
    def on_btn1_clicked(self):
        # 启动异步任务
        self.worker.start()
        # 启动异步任务监听定时器
        self.timer.start(1000)

    def handle_timer(self):
        if self.worker.isFinished():
            # 关闭定时器
            self.timer.stop()
            print('异步任务结束了')
        else:
            print('任务进行中')

    def handle_mysignal(self, val: int):
        # print(2222)
        print(val)
        self.browser.append(str(val) + '\n')


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
    demo = Demo2()
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
