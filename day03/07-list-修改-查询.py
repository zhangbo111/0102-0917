num_list = [1, 2, 3, 321, 4, 2, 4]
# len方法计算列表的长度
print(len(num_list))
# 计算指定元素在列表中的次数
print(num_list.count(2))
# 查找指定元素在列表中的位置 没有找到则报错
print(num_list.index(321))
# 通过指定的索引修改指定的元素
follows = ['菊花', '黄花', '牡丹']
follows[2] = '牵牛花'
print(follows)
# 将列表进行翻转 倒序输出
num_list1 = [1, 2, 3, 4, 5]
num_list1.reverse()
print(num_list1)
# 将列表从小到大进行排序
num_list2 = [131, 78, 99, 150]
num_list2.sort()
print(num_list2)

# 练习：
lst = [77, 62, {'name': '库里', 'score': 40}, '江河']
# 1.增加 ‘佛山’ ‘深圳’到我们的列表
# 2、增加 ‘香港’ 到‘江河’的前面
# 3、删除掉62，删除掉 'score': 40
# 4. 修改库里 为汤神
# 5. 查询到 name的值
lst.extend(['佛山', '深圳']) # 添加元素
print(lst)
lst.insert(-3, '香港') # 插入指定位置
print(lst)
# 可以接收删除掉的数据
pop_data = lst.pop(1)  # 删除掉指定位置的数据
print(pop_data)
print(lst)
# del lst[1]
# print(lst)
player = lst.pop(1)  # 删除指定位置的数据
print(player)
print(lst)
del player['score']  # 删除字典当中的键值对
player['name'] = '汤神'  # 修改 字典当中指定的键对应的值
print(player)
lst.insert(1, player)
print(lst)
print(lst[1].get('name')) # 获取指定位置的值

# 作业：
tup = ((2, 3), ['比亚迪', '奔驰'], '李白', '杜甫', '奥迪')
# 1、查找所有的车名 然后打印出来
# 2、给['比亚迪', '奔驰']添加一个 “五菱宏光”
age_list = [25, 88, 99, 60, 12, 1, 32, 14, 19, 34, 55]
# 将年龄小于12的存入一个列表，
# 将将年龄大于等于12 小于18存入一个列表
# 将年龄大于等于18 存入一个列表
dct = {'name': ['张飞', '关羽'], 'age': [45, 60]}
# 添加 ‘刘备’进入我们的['张飞','关羽']  添加62到[45, 60]
# 修改里面的张飞 为诸葛亮
# 删除 掉age键
# 查询出关羽
# 代码敲三遍（注释一定要写）















