class AA:
    pass


class A(AA):
    def hi(self):
        print(self)
        # 此时的super()并不是单纯的找直接父类，因为直接父类AA中并没有hi()方法，
        # 从上面打印的self（指向的是C的对象c）来看，super(A, self)依据的是父类查找规则（先深度后广度）找到的c的直接或间接父类
        print(super(A, self))
        super(A, self).hi()


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
