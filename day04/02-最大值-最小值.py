set1 = {3, 1, 6, 32, 23, 12}
# 获取序列里面的最大值
max_result = max(set1)
print(max_result)
# 获取序列里面的最小值
min_result = min(set1)
print(min_result)
# 获取整个序列的和
sum_result = sum(set1)
print(sum_result)

# （1）将下面的列表中的数按照奇数和偶数分开。存放到两个新的列表中。
# 最后输出[4, 6, 88] 和 [3, 43, 45]
lst = [3, 4, 6, 43, 45, 88]
jishu = []
oushu = []
for i in lst:
    # 获取偶数 偶数的对于2的取余为0
    if i % 2 == 0:
        oushu.append(i)
    # 获取奇数
    else:
        jishu.append(i)
print(jishu)
print(oushu)
# （2）去掉一个最大值，去掉一个最小值，求出下面列表的平均数
lst = [3, 4, 6, 43, 45, 88]
lst.remove(max(lst))
lst.remove(min(lst))
print(lst)
print(sum(lst) / len(lst))
# （3）如果不用max，min函数，如何求出下面列表的最大值和最小值
lst = [3, 1, 6, 32, 23, 12]
# 第一种方式
# lst.sort()
# print(lst[-1], lst[0])
# 默认最大值是第一个元素
max_num = lst[0]
min_num = lst[0]
# 然后从列表中一个一个与前面的最大值进行比较
for num in lst:
    if num > max_num:
        max_num = num
    # 前面的判断不成立则进行下面的判断
    elif num < min_num:
        min_num = num
print(max_num)
print(min_num)

# 3  6  32
# 3  1







