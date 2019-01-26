# 基本函数
def sqrt(x):
    return x * x
# result = sqrt(3)
# print(result)
# map的用法 第一个参数数传递函数名 第二个是传递给函数的（可循环的对象）例如：列表
# 返回一个map的对象
result = map(sqrt, [1, 2, 3])
# 将map对象转换为list 并显示出map之后的数据
lst = list(result)
print(lst)
'''
map函数：是将列表中的1，2，3一个一个传给sqrt函数
1 --> [1]
2 --> [1, 4]
3 --> [1, 4, 9]
这个[1, 4, 9]存放在map对象里面 需要转换为list才可以显示出来
'''
# map和lambda结合起来使用
result1 = map(lambda x: x + x, [1, 2, 3])
print(list(result1)) # [2, 4, 6]
