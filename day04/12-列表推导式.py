lst = []
# 负数也可以用range
for i in range(10):
    lst.append(i)
# print(lst)

# 列表推导式的方式生成列表
lst1 = [i for i in range(10)]
# print(lst1)

# 把三的倍数加入到列表当中
lst2 = []
for i in range(1, 10):
    # 三的倍数的余数为0
    if i % 3 == 0:
        lst2.append(i)
print(lst2)

lst3 = [i for i in range(1, 10) if i % 3 == 0]
print(lst3)












