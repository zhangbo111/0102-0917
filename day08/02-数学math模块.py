import math

# 向上取整
print(math.ceil(2.00001))

# 向下取整
print(math.floor(2.9999))

# 四舍五入
print(round(2.3))
print(round(2.5))  # n.5 n为偶数是舍
print(round(3.5))  # n.5 n为奇数是进

# 计算一个数的几次方 第一个参数是底数 第二个参数的幂
# 返回的是小数
print(math.pow(5, 3))

# 开平方 返回的也是小数
print(math.sqrt(5))

# 获取一个的绝对值 小数
print(math.fabs(-12.4))

# 获取一个数的绝对值 整数
print(abs(-12))

# 将小数和整数分开 小数不是很准确
print(math.modf(23.42))

# 将后面的数的正负号 赋值给前面的数
result = math.copysign(-23, 34)
print(result)

# 求和 返回浮点数
print(math.fsum([1, 2, 3]))

# 求和 返回整数
print(sum([1, 2, 3]))

# 获取圆周率
print(math.pi)

# 获取自然对数
print(math.e)
