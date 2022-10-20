from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Queue, current_process
import multiprocessing
from multiprocessing.managers import DictProxy


def task(x: int, mydict: DictProxy) -> int:
    print("正在执行任务:", x)
    mydict.update({x: x})
    return x


if __name__ == '__main__':
    print("主进程id:", current_process().pid)
    with ProcessPoolExecutor(max_workers=4) as pool:
        manager = multiprocessing.Manager()
        mydict = manager.dict()
        for i in range(10):
            res = pool.submit(task, i, mydict)

        pool.shutdown(True)
        print(mydict)