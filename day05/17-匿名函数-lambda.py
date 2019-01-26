# # 常规的函数
# def odd_eve(num):
#     if num % 2 == 0:
#         return '偶数'
#     else:
#         return "奇数"
# result = odd_eve(3)
# print(result)
# 匿名函数 没有函数名 没有return 和 for 循环 可以有if
func = lambda num: "偶数" if num % 2 == 0 else "奇数"
# 实参4 传递给 形参num
# 如果if后面的bool值为真 则返回前面的内容
# 如果 if 后面的bool为假 则返回else 语句后面的内容
result = func(4)
print(result)

# 传入多个参数
f = lambda x, y: x + y if 0 < x < 100 and 0 < y < 100 else "too big or too small"
result1 = f(3, 102)
print(result1)
result2 = f(3, 97)
print(result2)
