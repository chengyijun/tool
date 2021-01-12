# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 属性装饰器 getter setter.py
@time: 2020/10/29 11:42
@desc:
"""


class C:
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        print('delx()被执行')
        del self.__x


def main():
    c = C('abel')
    print(c.x)
    c.x = 'rox'
    print(c.x)
    del c.x


if __name__ == '__main__':
    main()
