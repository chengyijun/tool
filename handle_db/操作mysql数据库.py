# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 操作mysql数据库.py
@time: 2021/1/8 15:45
@desc:
"""
import pymysql


def main():
    # 1.连接
    conn = pymysql.connect(host='192.168.56.100', port=3306, user='root', password='root', database='abeltest',
                           charset='utf8')
    print(conn)

    # 2.创建游标
    cursor = conn.cursor()

    # 注意%s需要加引号
    sql = "select * from person where name='%s'" % ('abel',)
    print(sql)

    # 3.执行sql语句
    cursor.execute(sql)

    result = cursor.execute(sql)  # 执行sql语句，返回sql查询成功的记录数目
    print(result)
    print(cursor.fetchall())

    # 关闭连接，游标和连接都要关闭
    cursor.close()
    conn.close()

    if result:
        print('登陆成功')
    else:
        print('登录失败')


if __name__ == '__main__':
    main()
