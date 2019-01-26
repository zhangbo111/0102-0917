# str = '''Whatever pleasure Myra may have shown at the
# commencement of this speech gave way to a mutinous frown
# as its later purport penetrated her mind. Had she not had his
# explicit promise that she should not be directly involved in
# the handling of these illicit
# '''
# # 全文：查找is在字符串当中出现的次数
# print(str.count('is'))
#
# # 第一行：查找Myra第一次出现的位置
# list = str.splitlines()
# print(list[0].find('Myra'))
#
# # 第二行：将第二行分割成'commencement of this speech gave ', 'way',' to a mutinous frown '
# print(list[1].partition('way'))
#
# # 第三行：将mind替换成branie，将p和o 替换成a和z，指定translates方法
# str1 = list[2].replace('mind', 'branie')
# intab = 'po'
# outtab = 'az'
# str_trantab = str.maketrans(intab, outtab)
# print(str1.translate(str_trantab))
#
# # 第四行：将promise提取出来，将第四行反向打印输出
# print(list[3][9:16])
# print(list[3][::-1])
#
# # 第五行：判断字符串是否都是字母组成，判断每个单词首字母都是大写
# print(list[4])
# print(list[4].isalpha())
# print(list[4].istitle())

# # 作业：代码两遍（注释加上）
# str1 = '''Whatever pleasure Myra may have shown at the
# commencement of this speech gave way to a mutinous frown
# as its later purport penetrated her mind. Had she not had his
# explicit promise that she should not be directly involved in
# the handling of these illicit
# '''
# # #全文
# cou =str1.count('is')
# print(cou)
# # #第一行
# fir = str1.find('Myra')
# print(fir)
# # #第二行
# sec = str1.splitlines()
# result1=sec[1]
# print(result1[:33])
# print(result1[33:36])
# print(result1[36:])
# #第三行
# intab = 'po'
# outab = 'az'
# result2=sec[2]
# thr = result2.replace('mind','branie')
# print(thr)
# str_tran =str.maketrans(intab,outab)
# answer = thr.translate(str_tran)
# print(answer)
# #第四行
# four = sec[3]
# print(four[9:16])
# print(four[::-1])
# four1 = four.isalpha()#是否都是字母组成
# print(four1)
# four2 = four.istitle()#首字母是否大写
# print(four2)
# #第五行
# five = sec[4]
# five1 = five.isalpha()
# print(five1)
# five2 = five.istitle()
# print(five2)
# # 全文：查找is在字符串当中出现的次数
# # 第一行：查找Myra第一个出现的位置
# # 第二行：将第二行分割成'commencement of this speech gave ',
# # 'way',' to a mutinous frown '
# # 第三行：将mind替换成branie，将p和o 替换成a和z，指定translates方法
# # 第四行：将promise提取出来，将第四行反向打印输出
# # 四五行：判断字符串是否都是字母组成，判断每个单词首字母都是大写

# # 作业：代码两遍（注释加上）
str1 = '''Whatever pleasure Myra may have shown at the
commencement of this speech gave way to a mutinous frown
as its later purport penetrated her mind. Had she not had his
explicit promise that she should not be directly involved in
the handling of these illicit
'''
# # 全文：查找is在字符串当中出现的次数
# # 第一行：查找Myra第一个出现的位置
# # 第二行：将第二行分割成'commencement of this speech gave ',
# # 'way',' to a mutinous frown '
# # 第三行：将mind替换成branie，将p和o 替换成a和z，指定translates方法
# # 第四行：将promise提取出来，将第四行反向打印输出
# # 四五行：判断字符串是否都是字母组成，判断每个单词首字母都是大写
# print(str1.count('is'))
# print(str1.find('Myra'))
# a=str1.splitlines()
# a1=a[1]
# print(a1.partition('way'))
# a2=a[2]
# a3=a2.replace('mind','branie')
# print(a3)
# intab='po'
# outtab='az'
# b=str.maketrans(intab,outtab)
# print(a3.translate(b))
# a4=a[3]
# print(a4[::-1])
# print(a4[9:17])
# print(a4.isalpha())
# print(a[4].isalpha())
# print(a4.istitle())
# print(a[4].istitle())

# #全文出现的is次数为3次
# print(str1.count('is'))
# # 第一行出现Myra的位置是18
# str2 = str1.splitlines()
# str3 = str2[0]
# print(str3.find('Myra'))
# # 第二行分割
# str4 = str2[1]
# str5 = str4.partition('way')
# print(str5)
# # 第三行替换
# str6 = str2[2]
# str7 = str6.replace('mind','branie',1)
# str8 = str7.replace('p','a')
# str9 = str8.replace('o','z')
# print(str9)
# # 第四提取，反向输出
# str10 = str2[3]
# print(str10[9:17])
# print(str10[::-1])
# #第五行判断字符组成与是否大写
# str11 = str2[4]
# print(str11.isalpha())
# print(str11.istitle())


str1 = '''Whatever pleasure Myra may have shown at the 
commencement of this speech gave 0 way 0 to a mutinous frown 
as its later purport penetrated her mind. Had she not had his 
explicit promise that she should not be directly involved in 
the handling of these illicit 
'''
# 全文：查找is在字符串当中出现的次数
str_=str1.splitlines()
print(str1.count('is'))

# 第一行：查找Myra第一个出现的位置
str_1=str_[0]
print(str_1.index('Myra'))

# 第二行：将第二行分割成'commencement of this speech gave ','way',' to a mutinous frown '
str_2=str_[1]
print(str_2.split('0'))

# 第三行：将mind替换成branie，将p和o 替换成a和z，指定translates方法
str_3=str_[2]
print(str_3.replace('mind','branie'))
str_4='as its later aurazrt aenetrated her mind. Had she nzt had his '
str_5=str.maketrans(str_3,str_4)
str_6='as its later purport penetrated her mind. Had she not had his  '
jg=str_6.translate(str_5)
print(jg)

# 第四行：将promise提取出来，将第四行反向打印输出
str_7=str_[3]
print(str_7[9:16])
print(str_7[::-1])

# 第五行：判断字符串是否都是字母组成，判断每个单词首字母都是大写
str_8=str_[4]
print(str_8.isalpha())
print(str_8.isupper())

