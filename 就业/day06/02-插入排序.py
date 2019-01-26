def insert_sort(lst):
    for index in range(1, len(lst)):
        print(index, lst[index])
        # 使用x将需要做判断的数字 储存起来
        x = lst[index]   # index = 3 的时候 x = 1
        # 将索引赋值给 j
        j = index   # j = index = 3
        # 判断前面一位跟x比较大小 如果前面的大则交换位置
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j - 1]   # lst[3] = lst[2]
            j -= 1
        lst[j] = x
    return lst


lst = [3, 2, 4, 1, 5, 32, 12, 78, -3]
result = insert_sort(lst)
print(result)





