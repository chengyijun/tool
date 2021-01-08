# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 表格中放置按钮.py
@time: 2021/1/8 8:58
@desc:
"""
import sys
import typing

from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QTableWidget, QPushButton, QTableWidgetItem, QHeaderView


class Demo(QWidget):

    def __init__(self, parent: typing.Optional['QWidget'] = None) -> None:
        super().__init__(parent)

        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)
        self.table = QTableWidget()
        self.vbox.addWidget(self.table)
        self.table.setRowCount(4)
        self.table.setColumnCount(3)
        # TODO 优化 2 设置水平方向表格为自适应的伸缩模式
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置表头
        self.table.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])
        # 添加字符串
        self.table.setItem(0, 0, QTableWidgetItem('你好'))
        # 添加按钮
        self.table.setCellWidget(1, 1, QPushButton('添加'))


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
