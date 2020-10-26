# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 生成器.py
@time: 2020/10/26 16:26
@desc:
"""


def create_generator():
    for i in range(10):
        tmp = yield i
        print(tmp, '++++++++')


def main():
    g1 = create_generator()
    # print(next(g1))
    # print(next(g1))
    # print(next(g1))

    print(next(g1))
    g1.send('aaaa')
    # print(next(g1))
    # g1.send('bbbb')
    # g1.send('cccc')

    print(next(g1))


if __name__ == '__main__':
    main()
