class A:
    pass


class B(A):
    pass


def main():
    a = A()
    b = B()

    print(type(a))
    print(type(b))

    print(isinstance(a, A))
    # 结果为True 表明 isinstance()可以判断对象是否是某个类的直接实例或者间接实例（类继承）
    print(isinstance(b, B))
    print(isinstance(b, A))


if __name__ == '__main__':
    main()
