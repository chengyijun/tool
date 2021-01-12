# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 高阶函数.py
@time: 2020/10/29 10:59
@desc:
"""


def main():
    iterator = map(lambda x: x ** 2, [1, 2, 3])
    res = list(iterator)
    print(res)

    # 以上相当于
    b = [i ** 2 for i in [1, 2, 3]]
    print(b)

    filter1 = filter(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7, 8])
    print(list(filter1))

    # 以上相当于
    b = [i for i in [1, 2, 3, 4, 5, 6, 7, 8] if i > 5]
    print(b)


if __name__ == '__main__':
    main()
