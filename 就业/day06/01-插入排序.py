
'''
插入排序
lst = 【3， 2， 4， 1， 5】

[2, 3, 4]   1
[1, 2, 3, 4]

[0, 2, 4]  1
[0, 1, 2, 4]

第一步：判断一个列表是否只含有一个数字

第二步：判断第二个数字与第一个数字比较大小,
如果第二个数字大于第一个数字则，不用动任何操作
如果第二个数字小于第一个数字 两个数字交换位置.
首先将第二个数字保存在x当中   x = lst[1] = 2
lst[1] = lst[0]
lst[0] = x

lst = 【2， 3， 4， 1， 5】

第三个数字是4与他前面的最大数相比较 也就是他的前一位数字
大于则不做任何操作

第四个数字判断与他前面一位进行比较 如果大于则不做任何操作
如果小于则交换位置 x = lst[3] = 1
lst [3] = lst[2]
lst = 【2， 3， 4， 4， 5】
lst [2] = lst [1]
lst = 【2， 3， 3， 4， 5】
lst [1] = lst [0]
lst = 【2， 2， 3， 4， 5】
lst [0] = x
lst = 【1， 2， 3， 4， 5】

lst = 【0， 3， 4， 1， 5】
lst[3] = lst [2]
lst = 【0， 3， 4， 4， 5】
lst [2]  = lst [1]
lst = 【0， 3， 3， 4， 5】
lst [1]  = x
lst = 【0， 1， 3， 4， 5】

'''
