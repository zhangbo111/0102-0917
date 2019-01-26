# 添加一个元素进入集合 集合是无序的
set1 = {2, 5, '世界很大'}
# 只能添加一个
set1.add('我却很渺小')
print(set1)
# 将列表中的数据一个一个添加进集合
set1.update(['a', '不需要'])
print(set1)

set2 = {1, 2, 3, 4, 5, 32, 34}
# 随机删除集合里面的元素
# del_data = set2.pop()
# print(del_data)
# print(set2)
# 删除指定的元素 不存在则报错
# set2.remove(5)
# print(set2)
# 删除指定元素 不存在不报错 不做任何的操作
set2.discard(6)
print(set2)

