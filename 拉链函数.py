# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 拉链函数.py
@time: 2020/10/29 10:59
@desc:
"""


def main():
    a = ['name', 'age', 'gender']
    b = ['abel', 12, 'male']
    c = zip(a, b)
    # print(list(c))
    print(dict(c))


if __name__ == '__main__':
    main()
