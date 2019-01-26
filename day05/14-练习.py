# 练习：声明一个函数 传入3,5,68,9,0,1,2 然后返回他们的和以及平均值
def jisuan(*args):
    # 计算接收到的元组的和
    # 声明一个变量
    sum = 0
    # 遍历元组内的值 加到sum上面
    for i in args:
        sum += i
    print('和:',sum)
    avg = sum / len(args)
    print("平均数：", avg)
    return sum, avg
sum_avg = jisuan(3, 5, 68, 9, 0, 1, 2)
print("返回的元组", sum_avg)



