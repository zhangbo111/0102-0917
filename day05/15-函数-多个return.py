'''
1、函数里面可以放置多个return 一般分布在不同的分支上
2、函数执行的过程中 遇到return则终止函数执行
'''
def judge_sex(sex):
    if sex == 'man':
        return '杨过'
    elif sex == 'woman':
        return '小龙女'
    else:
        return '人妖'
# 传入的参数不一样 返回的值也不一样
name1 = judge_sex('man')
print('man:', name1)
name2 = judge_sex('woman')
print('woman:', name2)
name3 = judge_sex('renyao')
print('renyao:', name3)
# 练习：声明一个hobby函数，传入“谋笑” 返回“看美女”“足球”
# 传入建鑫 返回 “看人妖” “篮球”
# 传入向洋 返回  "看星星"  ”数太阳“
# 传入 豪斌 和 昌镐  返回 “小说” “晒太阳”


