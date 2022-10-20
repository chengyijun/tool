from concurrent.futures import ProcessPoolExecutor
from multiprocessing import current_process


def task(x: int) -> int:
    print("正在执行任务:", x)
    return x


def outter(mydict: dict):

    def callback(obj):
        x = obj.result()
        mydict.update({x: x})
        print("回调函数,结果:", x)

    return callback


if __name__ == '__main__':
    print("主进程id:", current_process().pid)
    mydict = {}
    with ProcessPoolExecutor(max_workers=4) as pool:
        for i in range(10):
            res = pool.submit(task, i)
            res.add_done_callback(outter(mydict))
        pool.shutdown(True)
        print("====", mydict)
