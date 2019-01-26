# 输出2-15的质数
# 质数：因数只有自己和1的数叫做质数。

for i in range(2, 16):
    # print(i)
    for j in range(2, i):
        # print(j)
        if i % j == 0:
            print('{}不是质数'.format(i))
            # 终止内层的循环 不是外层的循环
            break
    # 当前面的for正常运行 没有遇到break时执行这里
    else:
        print('{}是质数'.format(i))


# # 表示从0到9打印出来
# # for i in range(10):
# #     print(i)
# # # 表示从2到9打印出来 要前不要后
# # for j in range(2, 10):
# #     print(j)






