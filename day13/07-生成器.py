# 简单的生成器函数
def my_gen():
    n = 1
    print("first")
    yield n

    n += 1
    print("second")
    yield n

    n += 1
    print("three")
    yield n

# 调用使用生成器的函数中含有yield关键字 表示返回一个生成器对象
generator1 = my_gen()
print(generator1, type(generator1))
# 当使用next函数的时候才能返回出值 而且还会运行我们的生成器函数
# 每次调用generator1，函数都会从之前的保存的状态继续执行 直到没有任何的yield
# 如果没有更多的yield  则StopIteration报错
# print(next(generator1))  # 寻找到的是第一个yield n
# print(next(generator1))
# print(next(generator1))
# print(next(generator1))  # 没有跟多的yield 则报错

# 使用for循环获取生成器中的元素 没有更多的值 自动终止
for item in generator1:
    print(item)
