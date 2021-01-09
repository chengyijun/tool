# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 操作mysql数据库.py
@time: 2021/1/8 15:45
@desc:
"""
import pymysql


class DBUtils:
    def __init__(self):
        # 1.连接
        self.conn = pymysql.connect(host='192.168.56.100', port=3306, user='root', password='root', database='abeltest',
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def get_conn_and_cursor(self):
        return self.conn, self.cursor

    def destroy_conn(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(e)
            print('数据库关闭失败')

    def __del__(self):
        self.destroy_conn()
        print('__del__() 销毁了数据库连接')


def main():
    db = DBUtils()
    conn, cursor = db.get_conn_and_cursor()

    # 注意%s需要加引号
    sql = "select * from person where name='%s'" % ('abel',)
    print(sql)

    # 3.执行sql语句
    cursor.execute(sql)

    result = cursor.execute(sql)  # 执行sql语句，返回sql查询成功的记录数目
    print(result)
    print(cursor.fetchall())

    # db.destroy_conn()


if __name__ == '__main__':
    main()
