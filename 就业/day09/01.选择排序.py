# 5.选择排序：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，
# 将它与r1交换；第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，
# 将它与r2交换；以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，
# 将它与r[i]交换，使有序序列不断增长直到全部排序完毕
#  选择排序算法
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


# 选择排序算法
def select_sort(lst):
    for i in range(len(lst) - 1):  # 只需要循环len(lst) - 1次
        k = i
        for j in range(i, len(lst)):   # k是已知最小元素的位置  这个循环就是把最小元素k找出来
            if lst[j] < lst[k]:
                k = j
        if i != k:             # lst[k] 是确定的最小元素,检查是否需要交换
            lst[i], lst[k] = lst[k], lst[i]
    print(lst)


select_sort([3, 2, 4, 1, 5])
