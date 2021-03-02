import functools


def test(x, y):
    return x + y


fun = functools.partial(test, 1, 2)
print(fun())
