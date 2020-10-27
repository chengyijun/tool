# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 多线程.py
@time: 2020/10/27 9:57
@desc:
"""
import threading
from threading import Thread
from time import sleep


class Worker(Thread):
    count = 0

    def task(self):
        print('do something...', threading.currentThread().getName())

    def run(self) -> None:
        while True:
            sleep(1)
            self.task()
            self.count += 1
            if self.count == 10:
                break


def main():
    worker1 = Worker()
    worker2 = Worker()
    worker1.start()
    worker2.start()

    worker1.join()
    worker2.join()
    print('我是在主线程')


if __name__ == '__main__':
    main()
