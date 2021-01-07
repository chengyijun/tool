# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: pytest固件作用域.py
@time: 2020/12/15 17:59
@desc:
"""

# conftest.py

import pytest


@pytest.fixture(scope='class')
def class_scope():
    print('=====begin=====')
    yield
    print('=====end=====')


@pytest.mark.usefixtures('class_scope')
class TestClassScope:
    def test_1(self):
        pass

    def test_2(self):
        pass


def main():
    pytest.main('-sv --setup-show pytest固件作用域2.py'.split())


if __name__ == '__main__':
    main()
