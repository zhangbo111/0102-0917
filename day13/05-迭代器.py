# 声明一个列表
lst1 = [1, 2, 3, 4]
# 将列表转换为迭代器 (一)
iter1 = lst1.__iter__()
print(iter1, type(iter1))

# 按顺序获取迭代器中的元素
# 一个一个拿取数据 不放回
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))  # StopIteration迭代器中没有更多元素了 报这个错误

# 第二种获取迭代器中的元素  本质还是使用了next函数
# 这是自动触发的过程 for循环的方式在迭代器中没有更多的元素时 自动停止
for item in iter1:
    print(item)



