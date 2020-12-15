# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: pytest类的前后置.py
@time: 2020/12/15 18:16
@desc:
"""
import pytest


class TestAction:
    def setup_class(self):
        print('=====setup=====')

    def test_aaa(self):
        pass

    def test_bbb(self):
        pass

    def teardown_class(self):
        print('=====teardown=====')


def main():
    pytest.main('-sv --setup-show pytest类的前后置.py'.split())


if __name__ == '__main__':
    main()
