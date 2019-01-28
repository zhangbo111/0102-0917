# 选择排序算法
# def select_sort(lst):
# #     for i in range(len(lst) - 1):  # 只需要循环len(lst) - 1次
# #         k = i
# #         for j in range(i, len(lst)):   # k是已知最小元素的位置  这个循环就是把最小元素k找出来
# #             if lst[j] < lst[k]:
# #                 k = j
# #         if i != k:             # lst[k] 是确定的最小元素,检查是否需要交换
# #             lst[i], lst[k] = lst[k], lst[i]
# #     print(lst)
# # select_sort([3, 2, 4, 1, 5])
'''
第一次: k = i = 0  k表示最小值的位置（索引）
j = 0 --> 4
lst[0] < lst[0]
lst[1] < lst[0]  如果为True  k = 1
lst[2] < lst[1]
lst[3] < lst[1]  k = 3
lst[4] < lst[3]  找到最小的数
此时k = 3  i = 0
交换位置 交换两者的位置
lst[0], lst[3] = lst[3], lst[0]

第二次：跟第一次类似
选择排序是查找最小的数放在第一个位置，依次直到全部排完
'''


# 冒泡(交换)排序算法
def bubble_sort(lst):
    for i in range(len(lst)):
        found = False
        print(lst)
        for j in range(1, len(lst) - i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                found = True
            print(lst)
        # print(lst)
        if not found:
            break
    print(lst)
bubble_sort([30, 13, 25, 16, 47, 26, 19, 10])
'''
第一次：i = 0 --> 7
found = False
j = 1 -->  7 - i = 7  2.当 i = 1     j = 1 --> 7 - 1 = 6 ... i = 6  j = 1 --> 1
i = 0 
j = 1
lst[0] > lst[1]
[30, 13, 25, 16, 47, 26, 19, 10]
[13, 30, 25, 16, 47, 26, 19, 10]    found = True
j = 2
lst[1] > lst[2]
[13, 25, 30, 16, 47, 26, 19, 10]
[13, 25, 16, 30, 47, 26, 19, 10]
[13, 25, 16, 30, 47, 26, 19, 10]
[13, 25, 16, 30, 26, 47, 19, 10]
[13, 25, 16, 30, 26, 19, 47, 10]
[13, 25, 16, 30, 26, 19, 10, 47]

冒泡排序：就是把最大的数通过交换位置放到最后面
'''




# # 快速排序 20世纪最具影响力的算法之一
# def quick_sort(lst):
#     qsort_rec(lst, 0, len(lst)-1)
#     # print(lst)
#
#
# def qsort_rec(lst, l, r):
#     if l >= r:
#         return   # 分段无记录 或只有一个记录  只有一个数值的时候 下面就不进行了
#     i = l
#     j = r
#     pivot = lst[i]  # 是初始空位
#     while i < j:    # 找pivot的最终位置
#         while i < j and lst[j] >= pivot:  # 最后一个和第一个进行比较  后面大则 进行下去
#             j -= 1                   # 用j向左扫描小于pivot的记录
#         if i < j:
#             lst[i] = lst[j]
#             i += 1                  # 小记录移动到左边
#             print(lst)
#         while i < j and lst[i] <= pivot:
#             i += 1                     # 用i向右扫描找大于pivot的记录
#         if i < j:
#             lst[j] = lst[i]
#             j -= 1                  # 大记录移到右边
#             print(lst)
#     lst[i] = pivot  # 将pivot存入其最终位置
#     # print(lst)
#     qsort_rec(lst, l, i-1)               # 递归处理左半区间
#     qsort_rec(lst, i+1, r)                # 递归处理右半区间
#
#
# # quick_sort([30,13,25,16,47,26,19,10])
# quick_sort([4, 3, 5, 1, 2])
#



# 快速排序
# 通过一趟排序将要排序的数据分割成独立的两部分
# 其中一部分的所有数据都比另外一部分的所有数据都要小
# 然后再按此方法对这两部分数据分别进行快速排序
# 整个排序过程可以递归进行
# 以此达到整个数据变成有序序列。


def first_sort(numbers, i, j):
    # i是第一个数的索引 j是最后一个数的索引
    # 初始i = 0   j = len(numbers) - 1
    # 第一个数为temp
    temp = numbers[i]
    # 如果只有一个数字就不需要排序了 索引当列表长度大于1的时候下面就为True
    while i != j:
        # 在i = j的时候终止循环
        # 最后一个数和第一个数相比较 如果最后一个数大于第一个数
        # 则j -= 1， 如果第一个数和最后一个数相等或者小于第一个数
        # 则交换第一个数 从右边开始算 找到第一个小于等于第一个数的数
        # 然后把这个数赋值给第一个数
        while i < j and numbers[j] > temp:
            j = j-1
        numbers[i] = numbers[j]
        print("1", numbers)
        # 从左边开始寻找 找到第一个大于或者等于原始第一个数的数放到j的位置
        while i < j and numbers[i] < temp:
            i = i+1
        numbers[j] = numbers[i]
        print("2", numbers)
    numbers[i] = temp
    print("3", numbers)
    return i
def quickSort(numbers, i, j):
    # 初始i = 0   j = len(numbers) - 1
    if i < j:
        middle = first_sort(numbers, i, j)
        quickSort(numbers, i, middle-1)
        quickSort(numbers, middle+1, j)
if __name__ == '__main__':
    list1 = [2, 3, 5, 7, 8, 9, 6, 54, 1, 42]
    print(list1)
    quickSort(list1, 0, len(list1)-1)
    print(list1)


