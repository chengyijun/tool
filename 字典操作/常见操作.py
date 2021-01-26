# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 常见操作.py
@time: 2021/1/26 15:02
@desc:
"""


def main():
    # 快速生成一个字典
    dict_1 = dict(list(zip('abcd', range(4))))
    print(dict_1)
    # 字典取值
    a = dict_1['a']
    # get方法如果 不存在键 结果会给个默认值
    aa = dict_1.get('aa', 'noexist')
    print(a, aa)
    # 字典添加值
    dict_1['e'] = 5
    print(dict_1)
    dict_1.setdefault('f', 6)
    print(dict_1)
    # 通过dict类的构造方法创建一个字典
    dict_2 = dict(name='abel', age=11, gender='M')
    print(dict_2)


if __name__ == '__main__':
    main()
