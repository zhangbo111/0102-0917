# 大量的参数
# *args *是固定写法 接收多个 args是常用的参数名
def say_hello(*args):
    print(args, type(args))
# 当我们不传递参数时 args接收的是空元组
say_hello()
# 不管它传多少的参数过去 只要不是关键字参数 全部由args接收
# args是一个元组
say_hello('大江大河', '知否', '琅琊榜', '仙剑奇侠传')
# 传递单个也可以 args还是元组
say_hello(1)





