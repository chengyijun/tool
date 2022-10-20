from concurrent.futures import ProcessPoolExecutor


def task(x: int):

    print("任务正在执行:", x)
    return x


def callback(obj):
    # 由于回调函数都是主进程调用的  所以这里打开文件不用加锁 因为都是顺序执行的 没有并发
    with open("target.txt", "a") as f:
        f.write(str(obj.result()) + "\n")
    print("回调函数")


if __name__ == '__main__':
    with ProcessPoolExecutor() as pool:
        for i in range(10):
            future = pool.submit(task, i)
            future.add_done_callback(callback)
