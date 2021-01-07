# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: demo1.py
@time: 2021/1/7 14:23
@desc:
"""
import sqlite3


class InitDB:
    def __init__(self):
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()
        sql = "create table student(name Text,phone Text, address Text)"
        cursor.execute(sql)

        sql2 = "insert into student(name,phone,address) values('abel',1336464, '河北廊坊'),('tank', 1485643, '江西瑞金'),('rose', 158743643, '安徽安庆')"
        cursor.execute(sql2)
        conn.commit()


def main():
    InitDB()


if __name__ == '__main__':
    main()
