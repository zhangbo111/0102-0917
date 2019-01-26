# # # # a = 1
# # # # # while a<=9:
# # # # #    b = 1
# # # # #    while b <= a:
# # # # #       print('%d*%d=%d'%(b,a,a*b),end='\t')
# # # # #       b+=1
# # # # #    print('')
# # # # #    a+=1
# # # #
# # # #
# # # #
# # # # # for i in range(1,10):
# # # # #    for a in range(1,i+1):
# # # # #       print('%d*%d=%d'%(a,i,i*a),end='\t')
# # # # #    print('')
# # # # #
# # # # # for i in range(1,10):
# # # # # #    for a in range(i, 10-1):
# # # # # #       print(end='        ')
# # # # # #    for b in range(1,i+1):
# # # # # #       print('%d*%d=%2d'%(b,i,i*b),end='\t')
# # # # # #    print('')
# # # # #
# # # # #
# # # # #
# # # # # for i in range(1,10):
# # # # #    for a in range(i,10):
# # # # #       print('%d*%d=%d'%(i,a,i*a),end='\t')
# # # # #    print('')
# # # # #
# # # # # for i in range(1,10):
# # # # #    for a in range(1,10-i):
# # # # #       print(end='        ')
# # # # #    for b in range(1,i+1):
# # # # #       print('%d*%d=%d'%(i,b,i*b),end='\t')
# # # # #    print('')
# # # # #
# # # # # for i in range(1,10):
# # # # #      for k in range(1,10-i):
# # # # #          print(" "*7,end='')
# # # # #      for j in range(1,1+i):
# # # # #          print("%d*%d=%2d" % (j,i,j*i),end=" ")
# # # # #      print ("")
# # # # #
# # # # #
# # # # # a = 1
# # # # # while a <=9:
# # # # #    b=1
# # # # #    while b <= 9-a:
# # # # #       print('        ',end='')
# # # # #       b+=1
# # # # #    c = 1
# # # # #    while c <=a:
# # # # #       print('%d*%d=%2d'%(a,c,a*c),end='\t')
# # # # #       c+=1
# # # # #    print('')
# # # # #    a+=1
# # # #
# # # # str1 = [12, 13, 14, 12, 16, 17, 18, 16]
# # # # print(set(str1))
# # # #
# # # # str2 = []
# # # # for i in str1:
# # # #     if i not in str2:
# # # #         str2.append(i)
# # # # print (str2)
# # # #
# # # #
# # # # str3 = list({}.fromkeys(str1).keys())
# # # # print (str3)
# # # #
# # # # 九九乘法表一
# # # for i in range(1, 10):
# # #     for j in range(1, i + 1):
# # #         print('{} * {} = {: <2}'.format(j, i, i*j), end=' ')
# # #     print()
# # #
# # # print()  # 这是给2个乘法表分开
# # #
# # # # 九九乘法表二
# # # i = 1
# # # while i <= 9:
# # #     j = 9
# # #     while j >= i:
# # #         print('{} * {} = {: <2}'.format(j, i, i * j), end=' ')
# # #         j -= 1
# # #     i += 1
# # #     print()
# # #
# # # # 九九乘法表三
# # # for i in range(1, 10):
# # #     for j in range(1, 10 - i):
# # #         print(' '*11, end='')
# # #     for k in range(1, i + 1):
# # #         print('{} * {} = {: <2}'.format(k, i, i * k), end=' ')
# # #     print()
# # #
# # # print()  # 这是给2个乘法表分开
# # #
# # # # 九九乘法表四
# # # i = 1
# # # while i <= 9:
# # #     j = 1
# # #     while j < i:
# # #         print(' '*11, end='')
# # #         j += 1
# # #     j = 9
# # #     while j >= i:
# # #         print('{} * {} = {: <2}'.format(i, j, i * j), end=' ')
# # #         j -= 1
# # #     i += 1
# # #     print()
# # # 去重
# # lst = [1, 2, 3, 2, 3, 4]
# # lst = [1, 2, 2, 3, 3, 4]
# # # 第一种  集合可以去重  先转换成集合再转换成列表
# # print("方法一：", list(set(lst)))
# #
# # # 作业：使用另外的方式去重（至少两种）
# # # 第二种
# # lst.sort()
# # del_lst = []
# # for i in range(len(lst) - 1):
# #     if lst[i] == lst[i + 1]:
# #         del_lst.append(lst[i + 1])
# # for j in del_lst:
# #     lst.remove(j)
# # print("方法二：", lst)
# #
# # # 第三种
# # new_lst = []
# # for k in lst:
# #     if k not in new_lst:
# #         new_lst.append(k)
# # print("方法三：", new_lst)
# #
# # # 第四种
# # # fromkeys 是把所有的键都赋同样的值（如果不指定内容则默认赋值为None）
# # lst1 = []
# # dct = dict.fromkeys(lst)
# # print(dct)
# # for n in dct:
# #     lst1.append(n)
# # print("方法四：", lst1)
# #
# # # 第五种  第四种方法的简写
# # print("方法五：", list(dict.fromkeys(lst)))
# # #

# lst = [1, 2, 3, 2, 3, 4]#第一种
# [get.append(i) for  i in lst if i not in get]
# print(get)
#
#
# formatList = list({}.fromkeys(lst).keys())#第二种
# print(formatList)
#第一种
for i in range(1,10):
     for j in range(i,10):
         print('{}*{}={: <2}'.format(j, i, i * j), end=' ')
     print("")

#第二种
for i in range(1,10):
     for k in range(1,i):
         print (end="       ")
     for j in range(i,10):
         print('{}*{}={: <2}'.format(j, i, i * j), end=' ')
     print("")
