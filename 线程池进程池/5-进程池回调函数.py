from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Queue, current_process
import multiprocessing


def task(x: int) -> int:
    print("正在执行任务:", x)
    return x


res_queue = Queue()


def callback(obj):
    pid = multiprocessing.current_process().pid
    print("回调函数获取结果:", obj.result(), "当前进程是:", pid)
    res_queue.put(obj.result())


if __name__ == '__main__':
    print("主进程id:", current_process().pid)
    with ProcessPoolExecutor(max_workers=4) as pool:
        for i in range(10):
            res = pool.submit(task, i)
            # 与线程池中回调函数是子线程自己调用不同  进程池的回调函数是主进程调用的 从上面打印的进程id可以观察出
            res.add_done_callback(callback)

    print(res_queue.get())
    print(res_queue.get())
    print(res_queue.qsize())