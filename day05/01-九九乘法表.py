# # 需要从9 到 1的输出
# for i in range(1, 10):
#     print(' '*7*(i - 1), end='')
#     i = 10 - i
#     for j in range(1, i+1):
#         print("{}*{}={: >2}".format(i, j, i*j), end=' ')
#     print()

# for i in range(1, 10):
#     print(' ' * 7 * (9 - i), end='')
#     k = i
#     for j in range(1, i + 1):
#         print("{}*{}={: >2}".format(k, i, i * k), end=' ')
#         k -= 1
#     print()


# # 第一步 先打印第一行
# i = 9
# for j in range(1, i+1):
#     print("{}*{}={: >2}".format(i, j, i*j), end=' ')
#
# # 第二步
# # 第一行 --》 i = 9
# # 第二行 --》 i = 8
# # 第三行 --》 i = 7 ...
# # 第九行 --》 i = 1
# for i in range(1, 10):
#     i = 10 - i
#     print(i)

# i = 9
# for j in range(1, i + 1):
#     print('{}*{}={: >2}'.format(i, j, i*j), end=' ')

# for i in range(1, 10):
#     print(' '*7*(i-1), end='')
#     i = 10 - i
#     for j in range(1, i + 1):
#         print('{}*{}={: >2}'.format(i, j, i * j), end=' ')
#     print()
