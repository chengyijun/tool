# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 装饰器.py
@time: 2020/10/26 15:21
@desc:
"""


def outter(*args, **kwargs):
    x = args[0]
    print(f'外层传递进来的参数 {x}')

    def wrapper(f):
        print('开始执行装饰器')
        print(f'操作外层传入的参数 {x}')

        def inner(*args, **kwargs):
            f(*args, **kwargs)
            return

        return inner

    return wrapper


@outter('x')
def hello(name: str):
    print(f'hello {name}')


if __name__ == '__main__':
    hello('abel')
    # @wrapper 这种语法糖这相当于执行了
    # hello = wrapper(hello)
    # hello()
