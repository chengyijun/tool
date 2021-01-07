# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: viewmodel.py
@time: 2021/1/7 11:10
@desc:
"""
import os
import sys

from PyQt5.QtWidgets import QApplication, QTreeView, QDirModel


class Demo(QTreeView):

    def __init__(self, parent=None, *args, **kwargs) -> None:
        super(Demo, self).__init__(parent, *args, **kwargs)

        expanduser = os.path.expanduser('~')
        print(expanduser)
        model = QDirModel()
        self.setModel(model)
        self.setRootIndex(model.index(expanduser))


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
