# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 推倒式.py
@time: 2020/10/29 10:59
@desc:
"""


def main():
    # 字典推倒式
    a = ['name', 'age', 'gender']
    b = ['abel', 12, 'male']
    c = zip(a, b)
    d = {item[0]: item[1] for item in c}
    print(d)
    # e = dict(c)
    # print(e)

    # 列表推倒式
    a = [i for i in range(10)]
    print(a)

    # b = list(range(10))
    # print(b)

    # 迭代器 推倒式
    a = (i for i in range(10))
    print(a)

    # 复杂一些的推倒式
    a = [j for i in range(10) for j in range(i) if j > 5]
    print(a)


if __name__ == '__main__':
    main()
