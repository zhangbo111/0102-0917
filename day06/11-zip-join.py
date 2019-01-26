# 遍历一个列表
# lst = [1, 2, 3]
# for i in lst:
#     print(i)
# zip使用过程中遍历的列表必须长度一样
num_list = [1, 2, 3]
al_list = ['a', 'b', 'c']
china_list = ['唐', '宋', '明']
for i, j, k in zip(num_list, al_list, china_list):
    print(i, j, k)
    
# 字符串转换为列表 每一个字符会当做单个元素 存入列表
china = '唐宋元明清'
result_list = list(china)
print(result_list, type(result_list))

# 使用-连接所有列表中的元素 形成一个字符串
new_china1 = '-'.join(result_list)
print(new_china1, type(new_china1))
# 将列表拼接成字符串
new_china1 = ''.join(result_list)
print(new_china1, type(new_china1))
