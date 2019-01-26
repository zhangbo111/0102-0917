tup1 = (1, 2, 3, 4, 5, 'python', '雷后')
print(tup1[4])
print(tup1[-1])
print(tup1[0:4])
print(tup1[2:])
print(tup1[1:7:2])
print(tup1[::2])
print(tup1[::-1])  # 元组翻转

# 练习：
tup2 = ('大江', '大河', ["花千骨", "天龙八部"], 2, 5, (8, 3, '妇女节'))
# （1）访问：大河，（2）往["花千骨", "天龙八部"]列表中添加“人民的名义”
# （3）用切片的方式获取2，5两个，
# （4）切片的方式获取8，3  （5）将元组翻转
print(tup2[1])
tup2[2].append("人民的名义")
print(tup2)
print(tup2[3:5])
print(tup2[-1][:2])
print(tup2[::-1])







