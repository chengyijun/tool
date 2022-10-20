import concurrent.futures
import threading
import time

executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)


def func(x):
    time.sleep(0.5)
    return x


def callback(future):
    # time.sleep(random.random())
    tname = threading.current_thread().name

    x = future.result()
    print("回调函数取到的结果：", x, "当前线程:", tname)
    # cur_thread = threading.current_thread().name
    # if (cur_thread != x):
    #     print(cur_thread, x)


print('main thread: %s' % threading.current_thread().name)
for i in range(10):
    future = executor.submit(func, i)
    # 回调函数 任务只要执行完毕了就会触发回调函数
    future.add_done_callback(callback)
