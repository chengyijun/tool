# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: classinclass.py.py
@time: 2020/10/26 8:18
@desc:
"""


class A:
    """
    类中的成员 不仅有成员属性  成员方法  还可以有成员类
    """
    name = 'abel'

    def say_hello(self):
        print('say hello')

    class Meta:
        model = 'User'

        def get_outter_attr(self):
            print(self.model)
            print(A.name)
            print(A.Meta.model)


def main():
    a = A()
    print(a.__dir__())  # 相当于 dir(a)
    print(a.__class__)
    meta = A.Meta()
    a.Meta.get_outter_attr(meta)


if __name__ == '__main__':
    main()
