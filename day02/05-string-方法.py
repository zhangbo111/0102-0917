mystr = 'hello world'
# 查看o在mystr字符串出现的次数 不存在返回0次
print(mystr.count('o'))
# find表示查找o在mystr的索引位置
# 返回的是第一个查找到的位置 不存在则返回-1
print(mystr.find('o'))
# 从右往左 返回第一个出现的位置 不存在则返回-1
print(mystr.rfind('o'))
# index表示从左到右 查找第一个出现的位置 不存在则报错
print(mystr.index('o'))
# rindex表示从右到左 查找第一个出现的位置 不存在则报错
print(mystr.rindex('o'))

# 按照指定的字符串分割成三个部分分别是（指定字符之前的字符，
# 指定字符本身，指定字符之后的字符） 然后组成一个元组进行返回
mystr1 = 'hello world python'
result = mystr1.partition('world')
print(result)
# 打印输出类型
print(type(result))

# 按照换行符分割 返回的是每一行组成的列表
mystr2 = 'hello \n world \n python'
print(mystr2)
print(mystr2.splitlines())

# replace表示替换函数， 第一个参数是被替换的字符，
# 第二个参数是新字符 后面的1表示替换的次数（1） 不写默认替换所有
mystr3 = 'how are you'
print(mystr3.replace('o', 'a', 1))


