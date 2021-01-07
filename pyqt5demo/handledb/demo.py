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
from PyQt5.QtWidgets import QApplication, QTableView, QWidget


class Demo(QTableView):

    def __init__(self, parent: typing.Optional[QWidget] = None) -> None:
        super().__init__(parent)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('student.db')
        db.open()
        # 将模型与数据库绑定
        model = QSqlTableModel(None, db)
        # 设置模型对应数据库中的student表
        model.setTable('student')
        # 获取数据
        model.select()
        # 修改表格头
        model.setHeaderData(0, Qt.Horizontal, '姓名')
        model.setHeaderData(1, Qt.Horizontal, '手机号')
        model.setHeaderData(2, Qt.Horizontal, '地址')
        self.setModel(model)


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
