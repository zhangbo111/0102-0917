import itchat

# 登录操作
# hotReload=True 表示第一次登录完成之后 下次进入微信的时候不需要登录
# 相当于保存了账号和密码
itchat.auto_login(hotReload=True)

# 获取朋友信息
friends = itchat.get_friends()
# print(friends)
# print(type(friends))
# print(len(friends))

# 声明一个初始值
male = female = other = 0

# 将好友信息一个一个打印出来
for i in friends[1:]:
    print(i)
    if i['Sex'] == 1:
        male += 1
    elif i['Sex'] == 2:
        female += 1
    else:
        other += 1
print("好友总数：",len(friends[1:]))
print("男性数量：", male)
print("女性数量：", female)
print("未知性别数量：", other)

man = round(male / len(friends[1:]), 4) * 100
woman = round(female / len(friends[1:]), 4) * 100
other = other / len(friends[1:])
others = round(other * 100, 2)
# print(man)
# print(woman)
# print(others)
print('男性比例：{}'.format(man) + "%")
print('女性比例：{}'.format(woman) + "%")
print('未知性别比例：{}'.format(others) + "%")

# 小练习：打印出男性和女性分别占据的百分比 66.54%
# # 保留两位有效数字
# number = 1 / 3
# print(number)
# print(round(number, 2))
