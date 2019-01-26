# :的左边是键 右边是值，然后用逗号分隔为一个个的键值对
# 键是唯一的，通过键访问字典当中对应的值
dict1 = {'name': '罗大佑', 'song': '恋曲1980', 'addr': '台北'}
print(dict1['name'])
print(dict1['song'])
print(dict1['addr'])
# 添加一对键值对
dict2 = {'name': '周杰伦'}
dict2['age'] = 36
print(dict2)
dict2['tel'] = '18732763526'
print(dict2)
# 如果age在原来的字典当中有这个键，我们就对原来的age做出修改
# 如果原来的字典没有age键，则做出的是添加
dict2['age'] = 30
print(dict2)















