# name = 'Eric_green'
#
# # 循环：把字符串中的所有字符一个一个拿出来进行使用
# # i第一次会赋值为E，最后一次为n
# for i in name:
#     print('-'*20)
#     print(i)

# 在循环里面嵌套if语句（条件判断）
# break是终止循环
# name = 'student'
# for i in name:
#     print('----')
#     if i == 'd':
#         break
#     print(i)

# 首先while判断后面的条件
# 如何为true则执行while循环里面的代码
# 每次执行完while里面的代码之后，
# 都要再次判断 while后面的是否为真
# 永远循环
# while True:
#     print('永远循环')

# while后面如何是false，则终止循环
# i = 0
# while i < 5:
#     print(i)
#     i += 1
# break嵌入到while循环 if后面的条件为真 则终止循环
# i = 0
# while i < 5:
#     print(i)
#     if i == 3:
#         # 当i等于3时跳出循环
#         break
#     i += 1
# continue表示跳过本次循环 且本次循环以后的代码不执行
# i = 0
# while i < 5:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1
# for 循环的continue，跳过本次循环，循环下一个字符
# name = 'student'
# for i in name:
#     print('----')
#     if i == 'd':
#         continue
#     print(i)

# name = 'student'
# for i in name:
#     # end参数表示不换行的意思
#     print(i, end='')

i = 1
while i <= 5:
    j = 1
    # 需要执行完里面的循环 外面的循环才会执行
    while j <= i:
        # 第二层循环不换行
        print('*', end='')
        j += 1
    # 第一层循环 自动换行
    print('')
    i += 1

# 代码敲两遍
# 输出以下图形,选做
'''
    *
   **
  ***
 ****
*****
'''
'''
  *
 ***
*****
'''
# 最后把代码上传到CSDN
