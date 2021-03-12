# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 协程.py
@time: 2020/10/27 11:18
@desc:
"""
import asyncio
import time

import requests

"""
async 讲函数包装厂成为task或者future等 协程对象
await 后面跟的是耗时操作  也必须是协程对象
"""

start = time.time()


async def test2(i):
    # await 之后相当于遇到一个 IO阻塞任务 比如此处的dowload() 发起网络请求
    r = await download(i)
    # print(i, r)


async def download(i):
    print(f'开始下载 url: {i}')
    loop = asyncio.get_event_loop()
    # 由于requests.get() 是不支持async await的 所以通过 run_in_executor() 包装成future对象 进行协程操作
    future = loop.run_in_executor(None, requests.get, i)
    r = await future
    print(f'url: {i}下载完毕，耗时：{time.time() - start}', r)
    return r


async def main():
    url = ["https://segmentfault.com/p/1210000013564725",
           "https://www.jianshu.com/p/83badc8028bd",
           "https://www.baidu.com/",
           "https://www.sogou.com/"
           ]

    # 2. 创建一个任务队列
    tasks = [asyncio.create_task(test2(i)) for i in url]
    await asyncio.wait(tasks)
    endtime = time.time() - start
    print(endtime)


if __name__ == '__main__':
    asyncio.run(main())
