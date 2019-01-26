# 把字符串str1放在指定的长度中，居中摆放
# 可以指定填充内容 如果没有指定填充内容 则使用空格填充
# 如何不能居中，指定的长度为偶数则填充内容左短右长
# 如果不能居中，指定的长度为奇数则填充内容左长右短
str1 = '123'
result1 = str1.center(6, '#')
print(result1)

# ljust表示字符串在指定的长度中左对齐，可以指定填充内容
# 默认是以空格填充
str2 = '123'
result2 = str2.ljust(10, '#')
print(result2)
# rjust表示字符串在指定的长度中右对齐，可以指定填充内容
# 默认是空格填充
str3 = '123'
result3 = str3.rjust(10, '#')
print(result3)
# 没有指定的填充字符 右对齐 默认是0进行填充
str4 = '123'
result4 = str4.zfill(10)
print(result4)

# format方法是将参数依次的传给str5中的大括号，生成新的字符串
str5 = "{} very {}"
result5 = str5.format('today', 'happy')
print(result5)

# strip去除两边的空格 可以指定字符进行删除 默认是空格
str6 = ' 123***'
result6 = str6.strip('*')
print(result6)
# 删除左边指定的字符 如何没有指定字符 默认是空格
str7 = '*123***'
result7 = str7.lstrip('*')
print(result7)
# 删除右边指定的字符 如何没有指定字符 默认是空格
str8 = '*123***'
result8 = str8.rstrip('*')
print(result8)

str9 = """  1387649@163.com 88 
** 18645825642 && 
hellochinapython 
"""
# 练习：把邮箱，电话，china提取出来
result9 = str9.splitlines()
print(result9)
# 提取email
email1 = result9[0]
email2 = email1.strip()
email_result = email2[:15]
print(email_result)
# 提取电话
phone1 = result9[1]
print(phone1[3:14])
# 提取china
china1 = result9[2]
print(china1[5:10])


