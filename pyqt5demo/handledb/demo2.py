# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: demo.py
@time: 2021/1/7 14:32
@desc:
"""
import sys
import typing

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QVBoxLayout, QPushButton


class Demo(QWidget):

    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('student.db')
        db.open()
        # 创建view
        self.view = QTableView()
        # 将模型与数据库绑定
        self.model = QSqlTableModel(None, db)
        # 设置模型对应数据库中的student表
        self.model.setTable('student')
        # 获取数据
        self.model.select()
        # 修改表格头
        self.model.setHeaderData(0, Qt.Horizontal, '姓名')
        self.model.setHeaderData(1, Qt.Horizontal, '手机号')
        self.model.setHeaderData(2, Qt.Horizontal, '地址')
        self.view.setModel(self.model)

        vbox = QVBoxLayout()
        vbox.addWidget(self.view)

        self.btn_add = QPushButton("添加")
        self.btn_add.clicked.connect(self.slot_add)
        self.btn_del = QPushButton("删除")
        self.btn_del.clicked.connect(self.slot_del)

        vbox.addWidget(self.btn_add)
        vbox.addWidget(self.btn_del)

        self.setLayout(vbox)

    def slot_add(self):
        print(11)
        self.model.insertRows(self.model.rowCount(), 1)

    def slot_del(self):
        print(22)
        self.model.removeRow(self.view.currentIndex().row())


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
