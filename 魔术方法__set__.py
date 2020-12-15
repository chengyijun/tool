# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 魔术方法__set__.py
@time: 2020/12/15 16:27
@desc:
"""


class IntValidation:
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int) and 0 < value < 100:
            self.value = value  # 这个要注意 要用value，不能用instance 否则会陷入死循环
        else:
            print("请输入合法的数字")
            self.value = 100

    def __delete__(self, instance):
        pass


class Student:
    age = IntValidation()


def main():
    stu = Student()
    stu.age = 501
    print(stu.age)


if __name__ == '__main__':
    main()
