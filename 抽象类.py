# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 抽象类.py
@time: 2021/1/7 8:52
@desc:
"""
from abc import ABCMeta, abstractmethod


class MyAbstractClass(metaclass=ABCMeta):
    @abstractmethod
    def my_abstract_method(self):
        pass

    def laugh(self):
        print('laugh')


class Student(MyAbstractClass):

    def my_abstract_method(self):
        print(11111)


def main():
    student = Student()
    student.my_abstract_method()
    student.laugh()


if __name__ == '__main__':
    main()
