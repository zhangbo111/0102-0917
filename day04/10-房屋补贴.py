dict1 = {
    '001':{'name':'张三','age':28,'address':'广州','score':88},
    '002':{'name':'李四','age':18,'address':'山东','score':78},
    '003':{'name':'王五','age':38,'address':'广州','score':95},
    '004':{'name':'小明','age':48,'address':'河北','score':90}
   }
# # k表示接收的是键 v表示接收的是值
# for k, v in dict1.items():
#     # 获取地址 然后根据地址进行判断
#     addr = v['address']
#     # print(addr)
#     # 判断地址是不是广州 是的话 给10000元补贴
#     if addr == '广州':
#         v['house'] = 10000
#     print(k, v)

# 输出最大的age和最小的age
dict2 = {
    '001':{'name':'张三','age': 28,'address':'广州','score':88},
    '002':{'name':'李四','age': 18,'address':'山东','score':78},
    '003':{'name':'王五','age': 38,'address':'广州','score':95},
    '004':{'name':'小明','age': 48,'address':'河北','score':90}
   }
lst = []
for v in dict2.values():
    # 获取年龄
    age = v.get('age')
    # 将每个人的年龄加入到声明好的列表里面
    lst.append(age)
# 友好输出
print("最大值：", max(lst))
print("最小值：", min(lst))

