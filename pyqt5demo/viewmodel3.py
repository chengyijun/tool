# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: viewmodel.py
@time: 2021/1/7 11:10
@desc:
"""
import sys
import typing

from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant
from PyQt5.QtWidgets import QApplication, QTableView


class MyTableModel(QAbstractTableModel):

    def __init__(self, parent=None, *args, **kwargs) -> None:
        super(MyTableModel, self).__init__(parent, *args, **kwargs)

        self.headers = ['国家', '感染人数', '死亡人数']
        self.rows = [
            ('美国', 100, 85),
            ('印度', 456, 687),
            ('意大利', 4562, 754)
        ]

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.rows)

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return len(self.headers)

    def data(self, index: QModelIndex, role: int = ...) -> typing.Any:
        if role != Qt.DisplayRole:
            return QVariant()
        return self.rows[index.row()][index.column()]

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> typing.Any:
        if role != Qt.DisplayRole or orientation != Qt.Horizontal:
            return QVariant()
        return self.headers[section]


class MyTabelView(QTableView):

    def __init__(self, parent=None, *args, **kwargs) -> None:
        super(MyTabelView, self).__init__(parent, *args, **kwargs)
        model = MyTableModel()
        self.setModel(model)


def main():
    app = QApplication(sys.argv)
    demo = MyTabelView()
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
