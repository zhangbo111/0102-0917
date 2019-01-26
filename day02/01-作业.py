# i = 1
# while i <= 5:
#     print(' '*(5 - i), end='')
#     j = 1
#     # 需要执行完里面的循环 外面的循环才会执行
#     while j <= i:
#         # 第二层循环不换行
#         print('*', end='')
#         j += 1
#     # 第一层循环 自动换行
#     print('')
#     i += 1

# i = 1
# while i <= 5:
#     j = 1
#     if i == 2 or i == 4:
#         i += 1
#         continue
#     if i == 1:
#         print('  ', end='')
#     if i == 3:
#         print(' ', end='')
#     # 需要执行完里面的循环 外面的循环才会执行
#     while j <= i:
#         # 第二层循环不换行
#         print('*', end='')
#         j += 1
#     print('')
#     i += 1

# i=1
# while i<=5:
#     a=5
#     while a>=i:
#         print(' ',end='')
#         a-=1
#     b=1
#     while b<=i:
#         print('*',end='')
#         b+=1
#     print('')
#     i+=1

# i = 1
# while i <= 5:
#     j = 5
#     while j > i:
#         print(' ', end='')
#         j -= 1
#     k = 1
#     while k <= i:
#         print('*', end='')
#         k += 1
#     print('')
#     i += 1

# i = 1
# while i <= 3:
#     j = 2
#     while j >= i:
#         print(' ', end='')
#         j -= 1
#     k = 1
#     while k <= 2*i - 1:
#         print('*', end='')
#         k += 1
#     print('')
#     i += 1

# i=1
# while i<=5:
#     j=6
#     while j>i:
#         print(" ",end="")
#         j -= 1
#     while i>=j:
#         print('*'*i)
#         break
#     print('')
#     i+=1

# i=0
# while i<5:
#     k=5
#     while k>i:
#         k-=1
#         print(" ",end="")
#     j = 0
#     while j <= i:
#          j += 1
#          print("*", end="")
#     i+=1
#     print()

# i=1
# while i<=3:
#     j=3
#     while j>=i:
#         print(" ",end="")
#         j-=1
#     while i >j:
#         print('*'*(2*i-1))
#         break
#     print("")
#     i+=1


