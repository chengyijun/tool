# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: json序列化.py
@time: 2021/1/26 12:49
@desc:
"""
import json


def main():
    data = dict(list(zip('abcd', range(4))))
    with open('tmp2.json', 'w') as f:
        json.dump(data, f)
    print('序列化完成')

    with open('tmp2.json', 'r') as f:
        obj = json.load(f)
    print(obj, type(obj))


if __name__ == '__main__':
    main()
