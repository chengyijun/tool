from types import MethodType


class A:
    # __slots__ 作用为限制类A只能动态绑定指定的属性与方法
    __slots__ = ('fun', 'set_age')


def set_age(self, age):
    self.age = age


def main():
    a = A()

    a.set_age = MethodType(set_age, A)
    a.fun = lambda x: print('hahaha ', x)

    a.set_age(12)

    print(a.age)
    a.fun('abel')


if __name__ == '__main__':
    main()
