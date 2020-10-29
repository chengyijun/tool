# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: property函数.py
@time: 2020/10/29 11:35
@desc:
"""


class C:
    def __init__(self, x):
        self.__x = x

    def getx(self):
        return self.__x

    def setx(self, value):
        self.__x = value

    def delx(self):
        print('delx()被执行')
        del self.__x

    # 相当于拦截器 当外部访问x的时候 会通过getx()方法进行访问  设置x的时候 会通过setx()方法设置  同理删除x的时候 通过delx()方法操作
    # @property @x.setter @x.deleter 就是通过property()方法来实现的
    x = property(getx, setx, delx, "I'm the 'x' property.")


def main():
    c = C('abel')
    print(c.x)
    c.x = 'rox'
    print(c.x)
    del c.x


if __name__ == '__main__':
    main()
