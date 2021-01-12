class A:
    def __init__(self):
        # 只有本类内部才能访问私有方法
        self.__sleep()

    def cry(self):
        print('cry')

    @staticmethod
    def _laugh():
        print('_laugh')

    @staticmethod
    def __sleep():
        print('__sleep')


class B(A):
    def __init__(self):
        super().__init__()
        # 子类可以访问父类的受保护的方法
        self._laugh()
        # 子类不可以访问父类的私有方法
        # self.__sleep()


def main():
    b = B()
    # 对象只能访问公开方法
    b.cry()


if __name__ == '__main__':
    main()
