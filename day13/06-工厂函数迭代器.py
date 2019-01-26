# 创建迭代器对象
# 用法iter（iterable） 将可迭代对象转化为迭代器
# 可迭代对象：列表，元组，集合，迭代器
tup1 = (1, 2, 3)
# for i in tup1:
#     print(i)
# 工厂函数iter（）转换为迭代器
iterator1 = iter(tup1)
print(iterator1, type(iterator1))
# 获取迭代器中的元素
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# print(next(iterator1))
# 全部取出来
# for item in iterator1:
#     print(item)
# 获取的第三种方式
print(iterator1.__next__())
print(iterator1.__next__())
print(iterator1.__next__())
# print(iterator1.__next__())
