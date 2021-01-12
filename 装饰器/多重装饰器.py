# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 多重装饰器.py
@time: 2020/10/27 8:32
@desc:
"""


def wrapper1(f):
    print('wrapper1')

    def inner():
        f()

    return inner


def wrapper2(f):
    print('wrapper2')

    def inner():
        f()

    return inner


"""
多重装饰器的时候，执行顺序从内向外执行
"""


@wrapper1
@wrapper2
def test():
    print('test')


def main():
    test()


if __name__ == '__main__':
    main()
