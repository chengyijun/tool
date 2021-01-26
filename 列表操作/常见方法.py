# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 常见方法.py
@time: 2021/1/26 14:46
@desc:
"""


def main():
    list1 = ['a', 'b', 'c', 'd', 'e']
    # 追加元素
    print(list1)
    # 插入元素
    list1.insert(1, 'f')
    print(list1)
    # 取出一个元素 并从list中删除 如果不指定参数就表示删除list中最后一个元素
    tmp = list1.pop(1)
    print(tmp)
    # 直接删除一个元素
    list1.remove('c')
    print(list1)
    # 获取元素在列表中的位置 如果该元素不存在与列表中会抛出 ValueError 异常
    no = list1.index('b')
    print(no)
    print('aa' in list1)
    # 切片 隔一个 取一个
    list_2 = list1[::2]
    print(list_2)
    # 切片 巧妙倒序
    list_3 = list1[::-1]
    print(list_3)
    # 切片 取最后一个
    last = list1[-1]
    print(last)
    # 列表扩展 extend
    list_4 = ['x', 'y']
    list1.extend(list_4)
    print(list1)


if __name__ == '__main__':
    main()
