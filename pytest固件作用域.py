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


@pytest.fixture(scope='function')
def func_scope():
    pass


@pytest.fixture(scope='module')
def mod_scope():
    pass


@pytest.fixture(scope='session')
def sess_scope():
    pass


# test_scope.py

def test_multi_scope(sess_scope, mod_scope, func_scope):
    pass


def test_multi_scope1(sess_scope, mod_scope, func_scope):
    pass


def main():
    pytest.main('--setup-show pytest固件作用域.py'.split())


if __name__ == '__main__':
    main()
