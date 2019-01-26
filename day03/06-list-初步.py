# 定义一个列表使用中括号[]
# 定义空列表
list1 = []
print(type(list1))
# 顶一个列表 并打印出他的类型
list2 = ['明池', '向洋', '建鑫', '豪斌', '谋笑', '昌昌']
print(list2)
print(type(list2))
# 循环输出列表中的所有内容
for name in list2:
    print(name)

# 往列表里面添加一个元素 并添加到尾部
age_list = [25, 22, 18, 20]
age_list.append(21)
print(age_list)
# 将指定的序列一个一个插入到列表的尾部 插入多个元素
age_list.extend((23, 24))
print(age_list)
# 将指定的元素插入到指定的索引前面
# 元素可以包含字符串，元组，字典等
# 指定插入单个元素
age_list.insert(1, {'name': 'james'})
print(age_list)
# 两个列表的相加 返回一个新的列表
name_list1 = ['哈登', '库里']
name_list2 = ['james', '杜兰特']
name_list3 = name_list1 + name_list2
print(name_list3)
# 默认删除最后元素
name_list4 = ['Erick', 'damen', 'rose', 'jack']
name_list4.pop()
print(name_list4)
# 通过索引可以删除指定元素
name_list4.pop(0)
print(name_list4)
# 通过元素的值删除指定的元素
name_list5 = ['damen', 'rose', 'willian']
name_list5.remove('rose')
print(name_list5)
# 通过索引删除指定的值
del name_list5[1]
print(name_list5)

# 练习：
score = [150, 130, 90, 66]
# 将120，78，77这些分数添加进score
# 删除掉小于90分的分数 建议使用for循环
score.extend((120, 78, 77))
print(score)
# 声明一个新列表 用于收集大于等于90的分数
# new_score = []
# for s in score:
#     # 判断s是否大于等于90
#     if s >= 90:
#         # 将大于等于90的分数加入新列表
#         new_score.append(s)
# print(new_score)

# 第二种方式
# 声明一个收集删除掉的分数的列表
# del_score = []
# for s in score:
#     if s < 90:
#         del_score.append(s)
# print(del_score)
# # # 将需要删除的元素进行删除
# for d in del_score:
#     score.remove(d)
# print(score)
print(score)
for i in score:
    print(i)
    if i < 90:
        score.remove(i)
print(score)
# 66 -- 3 下一次拿索引 4  下一个拿到的是78  5 没有
# score = [150, 130, 90, 120, 78, 77]
# score = [150, 130, 90, 120, 77]
