import random

# 获取0-1之间的随机小数
print(random.random())

# 随机获取列表中的一个元素
print(random.choice([1, 2, 3, 4, "一", '二', '三', '四']))

# 随机打乱一个序列
math_list = [1, 2, 3, 4, "一", '二', '三', '四']
random.shuffle(math_list)
print(math_list)

# 获取指定范围内的间隔随机整数  第三个参数是间隔值
print(random.randrange(5, 15, 2))

# 获取指定范围内的随机小数
print(random.uniform(5, 15))

# 获取指定范围内的随机整数  要前也要后
print(random.randint(5, 5))
