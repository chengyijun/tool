# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 父子窗口传值.py
@time: 2021/1/6 8:33
@desc:
"""
import sys

from PyQt5.QtCore import QMetaObject, pyqtSlot, Qt, QPropertyAnimation, QPoint, QEasingCurve, QAbstractAnimation
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget


class ParentWin(QWidget):

    def __init__(self, parent=None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setStyleSheet("QWidget{background-color: yellow}")
        self.resize(500, 500)
        self.move(200, 200)

        self.vbox = QVBoxLayout()
        self.btn1 = QPushButton("切换窗口")
        self.btn1.setObjectName('btn1')
        self.vbox.addWidget(self.btn1)
        self.setLayout(self.vbox)
        self.childwin = None

        QMetaObject.connectSlotsByName(self)

    @pyqtSlot()
    def on_btn1_clicked(self):
        print('切换窗口')
        self.childwin = ChildWin(self)

        # todo 设置窗口动画
        self.animation = QPropertyAnimation(self)
        # 指定动画作用的对象
        self.animation.setTargetObject(self.childwin)
        # b'size' 改变大小  b'pos' 改变位置
        self.animation.setPropertyName(b'pos')
        # 设置动画持续时长
        self.animation.setDuration(1000)
        # 设置位置关键帧
        init_pos = self.childwin.pos()
        self.animation.setKeyValueAt(0, init_pos + QPoint(0, 0))
        self.animation.setKeyValueAt(0.2, init_pos + QPoint(-200, -200))
        self.animation.setKeyValueAt(0.4, init_pos + QPoint(-300, -300))
        self.animation.setKeyValueAt(0.6, init_pos + QPoint(-400, -400))
        self.animation.setKeyValueAt(0.8, init_pos + QPoint(-450, -450))
        self.animation.setKeyValueAt(1, init_pos + QPoint(-500, -500))
        # 设置动画速率曲线 缓动效果
        self.animation.setEasingCurve(QEasingCurve.OutBounce)

        # 设置动画循环次数
        # self.animation.setLoopCount(3)

        self.childwin.show()
        self.animation.start(QAbstractAnimation.DeleteWhenStopped)


class ChildWin(QWidget):

    def __init__(self, parent=None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.setStyleSheet("QWidget{background-color: green}")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.resize(500, 500)
        # 子窗口出现的位置 是相对于父窗口而言的
        self.move(500, 500)
        self.vbox = QVBoxLayout()
        self.btn1 = QPushButton("提交")
        self.btn1.setObjectName('btn1')
        self.vbox.addWidget(self.btn1)
        self.setLayout(self.vbox)
        QMetaObject.connectSlotsByName(self)

    @pyqtSlot()
    def on_btn1_clicked(self):
        print(222)

        # todo 设置窗口动画
        self.animation = QPropertyAnimation(self)
        # 指定动画作用的对象
        self.animation.setTargetObject(self)
        # b'size' 改变大小  b'pos' 改变位置
        self.animation.setPropertyName(b'pos')
        # 设置动画持续时长
        self.animation.setDuration(1000)
        # 设置位置关键帧
        init_pos = self.pos()
        self.animation.setKeyValueAt(0, init_pos + QPoint(0, 0))
        self.animation.setKeyValueAt(0.2, init_pos + QPoint(-200, -200))
        self.animation.setKeyValueAt(0.4, init_pos + QPoint(-300, -300))
        self.animation.setKeyValueAt(0.6, init_pos + QPoint(-400, -400))
        self.animation.setKeyValueAt(0.8, init_pos + QPoint(-450, -450))
        self.animation.setKeyValueAt(1, init_pos + QPoint(-500, -500))
        # 动画倒放
        # self.animation.setDirection(QAbstractAnimation.Backward)
        # 设置动画速率曲线 缓动效果
        self.animation.setEasingCurve(QEasingCurve.OutBounce)

        # 设置动画循环次数
        # self.animation.setLoopCount(3)

        self.animation.start(QAbstractAnimation.DeleteWhenStopped)

        # self.close()


def main():
    app = QApplication(sys.argv)
    parentwin = ParentWin()

    parentwin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
