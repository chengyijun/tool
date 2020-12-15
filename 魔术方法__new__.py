# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 魔术方法__new__.py
@time: 2020/12/15 12:18
@desc:
"""

"""
__new__()方法：用法一
在创建对象之前做一些额外的事情
通过类创建对象的时候，会调用类中的__new__()方法，生成对象
如果将new出来的对象返回，则__init__(self)方法将会被调用，并将new出来的对象传递给init中的第一个参数self
"""


class A:

    def __init__(self):
        print(self)
        print('A __init__')

    def __new__(cls, *args, **kwargs):
        print('A __new__')
        o = super(A, cls).__new__(cls, *args, **kwargs)
        print(o)
        return o


class B(A):
    def __init__(self):
        print(self)
        print('B __init__')

    def __new__(cls, *args, **kwargs):
        print('B __new__')
        o = super(B, cls).__new__(cls, *args, **kwargs)
        print(o)
        return o


def main():
    b = B()


if __name__ == '__main__':
    main()
