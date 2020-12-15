# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 魔术方法__setter__.py
@time: 2020/12/15 14:48
@desc:
"""


class A:
    def __new__(cls, *args, **kwargs):
        """
        创建对象 a = A() 时候被调用
        :param args:
        :param kwargs:
        """
        print('__new__')
        obj = super(A, cls).__new__(cls, *args, **kwargs)
        print('do something...')
        return obj

    def __init__(self):
        """
        初始化方法 用来初始化__new__()方法产生的对象
        """
        print('__init__')

    def __setattr__(self, key, value):
        """
        当给对象设置属性的时候 改方法被调用
        如 obj.age = 11
        :param key:
        :param value:
        :return:
        """
        print('__setattr__')
        super(A, self).__setattr__(key, value)

    def __getattr__(self, item):
        """
        当从对象上获取一个不存在的属性时，该方法被调用
        :param item:
        :return:
        """
        print('__getattr__')
        print(item)
        return 123

    def __getattribute__(self, item):
        """
        当从对象上获取已经存在的属性时候，该方法被调用
        :param item:
        :return:
        """
        print('__getattribute__')
        return super(A, self).__getattribute__(item)

    def __del__(self):
        """
        析构方法 生命周期最后调用
        :return:
        """
        print('__del__')

    def __repr__(self):
        """
        将对象转为字符串形式的时候 自动被调用
        注意：当同时存在 __str__() 方法的时候，本方法不被调用
        :return:
        """
        print('__repr__')
        return 'repr'

    def __str__(self):
        """
        将对象转为字符串形式的时候 自动被调用
        :return:
        """
        print('__str__')
        return 'str'

    def __call__(self, *args, **kwargs):
        """
        当类的实例 像函数一样+()执行的时候 该方法被调用
        :param args:
        :param kwargs:
        :return:
        """
        print('__call__')


def main():
    a = A()
    a.name = 'rox'
    a.cry = lambda: print('cry hi')
    print(a.x)
    print(a.name)
    print(A.__dict__)
    print(a.__dict__)
    print(a)
    a()


if __name__ == '__main__':
    main()
