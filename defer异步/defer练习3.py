# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: defer练习3.py
@time: 2021/1/22 13:30
@desc:
"""

import time

from twisted.internet import reactor
from twisted.internet.threads import deferToThread


# 耗时操作 这是一个同步阻塞函数
def mySleep(timeout):
    time.sleep(timeout)

    # 返回值相当于加进了callback里
    return timeout


def say(result):
    print("耗时操作结束了, 并把它返回的结果给我了", result)


def main():
    # 用functools.partial包装一下, 传递参数进去
    # cb = functools.partial(mySleep, 3)
    cb = lambda x=4: mySleep(x)

    d = deferToThread(cb)
    d.addCallback(say)

    print("你还没有结束我就执行了, 哈哈")

    reactor.run()


if __name__ == '__main__':
    main()
