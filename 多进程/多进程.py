# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 多进程.py
@time: 2020/10/27 10:51
@desc:
"""
import os
from multiprocessing import Process, Queue
from time import sleep


class MyProcess(Process):

    def __init__(self, q: Queue):
        super().__init__()
        self.q = q

    def task(self):
        if not self.q.empty():
            print(f'{os.getpid()} do something...{self.q.get()}')
            # self.q.task_done()

    def run(self) -> None:
        while True:
            sleep(1)
            self.task()
            if self.q.empty():
                break


def main():
    q = Queue()
    for i in range(20):
        q.put(i)

    worker1 = MyProcess(q)
    worker2 = MyProcess(q)
    worker1.start()
    worker2.start()

    worker1.join()
    worker2.join()
    print('我是在主进程')


if __name__ == '__main__':
    main()
