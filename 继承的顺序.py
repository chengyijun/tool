class AA:
    def hi(self):
        print('aa hi')


class A(AA):
    pass


class B:
    def hi(self):
        print('b hi')


class C(A, B):
    """
    继承的父类查找策略是从左到右，深度优先
    先深度，再广度
    """
    pass


c = C()
c.hi()
