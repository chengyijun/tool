# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 操作mysql数据库.py
@time: 2021/1/8 15:45
@desc:
"""
import pymongo
import pymysql


class MysqlDBUtils:
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


class MongoDBUtils:
    def __init__(self, db: str, collect: str):
        self.db = db
        self.collect = collect
        self.myclient = pymongo.MongoClient("mongodb://abel:abel@192.168.56.100:27017/")
        # 获取数据库对象 如果不存在就创建
        self.mydb = self.myclient[self.db]
        # 获取集合对象 如果不存在就创建
        self.mycol = self.mydb[self.collect]

    def get_collection_obj(self):
        return self.mycol

    def close_conn(self):
        try:
            if self.myclient:
                self.myclient.close()
        except Exception as e:
            print(e)

    def __del__(self):
        print('__del__() 关闭数据库连接')
        self.close_conn()


def main():
    # mysql_test()
    mongo_test()


def mongo_test():
    dbutils = MongoDBUtils('db1', 'coll1')
    mycoll = dbutils.get_collection_obj()

    # 新增数据
    # mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
    # x = mycoll.insert_one(mydict)
    # print('数据插入成功')
    # print(x)

    # 查询数据
    for x in mycoll.find():
        print(x)


def mysql_test():
    db = MysqlDBUtils()
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
