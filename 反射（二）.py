class A:
    def hi(self):
        print('a hi')


a = A()
# 通过getattr() 获取方法
attr = getattr(a, 'hi')
print(attr)
print(type(attr))
# 方法+() 执行方法
attr()
