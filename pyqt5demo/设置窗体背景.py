# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 设置窗体背景.py
@time: 2021/1/6 12:03
@desc:
"""
import sys

from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget


class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform, self).__init__(parent)
        self.setWindowTitle("paintEvent设置背景颜色")

    def paintEvent(self, event):
        """
        当窗口resize时候，改方法会被调用
        :param event:
        :return:
        """
        painter = QPainter(self)
        # todo 1 设置背景颜色
        # painter.setBrush(Qt.green)
        # painter.drawRect(self.rect())

        # todo 2 设置背景图片，平铺到整个窗口，随着窗口改变而改变
        pixmap = QPixmap("img/111.jpg")
        painter.drawPixmap(self.rect(), pixmap)


def main():
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
