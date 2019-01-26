dict1 = {'singer': '林俊杰', 'song': "江南", 'age': 35}
# keys方法 返回字典中所有的键
keys = dict1.keys()
print(keys)
print(type(keys))
# values()方法 获取字典中所有的值
values = dict1.values()
print(values)
# items()方法 获取字典当中的键值对
key_value = dict1.items()
print(key_value)

dict2 = {'name': '穿越火线', 'game': "枪战", 'age': 8}
# 以下循环语句只能获取到字典当中的所有的键
# for i in dict2:
#     print(i)
# 以下循环语句只能获取到字典当中的所有的值
# for j in dict2.values():
#     print(j)
# 以下循环可以同时获取到字典的当中的所有键值对
# for k, v in dict2.items():
#     print(k, end=' ')
#     print(v, end=' ')

# for循环回顾
# str1 = [1, 2, 3]
# for i in str1:
#     print(i)

# 练习：
dict3 = {'today': 'rain', 'date': '0104', 'year': 2020}
# 添加一个键值对 month：1
# 将year修改为2019
# 获取date的值
# 获取所有的键， 获取所有的值
# 获取所有的键值对

dict3['month'] = 1  # 添加一对键值对
print(dict3)
dict3['year'] = 2019  # 修改指定的键对应的值
print(dict3)
print(dict3['date'])  # 获取date的值
print(dict3.keys())  # 获取所有的键
print(dict3.values())  # 获取所有的值
print(dict3.items())  # 获取所有的键值对

dict4 = {'name': 'windows'}
# 获取里面的值得另外的一个操作
value1 = dict4.get('name')
print(value1)
# 获取不存在的键 返回一个None  不报错
value2 = dict4.get('age')
print(value2)
# 获取不存在的值 报错
# value3 = dict4['age']
# print(value3)
# update更新字典 如果键存在则进行修改操作
# 如果键不存在则进行 添加操作
dict4.update(name='Linux')
print(dict4)
dict4.update(age=18)
print(dict4)
# 测量字典中键值对的数量
print(len(dict4))
# pop删除指定键对应的整个键值对
dict5 = {'year': 2018, 'time': '下午两点', 'temp': 5}
dict5.pop('time')
print(dict5)
# 删除指定的键对应的键值对（另外一种方式）
del dict5['temp']
print(dict5)

dict6 = {'year': 2018, 'time': '下午两点', 'temp': 5}
# 随机的删除一对键值对 原因是字典无序
dict6.popitem()
print(dict6)
# 清空字典
dict6.clear()
print(dict6)

# 练习：
# 如果字典当中的数据很多 可以用下面的方式声明
dict7 = {
    'username': '世界真奇妙',
    'password': '110',
    "age": 18,
    "date": '2019-01-04'
}
print(dict7)
# 查询date  使用get
# 添加sex：女
# 删除age  pop del 两种方式任选一种
# 修改密码：112  使用update
print(dict7.get('date'))  # 查询
dict7.update(sex='女')  # 添加
print(dict7)
del dict7['age']   # 删除
print(dict7)
dict7.update(password='112')  # 修改
print(dict7)














