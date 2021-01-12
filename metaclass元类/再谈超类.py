# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 再谈超类.py
@time: 2020/12/15 13:24
@desc:
"""

"""
超类 动态创建类
"""


class MyMetaClass(type):
    def __new__(mcs, *args, **kwargs):
        print('__new__')
        args[2].setdefault('say', lambda self: print('say hi'))
        print(args[2])
        o = type(*args)
        print(o)
        return o


class Person(object, metaclass=MyMetaClass):
    pass


def main():
    person = Person()
    person.say()


if __name__ == '__main__':
    main()
