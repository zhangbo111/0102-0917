# 快速排序
# 通过一趟排序将要排序的数据分割成独立的两部分
# 其中一部分的所有数据都比另外一部分的所有数据都要小
# 然后再按此方法对这两部分数据分别进行快速排序
# 整个排序过程可以递归进行
# 以此达到整个数据变成有序序列。
'''
原理：
[9, 3, 5, 7, 8, 2, 6, 54, 1, 42，18，12]
以第一个数9为中心，大于9 放在右边
小于9的放在左边
[5，3, 1, 7, 8, 2, 6, 9, 18, 42，54，12]
再在[5，3, 1, 7, 8, 2, 6 ]中选择5为标杆，小于5的放左边，大于5的放右边
[18, 42，54，12] 以18为标杆 大于18的放右边，小于18的放左边
[2, 3, 1, 5，7, 8, 6, 9, 12，18, 42，54]

[1, 2, 3, 5，6，7, 8, 9, 12，18, 42，54]

依此递归下去，直到排完
'''


def first_sort(numbers, i, j):
    # i是第一个数的索引 j是最后一个数的索引
    # 初始i = 0   j = len(numbers) - 1
    # 第一个数为temp 把第一个数存在temp
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
    list1 = [9, 3, 5, 7, 8, 2, 6, 54, 1, 42]
    print(list1)
    quickSort(list1, 0, len(list1)-1)
    print(list1)


