# 迭代器原理
import asyncio


class MyIteration:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def deadline(self):
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __next__(self):
        get_value = self.deadline()
        if get_value is None:
            raise StopIteration()

        return self.count


class AsycMyIteration:
    def __init__(self):
        self.count = 0

    def __aiter__(self):
        return self

    async def deadline(self):
        # await asyncio.sleep(0.08)
        self.count += 1
        if self.count > 100:
            return None
        return self.count

    async def __anext__(self):
        get_value = await self.deadline()
        if get_value is None:
            raise StopIteration()
        return self.count


async def test():
    try:
        async for item in AsycMyIteration():
            print(item)
    except:
        pass


def main():
    asyncio.run(test())

    pass
    # myiteration = MyIteration()
    # for myi in myiteration:
    #     print(myi)


if __name__ == '__main__':
    main()
