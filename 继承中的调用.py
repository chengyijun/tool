# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 继承中的调用.py
@time: 2020/10/30 16:47
@desc:
"""


class A:
    FLAG = 'AAA'

    def say(self):
        print(self)
        print(self.FLAG)


class B(A):
    FLAG = 'BBB'


def main():
    b = B()
    b.say()


if __name__ == '__main__':
    main()
