str1 = 'nice'
str2 = '{} meet you'.format(str1)
# print(str2)
# :是固定的，'-'是填充符 >是填充方向为左
str3 = '{:->5}'.format(str1)
# print(str3)
# - 向右填充
str4 = '{:-<5}'.format(str1)
# print(str4)
# 2*4= 8
# 2*5=10

# 九九乘法表
# i表示纵向的 一共有9行
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}*{}={: <2}'.format(i, j, i*j), end=' ')
    # 表示换行的意思
    print()
# 作业：另外三种不同方向的九九乘法表。
# 不强调用for，可以用while循环 建议使用for循环





