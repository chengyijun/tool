# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 解包.py
@time: 2020/10/29 10:59
@desc:
"""


def main():
    a, b, c = [1, 2, 3]
    print(a)
    print(b)
    print(c)
    d, e, f = (4, 5, 6)
    print(d)
    print(e)
    print(f)

    # 快速生成一个字典
    dict1 = dict(zip('abcd', range(4)))
    dict2 = dict(zip('ef', range(2)))
    print(dict1)
    print(dict2)
    dict1.update(dict2)
    print(dict1)

    dict3 = dict(dict1, **dict2)
    dict4 = {**dict1, **dict2}
    print(dict3)
    print(dict4)


if __name__ == '__main__':
    main()
