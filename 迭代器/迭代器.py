# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 迭代器.py
@time: 2020/10/26 15:38
@desc:
"""


class Data:
    list: list = [1, 9, 3, 4, 5, 6]
    index = 0

    def __call__(self, *args, **kwargs):
        print('__call__()被调用了')
        item = self.list[self.index]
        self.index += 1
        return item


def main():
    # 创建迭代器方法一：迭代器推倒式
    iter1 = (x for x in range(3))
    print(type(iter1))
    print(next(iter1))
    print(next(iter1))
    # print(next(iter1)) 越界之后报StopIteration异常
    print(next(iter1))
    # 创建迭代器方法一：iter(参数1, [参数二]) 构造方法
    # 参数二是可选的  当存在参数二时，必须保证参数1是可调用的对象 如函数、对象等
    iter2 = iter([1, 2, 3])
    print(type(iter2))
    iter3 = iter('abel')
    print(type(iter3))

    # 当存在参数2时， 会给参数1+()进行调用  参数1是一个对象 给对象+()进行调用
    # 相当于调用了 Data类的__call__()方法
    # 当__call__() 返回值 等于 参数2 停止迭代
    for item in iter(Data(), 5):
        print(item)


if __name__ == '__main__':
    main()
