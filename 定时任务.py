# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 定时任务.py
@time: 2020/10/27 13:07
@desc:
"""
import sched
import time
from datetime import datetime

# 初始化sched模块的 scheduler 类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedule = sched.scheduler(time.time, time.sleep)


# 被周期性调度触发的函数
def printTime(inc):
    """
    周期性执行任务 原理：递归调用
    :param inc: 时间间隔 单位秒
    :return:
    """
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    schedule.enter(inc, 0, printTime, (inc,))


def main():
    # enter四个参数分别为：时间间隔、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，
    # 给该触发函数的参数（tuple形式）
    # schedule.enter(0, 0, printTime, (inc,))
    printTime(inc=5)
    schedule.run()


if __name__ == '__main__':
    main()
