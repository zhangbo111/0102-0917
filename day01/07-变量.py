# 变量的使用 直接用变量名即可
# 把变量名和变量用=连接 这是一个赋值的过程
num1 = 1
num2 = 2.2
num3 = num1 + num2
print(num3)
# 检查一个数据的类型
val_type = type(num1)
print(val_type)
# 判断一个数据的类型是不是指定的类型
# 第一个参数表示被检查的变量名，第二个是判断的类型
# 返回的是布尔值
bool1 = isinstance(num2, int)
print(bool1)


