# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 多进程.py
@time: 2020/10/27 10:51
@desc:
"""
import os
from multiprocessing import Process, Queue, cpu_count
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


def main(cpu_count):
    q = Queue()
    for i in range(20):
        q.put(i)

    cpu_count = cpu_count()

    # pool = Pool(cpu_count)
    # pool.apply_async()
    processes = []
    for _ in range(cpu_count):
        mp = MyProcess(q)
        mp.start()
        processes.append(mp)

    for p in processes:
        p.join()

    print('我是在主进程')


if __name__ == '__main__':
    main(cpu_count)
