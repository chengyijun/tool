# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 闭包.py
@time: 2020/10/26 15:14
@desc:
"""

"""
闭包的定义：
在A函数中定义一个B函数（函数的嵌套定义），在B函数中使用了A函数中的变量，就会产生闭包。具体来说，就是B就是一个闭包。
相当于调用闭包函数，返回了一个新函数，这个返回的新函数可以使用闭包函数中的变量
基于以上特性，闭包可以作为生成函数的模版 通过闭包的参数 改变模版函数 从而得到想要的函数，装饰器就是这个原理
"""


def closure(x: int):
    x += 1

    def inner():
        print(x)

    return inner


def main():
    c = closure(1)
    c()


if __name__ == '__main__':
    main()
