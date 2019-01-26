# 占位符：把一个字符串镶嵌到另外一个字符串当中
age = '十八'
result1 = '小明今年的年龄是%s，应该高考了'%(age)
print(result1)
# 传递整型使用%d
age = 15
result2 = '小花年龄是%d，应该中考了'%(age)
print(result2)
# 定义一个元组并打印
tup1 = (1, 2, 3)
print(type(tup1))
# 定义元组的另外的方式
tup2 = 2,3,4
print(type(tup2))
# ()并不是元组的充分必要条件，逗号才是
tup3 = (1,)
print(type(tup3))
# 定义复杂的tuple
tup4 = (1, '二', (2, 3), [3, 4], {'name': 'zhang'})
print(type(tup4))

tup5 = (11, 23, 53, 31, 3, 11)
print(type(tup5))
# 访问元组中的第二个元素
print(tup5[1])
# 检测指定元素在元组中出现的次数
print(tup5.count(11))
# 元组和元组之间可以相加 生成的是新的元组
# 但是本身没有修改的方法
tup6 = ('a', 'b', [1, 2])
result3 = tup6 + ('c', 'd')
print(result3)
# append表示往列表里面添加一个元素
# 虽然元组不可修改，但是里面的元素是可变类型则可以修改里面的元素信息
tup6[2].append(3)
print(tup6)
# 以下证明tuple不可以被修改
# tup7 = (11, 22, 33)
# tup7[0] = 100
# print(tup7)

# 列表转成元组
lst = ['雅思', '托福', 'test']
print(type(lst))
tup8 = tuple(lst)
print(tup8)
print(type(tup8))
# 把字符串转换成元组
# 一个一个的字母作为一个一个的元素放进元组
str1 = 'hello'
tup9 = tuple(str1)
print(tup9)
print(type(tup9))
# 元组里面嵌套元组 复杂元组的访问
# 元组里面的数据按照下标严格访问
tup10 = (('张三', '历史'), ('apple', 'min rice'), ('松江', '鄱阳湖'))
print(type(tup10))
print(tup10[0])
print(tup10[2][1])




