import asyncio


async def set_value(fut):
    await asyncio.sleep(2)
    fut.set_result('123')


async def make_task():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()
    loop.create_task(set_value(fut))
    res = await fut
    print(res)


def main():
    asyncio.run(make_task())


if __name__ == '__main__':
    main()
