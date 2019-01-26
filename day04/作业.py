# # # tup = ((2, 3), ['比亚迪', '奔驰'], '李白', '杜甫', '奥迪')
# # # # 1、查找所有的车名 然后打印出来
# # # print(tup[1][0],tup[1][1],tup[-1])
# # #
# # # # 2、给['比亚迪', '奔驰']添加一个 “五菱宏光”
# # # tup[1].append('五菱宏光')
# # # print(tup)
# # #
# # # age_list = [25, 88, 99, 60, 12, 1, 32, 14, 19, 34, 55]
# # # # 将年龄小于12的存入一个列表，
# # # xinbiao=[]
# # # for i in age_list:
# # #     if i>12:
# # #         xinbiao.append(i)
# # # print(xinbiao)
# # #
# # # # 将将年龄大于等于12 小于18存入一个列表
# # # xinbiao2=[]
# # # for a in age_list:
# # #     if 12<=a<18:
# # #         xinbiao2.append(a)
# # # print(xinbiao2)
# # #
# # # # 将年龄大于等于18 存入一个列表
# # # xinbiao3=[]
# # # for b in age_list:
# # #     if b>=18:
# # #         xinbiao3.append(b)
# # # print(xinbiao3)
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# #
# # tup = ((2, 3), ['比亚迪', '奔驰'], '李白', '杜甫', '奥迪')
# # # 1、查找所有的车名 然后打印出来
# # print(tup[1][0], tup[1][1], tup[-1])
# #
# # # 2、给['比亚迪', '奔驰']添加一个 “五菱宏光”
# # tup[1].append('五菱宏光')
# # print(tup)
# #
# # age_list = [25, 88, 99, 60, 12, 1, 32, 14, 19, 34, 55]
# # # 将年龄小于12的存入一个列表，
# # new_list = []
# # for i in age_list:
# #     if i < 12:
# #         new_list.append(i)
# # print('new_list:', new_list)
# #
# # # 将将年龄大于等于12 小于18存入一个列表
# # new_list1 = []
# # for i in age_list:
# #     if 12 <= i < 18:
# #         new_list1.append(i)
# # print('new_list1:', new_list1)
# #
# # # 将年龄大于等于18 存入一个列表并在原列表删除
# # del_list = []
# # for i in age_list:
# #     if i >= 18:
# #         del_list.append(i)
# # print('del_list:', del_list)
# # for j in del_list:
# #     age_list.remove(j)
# # print('age_list:', age_list)
# #
# # dct = {'name': ['张飞', '关羽'], 'age': [45, 60]}
# # # 添加 ‘刘备’进入我们的['张飞','关羽']  添加62到[45, 60]
# # dct['name'].append('刘备')
# # dct['age'].append(62)
# # print(dct)
# #
# # # 修改里面的张飞 为诸葛亮
# # dct['name'][0] = '诸葛亮'
# # print(dct)
# #
# # # 删除 掉age键
# # dct.pop('age')
# # print(dct)
# #
# # # 查询出关羽
# # print(dct['name'][1])
# #
# # 作业：
# tup = ((2, 3), ['比亚迪', '奔驰'], '李白', '杜甫', '奥迪')
# # 1、查找所有的车名 然后打印出来
# print(tup[1])
# # for i in tup[1]:
# #     print(i)
# # 2、给['比亚迪', '奔驰']添加一个 “五菱宏光”
# tup[1].append('五菱宏光')
# print(tup[1])
#
# age_list = [25, 88, 99, 60, 12, 1, 32, 14, 19, 34, 55]
# # 将年龄小于12的存入一个列表，
# age_list1 = []
# for age_list2 in age_list:
#     if age_list2<12:
#         age_list1.append(age_list2)
# print(age_list1)
# # 将将年龄大于等于12 小于18存入一个列表
# age_list3 = []
# for age_list4 in age_list:
#     if age_list4>=12 and age_list4<18:
#         age_list3.append(age_list4)
# print(age_list3)
# # 将年龄大于等于18 存入一个列表
# age_list5 = []
# for age_list6 in age_list:
#     if age_list6>=18:
#         age_list5.append(age_list6)
# print(age_list5)
#
# dct = {'name': ['张飞', '关羽'], 'age': [45, 60]}
# # 添加 ‘刘备’进入我们的['张飞','关羽']  添加62到[45, 60]
# dct['name'] = ['张飞','刘备', '关羽']
# dct['age'] = [45, 60,62]
# print(dct)
#
# # 修改里面的张飞 为诸葛亮
# dct['name'] = ['诸葛亮','刘备','关羽']
# print(dct)
# # # 删除 掉age键
# del dct['age']
# print(dct)
# # # 查询出关羽
# dct1 = dct.get('name')
# print(dct1[2])
#
# tup = ((2, 3), ['比亚迪', '奔驰'], '李白', '杜甫', '奥迪')
# # 1、查找所有的车名 然后打印出来
# print(tup[1][1],tup[1][0],tup[-1])
# # 2、给['比亚迪', '奔驰']添加一个 “五菱宏光”
# tup[1].append('五菱宏光')
# print(tup)
# age_list = [25, 88, 99, 60, 12, 1, 32, 14, 19, 34, 55]
# # 将年龄小于12的存入一个列表，
# new_list=[]
# for i in age_list:
#     if i<12 :
#         new_list.append(i)
# print(new_list)
# # 将将年龄大于等于12 小于18存入一个列表
# new_list1=[]
# for j in age_list:
#     if j>=12and j<18:
#         new_list1.append(j)
# print(new_list1)
# # 将年龄大于等于18 存入一个列表
# new_list2=[]
# for k in age_list:
#     if k>18:
#         new_list2.append(k)
# print(new_list2)
# dct = {'name': ['张飞', '关羽'], 'age': [45, 60]}
# # 添加 ‘刘备’进入我们的['张飞','关羽']  添加62到[45, 60]
# dct.get('name').append('刘备')
# print(dct)
# dct.get('age').append(62)
# print(dct)
# # 修改里面的张飞 为诸葛亮
# dct.get('name')[0]="诸葛亮"
# print(dct)
# # 删除 掉age键
# dct.pop('age')
# print(dct)
# # 查询出关羽
# print(dct.get('name')[1])


tup = ((2, 3), ['比亚迪', '奔驰'], '李白', '杜甫', '奥迪')
# 1、查找所有的车名 然后打印出来
# 2、给['比亚迪', '奔驰']添加一个 “五菱宏光”
print(tup[1],tup[4])        #查找所有的车名 然后打印出来
tup[1].append('五菱宏光')       #添加一个元素
print(tup)

age_list = [25, 88, 99, 60, 12, 1, 32, 14, 19, 34, 55]
# 将年龄小于12的存入一个列表，
# 将年龄大于等于12 小于18存入一个列表
# 将年龄大于等于18 存入一个列表
new_age_list=[]
for s in age_list:          #把年龄小于12的存入一个列表
    # print(s)
    if s<12:
        new_age_list.append(s)
print(new_age_list)

del_age_list=[]
for s in age_list:          #把年龄大于等于12 小于18存入一个列表
    if s >11:
        if s<18:
         del_age_list.append(s)
print(del_age_list)

new_age_list1=[]
for a in age_list:          #把年龄大于等于18的存入一个列表
    # print(a)
    if a>17:
        new_age_list1.append(a)
print(new_age_list1)

dct = {'name': ['张飞', '关羽'], 'age': [45, 60]}
# 添加 ‘刘备’进入我们的['张飞','关羽']  添加62到[45, 60]
# 修改里面的张飞 为诸葛亮
# 删除 掉age键
# 查询出关羽
# 代码敲三遍（注释一定要写）
dct['name'].append('刘备')    # 添加元素
dct['age'].append('62')         # 添加元素
print(dct)

dct['name']=['诸葛亮', '关羽', '刘备']     # 修改元素

dct.pop('age')      # 删除age键
print(dct)

print(dct.get('name')[1])       # 获取元素
