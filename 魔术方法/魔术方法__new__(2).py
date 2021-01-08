# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 魔术方法__new__.py
@time: 2020/12/15 12:18
@desc:
"""

"""
__new__()方法：用法二
单例模式 确保一个类只有一个实例
通过类创建对象的时候，会调用类中的__new__()方法，生成对象
如果将new出来的对象返回，则__init__(self)方法将会被调用，并将new出来的对象传递给init中的第一个参数self
"""


class Singleton:
    __singleton = None

    def __new__(cls, *args, **kwargs):
        if cls.__singleton is None:
            obj = super(Singleton, cls).__new__(cls, *args, **kwargs)
            cls.__singleton = obj
        return cls.__singleton


def main():
    s1 = Singleton()
    s2 = Singleton()
    print(s1)
    print(s2)
    print(s1 == s2)


if __name__ == '__main__':
    main()
