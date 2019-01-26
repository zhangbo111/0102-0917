# 使用input函数输入三位数，然后倒叙输出，例如：输入672，输出276
# 接受一个字符串三位数
num_str = input("请输入三位数：")
# 将字符串转换为整型
num = int(num_str)
# print(num)
# print(type(num))
# 获取个位上面的数字
gewei = num % 10
# print(gewei)
# 获取十位上面的数字
shiwei = (num // 10) % 10
# print(shiwei)
# 获取百位上面的数字
baiwei = num // 100
# print(baiwei)
# 生成倒序输出我们的结果
result = gewei * 100 + shiwei * 10 + baiwei
print(result)
