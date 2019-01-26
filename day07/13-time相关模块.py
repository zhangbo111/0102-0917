import calendar

# # calendar() 获取指定年份的日历
# resulr = calendar.calendar(2019, w=4, l=1, c=6, m=4)
# print(resulr)
'''
w --> 两个日期之间的宽度
l --> 一周占用几行的高度
c --> 两个月份只之间的宽度
m --> 表示一行可以显示几个月
'''

# month() 获取指定年月的月份日历 第一个参数是年份 第二个是月份
# result = calendar.month(2019, 1)
# print(result)

# 获取年月日历的矩阵
# result = calendar.monthcalendar(2019, 1)
# print(result)

# 判断指定年份是不是闰年
# 可以被100整除 但必须是400的倍数
# result = calendar.isleap(1900)
# print(result)

# 获取指定范围内的年份的闰年个数
# result = calendar.leapdays(2000, 2017)
# print(result)

# 0 - 6 表示周一 --> 周日
# 获取指定年月周几开始 以及它的天数
# result = calendar.monthrange(2019, 1)
# print(result)

# 获取指定年月日是周几
# result = calendar.weekday(2019, 1, 10)
# print(result)

# 将时间元组转换为时间戳
# 时间戳是距离1970年1月1日 0 0 0 秒数
ttp = (2019, 1, 10, 15, 21, 22)
result = calendar.timegm(ttp)
print(result)
