name = 'no'
# id是检查一个变量或者函数在内存中的地址
print(id(name))
def func():
    pass
a = func
# 打印一个函数的名称
print(a.__name__)
