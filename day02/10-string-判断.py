# 判断字符串是否只有字母或者数字
# 字符串仅有字母或者数字则返回True 反之则返回False
str1 = 'abc123de'
bool_res = str1.isalnum()
print(bool_res)
# 判断字符串时候只有字母组成 是返回True 否返回False
str2 = 'abc123de'
bool_res1 = str2.isalpha()
print(bool_res1)
# 判断字符串是否只由数字组成，如何是则放回True，否则返回False
str3 = '12a3'
bool_res2 = str3.isdigit()
print(bool_res2)
# 判断字符串里面的字母是否都是大写字母 是返回True 否 返回False
str4 = 'YOU ARE A JOK'
bool_res3 = str4.isupper()
print(bool_res3)
# 判读字符串里面的字母是否都是小写字母 是返回True 否返回 False
str5 = 'you are my sinny'
bool_res4 = str5.islower()
print(bool_res4)
# 判断字符串中的每个单词的首字母是否都是大写 是返回True 否返回False
str6 = 'This is A Kidding'
bool_res5 = str6.istitle()
print(bool_res5)
# 判断字符串是否由空格组成 是返回True 否返回False
str7 = ' dd'
bool_res6 = str7.isspace()
print(bool_res6)
# 判断字符串是否以指定的字符开头 是返回True 否返回False
str8 = 'today is very beautiful day'
bool_res7 = str8.startswith('today')
print(bool_res7)
# 判断字符串是否以指定字符结尾 是返回True 否返回False
str9 = 'i can do it'
bool_res8 = str9.endswith('it')
print(bool_res8)
# 通过指定的分隔符 对字符串进行分割 返回分割后的字符串组成列表
str10 = 'i0an0hungry'
result10 = str10.split('0')
print(result10)

str11 = """She stopped abruptly. 123 She was about to end with 
"how poor you are," and && recognized, somewhat late, 
that they were words 23 &&which politeness might not approve.
 
"""
# 第一行：判断是否由数字或者字母组成，判断是否每个单词的首字母都是大写
# 第二行：判断是否由全由字母组成
# 第三行：以23为分割 分割后组成一个列表
# 第四行：判断第四行是不是只有空格的字符串

# split以换行分割 最后一行也会进行分割
# splitlines 则不会进行最后一行分割
# lines = str11.split('\n')
# print(lines)

lines = str11.splitlines()
# 第一行
line1 = lines[0]
print(line1)
print(line1.isalnum())
print(line1.istitle())
# 第二行
line2 = lines[1]
print(line2.isalpha())
# 第三行
line3 = lines[2]
print(line3.split('23'))
# 第四行
line4 = lines[3]
print(line4.isspace())
