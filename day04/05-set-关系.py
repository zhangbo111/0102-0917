set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 5}
set3 = {11, 22, 33}
# 判断set1是不是set2的超集
result1 = set1.issuperset(set2)
print(result1)
# 判断set1是不是set2的子集
result2 = set1.issubset(set2)
print(result2)
# 判断两个集合是不是不存在交集 存在返回False
result3 = set1.isdisjoint(set3)
print(result3)





