# 生成器表达式

lst = [i for i in range(5)]
print(lst, type(lst))
# 把[] 改为() 就可以生成一个生成器
gen = (i for i in range(5))
print(gen, type(gen))

iter1 = iter(lst)   # 将列表变为迭代器
print(iter1, type(iter1))

print(next(iter1), type(iter1))  # 迭代器
print(next(gen), type(gen))   # 生成器
