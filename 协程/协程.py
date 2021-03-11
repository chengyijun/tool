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
    r = requests.get(i)
    # 由于需要模拟IO耗时较多造成的明显阻塞效果 可以再加一个 asyncio.sleep(4) 增加4s耗时
    await asyncio.sleep(4)
    print(f'url: {i}下载完毕，耗时：{time.time() - start}')
    return r


def main():
    url = ["https://segmentfault.com/p/1210000013564725",
           "https://www.jianshu.com/p/83badc8028bd",
           "https://www.baidu.com/",
           "https://www.sogou.com/"
           ]

    # 1. 创建一个事件循环
    loop = asyncio.get_event_loop()
    # 2. 创建一个任务队列
    task = [asyncio.ensure_future(test2(i)) for i in url]
    # 3. 执行事件循环直到任务队列中任务都跑完
    loop.run_until_complete(asyncio.wait(task))
    endtime = time.time() - start
    print(endtime)
    # 关闭事件循环
    loop.close()


if __name__ == '__main__':
    main()
