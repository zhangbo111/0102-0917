lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 获取4 5 6
# for i in range(3):
#     print(i)
# 使用列表推导式的方式加入新的列表
lst1 = [lst[1][i] for i in range(3)]
print(lst1)
# 使用列表推导式获取1 4 7
lst2 = [lst[i][0] for i in range(3)]
print(lst2)
# 使用列表推导式获取1 5 9
lst3 = [lst[i][i] for i in range(3)]
print(lst3)
# 获取 3 5 7
lst4 = [lst[i][2-i] for i in range(3)]
print(lst4)
# 3 --->0 2
# 5 --->1 1
# 7 --->2 0









