import copy
# # 赋值过程 只是引用
# alist = [1, 2, 3, ['a', 'b']]
# blist = alist
# print(alist)
# print(blist)
#
# # 往alist尾部添加一个值
# # blist对alist的引用，当alist做出改变的时候 blist也会做出相应的改变
# alist.append(5)
# print(alist)
# print(blist)
# alist = [1, 2, 3, ["a", "b"]]
# clist = copy.copy(alist)
# print(alist)
# print(clist)
# # append表示往列表里面添加一个元素
# # 顶级对象做出改变拷贝后的clist不会做出改变
# alist.append(5)
# print('alist:', alist)
# print('clist:',clist)
#
# # 列表里面的子对象做出改变 浅拷贝之后的clist会做出改变
# # 所以浅拷贝不是真正意义上的全部拷贝，由此引出深拷贝
# alist[3].append('c')
# print('alist:', alist)
# print('clist:', clist)
# 深拷贝（循环拷贝），拷贝里面所有的对象
alist = [1, 2, 3, ['a', 'b']]
dlist = copy.deepcopy(alist)
print(alist)
print(dlist)
# 顶级可以拷贝出来
alist.append(5)
print(alist)
print(dlist)
# 不管原来的数据如何改变 深拷贝出来的数据不会做出任何改变
alist[3].append('c')
print(alist)
print(dlist)



