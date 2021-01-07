# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: viewmodel.py
@time: 2021/1/7 11:10
@desc:
"""
import sys

from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication, QListView


class Demo(QListView):

    def __init__(self, parent=None, *args, **kwargs) -> None:
        super(Demo, self).__init__(parent, *args, **kwargs)

        model = QStringListModel(['abel', 'rox', 'tank', 'jeff'])
        self.setModel(model)


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
