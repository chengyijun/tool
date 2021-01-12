# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 迭代器（二）.py
@time: 2020/10/26 16:15
@desc:
"""
from collections.abc import *


class MyRange(object):
    def __init__(self, end):
        self.start = 0
        self.end = end

    def __iter__(self):
        """
        只要一个类 实现了 __iter__()方法就表示这个类的对象是可迭代的
        这个方法需要有一个返回值，而且这个返回值对象 必须是一个实现了 __next__()方法的对象，
        由于本类同时实现了 __next__()方法 所有满足以上要求
        :return:
        """
        return self

    def __next__(self):
        if self.start < self.end:
            ret = self.start
            self.start += 1
            return ret
        else:
            raise StopIteration


def main():
    a = MyRange(5)
    print(isinstance(a, Iterable))
    print(isinstance(a, Iterator))

    for i in a:
        print(i)


if __name__ == '__main__':
    main()
