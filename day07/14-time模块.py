import time
# 上海的东八区 相对于格林尼治时间为-8个小时
print(time.timezone)

# 将时间元组转换为我们可读的时间格式
ttp = (2019, 1, 10, 15, 44, 20, 3, 0, 0)
result1 = time.asctime(ttp)
print(result1)

# 获取当前时间的时间元组
result2 = time.localtime()
print(result2)

# 获取当前时间的字符串格式
result3 = time.ctime()
print(result3)

# 获取指定的时间元组对应的时间戳
ttp1 = (2019, 1, 10, 0, 0, 0, 0, 0, 0)
result4 = time.mktime(ttp1)
print(result4)

# 程序的睡眠时间
# time.sleep(5)

# 获取当前的时间戳
result5 = time.time()
print(result5)

# 将时间元组转换为 我们自己想要的格式的时间字符串
# 2019-01-10 15:55:59
ttp2 = (2019, 1, 10, 15, 55, 59, 0, 0, 0)
result6 = time.strftime("%Y-%m-%d %H:%M:%S", ttp2)
print(result6)

# 将时间字符串转换为时间元组 是上面的反向操作
result7 = time.strptime("2019年01月10日 00:15:00", "%Y年%m月%d日 %H:%M:%S")
print(result7)
