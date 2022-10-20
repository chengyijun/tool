from concurrent.futures import ThreadPoolExecutor
import time


def task(i: int):
    print("task", i)
    return i


pool = ThreadPoolExecutor()
# 通过submit()向线程池提交任务
res = pool.submit(task, 1)
# 通过done()方法判断任务是否完成
print(res.done())
time.sleep(1)
print(res.done())
# 通过result()取回任务结果
print(res.result())
