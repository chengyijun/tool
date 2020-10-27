# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 多线程（二）.py
@time: 2020/10/27 10:06
@desc:
"""
import threading
from queue import Queue
from threading import Thread
from time import sleep


class Worker(Thread):

    def __init__(self, q: Queue):
        super().__init__()
        self.q = q

    def task(self):
        if not self.q.empty():
            print(f'{threading.currentThread().getName()} do something...{self.q.get()}')
            self.q.task_done()

    def run(self) -> None:
        while True:
            if self.q.empty():
                break
            sleep(1)
            self.task()


def main():
    q = Queue()
    for i in range(20):
        q.put(i)

    worker1 = Worker(q)
    worker2 = Worker(q)
    worker1.start()
    worker2.start()

    worker1.join()
    worker2.join()
    print('我是在主线程')


if __name__ == '__main__':
    main()
