# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: 协程.py
@time: 2020/10/27 11:18
@desc:
"""
import asyncio
from asyncio.proactor_events import _ProactorBasePipeTransport
from functools import wraps

import aiohttp

"""
async 讲函数包装厂成为task或者future等 协程对象
await 后面跟的是耗时操作  也必须是协程对象
"""


def silence_event_loop_closed(func):
    # @functools.wraps() 让包装后的函数 保持之前的函数名不变
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                # 当条件成立 本来抛出RuntimeError异常 现在让其不抛出任何异常 相当于pass
                pass

    return wrapper


# 重写 _ProactorBasePipeTransport.__del__() 方法 忽略close 异常
_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)


async def fetch(session, url, index):
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        with open(f'{index}.jpg', 'wb') as f:
            f.write(content)


async def make_start():
    urls = [
        'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1310425826,3721364093&fm=26&gp=0.jpg',
        'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2738358416,447997076&fm=26&gp=0.jpg',
        'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3569046132,343759479&fm=26&gp=0.jpg',
        'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2139234778,1849918516&fm=26&gp=0.jpg',
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(session, url, index)) for index, url in enumerate(urls)]
        await asyncio.wait(tasks)


def main():
    asyncio.run(make_start())


if __name__ == '__main__':
    main()
