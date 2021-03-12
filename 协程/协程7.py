# 上下文管理器原理


class MyContextManger:
    def __enter__(self):
        print('before...')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('after...')

    def do_something(self):
        print('do something...')
        return 'res'


class AsyncMyContextManger:
    async def __aenter__(self):
        print('before...')
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('after...')

    async def do_something(self):
        print('do something...')
        return 'res'


async def test():
    async with AsyncMyContextManger() as f:
        v = await f.do_something()
        print(v)


def main():
    # asyncio.run(test())
    with MyContextManger() as f:
        v = f.do_something()
        print(v)


if __name__ == '__main__':
    main()
