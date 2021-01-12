# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 反射.py
@time: 2020/10/26 17:06
@desc:
"""

"""
反射主要掌握四个方法：
hasattr()
getattr()
setattr()
delattr()
"""


def hello():
    print('say hello')


class A:
    PI = 3.14


def main():
    a = A()
    print(hasattr(A, 'PI'))
    print(hasattr(a, 'PI'))

    print(getattr(A, 'PI'))
    setattr(A, 'Country', 'China')
    setattr(A, 'say_hello', hello)

    print(A.Country)
    A.say_hello()

    b = A()
    print(b.Country)

    delattr(A, 'PI')
    # print(A.PI) # 由于上一步中删除了 A类的PI属性 所以获取的时候报错


if __name__ == '__main__':
    main()
