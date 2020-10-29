# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 异常处理.py
@time: 2020/10/29 11:25
@desc:
"""


class MyException(Exception):
    pass


def division():
    # raise 1 / 0
    # raise Exception('发生了一个除0异常')
    raise MyException('发生了一个除0异常')
    # print('一切顺利')


def main():
    try:
        division()
    except Exception as e:
        # 发生了异常时才执行
        print('发生了异常', e)
    else:
        # 没有发生异常才执行
        print('没发生异常哦')
    finally:
        # 不管发不发生异常都执行
        print('不管如何都指向我！')


if __name__ == '__main__':
    main()
