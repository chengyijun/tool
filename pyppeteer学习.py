# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: pyppeteer学习.py
@time: 2020/12/31 10:29
@desc:
"""
import asyncio

from pyppeteer import launch


async def test():
    browser = await launch({"userDataDir": r"d:/tmp"})
    page = await browser.newPage()
    await page.goto('https://www.bilibili.com/')
    await page.screenshot({'path': './example.png'})
    await browser.close()


def main():
    asyncio.get_event_loop().run_until_complete(test())


if __name__ == '__main__':
    main()
