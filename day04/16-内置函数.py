lst1 = [0, 2]
# any判断列表中是否函数真值 如果有则放回True
# 否则返回False
result1 = any(lst1)
print(result1)
# 对列表中的所有元素进行判断 所有的值为真 则返回True
# 否则 返回False
result2 = all(lst1)
print(result2)

str1 = '1+1'
print(str1)
# eval里面的内容可以当做python代码执行
print(eval(str1))

# 练习：
set1 = {3, 4, 5, 7}
set2 = {8, 3, 7, 2}
set3 = {7, 2, 9, 11}
# 1、判断的set1和set2的交集是不是set3的子集
# 2、判断set1和set2的对称差集是不是 set3的超集
jiaoji = set1.intersection(set2)
print(jiaoji)
ziji = jiaoji.issubset(set3)
print(ziji)
duicheng = set1.symmetric_difference(set2)
print(duicheng)
chaoji = duicheng.issuperset(set3)
print(chaoji)

# 作业：代码敲两遍
# 另外三种不同方向的九九乘法表。
# 不强调用for，可以用while循环 建议使用for循环
# 作业：使用另外的方式去重（至少写两种）





