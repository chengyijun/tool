from concurrent.futures import ProcessPoolExecutor


def task(x: int):

    print("任务正在执行:", x)
    return x


def callback(obj):
    with open("target.txt", "a") as f:
        f.write(str(obj.result()) + "\n")
    print("回调函数")


if __name__ == '__main__':
    with ProcessPoolExecutor() as pool:
        for i in range(10):
            future = pool.submit(task, i)
            future.add_done_callback(callback)
