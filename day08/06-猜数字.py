import random
import time
'''
猜数字游戏：
1、电脑随机给出一个数字，范围在（1， 100）
2、人猜一次，然后机器猜一次 再人猜一次再机器猜
    直到人和机器有一个猜中为止
机器给了 66
1、人-->1-100  44  提示：你猜的数字太小了
机器猜：-->44 - 100   78  提示：猜的太大了
人猜： --> 44 - 78   67  提示太大了
机器：--> 44 - 67   66 机器猜中 break
'''
# 电脑给出一个1-99的数字 可以是1或者99
computer = random.randint(1, 99)
print("机器给定的数字是：{}".format(computer))
start = 0
end = 100
while True:
    # 人猜的时候
    p_num = int(input('请猜一个范围在{}到{}的整数:'.format(start, end)))
    # 猜的太大的情况
    if p_num > computer:
        print('您猜的数字太大了，还可以继续猜小一点')
        end = p_num
    # 猜中的情况
    elif p_num == computer:
        print('恭喜你 你猜中了')
        # 猜中之后推出循环
        break
    # 猜的太小了
    else:
        print('您猜的太小了,还可以继续猜大一点')
        start = p_num

    print('等待电脑输入{}到{}的数字:'.format(start, end))
    time.sleep(1)
    # 要前也要后 start和end可以猜 两边不猜 只猜中间的
    c_num = random.randint(start+1, end-1)
    print("电脑猜的数字是：{}".format(c_num))
    if c_num > computer:
        end = c_num
        print("电脑猜的太大了")
    elif c_num == computer:
        print("电脑猜中了")
        break
    else:
        start = c_num
        print("电脑猜的太小了")









