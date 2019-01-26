# 判断这个程序运行了多长的时间？单位是秒？
import time

# 开始时间
start = time.time()
print("开始的时间戳：", start, type(start))

lst = []
for i in range(10000000):
    lst.append(i)

end = time.time()
print("结束的时间戳：",end, type(end))

spend_time = end - start
print("程序运行的时间：", spend_time)


