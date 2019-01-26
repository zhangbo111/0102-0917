# 创建的第一种方式 自动过滤掉重复元素
set1 = set((1, 2, 3, 1, 2, 3))
print(set1)
# 创建集合的第二种方式
set2 = {1, 3, 5, 3, 5, 7}
print(set2)
# 集合不支持下标访问
# result = set2[0]
# print(result)

set3 = {'a', 'b', 'c', 'd'}
set4 = {'c', 'd', 'e', 'f'}
# 获取两个集合的交集
result1 = set3 & set4
print(result1)
# 获取两个集合的并集
result2 = set3 | set4
print(result2)
# 获取set3对set4的差集
result3 = set3 - set4
print(result3)
# 对称差集 相当于并集减去交集
result4 = set3 ^ set4
print(result4)






