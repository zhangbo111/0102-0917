# # lst接收了一个空列表
# def func(lst):
#     # 往空列表添加一个101的元素
#     # 传递的是可变参数 形参做出改变 外面的实参也会做出改变
#     # 是在实参列表的地址上直接插入一个元素
#     lst.insert(0, 101)
#     # lst表示重新在内存在开辟一个新的地址
#     # 并不会影响到外面的实参
#     lst = [2, 3, 4]
# list1 = []
# func(list1)
# print(list1)

def func(lst):
    lst.append(101)
    # 在新地址上开辟一个地址
    lst = [2, 3, 4]
    # 返回值是新赋值的lst即 [2,3,4]
    # 变量就近原则 变量的使用会就近选择
    return lst
list1 = []
# list1接收的是函数返回过来的lst 即 [2,3,4]
list1 = func(list1)
print(list1)
