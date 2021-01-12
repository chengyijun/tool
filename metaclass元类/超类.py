# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 超类.py
@time: 2020/10/26 8:37
@desc:
"""
from typing import Any

"""
众所周知，对象是类实例化出来的
Python中万物皆对象，那么，类是什么实例化出来的呢？
答案就是超类实例化出类

超类的应用：
超类中可以拿到并操作"子类"属性  这在继承中是难以实现的 这是超类的意义所在
"""


class A(type):

    def __new__(cls, *args, **kwargs) -> Any:
        print(cls)
        print('当B类被创建时，A.__new__()被调用了，并创建了B类，交给__init__()方法作为第一个参数')
        o = super().__new__(cls, *args, **kwargs)
        print(o.PI)  # 由此可见类属性是__new__()执行过程中就被初始化了 而对象属性是在之后的__init__()方法中进行初始化
        return o

    def __init__(self, *args, **kwargs) -> None:
        """
        __new__() 方法产生 对象之后 会交给__init__() 进行初始化工作
        """
        print('拿到__new__()方法产生的对象，开始初始化了，A.__init__()', self)
        print(self.PI)  # 超类拿到"子类"属性进行操作  这在继承中难以实现  这也是超类的实际应用方式
        self.PI += 1
        super().__init__(*args, **kwargs)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(args)
        print('当B类对象被调用时候，执行A.__call__()方法', self)
        o = self.__new__(self)
        self.__init__(o, *args)
        return o


class B(metaclass=A):
    """
    B类 只要像这样声明定义出来 就会调用超类A.__new__()方法 创建B类， 再把创建出来的B类 传递给A.__init__()方法进行初始化
    """
    PI = 3.14

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        print('我被调用了吗', self)

    def __new__(cls) -> Any:
        print('我被调用了 B.__new__()方法', cls)
        return super().__new__(cls)

    def __call__(self, *args, **kwargs):
        print('B.__call__()被调用了', self)


def main():
    b = B('abel')  # 如果把B类当做是超类A的对象实例，则B('abel')的过程相当于 执行超类A.__call__()方法
    print(b.name)
    print(B.PI)
    b()  # B类的对象+()执行  相当于调用B类中的B.__call__()方法


if __name__ == '__main__':
    main()
