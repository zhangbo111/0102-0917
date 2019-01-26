set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# 获取两个集合的并集 可以交换位置
bingji = set1.union(set2)
print(bingji)
# 获取两个集合的交集
jiaoji = set1.intersection(set2)
print(jiaoji)
# 差集 在set1里面的但是不在set2里面的
diff = set1.difference(set2)
print(diff)
# 对称差集 相当于并集减去交集
result = set1.symmetric_difference(set2)
print(result)















