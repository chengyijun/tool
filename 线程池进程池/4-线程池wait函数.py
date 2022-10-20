from concurrent.futures import ALL_COMPLETED, FIRST_COMPLETED, ThreadPoolExecutor, wait


def task(x: int) -> int:
    print("正在执行任务：", x)
    return x


with ThreadPoolExecutor() as pool:
    my_tasks = [pool.submit(task, i) for i in range(100)]

    # wait() 阻塞主线程  等待线程池中所有子线程全部执行结束才能继续进行
    wait(my_tasks, return_when=ALL_COMPLETED)
    print("=============")
print("main end")