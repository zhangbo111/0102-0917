import random
# 2、连续猜拳 知道有一方连续赢五次 才推出 打印出谁赢了，打印出比赛的次数
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
        computer = 0
        man += 1
        print("当前你赢了{}局".format(man))
        if man == 5:
            print("恭喜您 您连续赢了5次")
            break
    elif people_num == computer:
        man = 0
        computer = 0
        print('平局')
    else:
        man = 0
        computer += 1
        print("当前你赢了{}局".format(computer))
        if computer == 5:
            print("oh year 机器赢了5次了")
            break
    count += 1
print("一共猜了{}次".format(count))
