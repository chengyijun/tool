import asyncio


# 协程函数
async def test():
    print(111)
    await asyncio.sleep(2)
    print(222)


# 将协程函数包装成任务 等待任务都执行完毕后取结果
async def make_tasks():
    tasks = [
        asyncio.create_task(test(), name='t1'),
        asyncio.create_task(test(), name='t2'),
    ]
    done, pending = await asyncio.wait(tasks, timeout=None)
    print(done)


def main():
    # 开启事件循环 执行任务列表
    asyncio.run(make_tasks())


if __name__ == '__main__':
    main()
