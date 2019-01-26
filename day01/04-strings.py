# 三种方式声明字符串
# 单引号声明字符串
str1 = 'hello world'
print(str1)
# 双引号声明字符串
str2 = "人生苦短 我用python"
print(str2)
# 三引号声明字符串
str3 = '''hello world, 我用python'''
print(str3)
# 三引号换行输出
str4 = '''
hello world
我用python
'''
print(str4)
# 单引号里面可以包含双引号
str5 = '鲁迅说："阿甘是当代人的通病"'
print(str5)
# 双引号里面可以包含单引号
str6 = "三体：'这是一部很好看的科幻小说'"
print(str6)
# 三引号里面可以同时包含单引号和双引号
str7 = """人生"已经"如此'艰难'"""
print(str7)
# 常见转义字符 换行
str8 = '1\n2'
print(str8)
# \t表示横向制表符
str9 = '1\t2'
print(str9)
# 回车之后前面的字符不打印
str10 = '123\r2'
print(str10)

# 作业：开通CSDN博客，博客地址给我。

# 元字符串输出 对转义的字符原样输出
str11 = r'1\n2'
print(str11)
# 元字符串 原样输出所有字符
strval=R'锄禾日当午，\n汗滴\\禾下土，谁知\r盘中餐，\n粒粒\t辛苦'
print(strval)
