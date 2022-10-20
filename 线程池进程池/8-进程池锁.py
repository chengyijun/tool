from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager
from threading import RLock


def task(x: int, lock: RLock):
    with lock:
        with open("target.txt", "a") as f:
            f.write(str(x) + "\n")

    return x


if __name__ == '__main__':
    lock = Manager().RLock()
    with ProcessPoolExecutor() as pool:
        for i in range(10):
            pool.submit(task, i, lock)
