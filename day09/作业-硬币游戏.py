import random
'''
作业：完善上面的练习
连续抛1000次硬币 打印出连续出现4次0的次数  连续出现8次1的次数
举例：10000111000010  打印出2
'''
# 往列表中随机添加第一个元素
lst = [random.randint(0, 1)]

# 声明一个x变量 用于计算连续出现4次0
x = 1
y = 1
# 声明一个空列表 用于存储所有的连续出现4次0
count1 = 0
count2 = 0
c = 1
for i in range(1, 1000):
    # 随机把0或者1加入到lst里面
    lst.append(random.randint(0, 1))
    # 判断是否连续
    if lst[i] == lst[i-1] and lst[i-1] == 0:
        x += 1
        if x == 4:
            # print(c, lst)
            count1 += 1
        elif x == 5:
            count1 -= 1
    elif lst[i] == lst[i-1] and lst[i-1] == 1:
        y += 1
        if y == 8:
            print(c, lst)
            count2 += 1
        elif y == 9:
            count2 -= 1
    # 如果不连续则 初始化x的值
    else:
        x = 1
        y = 1
    c += 1

print("连续出现4次0的次数：", count1)
print("连续出现8次1的次数：", count2)

