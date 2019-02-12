# #
# 5.选择排序：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，
# 将它与r1交换；第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，
# 将它与r2交换；以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，
# 将它与r[i]交换，使有序序列不断增长直到全部排序完毕
#  选择排序算法
# # def select_sort(lst):
# #     for i in range(len(lst) - 1):  # 只需要循环len(lst) - 1次
# #         k = i
# #         for j in range(i,len(lst)):   # k是已知最小元素的位置  这个循环就是把最小元素k找出来
# #             if lst[j] < lst[k]:
# #                 k = j
# #         if i != k:             # lst[k] 是确定的最小元素,检查是否需要交换
# #             lst[i],lst[k] = lst[k],lst[i]
# #     print(lst)
# #
# #
# # select_sort([3, 2, 4, 1, 5])
#
# 3.冒泡排序：它重复地走访过要排序的数列，一次比较两个元素，
# 如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，
# 也就是说该数列已经排序完成

# # # 冒泡(交换)排序算法
# # def bubble_sort(lst):
# #     for i in range(len(lst)):
# #         found = False
# #         print(lst)
# #         for j in range(1, len(lst) - i):
# #             if lst[j-1] > lst[j]:
# #                 lst[j-1], lst[j] = lst[j], lst[j-1]
# #                 found = True
# #         # print(lst)
# #         if not found:
# #             break
# #     # print(lst)
# #
# #
# # bubble_sort([30, 13, 25, 16, 47, 26, 19, 10])
#
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
