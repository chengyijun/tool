# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: pickle序列化.py
@time: 2021/1/26 12:44
@desc:
"""
import pickle


class Person:
    pass


def main():
    # with open('tmp', 'wb') as f:
    #     pickle.dump(Person, f)
    # print('序列化完成')

    with open('tmp', 'rb') as f:
        obj = pickle.load(f)
    print(obj, type(obj))


if __name__ == '__main__':
    main()
