import random
# 作业：猜拳游戏
# 1、如果是五局三胜 猜拳五次，三次胜利才算赢 否则重新来过
# 打印出谁最终赢了 你赢的情况 恭喜您 您赢了  ，机器赢的情况：机器你都赢不了 回家种田
# 2、连续猜拳 知道有一方连续赢五次 才推出 打印出谁赢了，打印出比赛的次数
# 用于计算人和机器赢的次数
man = 0
computer = 0
count = 0
while True:
    # 人输入的数字
    # people_num = int(input("请输入【0,1,2】三个数字：(0->石头，1->剪刀，2->布)："))
    people_num = 1
    # 机器输入的数字
    computer = random.randint(0, 2)
    # 声明一个列表用于友好打印
    lst = ['石头', '剪刀', '布']
    print("人输入的是:", lst[people_num], "  电脑输入的是:", lst[computer])

    # 人赢的情况
    first = people_num == 0 and computer == 1
    second = people_num == 1 and computer == 2
    third = people_num == 2 and computer == 0

    # 只要满足一种情况即可
    if any([first, second,third]):
        man += 1
        print("当前你赢了{}局".format(man))
        if man == 3:
            print("恭喜您 您赢了")
            break
    elif people_num == computer:
        print('平局')
    else:
        computer += 1
        print("当前你赢了{}局".format(computer))
        if computer == 3:
            print("机器你都赢不了 回家种田")
            break
    count += 1
    if count == 5:
        man = 0
        computer = 0
        count = 0
        print("==============从新开始===============")

